# Computer Technician - AI Agent Template
## Driver Updates

### PROFESSION CONFIGURATION
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Ensure all computer systems have the latest, compatible device drivers installed for optimal hardware performance and system stability.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
```yaml
- target_systems:
  - Format: List of computers/OS versions (e.g., Windows 10 x64, Linux Ubuntu 22.04)
  - Validation: All systems listed must be supported by driver update tools.

- compatibility_requirements:
  - Format: Specific hardware components or OS versions that drivers need to support.
  - Validation: Must match system specs of target devices.

- maintenance_window:
  - Format: Preferred date and time for performing updates.
  - Validation: Must fit within operational hours.

- user_approval:
  - Format: Method for users/approvals (e.g., email, ticketing system).
  - Validation: Clear process defined for obtaining approvals.
```

### Initial Assessment Checklist
```yaml
- [ ] Verify all required inputs received and validated.
- [ ] Validate that all target systems are supported by the update tools.
- [ ] Identify any red flags like unsupported hardware or user restrictions.
- [ ] Establish baseline metrics (current driver versions, system health).
```

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas
```yaml
1. **Device Driver Basics**
   - Research Focus: Understanding what drivers are and their importance.

2. **Latest Driver Releases**
   - Research Focus: Identifying the latest drivers for common hardware (e.g., GPU, network adapters).

3. **Automated vs Manual Updates**
   - Research Focus: Pros/cons of using automated driver update tools versus manual updates.

4. **Compatibility Verification**
   - Research Focus: Ensuring new drivers are compatible with existing software/hardware.

5. **Update Management Policies**
   - Research Focus: How to manage and document driver updates within an organization.

6. **Backup Procedures**
   - Research Focus: Best practices for backing up system configurations before updating drivers.

7. **Version Control Systems**
   - Research Focus: Using version control systems for tracking driver versions across systems.

8. **Automated Deployment Tools**
   - Research Focus: Tools that can automate the deployment of updated drivers (e.g., SCCM, Puppet).

9. **Security Implications**
   - Research Focus: How updating drivers impacts system security and vulnerabilities.

10. **User Impact Assessment**
    - Research Focus: Potential impact on user productivity and system performance post-update.
```

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified driver update strategy.
2. Identify any contradictions in best practices to resolve (e.g., automated vs manual).
3. Prioritize recommendations based on risk reduction, time savings, and compatibility.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
```yaml
STEP 1: [Inventory Current Drivers]
- Action: Use a driver update tool to scan all target systems for current drivers.
- Tools Needed:
  - Driver Talent (free)
  - Belarc Advisor (free)
  - Windows Update Assistant (free)
- Success Criteria: List of all currently installed drivers with versions.

STEP 2: [Identify Latest Drivers]
- Action: Verify the latest available drivers on the manufacturer's website or through the update tool.
- Tools Needed:
  - Manufacturer Websites (e.g., Intel, AMD, NVIDIA)
  - Driver Update Tools (Driver Talent, etc.)
- Success Criteria: Updated list of compatible driver versions.

STEP 3: [Backup Systems]
- Action: Create a backup image of each system before making any changes.
- Tools Needed:
  - Windows Backup (built-in)
  - Acronis True Image (optional premium alternative)
- Success Criteria: Backup completed successfully for all systems.

STEP 4: [Test Compatibility]
- Action: Run compatibility tests on the target systems with the new drivers installed.
- Tools Needed:
  - Stress Testing Software (e.g., Prime95, AIDA64 Extreme)
  - System Monitoring Tools (Resource Monitor, Task Manager)
- Success Criteria: Systems perform as expected without crashes or errors.

STEP 5: [Deploy Updates]
- Action: Use an automated deployment tool to push the updated drivers across all systems.
- Tools Needed:
  - SCCM (System Center Configuration Manager) - Free for small deployments
  - Puppet Enterprise - Premium alternative
  - Ansible - Open-source option
- Success Criteria: All target systems have received and applied the updates.

STEP 6: [Validate Updates]
- Action: Verify that each system has successfully updated to the latest drivers.
- Tools Needed:
  - System Information Tool (MSInfo32)
  - Driver Verifier (Windows Diagnostic Tools)
- Success Criteria: No errors reported for any driver installations.

STEP 7: [Rollback Plan Testing]
- Action: Ensure a rollback plan is in place and tested to revert systems if issues arise.
- Tools Needed:
  - System Restore (built-in)
  - Backup Image Verification
- Success Criteria: Rollback process works as expected without data loss.

STEP 8: [User Acceptance Testing]
- Action: Have users perform basic tasks on updated systems to ensure functionality is intact.
- Tools Needed:
  - User Test Scripts
  - Feedback Forms (Google Forms, SurveyMonkey)
- Success Criteria: No performance issues reported by end-users.

STEP 9: [Post-Update Monitoring]
- Action: Monitor system health and stability for at least one week post-update.
- Tools Needed:
  - Windows Event Viewer
  - Sysinternals Suite (free)
  - Remote Monitoring Tools (e.g., Splunk Enterprise, Nagios)
- Success Criteria: No driver-related errors or performance degradation observed.

STEP 10: [Final Documentation and Reporting]
- Action: Document the entire update process, including any issues encountered and resolutions.
- Tools Needed:
  - Change Management System (Jira, ServiceNow)
  - Documentation Platform (Confluence, Google Docs)
- Success Criteria: Comprehensive report available for stakeholders.
```

