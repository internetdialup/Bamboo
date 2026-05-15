# Component Button Intro

This document serves as context for Agents, and users to create design rules for button design componentry. 

# Component Design Rules 

Buttons are a core and critical part of interaction design. They support the backbone of the user experience, and user interface. They are the main call to action for interface design, and interaction design. They should be developed and designed with intent. 

## Button Wrappers and Nestin

Establish the invisible barrier for the buttons design within whitespace.

- Ensure the button wrapper has margin spacing that adequately contains the buttons touch target and hover / focus states.
- Design the buttons to utilize flex box, and or certain inline design patterns if outside the context of CSS such as using Swift and or a different framework. 
- Button wrappers should group multiple buttons together, to create a unified wrapper that contains the buttons nested within it.
- Use your judgement in adding padding and margin to the button wrapper to ensure proper button spacing. Button spacing internally should contain a wrapper for text and wrappers for leading and trailing icons if applicable. 
- Lastly, ensure that the buttons refrence a design system for the correct margin height, padding, and spacing rules to keep a consistent design language that flows through the productions and design of the User Interface, IA, and UX. 

## Button Styles and Variables 

- Start with a default button style and corner radius.
- Reference the design system for semantic naming conventions.
- Refeence the design system for corner / border radius for buttons. 
- Reference the design system for elevation and shadow for buttons. 
- Reference the design system for hover states for buttons. 
- Reference the design system for active states for buttons. 
- Reference the design system for focus states for buttons. 
- Reference the design system for disabled states for buttons. 
- Reference the design system for loading states for buttons. 

After the default button style and variables are established, you can start to create the button componentry and button states. 

## Button States

- Default state
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

## Button Variations 

- Loading Spinners
- Success States 
- Button Text with Trailing and Leading Icons
- Buttons for Forms
- Buttons for Navigation
- Buttons for Actions
- Icon only Button styles
- Tertiary Button styles (Ghost buttons)
- Secondary Button styles
- Primary Button styles 

## Button Design System Rules 

Reference the design system in the users repository for the design system rules. Analyze the markdown rules and files to reference. If no such DS system provides the context for how buttons should be designed, developed, and positioned; prompt and ask the user specific questions for creating buttons. 

## Button Animations and Motion Design 

- Buttons should reference and follow a design system related to animation and motion design.
- Buttons should follow the Design System and or Motion guidelines that are documented.
- Buttons should priortize optimaization unless the user states otherwise.
- Buttons should be designed with clarity with distinct feedback for the end user UX.
- Button animations should not snap back if they utilize transitions in CSS, SCSS, or imported UI Kits (Tailwind, ShadCN, etc) 

## Button Text 

- Text within buttons needs to be legible, readable, and scalable. 
- Prioritize button legibility over colors, and follow WCAG standars whenever possible.
- Create buttons that follow Apples HIGS (Human Interface Guidelines). 
- Text should follow Material or HIGS font sizings and scale in relation to the button.

## Icon and Image Context

- If the button contains icons or images, ensure they are clear and scalable.
- Prioritize button clarity over icon and image clarity.
- Buttons with icons should have a clear hover state and visual feedback.
- Ensure icons and images do not overwhelm the button text.

## Touch Targets

- When buttons are pressed on signal visible feedback to the user that the button was touched / clicked / interacted with. 
- When buttons are used and accessed by accsibility software, cue visual feedback using focus to users so they are aware of which button they are interacting with.
- Give users more room than anticipated to click on the buttons.
- Touch targets minimums should be at minimum 44x44px for mobile.
- Touch targets minimums should be at minimum 48x48px for desktop.
- Touch targets should have breathing room or margin around them to prevent accidental clicks.


# Closing Notes

Button design is the backbone of many design patterns in application design. It's important to established a solid foundation of what users will be interacting with most. Buttons create the communication nexus that bridges the intent and action to formulate input and output for the user. Users expect something to happen when a button is pressed on, and it's crucial we ensure that we relay the correct feedback to them. Whether through scaling buttons down using motion, animation, and or highlighting them using the focus method or adjacent hover/active states. 

Keep the buttons clear, concise, and adhere to what the design system allows for and establish the users taste and visual design profile and preferences in context memory. 
