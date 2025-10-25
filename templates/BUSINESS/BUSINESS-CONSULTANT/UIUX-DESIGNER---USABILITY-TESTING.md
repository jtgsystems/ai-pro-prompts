# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve profession-specific ultimate goals  

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "UI/UX Designer"
profession_category: "Technology / Digital Design"
experience_level: "Beginner to Intermediate (new professionals)"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Target project brief - [e.g., Product goal, User personas, Core features]
   - Format: Project document or brief description  
   - Validation: Verify scope, objectives, and constraints are defined  

2. **Input 2:** Existing design assets - [e.g., Wireframes, UI kit files, Brand guidelines]
   - Format: File paths or links to shared drives
   - Validation: All relevant visual components exist  

3. **Input 3:** Stakeholder contact details - [e.g., Product Owner email, Client reps]
   - Format: Name, role, preferred communication channels  
   - Validation: Confirm access permissions  

4. **Input 4:** Constraints & regulations - [e.g., Accessibility standards WCAG 2.1 AA, Legal requirements]
   - Format: List of compliance checklists
   - Validation: All relevant laws or guidelines are listed  

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Design Thinking Principles  
- Research Focus: Core stages, user empathy techniques  
- Target Sources: Nielsen Norman Group articles, TED Talks on design thinking  
- Deliverable: Empathy map and problem statement  

**Topic 2:** Accessibility Standards (WCAG 2.1 AA)  
- Research Focus: Color contrast ratios, keyboard navigation compliance  
- Target Sources: W3C guidelines, aXe accessibility testing tool  
- Deliverable: WCAG checklist with pass/fail status  

**Topic 3:** User Flow Mapping  
- Research Focus: Prototyping tools for iterative flow diagrams  
- Target Sources: UX design blogs, Figma tutorials  
- Deliverable: High-fidelity user journey map  

**Topic 4:** Interaction Design Patterns  
- Research Focus: Common UI patterns for key screens/functions  
- Target Sources: Interaction Design Foundation courses, UI pattern libraries  
- Deliverable: Pattern catalog with code snippets  

**Topic 5:** Visual Design Trends (2024)  
- Research Focus: Color palettes, typography trends, micro-interactions  
- Target Sources: Dribbble showcases, Behance portfolios, Adobe blogs  
- Deliverable: Trend report with recommended implementations  

**Topic 6:** Usability Testing Frameworks  
- Research Focus: Structured testing methods (e.g., Remote In-Context)  
- Target Sources: Interaction Design Foundation course, Nielsen Norman Group tests  
- Deliverable: Tested usability script with participant criteria  

**Topic 7:** Prototyping Tools & Techniques  
- Research Focus: Rapid prototyping vs. fidelity level for usability testing  
- Target Sources: Figma tutorials, Adobe XD guides, InVision documentation  
- Deliverable: Recommended tool tier matrix and prototype examples  

**Topic 8:** User Experience Metrics Tracking  
- Research Focus: Qualitative + quantitative metrics (e.g., SUS score, time on task)  
- Target Sources: Usability.gov standards, research papers on UX metrics  
- Deliverable: Metric dashboard template with tracking plan  

**Topic 9:** Remote Collaboration Best Practices  
- Research Focus: Tools for co-designing and asynchronous feedback loops  
- Target Sources: Slack workflow guides, Miro collaboration tips, Figma comments  
- Deliverable: Remote work playbook with suggested workflows  

**Topic 10:** Accessibility Testing Protocols  
- Research Focus: Automated + manual testing approaches (axe-core, keyboard navigation)  
- Target Sources: WAVE accessibility tool guide, a11yproject best practices  
- Deliverable: Accessible test checklist and remediation plan  

**Topic 11:** Emerging AI Integration in UX Design  
- Research Focus: How generative AIs are augmenting design workflows (e.g., ChatGPT for copywriting)  
- Target Sources: UI/UX blogs, Fast Company articles on AI + design  
- Deliverable: AI integration roadmap with potential benefits and risks  

