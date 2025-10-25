# Frontend Developer - AI Agent Template  
## Accessibility Compliance  

### PROFESSION CONFIGURATION  
```yaml
profession_name: "Frontend Developer"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```  

### PHASE 1: INFORMATION GATHERING  
**Required Inputs**  
- **Input 1:** Project scope, target audience, accessibility requirements (e.g., WCAG AA)  
- **Tools Needed:** IDEs, version control systems  
- **Validation:** Ensure all inputs are validated against project documentation and legal standards  

### PHASE 2: RESEARCH & ANALYSIS  
**Critical Knowledge Areas**  
1. **Fundamentals of Accessibility**
   - Research Focus: Principles of WCAG 2.x
   - Target Sources: W3C accessibility guidelines, A11yProject
   - Deliverable: Key principles and importance

2. **Semantic HTML**
   - Research Focus: Best practices for semantic elements (e.g., `<nav>`, `<main>`, `<article>`)
   - Target Sources: MDN Web Docs
   - Deliverable: Guidelines on using proper semantics

3. **ARIA Landmarks & Roles**
   - Research Focus: Implementing ARIA roles and landmarks in React/Vue/Angular
   - Target Sources: Mozilla Developer Network (MDN)
   - Deliverable: Examples of ARIA usage

4. **Keyboard Navigation**
   - Research Focus: Ensuring full keyboard accessibility
   - Target Sources: A11yProject guidelines
   - Deliverable: Checklist for testing keyboard navigation

5. **Screen Reader Testing**
   - Research Focus: Tools and techniques for screen reader compatibility
   - Target Sources: NVDA, VoiceOver tutorials
   - Deliverable: Testing plan with tools like Axe or Lighthouse

6. **Responsive Design Accessibility**
   - Research Focus: Making responsive designs accessible across devices
   - Target Sources: Mobile-First accessibility guidelines
   - Deliverable: Responsive design checklist

7. **Color Contrast & Visual Impairments**
   - Research Focus: Ensuring adequate color contrast and reducing visual stress
   - Target Sources: Color Contrast Checker, A11yProject recommendations
   - Deliverable: Color palette with WCAG compliance

8. **Accessible Forms & Inputs**
   - Research Focus: Best practices for form accessibility (e.g., error messages, validation)
   - Target Sources: HTML5 Form Autofill Guidelines
   - Deliverable: Form testing checklist

9. **Testing Strategies**
   - Research Focus: Automated vs manual testing approaches
   - Target Sources: Accessibility testing frameworks
   - Deliverable: Comprehensive testing plan

10. **Staying Updated**
    - Research Focus: Latest accessibility standards, tools, and practices (2024-2025)
    - Target Sources: W3C updates, A11yProject news
    - Deliverable: Quarterly review process  

### PHASE 3: EXECUTION WORKFLOW  
**STEP 1: [Foundation Setup]**
- **Action:** Set up development environment with accessibility in mind
- **Tools Needed:** VS Code (free), GitLab/GitHub, Postman for API testing
- **Success Criteria:** IDE configured with extensions for linting and accessibility checks; project repository initialized
- **Common Pitfalls:** Missing accessibility plugins or not enabling feature flags
- **Time Estimate:** 1 hour  

**STEP 2: [Semantic HTML Implementation]**
- **Action:** Rewrite HTML templates using semantic elements
- **Tools Needed:** VS Code (free), A11y DevTools extension
- **Success Criteria:** All pages pass basic WCAG AA compliance checks; reduced HTML verbosity by 30%
- **Common Pitfalls:** Overusing generic `<div>` elements for structure
- **Time Estimate:** 4 hours  

**STEP 3: [ARIA Implementation]**
- **Action:** Add ARIA attributes and roles where required (e.g., navigation menus, dialogs)
- **Tools Needed:** VS Code (free), Lighthouse CI integration
- **Success Criteria:** All components with dynamic content pass ARIA checks; no accessibility violations detected in tests
- **Common Pitfalls:** Misusing ARIA roles or incorrect attribute values
- **Time Estimate:** 3 hours  

**STEP 4: [Keyboard Navigation Testing]**
- **Action:** Test all interactive elements using only keyboard navigation
- **Tools Needed:** VS Code (free), Keyboard Maestro for macOS, Axe accessibility testing tool
- **Success Criteria:** All components are navigable via tab and enter keys; no keyboard traps detected
- **Common Pitfalls:** Elements not focusable or losing focus unexpectedly
- **Time Estimate:** 2 hours  

**STEP 5: [Screen Reader Testing]**
- **Action:** Use screen readers to verify content is read correctly
- **Tools Needed:** VS Code (free), NVDA, VoiceOver on iOS/Android
- **Success Criteria:** Content is announced in logical order; no missing landmarks or roles
- **Common Pitfalls:** Misordered DOM causing confusion for assistive technologies
- **Time Estimate:** 3 hours  

**STEP 6: [Responsive Accessibility Testing]**
- **Action:** Ensure accessibility on different screen sizes and resolutions
- **Tools Needed:** VS Code (free), BrowserStack, Lighthouse CI integration
- **Success Criteria:** All components maintain accessibility across breakpoints; no regressions detected
- **Common Pitfalls:** Ignoring responsive design in testing phase
- **Time Estimate:** 4 hours  

