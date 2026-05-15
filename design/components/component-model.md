# Component Modal Intro

This document serves as context for Agents and users to create design rules for modal systems, overlays, dialogs, sheets, and focused interaction flows.

# Component Design Rules

Modals are a core part of interaction and flow interruption design. They temporarily shift user focus toward a specific action, piece of information, confirmation state, workflow, or decision.

Modals should be designed with clarity, restraint, hierarchy, and intentional focus management.

Poor modal design creates:
- cognitive overload
- interaction friction
- accessibility issues
- broken focus states
- visual clutter
- UX interruption fatigue

Modals should support the user experience, not fight against it.

---

## Modal Design Patterns

Modals often inherit their design atoms, to formulate patterns. Reference the users design system for how the modal patterns should be implemented.

Design patterns should be created with the user context in mind. And pulling from established context memories, and design system memory banks and rules. Secondly, AI Agents need to ask the user questions to establish the right pattern design. 

For example: A close button is often positioned at the top right corner of a modal. However, it can also be positioned at the top left, or bottom of a modal. Could not even be part of the pattern but a systems design note is instead attached to a modals design purpose where tapping outside creates the action of closing the modal.

System design, and IX are different topics but often times rely on one another so these need to also be chunked into the context memory to establish a baseline of the users design intended behaviour and patterns to ensure that the modal and UX do not drift in design architecture over time.

Always ask the user design and UX questions for crafting the appropriate context for the current pattern being designed for. If no such thing exists; scan a users existing repository to develop that reference. If either of these options are not available; develop a context based on the current project and state the assumptions being made and or explicitly ask the user what their desired outcome is.

Conxtext clarity creates clear and concise component architecture that becomes the baseline foundation for any design system with consistent standardization over time. 

Design drift is inveitable; it is whether or not we allow for the drift to continue or worsen over time without interveneing, stablizing the drift, and refactoring our patterns to match the current status of the project. 

---

## Modal Wrappers and Structure

Establish clear containment and layout hierarchy for modal systems.

- Modals should exist within a dedicated overlay and wrapper structure.
- Maintain proper spacing between:
  - modal container
  - viewport edges
  - modal content
  - footer actions
  - headers
- Modal wrappers should maintain proper alignment and responsive scaling.
- Modals should support:
  - centered layouts
  - bottom sheets
  - side sheets
  - fullscreen states
  - stacked modal systems (when necessary)
- Use judgment when determining modal width, height, and overflow behavior.
- Avoid oversized modal containers that reduce readability and focus.

---

## Modal Styles and Variables

- Start with a default modal container style.
- Reference the design system for:
  - corner radius
  - shadows
  - overlays
  - spacing
  - blur systems
  - border treatments
  - motion guidelines
  - typography hierarchy
- Modal containers should maintain visual separation from the background UI.
- Maintain consistent overlay opacity and layering behavior throughout the application.

---

## Modal States

Modals should support the following states:

- Open
- Closed
- Loading
- Success
- Error
- Warning
- Confirmation
- Destructive
- Empty State
- Scroll State
- Disabled Interaction State

---

## Modal Variations

- Confirmation Modals
- Alert Modals
- Destructive Action Modals
- Form Modals
- Settings Modals
- Fullscreen Modals
- Bottom Sheets
- Side Panels
- Contextual Action Sheets
- Media / Gallery Modals
- Multi-step Workflow Modals

---

## Modal Layout and Hierarchy

- Modal hierarchy should remain visually clear and easy to scan.
- Prioritize:
  - title clarity
  - content readability
  - action visibility
- Avoid excessive text density.
- Primary actions should remain visually dominant.
- Secondary actions should remain clearly distinguishable.
- Footer layouts should maintain consistent spacing and alignment.
- Avoid overwhelming users with too many actions inside a single modal.

---

## Modal Interaction Rules

- Users should always understand:
  - why the modal appeared
  - what action is required
  - how to dismiss it
- Modals should not trap users unnecessarily.
- Escape and dismissal behavior should remain predictable.
- Clicking outside the modal should only dismiss when appropriate.
- Destructive actions should require confirmation states when necessary.
- Avoid stacking multiple modals unless the workflow explicitly requires it.

---

## Focus and Accessibility

- Focus should automatically move into the modal when opened.
- Focus should return to the previously active element when closed.
- Keyboard navigation should remain fully functional.
- Modals should maintain:
  - readable contrast
  - accessible typography
  - visible focus states
  - semantic structure
- Screen readers should clearly identify:
  - modal titles
  - descriptions
  - action states

---

## Modal Animations and Motion Design

- Modal motion should feel smooth, intentional, and lightweight.
- Motion should reinforce:
  - hierarchy
  - focus
  - interaction feedback
- Avoid excessive bounce, scaling, or distracting motion effects.
- Modal transitions should maintain consistent timing and easing.
- Support smooth transitions for:
  - overlay fade
  - modal entrance
  - modal exit
  - loading transitions
  - success/error state transitions

---

## Overlay and Background Behavior

- Overlays should visually separate modal content from the underlying UI.
- Background dimming should preserve focus without fully obscuring context.
- Blur effects should remain subtle and performant.
- Avoid overly aggressive opacity that causes visual fatigue.
- Background interaction should remain disabled while the modal is active unless intentionally designed otherwise.

---

## Responsive Design

Modal systems should adapt cleanly across:
- desktop
- tablet
- mobile
- ultrawide displays

Responsive modal systems should:
- preserve readability
- preserve spacing
- prevent overflow issues
- maintain accessible touch targets
- avoid clipped actions or content

---

## Touch Targets

- Modal actions should provide strong interaction feedback.
- Minimum touch target sizes:
  - Mobile: 44x44px
  - Desktop: 48x48px
- Buttons and actions should include adequate spacing to reduce accidental interactions.
- Close actions should remain clearly visible and accessible.

---

# Modal Design System Rules

All modal implementations should inherit from the active design system’s:
- spacing rules
- typography scales
- motion guidelines
- semantic tokens
- elevation systems
- overlay treatments
- accessibility rules

If no design system exists, prompt the user with questions to establish:
- modal sizing
- overlay behavior
- motion direction
- interaction expectations
- accessibility requirements
- dismissal logic

---

# Closing Notes

Modal systems are one of the most interruption-sensitive components in UI and UX design. Poor modal implementation can quickly create frustration, confusion, and interaction fatigue.

Modals should create focused moments of interaction that guide users toward clear decisions and workflows while maintaining accessibility, responsiveness, and visual hierarchy.

Keep modal systems:
- clear
- predictable
- scalable
- accessible
- visually restrained
- aligned with the active design system

Preserve consistency in interaction behavior, motion, hierarchy, and accessibility throughout the application experience. Do not create patterns without the assigned systems rules and context to reference from. Update the context memory bank for better context entropy so over time their is less decay for the Agent to pull from, and more established context memory to reference for more accurate and consistent system design.