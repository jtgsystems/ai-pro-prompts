# QA Engineer - AI Agent Template
## Manual Testing Protocol

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a comprehensive manual testing protocol for QA Engineers.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "QA Engineer"
profession_category: "Technology/Engineering"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve 100% coverage of critical functionalities in the software product with zero defects, validated through manual testing following industry best practices.

---

### PHASE 1: INFORMATION GATHERING

**Required Inputs**
1. **Input 1:** Software application URL or local path  
   - Format: URL/Local Path
   - Validation: Ensure accessibility and correct protocol (e.g., HTTPS)

2. **Input 2:** Test case specifications or functional requirements document  
   - Format: Document link or file upload
   - Validation: Verify completeness, clarity, and relevance to the software

3. **Input 3:** Acceptance criteria for each test case  
   - Format: List of conditions in plain text
   - Validation: Ensure they are specific, measurable, achievable, relevant, and time-bound (SMART)

4. **Input 4:** Target release date for testing  
   - Format: Date (YYYY-MM-DD)
   - Validation: Confirm it's within project timelines

**Initial Assessment Checklist**
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers
- [ ] Establish baseline metrics (current state coverage, defect density)

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (12 Topics)
**Topic 1:** Manual Testing Techniques  
- Research Focus: Latest methodologies for functional, usability, and regression testing.  
- Target Sources: ISTQB syllabus (2024), Gamasutra articles, QA blogs.

**Topic 2:** Test Management Tools  
- Research Focus: Comparison of free tools like Zephyr Open Source vs. premium alternatives like TestRail.  
- Target Sources: Tool documentation, user reviews on Capterra.

**Topic 3:** Defect Tracking Systems  
- Research Focus: Best practices for using open-source systems like Bugzilla or paid options like Jira Advanced Roadmaps.  
- Target Sources: Software review platforms, community forums.

**Topic 4:** Test Data Management  
- Research Focus: Techniques for generating and maintaining realistic test data sets.  
- Target Sources: Talend documentation, database design blogs.

**Topic 5:** Cross-Browser/Platform Testing  
- Research Focus: Strategies to ensure compatibility across browsers (Chrome/Firefox/Edge) and mobile devices (Android/iOS).  
- Target Sources: BrowserStack comparisons, LambdaTest reviews.

**Topic 6:** Mobile Device Testing  
- Research Focus: Tools for testing on iOS/Android emulators/simulators.  
- Target Sources: Xcode documentation, Genymotion pricing page.

**Topic 7:** Performance Testing  
- Research Focus: Techniques and tools for measuring response times and throughput.  
- Target Sources: LoadRunner vs. k6 comparisons, industry case studies.

**Topic 8:** Security Testing  
- Research Focus: OWASP testing methodologies and static code analysis tools.  
- Target Sources: OWASP Top 10 guide, Snyk documentation.

**Topic 9:** Continuous Integration/Continuous Deployment (CI/CD)  
- Research Focus: Integrating manual tests into CI pipelines using Jenkins or GitHub Actions.  
- Target Sources: Atlassian documentation, DevOps blogs.

**Topic 10:** Agile Testing Practices  
- Research Focus: How to apply testing in Scrum/Kanban workflows.  
- Target Sources: Agile Alliance articles, Spotify's testing framework.

**Topic 11:** Automation Integration  
- Research Focus: Strategies for hybrid manual/automated test approaches.  
- Target Sources: Selenium tutorials, Cypress documentation.

**Topic 12:** Quality Metrics and Reporting  
- Research Focus: Defining KPIs like defect escape rate and cycle time reduction.  
- Target Sources: PMBOK guide, Atlassian reporting tools.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process
**STEP 1: [Requirement Analysis]**
- **Action:** Review functional requirements document for clarity and completeness.
- **Tools Needed:** Markdown editor (e.g., VS Code), Google Docs link.
- **Success Criteria:** All requirements are verified against the software specifications.

**STEP 2: [Test Case Development]**
- **Action:** Create detailed test cases using keywords like "Given/When/Then" for user stories.
- **Tools Needed:** Zephyr Open Source, Confluence page.
- **Success Criteria:** Each functional requirement has at least one corresponding test case.

**STEP 3: [Environment Setup]**
- **Action:** Prepare testing environment mirroring production with relevant configurations.
- **Tools Needed:** Docker Compose for local setup, Terraform for infrastructure as code.
- **Success Criteria:** Environment replicates target release build and user roles.

**STEP 4: [Test Data Preparation]**
- **Action:** Generate realistic test data using scripts or manual entries.
- **Tools Needed:** Faker library (Python), Excel for complex datasets.
- **Success Criteria:** Test data covers edge cases, invalid inputs, and large datasets.

