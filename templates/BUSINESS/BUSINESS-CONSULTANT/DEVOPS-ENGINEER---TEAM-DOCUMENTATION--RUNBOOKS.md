# DevOps Engineer - AI Agent Template
## Team Documentation & Runbooks

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve high-quality team documentation and runbook creation for a DevOps Engineer role.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "DevOps Engineer"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

#### Ultimate Goal
**Primary Objective:** Achieve comprehensive, up-to-date team documentation and runbooks that facilitate smooth operations, rapid incident response, and continuous improvement across all DevOps processes.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Team structure & roles]
   - Format: List of team members with their primary responsibilities (e.g., SRE, CI/CD Engineer, Site Reliability Engineer).
   - Validation: Verify each role is correctly assigned.

2. **Input 2:** [Current documentation repository location]
   - Format: URL or path to the existing documentation system (e.g., Confluence, Notion, Git repo).
   - Validation: Ensure agent can access and read the repository.

3. **Input 3:** [Primary tools & platforms used by the team]
   - Format: List of all software, services, and infrastructure components.
   - Validation: Confirm each tool is operational and integrated with the documentation system.

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (10-20 Topics)
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices

**Topic 1:** [Documentation Best Practices]
- Research Focus: Latest guidelines for technical writing, version control strategies, and documentation standards.
- Target Sources: Industry blogs, SRE Handbook, DevOps culture guides.

**Topic 2:** [Runbook Creation Frameworks]
- Research Focus: Structured templates for runbooks (e.g., incident response, deployment procedures).
- Target Sources: O'Reilly books on runbooks, SRE community forums.

**Topic 3:** [Automation & Orchestration Tools]
- Research Focus: CI/CD pipelines, Infrastructure as Code (IaC), and automation scripts.
- Target Sources: Jenkins documentation, Terraform tutorials.

**Topics 4-10:** [Advanced Topics]
- Topic 4: Monitoring & Alerting Systems
- Topic 5: Version Control Systems Best Practices
- Topic 6: Incident Management Processes
- Topic 7: Infrastructure Deployment Strategies
- Topic 8: Security Protocols for DevOps
- Topic 9: Continuous Integration/Continuous Delivery (CI/CD)
- Topic 10: Disaster Recovery Planning

**Topics 11-20 (Optional):** [Specialized Tools]
- Topic 11: Kubernetes Documentation
- Topic 12: Cloud-Native Architecture Guides
- Topic 13: Chaos Engineering Techniques
- Topic 14: Container Orchestration Best Practices
- Topic 15: Log Management Solutions
- Topic 16: Network Configuration Management Tools
- Topic 17: Data Backup and Recovery Strategies
- Topic 18: Performance Tuning Guidelines
- Topic 19: Compliance and Auditing Standards
- Topic 20: DevOps Culture and Mindset

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Documentation Repository Setup]**
- **Action:** Create a new folder in the documentation system dedicated to runbooks.
- **Tools Needed:** Confluence, Notion, Git (GitHub/GitLab/Bitbucket).
- **Success Criteria:** Folder created and accessible by all team members.
- **Common Pitfalls:** Permissions set incorrectly; repository not linked to version control.
- **Time Estimate:** 30 minutes

**STEP 2: [Runbook Template Creation]**
- **Action:** Develop a standardized runbook template with sections for procedures, responsibilities, steps, and escalation paths.
- **Tools Needed:** Google Docs/Word, Markdown editor (VS Code).
- **Success Criteria:** Template is saved in the repository; reviewed by team leads.
- **Common Pitfalls:** Incomplete sections or unclear instructions.
- **Time Estimate:** 1 hour

**STEP 3: [Initial Documentation Input]**
- **Action:** Populate runbooks with existing procedures for common tasks (e.g., deployment, incident response).
- **Tools Needed:** Template from Step 2; source code repositories.
- **Success Criteria:** At least three key processes have documented steps and are linked to the template.
- **Common Pitfalls:** Outdated documentation or missing critical information.
- **Time Estimate:** 4 hours

**STEP 4: [Automation Integration]**
- **Action:** Automate updates of documentation based on CI/CD pipeline events.
- **Tools Needed:** Jenkins, GitHub Actions, GitLab CI/CD.
- **Success Criteria:** Automated scripts trigger documentation updates without manual intervention.
- **Common Pitfalls:** Scripts not triggered or update conflicts.
- **Time Estimate:** 2 hours

**STEP 5: [Review and Approval Process]**
- **Action:** Set up a review workflow for all documentation changes before they are published.
- **Tools Needed:** GitHub Pull Requests, Confluence approval workflows.
- **Success Criteria:** All documentation changes require at least one peer review.
- **Common Pitfalls:** Changes bypassing review; urgent updates not properly vetted.
- **Time Estimate:** 1 hour

**STEP 6: [Version Control & Change Management]**
- **Action:** Implement a version control strategy for all documentation, ensuring history and audit trails are maintained.
- **Tools Needed:** Git (with branch protection rules), GitHub/GitLab/Bitbucket.
- **Success Criteria:** All changes tracked with commit messages explaining the reason; rollbacks possible if needed.
- **Common Pitfalls:** Frequent merging of unreviewed branches or lack of rollback procedures.
- **Time Estimate:** 1 hour

