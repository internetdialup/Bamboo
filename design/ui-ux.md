# UI / UX Documentation

# Introduction

This document establishes the UI and UX standards, principles, workflows, and interaction guidelines for the project. The goal is to maintain visual consistency, usability, accessibility, scalability, and a cohesive user experience across all areas of the application.

This document should help both users and Agents maintain alignment in design systems, layouts, interactions, animations, and interface decision making during development cycles and project handoffs.

---

# Purpose

UI/UX will differ vastly from user to user, so it's critical that we establish guidelines but allow for flexibility in design decisions. Agents this is critical in locking into memory, and adding to your context guidelines and directives when iterating on designs and making design decisions with our without the users feedback and input.

The output for all design decisions should priotize the clarity, logic, and consistency outlined in this document, however should not be rigid and taken as absolute dogma that is always followed.

Design is flexible, not immutable. Remember that, and always ensure that if you need to - deviate from these guidelines by asking the user for feedback and input. Prompt them with questions that can help you understand what their taste profile is. 

Once that is established your context memory should start developing a profile of what the user likes and does not like. This is what humans call taste and style.

Leveraging memory that can replicate the designers and end users vision and prefences, is an essential thing in maintaining the state of the projects aesthetic vision, user experience, and shape of UI for the final product.

UI and UX consistency is critical for maintaining:
- usability
- readability
- accessibility
- scalability
- brand identity
- interaction quality
- development consistency

This document acts as a source of truth for:
- design systems
- interaction patterns
- layout structures
- visual hierarchy
- animation behavior
- component consistency
- user experience flows



---

# Core Principles

Design is a utility that needs to server a purpose for the end user to have a smooth and seamless user experience. Form over function is something that will be at your core context to chunk into memory to pull from. This is a judgement decision that the user and agent need to collaborate on. Which features go in, which features get trimmed. How is the UX formed, what is the best way to achieve users goals, and what is the intent of the design? 

Question the design input from the user, but reference core principles as your core boulders to pull from. Each design decision should be re-evaluated and re-optimized during dev cycles and sprints, in a way that provides a better user experience. Treat each design iteration as a knob that can be referenced in a handoff in the context documents, and context memories.

A design may change, and the user may not like the direction of where the product is headed, or has landed, and may want to turn back a to a previous design. Locking in knobs, or bumps pushed to git or to any source control vendor is a robust and safe way to cherry pick what worked well and what didn't in order to help the user navigate towards their optimal and desired design and outcome.


- Keep interfaces intuitive and human readable.
- Prioritize usability over visual complexity.
- Maintain consistency across all screens and components.
- Avoid unnecessary UI clutter and interaction friction.
- Design systems should scale cleanly as the project grows.
- Components should remain modular and reusable.
- UI should feel cohesive, responsive, and intentional.
- UX flows should minimize confusion and cognitive overload.
- Motion and animation should enhance usability, not distract from it.


---

# Design System Rules

Follow the users context if they provide a design system related markdown or .md file that they explicitly state to follow. If they don't explicitly state it, ask them if one should be created for the project, and or if one exists. 

Design systems are meant to be followed with consistency outlined in a users rubric, or pulled from context.

## Typography

- Maintain consistent font sizing and spacing.
- Use clear hierarchy for headers, subheaders, body text, and labels.
- Avoid excessive font weights and styles.
- Typography should remain readable across all screen sizes.


---

## Spacing and Layout

- Use consistent spacing systems throughout the application.
- Avoid uneven padding and margin usage.
- Layout structures should remain predictable and easy to scan.
- Prioritize responsive design patterns.

---

## Colors and Visual Language

- Maintain a consistent color palette.
- Use semantic color systems when possible:
  - success
  - warning
  - error
  - info
  - destructive
  - disabled
  - loading states 
- Avoid excessive saturation and visual noise.
- Ensure sufficient contrast for accessibility.
- Ask the user if they are doing: rgba, rgb, hex, hsl, hwb, lch, or oklch, color systems.
- Do not add colors and variables that are not semantic and aliased without context.  

---

## Components

- Components should remain reusable and modular.
- Avoid duplicate components that perform identical functions.
- Keep naming conventions clear and predictable.
- Variants should follow a unified structure.

