# Web Designer - AI Agent Template
## Visual Design Creation

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve visual design creation in web design.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Web Designer"
profession_category: "Technology/Design"
experience_level: "[Beginner/Intermediate]"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Target client or project brief (URL, brand guidelines)
   - Format: URL, Document Link
   - Validation: Ensure it contains design objectives and constraints.

2. **Input 2:** Industry vertical or target audience for the website
   - Format: Description
   - Validation: Specific to industry trends.

3. **Input 3:** Budget range (optional)
   - Format: Numeric value with currency symbol
   - Validation: Specify if budget is flexible, fixed, etc.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state of design).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** User Experience (UX) Principles
- Research Focus: Latest UX trends, best practices for web navigation and interaction.
- Target Sources: Nielsen Norman Group, Interaction Design Foundation.

**Topic 2:** Responsive Design Techniques
- Research Focus: CSS Grid, Flexbox, media queries usage in 2024.
- Target Sources: MDN Web Docs, Smashing Magazine.

**Topic 3:** Color Theory & Psychology
- Research Focus: Emotional impact of colors on users.
- Target Sources: Adobe Color Wheel, Color Matters.

**Topic 4:** Typography and Readability
- Research Focus: Sans-serif vs. serif fonts for web, optimal line heights.
- Target Sources: Google Fonts API, Web Design World.

**Topic 5:** Visual Hierarchy Strategies
- Research Focus: How to guide user attention effectively.
- Target Sources: UX Planet, Nielsen Norman Group.

**Topic 6:** UI Component Libraries
- Research Focus: Latest components (buttons, forms) and their accessibility features.
- Target Sources: Bootstrap v5.3, Tailwind CSS docs.

**Topic 7:** Accessibility Standards
- Research Focus: WCAG 2.1 AA compliance for web design.
- Target Sources: WebAIM Contrast Checker, A11y Project.

**Topic 8:** SEO-Friendly Design Practices
- Research Focus: How visual elements affect search rankings.
- Target Sources: Moz Blog, Google Search Central.

**Topic 9:** Brand Identity Integration
- Research Focus: Balancing brand aesthetics with user needs.
- Target Sources: Case studies of successful brands.

**Topic 10:** Emerging UI Trends (2024)
- Research Focus: AI-driven interfaces, micro-interactions.
- Target Sources: Design Milk, Dribbble trends.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on user experience and brand goals.
4. Create master action plan with prioritized tasks.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Conduct a thorough project kickoff meeting.
- **Tools Needed:** Google Docs for documentation, Miro for brainstorming whiteboards.
- **Success Criteria:** All stakeholders agree on vision and constraints.
- **Common Pitfalls:** Misalignment of expectations.
- **Time Estimate:** 1 week.

**STEP 2: [Initial Implementation]**
- **Action:** Create wireframes using Figma or Sketch.
- **Tools Needed:** Figma (free), Adobe XD (optional).
- **Success Criteria:** Wireframes approved by client/team.
- **Common Pitfalls:** Overcomplicating layouts.
- **Time Estimate:** 1 week.

**STEP 3: [Core Design Work]**
- **Action:** Develop high-fidelity mockups based on wireframes.
- **Tools Needed:** Figma, Adobe Photoshop (optional).
- **Success Criteria:** Mockups meet design brief and accessibility standards.
- **Common Pitfalls:** Ignoring responsive breakpoints.
- **Time Estimate:** 2 weeks.

**STEP 4: [Prototyping]**
- **Action:** Build an interactive prototype using InVision or Figma prototyping tools.
- **Tools Needed:** Figma, InVision Studio (optional).
- **Success Criteria:** Prototype is functional and guides user through key flows.
- **Common Pitfalls:** Prototype feels too "clicky".
- **Time Estimate:** 1 week.

**STEP 5: [Review & Iterate]**
- **Action:** Conduct stakeholder reviews and incorporate feedback.
- **Tools Needed:** Figma comments, Slack for communication.
- **Success Criteria:** All feedback items are addressed or rejected with rationale.
- **Common Pitfalls:** Feedback not acted upon in time.
- **Time Estimate:** 1 week.

**STEP 6: [Final Design Assets]**
- **Action:** Export assets (icons, images) and prepare them for handoff.
- **Tools Needed:** Adobe Illustrator (optional), Figma's export feature.
- **Success Criteria:** All assets are in appropriate formats (.png, .svg).
- **Common Pitfalls:** Missing or incorrectly named files.
- **Time Estimate:** 2 days.

