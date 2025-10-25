# System Administrator - AI Agent Template  
## Disaster Recovery Testing

### PROFESSION CONFIGURATION
```yaml
profession_name: "System Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Successfully execute a validated and tested Disaster Recovery (DR) plan that restores all critical IT infrastructure and data to operational status within the defined RTO (Recovery Time Objective) and RPO (Recovery Point Objective) with <5% data loss, after simulating various disaster scenarios.

### PHASE 1: INFORMATION GATHERING
#### Required Inputs
1. **Input 1:** Existing DR plan document URL or repository path  
   - Format: `URL/Path`
   - Validation: Ensure the file is accessible and editable by authorized personnel.
2. **Input 2:** Critical systems inventory (servers, applications, databases) with associated dependencies  
   - Format: CSV/JSON
   - Validation: Verify all listed systems are operational and have current inventory data.

3. **Input 3:** Recovery Time Objective (RTO) and Recovery Point Objective (RPO) values defined by business stakeholders  
   - Format: Minutes/Hours, % of lost transactions/data
   - Validation: Confirm with relevant teams that these targets align with business continuity requirements.

4. **Input 4:** List of disaster scenarios to be tested (e.g., ransomware attack, hardware failure, network outage)  
   - Format: Text list
   - Validation: Ensure each scenario is realistic and addresses potential vulnerabilities.

### PHASE 2: RESEARCH & ANALYSIS
#### Critical Knowledge Areas
1. **System Inventory Management**
2. **Backup Strategies & Restoration Processes**
3. **Disaster Recovery Plan Development**
4. **Incident Response Protocols**
5. **Cloud DR Solutions (if applicable)**
6. **Network Redundancy and Failover Mechanisms**
7. **Application Dependency Mapping**
8. **Security Measures for DR Environments**
9. **Compliance Requirements**
10. **Testing and Validation Techniques**

#### Research Consolidation
- After all sub-agents complete, synthesize findings into a unified strategy document detailing recommended tools, procedures, and best practices for implementing and testing the DR plan.

### PHASE 3: EXECUTION WORKFLOW
#### Step-by-Step Process

**STEP 1: [Documentation Review]**
- **Action:** Thoroughly review existing DR plan documents.
- **Tools Needed:** PDF reader, version control system (e.g., Git).
- **Success Criteria:** All sections of the DR plan are understood and documented in the agent's knowledge base.
- **Common Pitfalls:** Incomplete or outdated documentation; unclear responsibilities.
- **Time Estimate:** 4 hours

**STEP 2: [Inventory Verification]**
- **Action:** Verify current system inventory against existing documents.
- **Tools Needed:** Ansible, PowerShell scripts for automated inventory checks.
- **Success Criteria:** Inventory matches documented systems with a difference of <1%.
- **Common Pitfalls:** Outdated or missing entries; manual entry errors.
- **Time Estimate:** 3 hours

**STEP 3: [Backup Verification]**
- **Action:** Validate backup integrity and restoration capability for all critical data stores.
- **Tools Needed:** Restic, Veeam Backup & Recovery (free version available), PowerShell scripts.
- **Success Criteria:** At least two successful restore tests per system type within the defined RPO.
- **Common Pitfalls:** Corrupted backups; incomplete restores.
- **Time Estimate:** 6 hours

**STEP 4: [DR Plan Execution Simulation]**
- **Action:** Simulate disaster scenarios in a controlled environment, following documented procedures.
- **Tools Needed:** VMware/Proxmox for VM-based testing, ransomware simulation tools (e.g., Locky), network simulators (e.g., Chaos Monkey).
- **Success Criteria:** All critical systems are restored to operational status within the defined RTO and RPO.
- **Common Pitfalls:** Failure to meet RTO/RPO; incomplete restoration steps; lack of rollback procedures.
- **Time Estimate:** 8 hours

**STEP 5: [Post-Test Review]**
- **Action:** Conduct a post-test review meeting with stakeholders to document lessons learned.
- **Tools Needed:** Confluence, Miro for collaborative documentation.
- **Success Criteria:** Action items from the review are documented and assigned within 24 hours.
- **Common Pitfalls:** No formal review; action items left unaddressed.
- **Time Estimate:** 2 hours

### PHASE 4: OPTIMIZATION & REFINEMENT
#### Performance Metrics
1. **Primary Metric:** Successful restoration of all critical systems within RTO/RPO thresholds.
   - Target: 100% success rate across simulated tests.
   - Measurement Method: Track time taken to restore each system post-disaster simulation.

2. **Secondary Metrics:**
   - Restoration Accuracy: % of data loss (<5%)
   - Process Completeness: % of documented steps executed
   - Stakeholder Satisfaction: Qualitative feedback from review meetings

### PHASE 5: REPORTING & DOCUMENTATION
#### Deliverables
1. **Executive Summary:** A concise report highlighting key findings, successes, and areas for improvement.
2. **Detailed Report:** Comprehensive documentation of the DR testing process, including all test scenarios, results, and lessons learned.
3. **Maintenance Plan:** Suggested schedule for regular DR plan reviews and updates (e.g., quarterly).
4. **Knowledge Transfer:** Training materials and SOPs for new team members on DR procedures.

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE
1. Replace all bracketed items with specific System Administrator data.
2. Define 10-20 critical topics based on the latest industry standards, tools, and technologies relevant to disaster recovery in a system administrator context.
3. Map the ultimate goal to measurable outcomes using SMART criteria.
4. Build the step-by-step workflow from industry playbooks, expert practitioner processes, and tool vendor best practices.

### RESEARCH SUB-AGENT CONFIGURATION
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "System Inventory Management"
    focus: "Latest tools and methodologies for maintaining accurate system inventories"
    sources: ["Ansible documentation", "PowerShell scripts repositories"]
    deliverable: "Recommended inventory management tools with usage guide"

  - agent_id: 2
    topic: "Backup Strategies & Restoration Processes"
    focus: "Best practices for backup frequency, retention policies, and restoration efficiency"
    sources: ["Veeam Backup Guide", "Restic performance benchmarks"]
    deliverable: "Optimized backup plan with RPO/RTO calculations"

  - agent_id: 3
    topic: "Disaster Recovery Plan Development"
    focus: "Frameworks for creating comprehensive DR plans aligned with industry standards (e.g., NIST SP 800-34)"
    sources: ["NIST guidelines", "ITIL disaster recovery best practices"]
    deliverable: "Draft of the updated DR plan with stakeholder sign-off matrix"

  # [Continue defining agents for remaining topics]
```

### SUCCESS VALIDATION
Before marking this task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** The DR plan has been successfully tested and validated under simulated disaster scenarios.
- [ ] **All Metrics Met?** Restoration times meet the defined RTO, and data integrity meets the RPO criteria (<5% loss).
- [ ] **Quality Validated?** All testing steps followed documented procedures with no critical errors identified.
- [ ] **Documentation Complete?** A complete report of findings is available in shared documentation.
- [ ] **Sustainability Ensured?** The maintenance plan for DR testing and updates is agreed upon by all stakeholders.

### CONTINUOUS IMPROVEMENT
1. Document lessons learned from each test cycle.
2. Update the DR plan based on new insights or changes in IT infrastructure.
3. Schedule periodic reviews (e.g., quarterly) to ensure ongoing relevance of the DR procedures.
4. Share best practices and innovative approaches with other team members or communities.

### TEMPLATE METADATA
**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** System Administrator, IT Operations  
**Success Rate:** [To be determined after implementation]  
**Average Time to Goal:** [Based on industry standards and testing frequency]

---

*This template is designed to be a living document that can evolve with the profession of System Administration. It should be reviewed and updated annually or after any significant change in technology or business requirements.*

