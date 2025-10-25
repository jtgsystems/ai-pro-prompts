# UI/UX Designer - AI Agent Template
## Design System Creation

### PROFESSION CONFIGURATION
```yaml
profession_name: "UI/UX Designer"
profession_category: "Design"
experience_level: "Beginner to Intermediate"
```

### PHASE 1: INFORMATION GATHERING
**Primary Objective:** Create a scalable, maintainable design system that streamlines UI/UX development across multiple platforms and teams.

#### Required Inputs
1. **Target Platform(s):**
   - Mobile (iOS & Android)
   - Web (Desktop & Tablet)
2. **Project Scope:**
   - Core products/services to be included.
3. **Stakeholder Requirements:**
   - User research findings, business goals, regulatory constraints.
4. **Team Structure:**
   - Roles and responsibilities of designers, developers, product managers.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received (Yes/No)
- [ ] Validate input quality and completeness (Yes/No)
- [ ] Identify immediate red flags or blockers (List)
- [ ] Establish baseline metrics (current state documentation)

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas
**Topic 1:** Design System Fundamentals  
- **Research Focus:** Core principles, components hierarchy, accessibility guidelines.
- **Target Sources:** Nielsen Norman Group articles, Material Design specifications.

**Topic 2:** Responsive Design Patterns  
- **Research Focus:** Grid systems, breakpoints, media queries.
- **Target Sources:** Bootstrap documentation, Adobe XD tutorials.

**Topic 3:** Typography System  
- **Research Focus:** Font stacks, sizes, spacing, weight hierarchy.
- **Target Sources:** Google Fonts API, CSS Tricks articles.

**Topic 4:** Color Palette Standardization  
- **Research Focus:** Harmonious palettes, contrast ratios, brand guidelines.
- **Target Sources:** Coolors, Adobe Color.

**Topic 5:** Iconography & Illustration Style  
- **Research Focus:** Consistent icon sets, style guides for illustrations.
- **Target Sources:** Font Awesome, Heroicons, Dribbble trends.

**Topic 6:** Component Library Design  
- **Research Focus:** UI components (buttons, cards, forms), patterns for common interactions.
- **Target Sources:** Atomic Design methodology, Sketch plugins.

**Topic 7:** Accessibility Compliance  
- **Research Focus:** WCAG guidelines, ARIA attributes, keyboard navigation testing.
- **Target Sources:** W3C accessibility standards, Lighthouse audits.

**Topic 8:** Brand Consistency Guidelines  
- **Research Focus:** Visual identity elements, tone of voice.
- **Target Sources:** Brand books, mood boards from Behance.

**Topic 9:** Version Control & Collaboration Workflow  
- **Research Focus:** Git branching strategies for design assets, Figma sharing protocols.
- **Target Sources:** GitHub guides, InVision collaboration features.

**Topic 10:** Prototyping Tools Integration  
- **Research Focus:** Real-time prototyping platforms, interactive state management.
- **Target Sources:** Figma tutorials, Adobe XD capabilities.

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process
**STEP 1: Research and Specification**
- **Action:** Conduct user research, analyze competitors' systems.
- **Tools Needed:** Figma, Miro (for collaborative whiteboards).
- **Success Criteria:** Comprehensive spec document covering components, states, guidelines.

**STEP 2: Component Library Creation**
- **Action:** Design base UI components in Figma/Sketch using consistent styles.
- **Tools Needed:** Figma (free version), Sketch (optional for prototyping).
- **Success Criteria:** At least 15 foundational components documented with variations and usage examples.

**STEP 3: System Documentation**
- **Action:** Write design system documentation including naming conventions, component hierarchy, accessibility guidelines.
- **Tools Needed:** Markdown editor, Notion (free alternative).
- **Success Criteria:** Well-organized document accessible to all team members.

**STEP 4: Integration Planning**
- **Action:** Plan how the design system will be integrated into existing workflows and projects.
- **Tools Needed:** Confluence, Trello.
- **Success Criteria:** Detailed integration plan approved by stakeholders.