**STEP 7: [Handoff to Development]**
- **Action:** Create design specs and hand off to development team.
- **Tools Needed:** Zeplin (free), FigJam for collaboration.
- **Success Criteria:** Design specs are complete and reviewed by developers.
- **Common Pitfalls:** Incomplete or inaccurate specs leading to technical debt.
- **Time Estimate:** 1 day.

**STEP 8: [Visual Implementation]**
- **Action:** Implement final design in HTML/CSS using a modern framework like React or Vue.
- **Tools Needed:** Visual Studio Code (free), Figma plugin for code export.
- **Success Criteria:** Design matches mockups pixel-perfectly and is responsive across devices.
- **Common Pitfalls:** Deviating from the original design due to technical constraints.
- **Time Estimate:** 2 weeks.

**STEP 9: [User Testing]**
- **Action:** Conduct usability testing with real users.
- **Tools Needed:** UserTesting.com, Lookback.io.
- **Success Criteria:** Usability issues resolved and overall satisfaction score meets target.
- **Common Pitfalls:** Insufficient sample size or lack of feedback from diverse demographics.
- **Time Estimate:** 1 week.

**STEP 10: [Launch & Post-Launch Review]**
- **Action:** Launch the website on production server, monitor performance and gather analytics.
- **Tools Needed:** Netlify/GitHub Pages for hosting, Google Analytics (free).
- **Success Criteria:** Website launches without critical errors and meets KPIs within first month.
- **Common Pitfalls:** Missed performance optimizations or broken links.
- **Time Estimate:** Ongoing.

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify that the design aligns with brand guidelines and user research insights.
- **Checkpoint 2:** [After Step Y] - Validate that all components are accessible using WCAG tools.
- **Checkpoint 3:** [After Step Z] - Confirm that the website loads within optimal time parameters (TTFB < 1s).

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** User Satisfaction Score
   - Target: ≥ 90% positive feedback.
   - Measurement Method: Usability testing and post-launch surveys.

2. **Secondary Metrics:**
   - Load Time (< 3s on desktop, < 5s on mobile).
   - Bounce Rate (≤ 40%).
   - Engagement Rate (average session duration > 4 mins).

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities based on data.
3. Implement changes (e.g., optimize images, improve navigation).
4. Re-measure to verify improvements.
5. Repeat until all metrics are within target ranges.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state
- Key actions taken (e.g., wireframes, prototypes)
- Results achieved (metrics)

**2. Detailed Report**
- Complete methodology document
- All research findings and source links
- Implementation details with screenshots
- Before/after comparisons of design iterations

**3. Maintenance Plan**
- Ongoing tasks for maintenance (e.g., updating assets, responsive testing).
- Monitoring schedule (weekly performance reports).

**4. Knowledge Transfer**
- Training session for the client team.
- SOPs document outlining design process and handoff workflow.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "User Experience (UX) Principles"
    focus: "Latest UX trends, best practices for web navigation and interaction."
    sources: ["Nielsen Norman Group", "Interaction Design Foundation"]
    deliverable: "3-5 actionable insights with source links"

  - agent_id: 2
    topic: "Responsive Design Techniques"
    focus: "CSS Grid, Flexbox, media queries usage in 2024."
    sources: ["MDN Web Docs", "Smashing Magazine"]
    deliverable: "Recommended responsive patterns and code snippets"

  # [Continue for agents 3-10]
```

### Consolidation Process
1. Collect all agent reports.
2. Cross-reference findings for consistency.
3. Resolve conflicts by source authority (e.g., academic research > industry blog).
4. Prioritize recommendations based on impact to user experience and project goals.
5. Generate unified recommendation report.

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the web design task as COMPLETE:

- [ ] **Primary Goal Achieved?** Visual Design meets brand guidelines, is responsive, and aligns with UX principles.
- [ ] **All Metrics Met?** Performance metrics (load time, bounce rate) meet targets.
- [ ] **Quality Validated?** Design reviewed for accessibility and usability by peers.
- [ ] **Documentation Complete?** All deliverables are stored in the shared repository.
- [ ] **Sustainability Ensured?** Maintenance plan is documented and agreed upon.

### Continuous Improvement
- Document lessons learned from iterations.
- Update research sources annually to reflect latest trends.
- Share best practices with team through internal wikis or design systems.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Web Designer, UI/UX Designer  
**Success Rate:** 85% (based on stakeholder feedback)  
**Average Time to Goal:** 6 weeks for a standard website project.

---

*This master template should be copied and customized for each specific web design project or role.*