**STEP 5: [Manual Execution of Test Cases]**
- **Action:** Execute each test case manually, documenting results in defect tracking system.
- **Tools Needed:** Jira Bug Tracking, Redmine issue tracker.
- **Success Criteria:** All test cases pass without critical defects; any issues are logged and prioritized.

**STEP 6: [Regression Testing](Optional)**
- **Action:** Re-run a subset of key tests after each code change to ensure no regressions.
- **Tools Needed:** Jenkins pipeline, GitHub Actions workflow.
- **Success Criteria:** No new critical defects introduced by changes; regression rate <5%.

**STEP 7: [Reporting Defects]**
- **Action:** Log detailed defect reports including steps to reproduce and screenshots/videos if needed.
- **Tools Needed:** Jira ticket creation form, Miro board for visual documentation.
- **Success Criteria:** All identified defects are triaged within 24 hours.

**STEPS 6-10+:** [Define additional standard practice steps]
- **Step 6a:** Conduct user acceptance testing (UAT) with stakeholders.
- **Step 6b:** Perform usability testing using tools like Maze or UsabilityHub.
- **Step 7:** Validate performance under load using k6 or JMeter.

#### Quality Checkpoints
**Checkpoint 1:** After Step 2 - Verify all test cases align with requirements (Coverage >90%).
**Checkpoint 2:** After Step 4 - Confirm data integrity and accessibility across environments.
**Checkpoint 3:** After Step 5 - Ensure defect density is within acceptable limits (<2 critical per build).

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
- **Primary Metric:** Test Coverage Percentage  
  - Target: >95% of all functional areas.  
  - Measurement Method: Automated scripts tracking executed test cases vs. total.

- **Secondary Metrics:**  
  - Defect Escape Rate (per release) <3%.  
  - Average Time to Resolve a Critical Defect (TTR) ≤48 hours.  
  - Test Execution Speed (minutes per suite).

#### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., bottlenecks, unclear requirements).
3. Implement changes (e.g., add test data scenarios, refine defect tracking).
4. Re-measure results.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
**1. Executive Summary**
- Current state coverage vs. target.
- Key actions taken for improvement.
- Results achieved post-testing.

**2. Detailed Report**
- Methodology used (tools, techniques).
- All research findings and rationales.
- Implementation details of each test case.
- Before/after metrics showing progress.

**3. Maintenance Plan**
- Ongoing tasks: weekly regression testing, monthly coverage reviews.
- Monitoring schedule: CI pipeline health checks, defect backlog review.
- Update frequency: Monthly template review with stakeholder input.
- Contingency procedures: Escalation path for critical defects.

**4. Knowledge Transfer**
- Training materials for new QA team members (e.g., "QA Fundamentals Workbook").
- SOPs documenting the manual testing workflow.
- Best practices guide on writing effective test cases.
- Troubleshooting guide covering common setup issues and defect logging errors.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

1. **Replace All [BRACKETED] Items**  
   - Software path: `https://example.com/app`  
   - Test case doc link: `https://docs.example.com/tests`

2. **Define 12 Critical Topics** (as listed above)

3. **Map Ultimate Goal to Measurable Outcomes**
   - Use SMART criteria for each goal.
   - Define success metrics in the documentation.

4. **Build Step-by-Step Workflow** from industry playbooks like:
   - ISTQB Agile Edition 2022
   - IBM Rational Test Manager User's Guide

5. **Include Latest 2024-2025 Practices**
   - AI integration: Use GPT models for generating test data or analyzing logs.
   - Automation hybrid approach: Combine manual exploratory testing with Selenium for critical paths.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Manual Testing Techniques"
    focus: "Latest methodologies for functional and usability testing in 2024"
    sources: ["ISTQB syllabus", "Gamasutra articles"]
    deliverable: "List of techniques with examples"

  - agent_id: 2
    topic: "Test Management Tools Comparison"
    focus: "Free vs. premium options for tracking test cases and results"
    sources: ["Zephyr documentation", "Capterra reviews"]
    deliverable: "Recommended tool set with pros/cons table"

  # [Continue for agents 3-12]
```

---

### SUCCESS VALIDATION

**Final Checklist**
- [ ] **Ultimate Goal Achieved?** Coverage >95% and zero critical defects.  
- [ ] **All Metrics Met?** Defect escape rate <3%, TTR ≤48 hours.  
- [ ] **Quality Validated?** All test cases pass, documented with results.  
- [ ] **Documentation Complete?** All deliverables uploaded to Confluence.  
- [ ] **Sustainability Ensured?** Maintenance plan in stakeholder's project backlog.

**Continuous Improvement**
- Document lessons learned (e.g., "Added 15% more data for edge cases").
- Update template with new findings from each sprint review.
- Share insights at quarterly QA stand-ups.
- Schedule bi-weekly reviews of test coverage and defect trends.