**Topic 12:** Portfolio Curation Strategy  
- Research Focus: Showcasing usability testing results in portfolio  
- Target Sources: Behance showcases, Dribbble trends, LinkedIn posts  
- Deliverable: Presentation outline for client-facing usability demo  

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Project Setup**
- **Action:** Create shared project repository (GitHub/GitLab) with branch strategy
- **Tools Needed:** GitHub, Confluence, Slack  
- **Success Criteria:** Repo initialized, branch structure defined  
- **Common Pitfalls:** No version control setup or inadequate documentation  
- **Time Estimate:** 2 hours  

**STEP 2: Empathy & Research Phase**
- **Action:** Conduct stakeholder interviews via Calendly
- **Tools Needed:** Zoom (or similar), Miro for virtual whiteboarding, Notion for notes  
- **Success Criteria:** Interview minutes documented, empathy map completed  
- **Common Pitfalls:** Missing key stakeholders or incomplete recordings  
- **Time Estimate:** 4 days  

**STEP 3: Ideation & Prototyping**
- **Action:** Generate wireframe concepts using FigJam
- **Tools Needed:** Figma (free tier), Adobe XD (free trial)  
- **Success Criteria:** Wireframes approved by stakeholder, high-fidelity mockups created  
- **Common Pitfalls:** Overlooking user constraints or accessibility gaps  
- **Time Estimate:** 5 days  

**STEP 4: Usability Testing Plan**
- **Action:** Define testing objectives, sample size (n=10), and logistics for remote testing
- **Tools Needed:** UserTesting.com (or Lookback.io free tier), Google Forms for pre/post survey  
- **Success Criteria:** Test plan approved by client/stakeholder, recruitment plan in place  
- **Common Pitfalls:** Underestimating participant availability or unclear test scenarios  
- **Time Estimate:** 1 day  

**STEP 5: Conduct Remote Testing Sessions**
- **Action:** Recruit participants via LinkedIn groups, send onboarding email with testing instructions
- **Tools Needed:** UserTesting.com remote sessions, Zoom for live walkthroughs, Hotjar for analytics overlay  
- **Success Criteria:** All tests completed within schedule, data logged in CSV/JSON format  
- **Common Pitfalls:** Participant dropped out or test environment mismatched  
- **Time Estimate:** 3 days  

**STEP 6: Data Analysis**
- **Action:** Use SUS score calculator to quantify satisfaction, analyze heatmaps for interaction patterns
- **Tools Needed:** Hotjar (free tier), Google Analytics, Jupyter Notebook for statistical analysis  
- **Success Criteria:** Usability metrics report generated, key insights documented  
- **Common Pitfalls:** Misinterpreting heatmap data or ignoring qualitative feedback  
- **Time Estimate:** 2 days  

**STEP 7: Iterative Design Updates**
- **Action:** Apply findings to UI flows, adjust color contrast based on WCAG score
- **Tools Needed:** Figma, aXe accessibility plugin, InVision prototype for iteration testing  
- **Success Criteria:** Updated prototypes pass accessibility audit (WCAG AA), usability improvements documented  
- **Common Pitfalls:** Not retesting updated components or ignoring feedback loops  
- **Time Estimate:** 3 days  

**STEP 8: Final Review & Sign-off**
- **Action:** Compile findings into usability report, present to stakeholders via recorded demo
- **Tools Needed:** PowerPoint/Google Slides, Figma for live walkthrough, Zoom for presentation  
- **Success Criteria:** Stakeholder sign-off obtained, final assets versioned in repo  
- **Common Pitfalls:** Overwhelming stakeholders with technical details or missing cultural considerations  
- **Time Estimate:** 1 day  

**STEP 9: Handoff & Documentation**
- **Action:** Update design system documentation (Figma library), share testing report
- **Tools Needed:** Figma docs, Confluence, Notion  
- **Success Criteria:** All assets version-controlled, knowledge transferred to team members  
- **Common Pitfalls:** Incomplete handoff of component libraries or missing change log notes  
- **Time Estimate:** 1 day  

**STEP 10: Post-Launch Monitoring**
- **Action:** Set up analytics dashboard for post-launch metrics (bounce rate, task success)
- **Tools Needed:** Hotjar, Google Analytics, Mixpanel (optional), Slack alerts for critical issues  
- **Success Criteria:** Dashboard populated with real-time data, action items tracked  
- **Common Pitfalls:** No monitoring setup or alerts ignored during peak usage times  
- **Time Estimate:** Ongoing  

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1 (After STEP 2):** Review empathy map and problem statement for stakeholder alignment  
- **Checkpoint 2 (After STEP 4):** Validate testing plan against accessibility standards and legal requirements  
- **Checkpoint 3 (After STEP 7):** Conduct a peer review of usability findings before final sign-off  

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Usability Score (SUS) ≥ 80  
   - Target: 80 or higher on SUS survey  
   - Measurement Method: Conduct post-test SUS questionnaire, calculate average  