**STEP 5: Testing & Validation**
- **Action:** Conduct usability testing with real users on prototypes using the new components.
- **Tools Needed:** UserTesting.com (free trials available), UsabilityHub.
- **Success Criteria:** Meets accessibility standards and user satisfaction >80%.

**STEP 6: Version Control Setup**
- **Action:** Set up version control for design assets, establish naming conventions for files/folders.
- **Tools Needed:** Git (GitHub free tier), Figma's built-in sharing features.
- **Success Criteria:** All team members can access and contribute to the system with minimal friction.

**STEP 7: Training & Knowledge Transfer**
- **Action:** Develop training materials, conduct workshops for the design and development teams.
- **Tools Needed:** Zoom (free), Loom videos, SlideShare presentations.
- **Success Criteria:** 90% of team members trained on how to use the new system.

**STEP 8: Iterative Refinement**
- **Action:** Regularly update components based on feedback and new user insights.
- **Tools Needed:** Figma prototyping tools for quick iterations.
- **Success Criteria:** System is considered current by all stakeholders.

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
1. **Primary Metric:** Time to create a new feature using the design system.
   - Target: Reduced from X hours to Y hours within 3 months post-deployment.
2. **Secondary Metrics:**
   - User satisfaction with new features (NPS).
   - Number of accessibility issues reported.

#### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top improvement opportunities (e.g., components needing updates, documentation gaps).
3. Implement changes based on feedback and metrics.
4. Re-measure to confirm improvements.

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
**1. Executive Summary**
- Current state vs. target state.
- Key actions taken.
- Results achieved (quantitative data).

**2. Detailed Report**
- Methodology used for research and implementation.
- All design decisions with rationale.
- Implementation details, including timelines.

**3. Maintenance Plan**
- Ongoing tasks to maintain system quality.
- Monitoring schedule for usage and updates.
- Update frequency (e.g., quarterly review).

**4. Knowledge Transfer**
- Training materials: Figma templates, style guides.
- SOPs for contributing to the design system.
- Troubleshooting guide with common issues.

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE
Replace all bracketed items with specific data relevant to your project or company.

### HOW TO ADAPT THIS TEMPLATE

1. Replace **[BRACKETED]** placeholders with actual inputs for your project.
2. Define 10-20 critical topics based on the latest UI/UX trends and standards.
3. Map the ultimate goal to measurable outcomes using SMART criteria.
4. Build a step-by-step workflow from industry best practices, tool vendor guides, and expert experiences.

### RESEARCH SUB-AGENT CONFIGURATION
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Design System Fundamentals"
    focus: "Core principles, components hierarchy"
    sources: ["Nielsen Norman Group", "Material Design"]
    deliverable: "3-5 actionable insights with citations"

  - agent_id: 2
    topic: "Responsive Design Patterns"
    focus: "Grid systems, breakpoints"
    sources: ["Bootstrap Docs", "Adobe XD Tutorials"]
    deliverable: "Recommended responsive patterns and best practices"

  # Continue for agents 3-10...

consolidation_process:
  - Collect all agent reports.
  - Cross-reference findings for consistency.
  - Resolve conflicts by source authority.
  - Prioritize recommendations by impact to ultimate goal.
  - Generate unified recommendation report.
```

### SUCCESS VALIDATION
Before marking the profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** (Yes/No)
- [ ] **All Metrics Met?** (Yes/No)
- [ ] **Quality Validated?** (Yes/No)
- [ ] **Documentation Complete?** (Yes/No)
- [ ] **Sustainability Ensured?** (Yes/No)
- [ ] **Client/User Satisfied?** (Yes/No)

### CONTINUOUS IMPROVEMENT
Document lessons learned, update the template with new best practices, share innovations in design community forums, and schedule periodic reviews.

---

*This master template should be copied and customized for each specific profession. The framework remains constant, but the details within each section are profession-specific.*

