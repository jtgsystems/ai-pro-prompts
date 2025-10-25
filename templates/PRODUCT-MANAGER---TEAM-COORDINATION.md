# Product Manager - AI Agent Template
## Team Coordination

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve product management team coordination.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Product Manager"
profession_category: "Technology/Engineering"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve seamless cross-functional collaboration and alignment within the product development lifecycle, resulting in on-time delivery of high-quality products that meet market needs and organizational goals.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** Product Vision Statement  
   - Format: Text (max 150 words)  
   - Validation: Concise, inspiring, and aligned with business strategy.
2. **Input 2:** Target Customer Segments  
   - Format: List of personas or segments  
   - Validation: Each segment defined by demographics, needs, pain points.
3. **Input 3:** Key Performance Indicators (KPIs) for Team Coordination  
   - Format: Metrics (e.g., cycle time, on-time delivery rate)  
   - Validation: Measurable and tied to team performance.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Agile Methodologies  
- **Research Focus:** Latest frameworks, tools, and practices for agile implementation.  
- **Target Sources:** Scrum.org, Atlassian's Agile University, industry case studies.

**Topic 2:** Product Development Lifecycle (PDL)  
- **Research Focus:** Best practices for each stage: discovery, design, development, testing, launch.  
- **Target Sources:** Lean Startup Playbook, product management blogs.

**Topic 3:** Stakeholder Management  
- **Research Focus:** Techniques for aligning stakeholders and managing expectations.  
- **Target Sources:** Intercom's Guide to Customer Feedback, Crucial Conversations books.

**Topic 4:** Cross-functional Team Alignment  
- **Research Focus:** Tools and rituals that facilitate collaboration across engineering, design, UX, sales, support, etc.  
- **Target Sources:** Remote.io's guide to distributed teams, Asana Ultimate Guide.

**Topic 5:** Communication Protocols  
- **Research Focus:** Daily stand-ups, sprint reviews, retrospectives, documentation standards.  
- **Target Sources:** ProductOps Institute, Confluence best practices.

**Topic 6:** Version Control & Collaboration Tools**  
- **Research Focus:** Latest features in Git, GitHub Actions, and other collaboration platforms.  
- **Target Sources:** GitHub's official docs, Atlassian Bitbucket tutorials.

**Topic 7:** Project Management Software**  
- **Research Focus:** Integration capabilities with Agile boards, roadmaps, and scheduling tools.  
- **Target Sources:** Jira Data Center User Guide, Asana Ultimate Guide.

**Topic 8:** Continuous Integration/Continuous Deployment (CI/CD)**  
- **Research Focus:** Best practices for automated testing, deployment pipelines, and rollback processes.  
- **Target Sources:** Jenkins Documentation, CircleCI Guides.

**Topic 9:** Defect Tracking & Quality Assurance**  
- **Research Focus:** Tools for logging bugs, tracking fixes, and ensuring quality standards are met.  
- **Target Sources:** Bugzilla Official Docs, Jira Issue Management Guide.

**Topic 10:** Market Research & Competitive Analysis**  
- **Research Focus:** Methods for gathering customer insights and competitor benchmarking.  
- **Target Sources:** Google Trends API, SEMrush tutorials.

**Topic 11:** Customer Feedback Loops**  
- **Research Focus:** Tools for collecting, analyzing, and acting on user feedback in real-time.  
- **Target Sources:** Hotjar for analytics, Typeform for surveys.

**Topic 12:** Cross-functional Team Enablement**  
- **Research Focus:** Training programs, workshops, and resources to upskill team members.  
- **Target Sources:** Coursera's product management courses, LinkedIn Learning.

**Topic 13:** Regulatory Compliance & Security Standards**  
- **Research Focus:** Ensuring products meet industry regulations (e.g., GDPR, HIPAA) and security best practices.  
- **Target Sources:** OWASP Top 10 Guide, NIST Cybersecurity Framework.

**Topic 14:** Remote Team Collaboration Best Practices**  
- **Research Focus:** Strategies for maintaining engagement, productivity, and culture in distributed teams.  
- **Target Sources:** Zapier's guide to remote work, Buffer's article on team collaboration tools.