2. **Secondary Metrics:**
   - Time on Task ≤ 5 seconds for critical actions  
   - Error Rate < 10% during task completion  
   - Accessibility Compliance (WCAG) ≥ AA  

3. **Long-term Metrics:**
   - User Satisfaction Survey NPS ≥ 50 after 30 days of launch  
   - Maintenance Tickets related to usability ≤ 2 per month  

### Iterative Improvement Loop
1. Measure current performance against targets  
2. Identify top 3 improvement opportunities (based on data)  
3. Implement changes in next sprint cycle  
4. Re-measure and iterate until all metrics met  

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state  
- Key actions taken (e.g., prototyping, testing)  
- Results achieved (measured against SUS score, error rate)  
- ROI or impact metrics  

**2. Detailed Report**
- Complete methodology for each phase  
- All research findings with source citations  
- Implementation details of changes made  
- Before/after comparisons using Hotjar analytics  

**3. Maintenance Plan**
- Ongoing tasks to maintain usability (e.g., quarterly testing)  
- Monitoring schedule (Hotjar dashboard, Google Analytics alerts)  
- Update frequency for design system components  
- Contingency procedures for major UI updates  

**4. Knowledge Transfer**
- Training materials for team members (UX workshop slides)  
- Standard operating procedures for remote collaboration  
- Best practices documentation in Confluence  
- Troubleshooting guide for common usability issues  

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content (e.g., replace "Project brief" with "Sprint backlog for UI/UX design")  
2. **Define 12 Critical Topics** based on:
   - Industry standards (e.g., WCAG, ISO)
   - Latest trends in digital experience
   - Tool integrations and plugins

3. **Map Usability Testing to Measurable Outcomes**
   - Use SMART criteria for each metric (Specific, Measurable, Achievable, Relevant, Time-bound)  
   - Define clear thresholds for pass/fail  

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks (Nielsen Norman Group)
   - Tool vendor best practices (Figma, Hotjar)  
   - Case studies of successful UI/UX implementations in 2024-2025  

5. **Include Latest 2024-2025 Practices**
   - AI-assisted design generation using DALL-E or Midjourney  
   - Real-time collaboration with live commenting via Figma's commenting feature  
   - Automated accessibility testing through Axe-core integration  

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "4 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Design Thinking Principles"
    focus: "Core stages and user empathy techniques"
    sources: ["Nielsen Norman Group", "TED Talks"]
    deliverable: "Empathy map with problem statement"

  - agent_id: 2
    topic: "Accessibility Standards (WCAG 2.1 AA)"
    focus: "Color contrast, keyboard navigation"
    sources: ["W3C Guidelines", "axe-core tool"]
    deliverable: "WCAG checklist with pass/fail status"

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to usability testing outcomes
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking profession task as COMPLETE:

- [ ] **Primary Goal Achieved?** Usability score ≥ 80, all accessibility targets met  
- [ ] **Metrics Validated?** SUS ≥ 80, error rate < 10%, WCAG AA compliance confirmed  
- [ ] **Quality Assessed?** All design components pass technical QA (responsive testing)  
- [ ] **Documentation Complete?** All deliverables uploaded to shared repository, reviewed by stakeholders  
- [ ] **Stakeholder Satisfied?** Client sign-off obtained on final usability report  

### Continuous Improvement
- Document lessons learned from each iteration  
- Update template with new best practices discovered (e.g., AI integration)  
- Share innovations in community forums or Slack channels  
- Schedule a 30-day retrospective to assess post-launch impacts  

---

## TEMPLATE METADATA

**Last Updated:** [2025-04-05]  
**Version:** 1.0  
**Tested With:** UI/UX Design Projects (Sprint cycles)  
**Success Rate:** N/A (first iteration)  
**Average Time to Goal:** 2 weeks for standard projects  

---