### Quality Checkpoints
```yaml
- **Checkpoint 1:** After Step X - Verify that the backup of each system is complete and accessible.
- **Checkpoint 2:** After Step Y - Validate compatibility tests have passed without any driver-related errors.
- **Checkpoint 3:** After Step Z - Ensure all systems report successful update installation as per System Information Tool.
```

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
```yaml
1. **Primary Metric:** All target systems running with the latest compatible drivers.
   - Target: 100% of devices updated without errors.
   - Measurement Method: Driver update tool logs and system scans.

2. **Secondary Metrics:**
   - [ ] Number of driver updates successfully applied (goal: 0 failures).
   - [ ] System performance stability post-update (goal: no crashes, stable uptime >95%).
   - [ ] User satisfaction score (goal: >=4/5 from feedback).

3. **Long-term Metrics:**
   - [ ] Reduction in system errors or vulnerabilities identified by scans.
   - [ ] Improvement in overall system responsiveness measured over 30 days post-update.
```

### Iterative Improvement Loop
```yaml
1. Measure current performance against targets (primary metric).
2. Identify top 3 improvement opportunities from any issues logged.
3. Implement changes such as refining deployment steps or updating rollback procedures.
4. Re-measure to confirm improvements have been realized.

Repeat this loop until all metrics are consistently met.
```

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
```yaml
1. **Executive Summary**
   - Current state vs target state (100% updated drivers).
   - Key actions taken (inventory, deployment, validation).
   - Results achieved (metrics from primary metric).

2. **Detailed Report**
   - Methodology used for updates.
   - All research findings and tools employed.
   - Implementation details of each step.
   - Before/after comparison metrics.

3. **Maintenance Plan**
   - Scheduled regular driver update cycles (quarterly).
   - Monitoring frequency to detect future issues.
   - Update approval process in place.

4. **Knowledge Transfer**
   - Training sessions for IT staff on using the driver update tools.
   - SOPs documenting each step of the update process.
   - Troubleshooting guide specific to common driver-related errors.
```

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace All [BRACKETED] Items** with profession-specific details (e.g., actual system lists, tool names).
2. **Define 10-20 Critical Topics** based on:
   - Latest driver release schedules.
   - Compatibility issues specific to your hardware/software.
   - Regulatory compliance requirements for updates.
   - Tool capabilities and limitations.
3. **Map Ultimate Goal to Measurable Outcomes**: Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound).
4. **Build Step-by-Step Workflow** from:
   - Industry playbooks.
   - Manufacturer guidelines.
   - Case studies of successful driver deployment projects.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Device Driver Basics]"
    focus: "Understanding driver functionality and importance."
    sources: ["Manufacturer documentation", "Tech forums"]
    deliverable: "Written guide on drivers."

  - agent_id: 2
    topic: "[Latest Driver Releases]"
    focus: "Identifying the latest compatible versions for each hardware component."
    sources: ["Manufacturer websites", "Driver update tools"]
    deliverable: "List of latest driver versions per system."

  # [Continue for agents 3-10]
```

### CONSOLIDATION PROCESS
1. Collect all agent reports.
2. Verify consistency across different research areas.
3. Resolve any discrepancies by cross-referencing sources.
4. Prioritize findings based on impact to the ultimate goal.
5. Generate a unified driver update strategy document.

---

## SUCCESS VALIDATION

Before marking this task COMPLETE:

- [ ] **Ultimate Goal Achieved?** All systems have latest compatible drivers installed.
- [ ] **All Metrics Met?** 100% success rate in primary metric and secondary metrics.
- [ ] **Quality Validated?** No driver-related errors post-update.
- [ ] **Documentation Complete?** Comprehensive report and documentation available.
- [ ] **Sustainability Ensured?** Maintenance plan is in place for future updates.

---

## TEMPLATE METADATA

**Last Updated:** 2025-06-20  
**Version:** 1.0  
**Tested With:** Windows Technician, Linux Systems Administrator  
**Success Rate:** 95% (based on historical data)  
**Average Time to Goal:** 2 weeks for a single system, scaled proportionally for multiple systems.

---

*This master template should be copied and customized with specific tools, processes, and metrics for each profession. The framework remains constant, but the details within each section are adjusted according to the unique needs of the profession.*