**Topic 15:** AI & Automation Integration**  
- **Research Focus:** Tools that can automate routine tasks or augment decision-making (e.g., chatbots for support requests).  
- **Target Sources:** Rasa Docs for conversational AI, Zapier's automation guide.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact to team coordination.
4. Create master action plan with clear timelines and ownership.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Kickoff & Vision Alignment]**
- **Action:** Host a kickoff meeting, share vision statement, and establish product roadmap.  
- **Tools Needed:** Zoom (free), Miro (free for teams of <15), Notion (free).  
- **Success Criteria:** All stakeholders sign off on the vision and roadmap within 3 days.  
- **Common Pitfalls:** Lack of stakeholder engagement or unclear communication channels.  
- **Time Estimate:** 1 week.

**STEP 2: [Define & Prioritize Requirements]**
- **Action:** Conduct workshops to elicit requirements from customers, internal teams, and market research.  
- **Tools Needed:** SurveyMonkey (free tier), Jira Software (free for small projects).  
- **Success Criteria:** Top 10 prioritized features documented with acceptance criteria.  
- **Common Pitfalls:** Scope creep or unclear priorities.  
- **Time Estimate:** 1 week.

**STEP 3: [Design & Prototyping]**
- **Action:** Lead design sessions, create wireframes, and develop high-fidelity mockups.  
- **Tools Needed:** Figma (free tier), Adobe XD (free trial), InVision (free for students/staff).  
- **Success Criteria:** Design system approved by stakeholders and technical feasibility documented.  
- **Common Pitfalls:** Poor communication between design and development teams.  
- **Time Estimate:** 2 weeks.

**STEP 4: [Development Sprint Planning]**
- **Action:** Break down features into user stories, estimate effort using T-shirt sizes or story points, and assign to developers.  
- **Tools Needed:** Jira Agile Boards (free), Azure DevOps Agile Boards (free).  
- **Success Criteria:** All tasks linked to epics, with clear owners and due dates.  
- **Common Pitfalls:** Insufficient capacity planning or unclear dependencies.  
- **Time Estimate:** 1 week.

**STEP 5: [Development & Code Review]**
- **Action:** Developers implement features, code is committed to the main branch after peer review.  
- **Tools Needed:** GitHub Actions (free), GitLab CI/CD (free tier).  
- **Success Criteria:** All commits pass automated tests and are reviewed by at least one teammate.  
- **Common Pitfalls:** Manual bypasses of reviews or failing tests.  
- **Time Estimate:** Ongoing.

**STEP 6: [Automated Testing & Deployment]**
- **Action:** Run automated test suites, deploy to staging, conduct UAT (User Acceptance Testing).  
- **Tools Needed:** Jenkins (free), CircleCI (free tier), LaunchDarkly (free for <10 flags).  
- **Success Criteria:** All tests pass in CI pipeline, no critical blockers on staging.  
- **Common Pitfalls:** Incomplete test coverage or missed security scans.  
- **Time Estimate:** 1 day per sprint.

**STEP 7: [Release to Production]**
- **Action:** Coordinate with the release manager to promote changes from staging to production.  
- **Tools Needed:** GitHub Actions, LaunchDarkly (for feature flag management).  
- **Success Criteria:** Release notes published, rollback plan in place if needed.  
- **Common Pitfalls:** Lack of communication between teams or incomplete documentation.  
- **Time Estimate:** 1 day per release.

**STEP 8: [Post-release Monitoring & Feedback Loop]**
- **Action:** Track key metrics post-launch (e.g., error rates, performance), gather user feedback via surveys and analytics tools.  
- **Tools Needed:** Mixpanel (free tier), Amplitude (free for <10k events/month), Sentry (open source).  
- **Success Criteria:** No critical errors exceeding SLA thresholds, positive NPS scores from users.  
- **Common Pitfalls:** Failure to react quickly to issues or siloed feedback collection.  
- **Time Estimate:** Ongoing.