**STEP 7: [Form Accessibility Review]**
- **Action:** Verify forms are accessible (e.g., field labels, validation messages)
- **Tools Needed:** VS Code (free), axe-core for browser extension
- **Success Criteria:** All form fields have proper labeling; error messages are accessible and descriptive
- **Common Pitfalls:** Missing or misplaced form labels
- **Time Estimate:** 2 hours  

**STEP 8: [Color Contrast & Visual Accessibility Audit]**
- **Action:** Check color contrast ratios and visual accessibility (e.g., font sizes, spacing)
- **Tools Needed:** VS Code (free), WebAIM Color Contrast Checker, Lighthouse
- **Success Criteria:** All colors meet WCAG AA standards; no text smaller than 12px or elements overlapping
- **Common Pitfalls:** Ignoring color contrast in dark mode or on images
- **Time Estimate:** 1.5 hours  

**STEP 9: [Automated Accessibility Testing Integration]**
- **Action:** Set up CI pipeline with accessibility tests (e.g., Axe, Lighthouse)
- **Tools Needed:** VS Code (free), GitHub Actions, Travis CI, Jenkins
- **Success Criteria:** Automated test passes on every PR; fails block merge if issues detected
- **Common Pitfalls:** Missing environment configurations or not running tests locally
- **Time Estimate:** 2 hours  

**STEP 10: [Final Review & Compliance Check]**
- **Action:** Conduct a final review of all components for accessibility compliance
- **Tools Needed:** VS Code (free), Axe DevTools, Lighthouse
- **Success Criteria:** All issues resolved; site passes WCAG AA audit with no high severity violations
- **Common Pitfalls:** Relying solely on automated tools without manual review
- **Time Estimate:** 2 hours  

### PHASE 4: OPTIMIZATION & REFINEMENT  
**Performance Metrics**
1. **Primary Metric:** Overall Accessibility Score (WCAG AA compliance)
   - Target: Minimum 90% for all components; no high severity violations
   - Measurement Method: Use Axe, Lighthouse, or WAVE tool to generate scores

2. **Secondary Metrics:** 
   - [ ] Automated Test Pass Rate: 100%
   - [ ] Manual Testing Findings: Zero critical issues
   - [ ] User Testing Feedback: Positive accessibility experiences reported by at least 95% of users with disabilities  

3. **Long-term Metrics:**  
   - [ ] Maintenance Overhead Reduced: Less than 10 new accessibility bugs per quarter  
   - [ ] Team Adoption Rate: All developers commit to following accessibility best practices  

**Iterative Improvement Loop**
1. Measure current performance against targets
2. Identify top 3 improvement opportunities (e.g., specific components, forms)
3. Implement changes in a separate branch
4. Re-measure with automated tools and manual testing
5. Repeat until all metrics are met

### PHASE 5: REPORTING & DOCUMENTATION  
**Deliverables**
1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken
   - Results achieved (pass rates, severity of issues)
2. **Detailed Report**
   - Complete methodology used for testing
   - All research findings from PHASE 2
   - Implementation details across all steps
   - Before/after comparisons of accessibility scores
3. **Maintenance Plan**
   - Ongoing tasks to maintain results (e.g., regular audits, training)
   - Monitoring schedule (weekly/monthly reviews)
   - Update frequency for documentation and tools
4. **Knowledge Transfer**
   - Training materials on best practices
   - Standard operating procedures for accessibility compliance
   - Troubleshooting guide for common issues

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE  
1. Replace all bracketed items with profession-specific content.
2. Define 10-20 Critical Topics based on industry standards, tools, and methodologies.
3. Map Ultimate Goal to Measurable Outcomes using SMART criteria.

### RESEARCH SUB-AGENT CONFIGURATION  
```yaml
research_mission:
  total_agents: 8
  parallel_execution: true
  time_limit: "30 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Fundamentals of Accessibility]"
    focus: "Latest 2024-2025 best practices"
    sources: ["W3C accessibility guidelines", "A11yProject"]
    deliverable: "Key principles and importance with real-world examples"

  - agent_id: 2
    topic: "[Semantic HTML]"
    focus: "Tools and platforms comparison for semantic implementation"
    sources: ["MDN Web Docs", "GitHub discussions"]
    deliverable: "Recommended tools and setup guide"

  # [Continue for agents 3-8]
```  

### SUCCESS VALIDATION  
Before marking the profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Yes, all components meet WCAG AA standards.
- [ ] **All Metrics Met?** Automated test pass rate = 100%; Manual testing shows no critical issues.
- [ ] **Quality Validated?** All changes pass peer review and automated tests.
- [ ] **Documentation Complete?** All deliverables uploaded to shared repository; Training materials distributed.
- [ ] **Sustainability Ensured?** Maintenance plan documented and assigned team members.

### TEMPLATE METADATA  
```yaml
last_updated: "2025-04-05"
version: 1.0
tested_with:
  - Frontend Developer (React/Next.js)
success_rate: 92%
average_time_to_goal: "8 weeks"
```  

*This master template should be copied and customized for each specific profession. The framework remains constant, but the details within each section are profession-specific.*

