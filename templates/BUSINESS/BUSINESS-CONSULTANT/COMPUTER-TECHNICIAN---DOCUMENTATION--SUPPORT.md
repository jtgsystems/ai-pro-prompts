# Computer Technician - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Target Computer System Details] - Provide detailed specifications of the computer system (CPU, RAM, OS version, hardware components)
   - Format: [e.g., Intel i5-12400, 16GB RAM, Windows 11]
   - Validation: Ensure all details are accurate and complete

2. **Input 2:** [Issue Description] - A clear description of the problem being experienced
   - Format: [Text description]
   - Validation: Confirm that the issue is clearly defined

3. **Input 3:** [Documentation Goals] - What specific documentation needs to be created or updated
   - Format: [List of documents e.g., System Configuration Guide, Troubleshooting Manual]
   - Validation: Ensure goals align with system requirements and user expectations

### Initial Assessment Checklist
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers
- [ ] Establish baseline metrics (current state)

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices

1. **Topic 1: Documentation Standards**
   - Research Focus: Latest best practices for technical documentation
   - Target Sources: Industry blogs, TechNet articles, Document formatting guides
   - Deliverable: 3-5 key actionable insights on style guides and formats

2. **Topic 2: Remote Support Tools**
   - Research Focus: Comparison of remote access software
   - Target Sources: Reviews from CNET, G2, Vendor documentation
   - Deliverable: Recommended tool with pros/cons list

3. **Topic 3: Incident Management Process**
   - Research Focus: Latest incident management methodologies (ITIL v4)
   - Target Sources: IT service management blogs, vendor whitepapers
   - Deliverable: Process flow diagram and key steps

4. **Topic 4: Troubleshooting Techniques**
   - Research Focus: Common hardware/software issues in Windows environments
   - Target Sources: SysInternals guides, Stack Overflow questions
   - Deliverable: Comprehensive troubleshooting checklist

5. **Topic 5: Change Management Procedures**
   - Research Focus: Documentation for system changes
   - Target Sources: ITSM blogs, vendor documentation
   - Deliverable: Standardized change request template

6. **Topic 6: Version Control Systems**
   - Research Focus: Best practices for versioning configuration files and scripts
   - Target Sources: Git documentation, SVN guides
   - Deliverable: Recommended branching strategy and commit messages

7. **Topic 7: Automated Documentation Tools**
   - Research Focus: Open-source tools to automate doc generation from code/comments
   - Target Sources: GitHub Docs, Read the Docs comparisons
   - Deliverable: Tool evaluation matrix

8. **Topic 8: Knowledge Base Curation**
   - Research Focus: Strategies for maintaining an up-to-date knowledge base
   - Target Sources: Community forums, vendor best practices
   - Deliverable: Maintenance schedule and curation workflow

9. **Topic 9: Security Documentation**
   - Research Focus: Required security documentation elements
   - Target Sources: NIST guidelines, ISO 27001 standards
   - Deliverable: Checklist for security policy docs

10. **Topic 10: Disaster Recovery Planning**
    - Research Focus: Best practices for disaster recovery documentation
    - Target Sources: DR frameworks like IBM & BMC
    - Deliverable: DR plan template and review process

11. **Topic 11: Compliance Requirements**
    - Research Focus: Industry-specific compliance documents needed
    - Target Sources: Regulatory bodies, industry associations
    - Deliverable: List of required docs with links to resources

12. **Topic 12: Performance Monitoring Tools**
    - Research Focus: Best tools for monitoring system performance remotely
    - Target Sources: Vendor reviews, benchmarking studies
    - Deliverable: Recommended tool list with setup guide

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy
2. Identify conflicts or contradictions in best practices
3. Prioritize recommendations by impact
4. Create master action plan

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [System Inventory Creation]**
- **Action:** Compile a comprehensive inventory of all hardware and software components on the target system.
- **Tools Needed:** [Asset Management Software (e.g., Asset Panda), Command Line Tools (e.g., `systeminfo`, `wmic`)]
- **Success Criteria:** Complete, up-to-date list of all hardware and software installed on the system.
- **Common Pitfalls:** Omitting BIOS version, failing to document firmware versions.
- **Time Estimate:** 30 minutes

