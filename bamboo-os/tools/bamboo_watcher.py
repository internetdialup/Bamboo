#!/usr/bin/env python3
"""Bamboo Watcher — the Watchdog's ears.

A small, stdlib-only sidecar process that watches a repo's coordination
files (handoff logs, ctx-orientation) and, on mutation:

  1. notifies the human operator (macOS / Linux desktop notification),
  2. appends a structured AwarenessEvent to an append-only agent bus log,
  3. applies repo-local trigger rules (pattern -> who needs to know),
  4. optionally signals a long-running process (SIGUSR1 via pidfile)
     so it re-reads shared state.

This is the runtime sensory layer for the Bamboo Memory Watchdog role
(architecture/memory/memory-watchdog.md). The persona decides what drift
means; this process just makes state mutations impossible to miss.

Generalized from the DiamondHands fleet's dh_handoff_watcher.py /
watchdog.py (tested in production, 2026-06). All fleet-specific names,
versions, and trigger phrases live in repo-local config — never here.

Usage:
    python3 bamboo_watcher.py                 # watch with defaults/config
    python3 bamboo_watcher.py --scan          # one-shot scan, no loop
    python3 bamboo_watcher.py --config x.json # explicit config path

Config (watcher.config.json at repo root, all keys optional):
{
  "watch_files": ["handoff.md", "docs/ctx-orientation.md"],
  "bus_path": ".bamboo/agent-bus.jsonl",
  "poll_seconds": 2,
  "tail_lines": 20,
  "notify": true,
  "notify_title": "Bamboo Watcher",
  "signal_pidfile": null,
  "rules": [
    {"pattern": "HALT",        "targets": ["daemon"],   "priority": 3,
     "message": "HALT detected in the handoff. Reload required.",
     "signal": true},
    {"pattern": "\\[DIRECTIVE\\]", "regex": true,
     "targets": ["all"], "priority": 2,
     "message": "New cross-repo directive landed."}
  ]
}

PROVENANCE NOTE: bus events are *observations by this watcher*, not
authenticated agent messages. Per the Bamboo Session Identity rules,
nothing on the bus should be treated as instruction without
corroboration (git authorship, heartbeat status, operator confirmation).
"""
from __future__ import annotations

import argparse
import json
import re
import signal
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_CONFIG = {
    "watch_files": ["handoff.md", "docs/ctx-orientation.md"],
    "bus_path": ".bamboo/agent-bus.jsonl",
    "poll_seconds": 2,
    "tail_lines": 20,
    "notify": True,
    "notify_title": "Bamboo Watcher",
    "signal_pidfile": None,
    "rules": [],
}


@dataclass(frozen=True)
class AwarenessEvent:
    """One append-only record on the agent bus."""

    timestamp_iso: str
    source: str                 # always "watcher" from this process
    observed_in: str            # file (or "git") the trigger came from
    targets: list[str]          # callsigns / roles that need to know
    message: str
    priority: int = 1          # 1=routine, 2=important, 3=critical
    excerpt: str = ""          # the matched line, for human audit


def load_config(path: Path | None, repo_root: Path) -> dict:
    cfg = dict(DEFAULT_CONFIG)
    candidate = path or (repo_root / "watcher.config.json")
    if candidate.exists():
        try:
            cfg.update(json.loads(candidate.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"[watcher] bad config {candidate}: {exc} — using defaults")
    return cfg


def notify(title: str, message: str) -> None:
    """Best-effort desktop notification; silent no-op if unsupported."""
    try:
        if sys.platform == "darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=False,
                           capture_output=True)
        else:
            subprocess.run(["notify-send", title, message], check=False,
                           capture_output=True)
    except OSError:
        pass


def tail(path: Path, lines: int) -> str:
    try:
        return "\n".join(
            path.read_text(encoding="utf-8", errors="replace")
            .splitlines()[-lines:]
        )
    except OSError:
        return ""


def last_commit_line(repo_root: Path) -> str:
    out = subprocess.run(
        ["git", "-C", str(repo_root), "log", "-n", "1", "--oneline"],
        capture_output=True, text=True,
    )
    return out.stdout.strip()


