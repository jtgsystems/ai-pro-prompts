# Frontend Developer - AI Agent Template

## React/Vue Component Library

### 1. Critical Knowledge Areas

- **JavaScript ES6+**: Understanding modern JavaScript syntax, modules, and features.
- **React or Vue.js**: Proficiency in building components, state management (useState, useReducer), lifecycle methods (hooks for React), and routing.
- **TypeScript**: Type safety and advanced TypeScript features for large codebases.
- **CSS/SCSS**: Styling with CSS Grid, Flexbox, responsive design, and SCSS syntax.
- **State Management Libraries**: Redux for React or Vuex for Vue to manage global state effectively.
- **Component Design Systems**: Principles of creating reusable UI components.
- **Performance Optimization**: Techniques like lazy loading, code splitting, and optimizing images.
- **Testing**: Unit testing with Jest (React) or Mocha (Vue), integration testing, and end-to-end testing with Cypress or Playwright.
- **Deployment Strategies**: Best practices for deploying libraries on npm, GitHub Packages, or similar platforms.
- **Accessibility**: Implementing ARIA roles, keyboard navigation, and ensuring compliance with WCAG guidelines.
- **Version Control**: Using Git for collaboration, branching strategies (Gitflow), and merge requests.

### 2. Execution Steps

1. **Set Up Development Environment**
   - Install Node.js LTS from the official website.
   - Use Visual Studio Code (VS Code) as your primary IDE.

2. **Create a New Component Library Project**
   - Initialize a new React or Vue project using `create-react-app` or `vue-cli`.
   - Organize the directory structure to separate components, styles, and scripts.

3. **Develop Core Components**
   - Start with basic UI components like buttons, input fields, dropdowns, etc.
   - Implement accessibility features in all components.

4. **Implement State Management**
   - For React: Integrate Redux or MobX for global state management.
   - For Vue: Use Vuex to manage state across the application.

5. **Create Custom Hooks (if using React)**
   - Develop reusable logic that can be shared between components, such as data fetching or form validation.

6. **Style Components**
   - Utilize CSS/SCSS for styling components consistently.
   - Ensure responsiveness and cross-browser compatibility.

7. **Testing**
   - Write unit tests for each component using Jest (React) or Mocha (Vue).
   - Conduct integration tests to ensure components work well together.
   - Use Cypress or Playwright for end-to-end testing.

8. **Documentation**
   - Generate API documentation automatically using tools like Storybook or JSDoc.
   - Provide usage examples and customization options in the README.

9. **Performance Optimization**
   - Implement code splitting and lazy loading to reduce initial load time.
   - Optimize images and assets for faster delivery.

10. **Deployment**
    - Set up a GitHub repository and configure continuous integration (CI) with actions.
    - Publish your component library on npm or GitHub Packages.

### 3. Tools, Software, and Platforms

- **IDE**: Visual Studio Code (VS Code)
- **Version Control**: Git + GitHub/GitLab/Bitbucket
- **State Management**:
  - Redux (React)
  - Vuex (Vue)
- **Styling**:
  - CSS/SCSS
  - TailwindCSS or Bootstrap for utility-first styling
- **Testing**:
  - Jest (React)
  - Mocha + Chai (Vue)
  - Cypress or Playwright
- **Documentation**: Storybook, JSDoc
- **CI/CD**: GitHub Actions, GitLab CI

### 4. Success Criteria

- **Code Quality**: Code passes linting and formatting checks without errors.
- **Testing Coverage**: Achieve at least 80% coverage for all components using Jest or Mocha.
- **Documentation**: Comprehensive API documentation with examples.
- **Performance Metrics**: Load time under 2 seconds on a standard connection, as measured by Lighthouse.
- **User Adoption**: At least 10 contributors and 5 dependent projects using the component library.

### 5. Troubleshooting

- **Component Not Rendering**: Check for TypeScript errors or missing dependencies in `package.json`.
- **State Management Issues**: Ensure actions are dispatched correctly and reducers handle state changes accurately.
- **Style Overriding**: Use CSS Modules to isolate styles and avoid global style conflicts.
- **Test Failures**: Review test cases, ensure they cover both happy paths and edge cases.

### 6. Recommended Tool Stack

#### Primary Tools (Free/Open Source)

- **IDE**: Visual Studio Code
- **Version Control**: Git + GitHub
- **State Management**:
  - Redux for React
  - Vuex for Vue
- **Styling**: CSS/SCSS
- **Testing**: Jest, Mocha, Cypress
- **Documentation**: Storybook
- **CI/CD**: GitHub Actions

#### Optional/Premium Tools (Paid Alternatives)

- **IDE**: Sublime Text ($75)
- **Version Control**: GitLab Premium features
- **State Management**:
  - MobX for React (optional premium support)
  - Nuxt.js for Vue (offers more built-in functionality and server-side rendering capabilities)
- **Styling**: Tailwind CSS Pro Edition
- **Testing**: Jest with snapshots testing or Mocha with coverage reports
- **Documentation**: JSDoc Pro

### 7. Timeline to Achieve React/Vue Component Library

**Month 1: Setup and Core Development**
- Week 1: Set up development environment, install tools.
- Week 2-3: Create a new component library project, develop core components.

**Month 2: State Management and Testing**
- Week 4: Implement state management solutions (Redux/Vuex).
- Week 5-6: Write unit tests for all components, implement custom hooks if necessary.

**Month 3: Styling and Documentation**
- Week 7: Style components using CSS/SCSS or TailwindCSS.
- Week 8: Generate API documentation with Storybook and write README.

**Month 4: Performance Optimization and Deployment**
- Week 9: Optimize performance (code splitting, lazy loading).
- Week 10: Set up CI/CD pipeline, deploy the library on npm or GitHub Packages.

### 8. Best Practices and AI Integration for 2024-2025

- **Adopt TypeScript**: Enhance code quality with static typing.
- **Use AI for Code Generation**: Leverage tools like Tabnine to suggest code patterns efficiently.
- **Continuous Learning**: Subscribe to newsletters on React or Vue updates, follow relevant GitHub repositories.
- **Community Engagement**: Contribute back to the community by fixing issues and submitting pull requests to open-source projects using your library.

This comprehensive guide provides a structured approach for new Frontend Developers aiming to create and manage a robust React/Vue Component Library. By adhering to these steps and utilizing the recommended tools, developers can achieve high-quality outcomes while staying aligned with industry best practices.