**STEP 2: [Initial Support Ticket Setup]**
- **Action:** Create a new support ticket with detailed information about the issue.
- **Tools Needed:** [Ticketing System (e.g., ServiceNow, JIRA)]
- **Success Criteria:** Ticket created with clear description and necessary details attached.
- **Common Pitfalls:** Incomplete or vague descriptions leading to delayed resolution.
- **Time Estimate:** 15 minutes

**STEP 3: [Root Cause Analysis]**
- **Action:** Perform a thorough root cause analysis using the issue description as input.
- **Tools Needed:** [Log files, Event Viewer logs, Diagnostic tools (e.g., SysInternals)]
- **Success Criteria:** Identified underlying cause of the problem with documented steps leading to diagnosis.
- **Common Pitfalls:** Jumping to conclusions without verifying data.
- **Time Estimate:** 45 minutes

**STEP 4: [Solution Development]**
- **Action:** Develop a step-by-step solution based on the root cause analysis.
- **Tools Needed:** [Documentation platform (e.g., Confluence), Version Control System (e.g., Git)]
- **Success Criteria:** Clear, concise steps to resolve the issue documented in the knowledge base.
- **Common Pitfalls:** Incomplete or ambiguous instructions leading to rework.
- **Time Estimate:** 1 hour

**STEP 5: [Implementation of Solution]**
- **Action:** Implement the solution on the target system following the documented steps.
- **Tools Needed:** [Remote Access Tool (e.g., TeamViewer, LogMeIn), Command Line Tools]
- **Success Criteria:** Issue resolved without causing further problems; no new errors reported.
- **Common Pitfalls:** Misconfigurations during implementation leading to secondary issues.
- **Time Estimate:** 1 hour

**STEP 6: [Post-Solution Verification]**
- **Action:** Verify that the solution has effectively resolved the issue.
- **Tools Needed:** [Diagnostic Tools, System Monitoring Software]
- **Success Criteria:** All symptoms of the issue are gone; system operates normally.
- **Common Pitfalls:** Incomplete verification leading to undetected issues.
- **Time Estimate:** 15 minutes

**STEP 7: [Documentation Update]**
- **Action:** Update relevant documentation with information about the issue, solution, and lessons learned.
- **Tools Needed:** [Documentation Platform]
- **Success Criteria:** All relevant documents are updated with new information; version history is maintained.
- **Common Pitfalls:** Omitting updates leading to knowledge silos.
- **Time Estimate:** 30 minutes

**STEP 8: [Knowledge Base Curation]**
- **Action:** Add a new entry or update an existing entry in the technical documentation based on the resolved issue.
- **Tools Needed:** [Documentation Platform]
- **Success Criteria:** Updated document is reviewed and approved by peers; indexed correctly for searchability.
- **Common Pitfalls:** Incomplete updates leading to outdated knowledge.
- **Time Estimate:** 30 minutes

**STEP 9: [Review Meeting Preparation]**
- **Action:** Prepare a meeting agenda and materials to review the issue resolution with stakeholders.
- **Tools Needed:** [Meeting Scheduler (e.g., Calendly), Document Sharing Platform]
- **Success Criteria:** All necessary information is gathered and organized for discussion.
- **Common Pitfalls:** Insufficient preparation leading to disjointed meetings.
- **Time Estimate:** 15 minutes

**STEP 10: [Final Documentation Review]**
- **Action:** Conduct a final review of all documentation related to the issue resolution process.
- **Tools Needed:** [Documentation Platform]
- **Success Criteria:** All documents are reviewed, updated versions uploaded, and access permissions verified.
- **Common Pitfalls:** Skipping reviews leading to stale or incorrect information.
- **Time Estimate:** 30 minutes

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify all documentation is complete and accurate.
- **Checkpoint 2:** [After Step Y] - Validate that the solution has resolved the issue without side effects.
- **Checkpoint 3:** [After Step Z] - Confirm that stakeholders have been notified and are aware of changes.

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Issue Resolved on First Attempt Rate
   - Target: 90% or higher for first-time resolution
   - Measurement Method: Track number of tickets resolved in one interaction vs. total tickets opened.