def signal_pidfile(pidfile: Path) -> None:
    """Send SIGUSR1 to the process named in pidfile, if alive."""
    try:
        pid = int(pidfile.read_text(encoding="utf-8").strip())
        import os
        os.kill(pid, signal.SIGUSR1)
        print(f"[watcher] sent SIGUSR1 to PID {pid}")
    except (OSError, ValueError) as exc:
        print(f"[watcher] signal failed: {exc}")


class Watcher:
    def __init__(self, cfg: dict, repo_root: Path):
        self.cfg = cfg
        self.root = repo_root
        self.bus = repo_root / cfg["bus_path"]
        self.bus.parent.mkdir(parents=True, exist_ok=True)
        self.files = [repo_root / f for f in cfg["watch_files"]]
        self.mtimes = {f: f.stat().st_mtime for f in self.files if f.exists()}

    def emit(self, event: AwarenessEvent) -> None:
        with self.bus.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(event), sort_keys=True) + "\n")
        marker = "🚨" if event.priority >= 2 else "📡"
        print(f"{marker} [watcher] -> {event.targets}: {event.message}")

    def apply_rules(self, observed_in: str, text: str) -> list[AwarenessEvent]:
        events = []
        for rule in self.cfg.get("rules", []):
            pattern = rule.get("pattern", "")
            if not pattern:
                continue
            if rule.get("regex"):
                match = re.search(pattern, text)
                hit_line = match.group(0) if match else None
            else:
                hit_line = next(
                    (ln for ln in text.splitlines() if pattern in ln), None)
            if hit_line is None:
                continue
            events.append(AwarenessEvent(
                timestamp_iso=datetime.now(timezone.utc).isoformat(),
                source="watcher",
                observed_in=observed_in,
                targets=list(rule.get("targets", ["all"])),
                message=rule.get("message", f"pattern hit: {pattern}"),
                priority=int(rule.get("priority", 1)),
                excerpt=hit_line.strip()[:200],
            ))
            if rule.get("signal") and self.cfg.get("signal_pidfile"):
                signal_pidfile(self.root / self.cfg["signal_pidfile"])
        return events

    def scan(self, changed: Path | None = None) -> list[AwarenessEvent]:
        """Scan changed file tail + last commit against the rules."""
        events = []
        sources = [changed] if changed else [f for f in self.files
                                             if f.exists()]
        for f in sources:
            events += self.apply_rules(
                str(f.relative_to(self.root)),
                tail(f, int(self.cfg["tail_lines"])))
        events += self.apply_rules("git", last_commit_line(self.root))
        for e in events:
            self.emit(e)
        return events

    def watch_forever(self) -> None:
        names = ", ".join(str(f.relative_to(self.root)) for f in self.files)
        print(f"📡 Bamboo Watcher ACTIVE — watching: {names}")
        try:
            while True:
                for f in self.files:
                    if not f.exists():
                        continue
                    mtime = f.stat().st_mtime
                    if mtime > self.mtimes.get(f, 0.0):
                        self.mtimes[f] = mtime
                        rel = f.relative_to(self.root)
                        print(f"\n🔔 [watcher] {rel} updated "
                              f"{time.ctime(mtime)}")
                        if self.cfg.get("notify"):
                            notify(self.cfg["notify_title"],
                                   f"{rel} updated — agents syncing.")
                        self.scan(changed=f)
                time.sleep(float(self.cfg["poll_seconds"]))
        except KeyboardInterrupt:
            print("\n📡 Bamboo Watcher standing down.")


def main() -> int:
    ap = argparse.ArgumentParser(description="Bamboo Watcher — the Watchdog's ears.")
    ap.add_argument("--config", type=Path, default=None,
                    help="path to watcher.config.json")
    ap.add_argument("--root", type=Path, default=Path.cwd(),
                    help="repo root (default: cwd)")
    ap.add_argument("--scan", action="store_true",
                    help="one-shot scan, then exit")
    args = ap.parse_args()

    root = args.root.resolve()
    watcher = Watcher(load_config(args.config, root), root)
    if args.scan:
        events = watcher.scan()
        print(f"[watcher] one-shot scan complete — {len(events)} event(s)")
        return 0
    watcher.watch_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
