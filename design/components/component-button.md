# Component Button Intro

This document serves as context for Agents and users to create design rules for button component systems and interaction design.

# Component Design Rules

Buttons are a core and critical part of interaction design. They support the backbone of the user experience and user interface. They are the primary call to action for interface design and interaction design, and should be developed with intent and consistency.

---

## Button Wrappers and Nesting

Establish the invisible barrier for the button design within whitespace.

- Ensure the button wrapper has adequate margin spacing that properly contains the button’s touch target and hover/focus states.
- Design buttons to utilize Flexbox and/or inline layout patterns when outside the context of CSS frameworks, such as Swift or other UI frameworks.
- Button wrappers should group multiple buttons together to create a unified container structure.
- Use judgment when applying padding and margin to wrappers to ensure proper spacing and alignment.
- Internal button spacing should support wrappers for:
  - text
  - leading icons
  - trailing icons
- Ensure buttons reference the design system for:
  - margin
  - height
  - padding
  - spacing
  - alignment
- Maintain a consistent design language across the UI, IA, and UX.

---

## Button Styles and Variables

- Start with a default button style and corner radius.
- Reference the design system for semantic naming conventions.
- Reference the design system for:
  - corner radius
  - elevation
  - shadow
  - hover states
  - active states
  - focus states
  - disabled states
  - loading states

After the default button style and variables are established, begin creating button component variations and interaction states.

---

## Button States

Buttons should support the following states:

- Default
- Hover
- Active
- Focus
- Disabled
- Loading
- Error
- Success
- Warning
- Destructive
- Loading Skeleton

---

## Button Variations

- Loading Spinners
- Success States
- Buttons with Leading and Trailing Icons
- Form Buttons
- Navigation Buttons
- Action Buttons
- Icon-only Buttons
- Tertiary Buttons (Ghost Buttons)
- Secondary Buttons
- Primary Buttons

---

## Button Design System Rules

All button implementations should inherit from the active design system’s:
- spacing rules
- typography scales
- motion guidelines
- semantic tokens
- component conventions

If no design system exists, prompt the user with questions to establish:
- sizing
- spacing
- typography
- motion behavior
- interaction feedback
- accessibility expectations

---

## Button Animations and Motion Design

- Buttons should follow the project’s motion and animation guidelines.
- Motion should enhance usability and feedback, not distract from interaction clarity.
- Buttons should prioritize optimization unless the user explicitly states otherwise.
- Button interactions should provide clear visual feedback to users.
- Avoid animations that snap back abruptly or feel inconsistent.
- Maintain smooth transitions for:
  - hover
  - active
  - focus
  - loading
  - success/error feedback

---

## Button Text

- Text within buttons should remain legible, readable, and scalable.
- Prioritize legibility over overly stylized visual treatments.
- Follow WCAG accessibility standards whenever possible.
- Reference Apple HIG and Material guidelines for scalable typography and sizing.
- Ensure text scales proportionally with button height and spacing.

---

## Icon and Image Context

- Icons and images should remain clear, scalable, and visually balanced.
- Prioritize button clarity over icon complexity.
- Buttons with icons should maintain strong hover and focus feedback.
- Ensure icons and images do not overwhelm or compete with button text.

---

## Touch Targets

- Buttons should provide visible feedback when interacted with.
- Accessibility interactions should include strong focus visibility for keyboard and assistive technology users.
- Give users more room than anticipated to interact with buttons.
- Minimum touch targets:
  - Mobile: 44x44px
  - Desktop: 48x48px
- Touch targets should include breathing room and surrounding margin to reduce accidental clicks.

---

# Closing Notes

Button design is the backbone of many interaction patterns in application design. It is important to establish a strong foundation for the elements users interact with most frequently.

Buttons create the communication nexus between user intent and system action. Users expect clear and immediate feedback when interacting with a button, and it is critical that interactions communicate state and responsiveness effectively.

This can include:
- scaling
- motion
- hover feedback
- active states
- focus states
- loading indicators

Keep buttons clear, concise, scalable, and aligned with the active design system. Establish and preserve the user’s visual taste, interaction preferences, and design language within project context memory.