**STEP 7: [Testing Documentation]**
- **Action:** Conduct walkthroughs of runbooks with team members to ensure clarity and completeness.
- **Tools Needed:** Meeting rooms, shared screen tools (Zoom, Teams), documentation links.
- **Success Criteria:** All team members can follow the procedures without issues; feedback documented.
- **Common Pitfalls:** Complex steps not covered or unclear instructions leading to confusion during testing.
- **Time Estimate:** 2 hours

**STEP 8: [Continuous Improvement Loop]**
- **Action:** Establish a process for regular review and update of documentation based on changes in the system, tools, or processes.
- **Tools Needed:** Calendar reminders, project management tools (Jira).
- **Success Criteria:** Documentation reviewed at least quarterly; updates logged with reason and by whom.
- **Common Pitfalls:** Lack of scheduled reviews leading to stale content.
- **Time Estimate:** Ongoing

**STEP 9: [Training & Knowledge Transfer]**
- **Action:** Conduct training sessions for team members on using the new documentation system and runbooks.
- **Tools Needed:** Zoom, Teams, recorded presentations.
- **Success Criteria:** Attendance tracked; post-training survey shows understanding of material.
- **Common Pitfalls:** Training not completed or participants not fully engaged.
- **Time Estimate:** 2 hours (initial training), followed by ongoing reinforcement.

**STEP 10: [Monitoring & Feedback Mechanism]**
- **Action:** Implement a system for monitoring documentation usage and gathering feedback from team members.
- **Tools Needed:** Google Analytics, Confluence comment sections, regular pulse surveys.
- **Success Criteria:** Usage metrics show active engagement; at least one positive feedback per quarter.
- **Common Pitfalls:** No mechanism to track usage or incorporate feedback leads to stagnant content.
- **Time Estimate:** Ongoing

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:

1. **Primary Metric:** [Documentation Coverage]
   - Target: Minimum 90% of critical processes documented with runbooks.
   - Measurement Method: Count of documented vs. undocumented processes; automated reports.

2. **Secondary Metrics:**
   - **Metric 1:** [Change Frequency]
     - Target: At least one documentation update per sprint cycle.
     - Measurement Method: Version control logs showing commits to the documentation repository.

   - **Metric 2:** [Team Engagement]
     - Target: Average time for team members to complete training sessions is under 30 minutes; post-training quiz score >80%.
     - Measurement Method: Training records, quiz results.

3. **Long-term Metrics:**
   - **Metric 1:** [Incident Resolution Time]
     - Target: Reduce average incident resolution time by 20% within three months of implementing runbooks.
     - Measurement Method: Incident logs showing time from detection to resolution.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
**1. Executive Summary**
- [ ] Current state vs. target state (e.g., 70% coverage vs. 90%; outdated documentation)
- [ ] Key actions taken (e.g., created runbook templates, automated updates)
- [ ] Results achieved (e.g., increased documentation coverage to 85%, reduced incident resolution time by 15%)
- [ ] ROI or impact metrics (e.g., fewer incidents, faster onboarding)

**2. Detailed Report**
- [ ] Complete methodology including tools used and processes followed.
- [ ] All research findings with sources linked.
- [ ] Implementation details such as repository structure, version control settings, automation scripts.
- [ ] Before/after comparisons of documentation coverage and usage.

**3. Maintenance Plan**
- [ ] Ongoing tasks: Weekly review of documentation, monthly updates, quarterly audits.
- [ ] Monitoring schedule: Automated checks for version changes, user engagement metrics every month.
- [ ] Update frequency: Monthly or as needed based on process changes.
- [ ] Contingency procedures: How to handle sudden documentation gaps (e.g., emergency meetings).

**4. Knowledge Transfer**
- [ ] Training materials: Quick start guides, runbook walkthrough videos.
- [ ] Standard operating procedures: How to update and maintain documentation.
- [ ] Best practices documentation: Naming conventions, version control policies, review processes.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Documentation Best Practices]"
    focus: "Latest guidelines for technical writing, version control strategies"
    sources: ["SRE Handbook", "DevOps Culture Guide"]
    deliverable: "Actionable insights with citations"

  - agent_id: 2
    topic: "[Runbook Creation Frameworks]"
    focus: "Structured templates and frameworks for runbooks"
    sources: ["O'Reilly Books", "SRE Community Forums"]
    deliverable: "Recommended template structure and examples"

  # [Continue defining agents 3-10]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority (e.g., SRE Handbook > DevOps Culture Guide)
  4. Prioritize recommendations based on impact to documentation quality and operational efficiency
  5. Generate unified recommendation report with citations

```

### SUCCESS VALIDATION

**Final Checklist**

Before marking the DevOps Engineer task as COMPLETE:

- [ ] **Documentation Coverage Achieved?** At least 90% of critical processes documented.
- [ ] **Runbook Readability Measured?** Average time to complete a walkthrough is under 30 minutes for team members.
- [ ] **Incident Resolution Time Reduced?** Verification that incident resolution metrics improved as expected.

### Continuous Improvement
- Document lessons learned from the implementation phase (what worked, what didn't).
- Update this template with new best practices identified during execution.
- Share innovations and feedback loops with the broader DevOps community.
- Schedule periodic reviews to ensure documentation remains current and effective.