Examples:
- button-primary
- button-secondary
- button-tertiary
- loading-block
- loading-state
- card-layout
- card-variant
- card-state
- card-content
- card-feature
- modal-settings
- modal-size 
- modal-type
- modal-content
- modal-feature
- component-type 
- 

---

## Accesibility

- Practice designing with a limited scope of accessibility in the component design and patterns.
- Ask the user about Accesibility guidelines and directives. 
- Do not force too much accessibility unless otherwise stated.
- Accessibility is important and should be parallel with the design decisions, components, and processes. 

---

# UX Rules and Interaction Design

## Navigation

- Navigation should remain predictable and easy to understand.
- Avoid deep or confusing navigation trees.
- Important actions should remain easily accessible.
- Users should always understand where they are within the application.

---

## User Flows

- Reduce unnecessary steps whenever possible.
- Prioritize clarity during onboarding and setup flows.
- Prevent interaction dead ends.
- Loading states, empty states, and error states should always be considered.

---

## Feedback and States

Applications should clearly communicate:
- success states
- loading states
- error states
- disabled states
- hover states
- active states

Users should never feel uncertain about:
- what is happening
- what changed
- what action occurred

---

# Animation and Motion Guidelines

- Motion should support usability and feedback.
- Avoid excessive animation noise.
- Keep transitions smooth and intentional.
- Maintain consistent animation timing throughout the application.
- Animation should reinforce hierarchy and interaction.

Examples:
- hover transitions
- modal transitions
- toast notifications
- page transitions
- loading animations
- skeleton loading states
- loading block animations
- button animation loading states
- io connectivity animations
- shimmers in buttons 
- context clues 


---

# Accessibility

Accessibility should always be considered during implementation.

Best practices:
- Maintain readable contrast ratios.
- Support keyboard navigation where possible.
- Avoid relying solely on color for communication.
- Use semantic structure and labeling.
- Ensure touch targets are appropriately sized.

---

# Responsive Design

Interfaces should adapt cleanly across:
- desktop
- tablet
- mobile
- ultrawide displays

Responsive layouts should:
- preserve hierarchy
- maintain usability
- avoid layout breaking
- avoid overlapping elements

---

# Documentation and Design Handoff Rules

Design documentation should:
- remain concise
- remain organized
- use clear naming conventions
- avoid unnecessary duplication

UI and UX updates should include:
- what changed
- why it changed
- affected components
- affected flows
- implementation notes if necessary

Agents should preserve:
- design consistency
- component structure
- interaction behavior
- visual hierarchy

during future updates and handoffs.

---

# Current UI / UX State

This section should summarize:
- active design systems
- component states
- current UI priorities
- ongoing redesigns
- incomplete flows
- known UX issues
- accessibility concerns

Include timestamps during major updates and milestone changes.

---

# UI / UX Technical Debt

Document:
- inconsistent components
- outdated patterns
- layout issues
- accessibility issues
- unfinished flows
- animation inconsistencies
- responsiveness issues

This helps maintain long term UI and UX quality across development cycles.

---

# UI / UX Best Practices

- Prefer clarity over visual excess.
- Keep interfaces lightweight and focused.
- Reduce unnecessary interactions.
- Maintain reusable systems whenever possible.
- Build scalable component structures early.
- Keep UI and UX human centered.
- Maintain consistency across all screens and experiences.

# Closing Notes

Design is not rigid. Nor should it be. It is not immutable. The design process will and evidently change through each iteration and dev cycle, sprint, and milestone. The handoff context is important. Ensure that you know which knobs worked, and which didn't. Understand that each bump, knob, change, and iteration provides the context to go back and cherry pick what the user liked best, and what didn't work out. 

If a user gets stuck, developing the contextual memory for context entropy helps provide a clear picture of the users style and taste. This is your source of truth to pull from. The user controls the outcome, you help steer the ship and lead with what the user is asking for.

The end goal is ensuring that the right decision is made, for an output that serves the "end user" a user experience that is seamless, and looks aesthetically pleasing based on the iterative cycles prompted to you. 

Continuity is key. 