**STEP 9: [Retrospective & Continuous Improvement]**
- **Action:** Hold a sprint retrospective meeting to identify areas for improvement and capture lessons learned.  
- **Tools Needed:** Miro (free), Notion (free).  
- **Success Criteria:** Action items from the retrospective are added to the backlog within 48 hours.  
- **Common Pitfalls:** Lack of action on findings or blame culture during retrospectives.  
- **Time Estimate:** 1 hour per sprint.

**STEP 10: [Quarterly Team Alignment Review]**
- **Action:** Hold a quarterly meeting with all product stakeholders to review progress, re-prioritize features, and adjust the roadmap.  
- **Tools Needed:** Google Meet (free), Teams (if using Office 365).  
- **Success Criteria:** Updated roadmap shared and approved by leadership within 2 weeks.  
- **Common Pitfalls:** Inadequate visibility into team status or missed alignment sessions.  
- **Time Estimate:** Quarterly.

---

### Quality Checkpoints
1. **Checkpoint 1:** After STEP 4 - Verify all tasks are linked, assigned, and have clear due dates.
2. **Checkpoint 2:** After STEP 6 - Ensure CI pipeline passes without critical failures.
3. **Checkpoint 3:** After STEP 7 - Confirm rollback plan is documented and tested in staging.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** On-time Delivery Rate  
   - Target: ≥90% of features delivered on schedule.  
   - Measurement Method: Compare planned vs. actual release dates across sprints.

2. **Secondary Metrics:**  
   - Cycle Time (average time from task creation to completion): ≤10 days per sprint.  
   - Defect Escape Rate: ≤5%.  
   - Customer Satisfaction (NPS): ≥50.

3. **Long-term Metrics:**  
   - Product Growth Rate: Track monthly active users and revenue growth.  
   - Team Velocity: Measure story points completed per sprint.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities in retrospectives.
3. Implement changes (e.g., adjust capacity planning, improve testing coverage).
4. Re-measure metrics post-implementation.
5. Repeat until all goals are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary:**  
   - Current state vs. target state for each metric.  
   - Key actions taken to improve team coordination.  

2. **Detailed Report:**  
   - Methodology used (Agile framework, tools).  
   - Research findings and recommendations.  
   - Implementation timeline with owners and responsibilities.

3. **Maintenance Plan:**  
   - Ongoing tasks: Quarterly alignment reviews, monthly retrospectives.  
   - Monitoring schedule: Weekly dashboard updates on key metrics.  

4. **Knowledge Transfer:**  
   - Training materials for new team members (Agile basics, tool usage).  
   - SOPs for sprint planning, retrospectives, and releases.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Agile Methodologies]"
    focus: "Latest frameworks and tools for agile implementation"
    sources: ["Scrum.org", "Atlassian's Agile University"]
    deliverable: "3 actionable insights with source links"

  - agent_id: 2
    topic: "[Product Development Lifecycle (PDL)]"
    focus: "Best practices per stage of product development"
    sources: ["Lean Startup Playbook", "Product Management blogs"]
    deliverable: "Stage-specific best practices document"

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to team coordination
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

Before marking the product management project as COMPLETE:

- [ ] **Primary Objective Achieved?** The product is delivered on time and meets defined quality standards.
- [ ] **All Metrics Met?** On-time delivery rate ≥90%, cycle time ≤10 days, defect escape rate ≤5%.
- [ ] **Quality Validated?** No critical bugs in production, user satisfaction NPS ≥50.
- [ ] **Documentation Complete?** All processes and knowledge transferred to the team.
- [ ] **Sustainability Ensured?** Maintenance plan documented with owners and schedule.

---

## TEMPLATE METADATA

**Last Updated:** 2024-08-14  
**Version:** 1.0  
**Tested With:** Product Manager roles across SaaS, Fintech, and Healthcare  
**Success Rate:** [Track completion in your PM tool]  
**Average Time to Goal:** [Analyze historical data for delivery timelines]

---

*This master template should be copied and customized for each specific product management task. The framework remains constant, but the details within each section are profession-specific.*