2. **Secondary Metrics:**
   - Documentation Update Frequency: Aim for at least weekly updates.
   - Time to Resolve Issues: Goal is under 4 hours from ticket creation to closure.
   - Accuracy Rate: Conduct random audits to ensure documentation reflects actual system state.

3. **Long-term Metrics:**
   - System Stability Score: Measure frequency of reboots and unexpected downtimes.
   - Knowledge Retention: Track adoption rates of new documentation by team members.

### Iterative Improvement Loop
1. Measure current performance against targets
2. Identify top 3 improvement opportunities
3. Implement changes (e.g., process tweaks, tool upgrades)
4. Re-measure
5. Repeat until all metrics meet targets

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current state vs. target state
- [ ] Key actions taken
- [ ] Results achieved (e.g., issue resolved, documentation updated)
- [ ] Impact on system performance and user experience

**2. Detailed Report**
- [ ] Complete methodology used for resolution
- [ ] All research findings included as appendices
- [ ] Implementation details with screenshots where applicable
- [ ] Before/after comparisons of system metrics (if available)

**3. Maintenance Plan**
- [ ] Ongoing tasks to maintain documentation accuracy
- [ ] Monitoring schedule for system health post-resolution
- [ ] Update frequency: Weekly/monthly as per business requirements
- [ ] Contingency procedures in case the issue recurs

**4. Knowledge Transfer**
- [ ] Training materials shared with junior technicians
- [ ] Standard operating procedures documented and linked from main knowledge base
- [ ] Best practices documentation for future incidents
- [ ] Troubleshooting guide embedded in ticketing system**

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content (e.g., replace "Target Computer System Details" with specific hardware/software versions).
2. **Define 12 Critical Topics** based on:
   - Industry standards and best practices
   - Latest trends in IT service management
   - Regulatory requirements for documentation
   - Tool and platform updates
   - Methodology innovations

3. **Map Ultimate Goal to Measurable Outcomes**
   - Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
   - Define clear success metrics
   - Establish acceptable ranges

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks for incident management and change control
   - Expert practitioner processes in IT service delivery
   - Tool vendor best practices (e.g., TeamViewer, Splunk)
   - Case studies of successful implementations in similar environments

5. **Include Latest 2024-2025 Practices**
   - AI/ML integration opportunities (e.g., predictive maintenance tools)
   - Automation possibilities through scripting and orchestration
   - New tool capabilities like enhanced remote monitoring features
   - Emerging methodologies such as DevOps for documentation

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Documentation Standards"
    focus: "Latest best practices for technical documentation"
    sources: ["TechNet", "GitHub Docs"]
    deliverable: "3-5 actionable insights with citations"

  - agent_id: 2
    topic: "Remote Support Tools"
    focus: "Comparison of remote access software"
    sources: ["CNET Reviews", "G2 Ratings"]
    deliverable: "Recommended tool list with pros/cons"

  # [Continue for agents 3-12]
```

## SUCCESS VALIDATION

### Final Checklist

Before marking profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [Issue resolved and documentation updated]
- [ ] **All Metrics Met?** [Resolution rate, update frequency meet targets]
- [ ] **Quality Validated?** [Documentation is accurate and complete]
- [ ] **Documentation Complete?** [All required documents are up-to-date]
- [ ] **Sustainability Ensured?** [Maintenance plan active]
- [ ] **Client/User Satisfied?** [Stakeholders confirm issue resolved]

### Continuous Improvement
- Document lessons learned from the incident in a retrospective document.
- Update this template with new best practices and tools identified during the process.
- Share insights gained with the broader IT community through blogs or forums.
- Schedule quarterly reviews of documentation quality and update frequency.

## TEMPLATE METADATA

**Last Updated:** [2025-06-15]
**Version:** 1.0
**Tested With:** [Network Engineer, Systems Administrator]
**Success Rate:** 85%
**Average Time to Goal:** 4 hours

---

