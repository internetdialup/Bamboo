# Component Nav Header Intro 

This document serves as context for Agents and users to create design rules for navigation headers, otherwise known as nav header for short. This can apply to main nav-headers (navigation headers), sub navigation headers, and any usage in the form of a nav-header. 

## Designing for Nav Headers 

Design for Nav headers using the users preffered view port width, and or container / wrappers. If the user is using ShadCN / Tailwind or any other type of Bootstrapped like UI/UX kit and or foundation then measure the nav header implementation by the rulesets of those packages. Material, Apple HIGS, etc. 

Navigation headers are simple to design in nature at first glance.

- Logo / Branding on the left 
- Trailing Icons that contain IX that drive navigation and or actions
- Leading Icons that contain IX that drive navigation and or actions
- Users may also center Logo's than the traditional heuristic of Brand / Logo on the left. 
- The context of the Nav Header should be reflected in the design and the users needs and or requirements. 
- Nav Headers typically have a border at the bottom of them that is about 1px and takes up the entire viewport width 
- Nav Headers may not also have a border at the bottom of them but design in extra margin and padding to accomodate for this.

## Common Nav Header Patterns
- Centered Logo / Branding with Navigation links on the Left and Right. 
- Branding / Logo on the left with navigation links on the right. 
- Branding / Logo on the left with navigation links on the left. 
- Centered Logo / Branding with no navigation links. 
- Centered Logo / Branding with navigation links on the right. 
- Centered Logo / Branding with navigation links on the left.
- Centered Logo / Branding with no navigation links.
- Icon + Logo / Branding centered with navigation links on the left.
- Icon + Logo / Branding centered with navigation links on the right. 
- Icon / Logo on the left with navigation links on the left. 
- Icon / Logo on the left with navigation links on the right.
- Icon / Logo on the left with no navigation links.
- Icon / Logo on the right with navigation links on the left. 
- Icon / Logo on the right with navigation links on the right.
- Icon / Logo on the right with no navigation links.

## Sub Nav Headers 

Sub navigation headers may adopt the same ruleset as main nav headers, but may have different heuristics to guide users. 
Common sub nav headers are usually acting as CTA dividers that prompt a user to explore another area of an app, or page.

- Design the sub nav header similar to the top nav header but it will usually be taller and provide more context for the user.
- Sub nav headers usually include buttons, and primary CTA's that guide user behavior
- Sub nav headers may contain tabs that help route users to the appropriate pages 
- Sub nav headers may not always include a logo/branding
- Sub nav headers should be WCAG compliant, responsive, and user-friendly. 
- Sub nav headers will incorperate and pull in button patterns: ensure that they work, on hover, on click, focus on elements.
- Sub nav headers are usually full width, or contain a container
- Sub nav headers usually are driven by icon + text pairs to drive navigation
- There may be multile sub nav headers on a landing page, north star, or other designated page type, screen, modal pop up, bottom sheet, top sheet
- Sub nav headers need to be Responsive and adhere to the existing ruleset and Design System that the user is developing, and using.
- Sub nav headers may also not include a border at the bottom of them and at the top to indicate a divider.
- Include typical icons such as: Chevrons, down arrows, outbound share icons, link icons, pagination dots, etc.


## Navigation Rules 

- Nav headers should be WCAG compliant, responsive, and user-friendly. 
- Nav headers will incorperate and pull in button patterns: ensure that they work, on hover, on click, focus on elements.
- Design skeleton nav header elements on FTUX, FTUE, and or loading / reload states.
- Ensure that Nav headers have the appropriate margin and padding in responsive design 
- Do not reinvent the wheel. Do not create a nav header unless it is needed. 

## Navigation Headers are not a replacement for page titles 

- Do not use nav headers as page titles. 
- Do not use nav headers to display a breadcrumb trail. 
- Do not use nav headers to display information that is not relevant to navigation. 
- Never use a nav-header to push content down in order to make room for a logo
- Fit the logo inside the navigation header wrapper
- Wrappers define nav header boundaries

## React Component Architecture 
- Next.js and Tailwind CSS
- Use shadcn/ui for component library
- Ensure proper use of flexbox for alignment
- Import existing button components, and navigation components
- Embed Nav header cleanly in a components folder

## Swift Component Architecture 
- XCode project using SwiftUI
- Import existing button components, and navigation components
- Embed Nav header cleanly in a components folder

## C# Unity Component Architecture 
- Create NavHeader.cs and NavHeaderController.cs
- Use Unity UI system 
- Use RectTransform for positioning
- Embed Nav header cleanly in a components folder

## Web Component Architecture 
- React component architecture ruleset should apply here
- Embed Nav header cleanly in a components folder

## Flutter Component Architecture 
- Create NavHeader.dart and NavHeaderController.dart
- Use Flutter UI system 
- Use RectTransform for positioning
- Embed Nav header cleanly in a components folder

## Android Component Architecture 
- Create NavHeader.cs and NavHeaderController.cs
- Use Android UI system 
- Use RectTransform for positioning
- Embed Nav header cleanly in a components folder

## Naming Conventions for Component Architecture

- Class Name "NavHeader.tsx", "NavHeader.jsx", "NavHeader.vue"
- Import @ "../../components/ui/nav-header" and rename 
- There may be multiple component files for the Nav Header, and embedded classes
- Sub Nav headers class name will also be "SubNavHeader.tsx", "SubNavHeader.jsx", "SubNavHeader.vue" but with different component architecture
- Sub Nav Headers should be designed around the existing ruleset for Nav Headers
- Use Hooks if applicable
- Use Tailwind CSS grid and flexbox for alignment


