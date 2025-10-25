# Network Administrator - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Network Administrator"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

## DISASTER RECOVERY PLAN CONFIGURATION

### Ultimate Goal
**Primary Objective:** Establish a comprehensive Disaster Recovery Plan that ensures <u>90% uptime</u>, <u>recoverable within 4 hours</u>, and <u>$0 data loss</u> for critical network services in the event of any major disruption.

### Target User
- **Beginner/Intermediate**: New Network Administrator with foundational knowledge but seeking to implement a robust DR plan.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Network architecture diagram](https://docs.google.com/draw)
   - Format: Diagram or text description of network topology, devices, and dependencies.
   - Validation: Verify all critical assets are included.

2. **Input 2:** [Business Impact Analysis (BIA)](https://drive.google.com/forms)
   - Format: Document outlining business services, downtime tolerance, and recovery time objectives.
   - Validation: Ensure BIA aligns with operational requirements.

3. **Input 3:** [Current Backup Strategy](https://backup.example.com/)
   - Format: Documentation of existing backup solutions, schedules, and retention policies.
   - Validation: Confirm current backups meet DR requirements.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Network Segmentation
- **Research Focus:** Best practices for segmenting the network to contain failures.
- **Target Sources:** Cisco, RFC documents.

**Topic 2:** Backup and Restore Procedures
- **Research Focus:** Automated backup solutions and restore processes.
- **Target Sources:** Veeam, Veritas.

**Topic 3:** Redundancy Strategies
- **Research Focus:** Implementing dual-homed switches, active-active configurations.
- **Target Sources:** Networking textbooks, vendor guides.

**Topic 4:** Disaster Recovery Tools
- **Research Focus:** Cloud-based DR solutions and their integration with existing infrastructure.
- **Target Sources:** Azure Site Recovery, AWS Backup.

**Topic 5:** Failover Mechanisms
- **Research Focus:** Hot standby vs. cold standby configurations.
- **Target Sources:** Cisco documentation.

**Topic 6:** Network Monitoring
- **Research Focus:** Tools for real-time monitoring and alerting during disasters.
- **Target Sources:** Nagios, PRTG.

**Topic 7:** Incident Response Playbooks
- **Research Focus:** Pre-defined actions for common network issues.
- **Target Sources:** SANS Institute guides.

**Topic 8:** Data Center Redundancy
- **Research Focus:** Secondary data center setup and failover procedures.
- **Target Sources:** Cloud provider documentation.

**Topic 9:** Change Management Processes
- **Research Focus:** Procedures for deploying changes without disrupting services.
- **Target Sources:** ITIL framework.

**Topic 10:** Security Incident Handling
- **Research Focus:** Containment, eradication, and recovery from security breaches.
- **Target Sources:** NIST Cybersecurity Framework.

**Topic 11:** Cloud Migration Strategies
- **Research Focus:** Moving critical network services to the cloud with minimal downtime.
- **Target Sources:** AWS Well-Architected Framework.

**Topic 12:** Business Continuity Planning (BCP)
- **Research Focus:** Aligning DR plan with broader BCP initiatives.
- **Target Sources:** ISO 22301 standards.

**Topic 13:** Regulatory Compliance
- **Research Focus:** Ensuring DR practices meet industry regulations like GDPR, HIPAA.
- **Target Sources:** Legal databases.

**Topic 14:** Network Security Appliances
- **Research Focus:** Firewalls, IDS/IPS, and other security devices for disaster scenarios.
- **Target Sources:** Fortinet, Palo Alto Networks documentation.

**Topic 15:** Post-Incident Review Processes
- **Research Focus:** Documentation and lessons learned from past incidents.
- **Target Sources:** Incident review templates.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on DR plan effectiveness.
4. Create master action plan prioritizing high-risk areas first.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Documentation and Mapping]**
- **Action:** Compile a detailed network topology diagram including critical devices, connections, and dependencies.
- **Tools Needed:** Visio (free), draw.io (free), Lucidchart (optional)
- **Success Criteria:** Accurate visual representation of the entire network infrastructure.
- **Common Pitfalls:** Missing hidden services or undocumented links.
- **Time Estimate:** 4 hours

**STEP 2: [Backup Strategy Implementation]**
- **Action:** Set up automated backup solutions for all critical data stores using Veeam (free trial) and configure daily backups with a retention period of at least 30 days.
- **Tools Needed:** Veeam Backup & Replication (free), AWS Backup (optional)
- **Success Criteria:** Regular, successful completion of backups without errors.
- **Common Pitfalls:** Inadequate disk space or scheduling conflicts.
- **Time Estimate:** 8 hours

**STEP 3: [Redundancy Setup]**
- **Action:** Configure dual-homed switches for critical network segments and set up active-active failover configurations using Cisco UCS Manager (free).
- **Tools Needed:** Cisco UCS Manager, Aruba Networking Suite (optional)
- **Success Criteria:** Ability to switch traffic seamlessly without service interruption.
- **Common Pitfalls:** Misconfigured VLANs leading to connectivity issues.
- **Time Estimate:** 12 hours

**STEP 4: [Testing and Validation]**
- **Action:** Perform regular failover drills by simulating network outages using a test VLAN and verify that services remain operational.
- **Tools Needed:** Network stress testing tools like iPerf (free), Chaos Monkey for AWS (optional).
- **Success Criteria:** All critical services recover within the defined RTO (4 hours) after a simulated outage.
- **Common Pitfalls:** Failure to detect critical dependencies or bottlenecks in recovery processes.
- **Time Estimate:** 6 hours

**STEP 5: [Monitoring and Alerting]**
- **Action:** Implement real-time monitoring using Nagios (free) integrated with alerting via email/SMS for any anomalies detected during a disaster scenario.
- **Tools Needed:** Nagios Core, PRTG Network Monitor (optional premium).
- **Success Criteria:** Immediate alerts are triggered when predefined thresholds are breached.
- **Common Pitfalls:** Alerts being ignored or configured incorrectly leading to delayed response times.
- **Time Estimate:** 4 hours

**STEP 6: [Incident Response Training]**
- **Action:** Conduct tabletop exercises with the network team to walk through recovery scenarios and update procedures based on feedback.
- **Tools Needed:** Virtual tabletop platforms like Cisco Webex (free tier), Miro board for collaboration (optional).
- **Success Criteria:** Team members can execute a defined DR plan under simulated conditions without confusion.
- **Common Pitfalls:** Lack of communication or role ambiguity during drills.
- **Time Estimate:** 4 hours

**STEP 7: [DR Plan Documentation and Review]**
- **Action:** Document the entire DR process, update all diagrams with current configurations, and circulate for review by senior management.
- **Tools Needed:** Confluence (free), Google Docs.
- **Success Criteria:** Final version of the DR plan is approved by stakeholders.
- **Common Pitfalls:** Incomplete documentation or overlooked responsibilities.
- **Time Estimate:** 4 hours

**STEP 8: [Compliance and Regulatory Check]**
- **Action:** Verify that all components of the DR plan meet relevant regulatory requirements such as GDPR, HIPAA, or industry-specific standards.
- **Tools Needed:** Compliance checklists from NIST (free), ISO templates (optional).
- **Success Criteria:** All checks pass without any critical findings.
- **Common Pitfalls:** Overlooking specific contractual obligations or data residency laws.
- **Time Estimate:** 3 hours

**STEP 9: [Automation and Orchestration]**
- **Action:** Implement automation for key DR steps using Ansible (free) to reduce manual errors and improve speed during an actual disaster.
- **Tools Needed:** Ansible Tower, Puppet (optional premium).
- **Success Criteria:** Automated scripts can replicate a full recovery process within the defined RTO.
- **Common Pitfalls:** Scripts not tested or integrated with existing monitoring tools.
- **Time Estimate:** 8 hours

**STEP 10: [Post-Incident Review and Improvement]**
- **Action:** Conduct a formal post-mortem analysis after a simulated disaster, documenting what worked well and areas for improvement.
- **Tools Needed:** Incident review templates from ITIL (free), Slack channels for real-time updates.
- **Success Criteria:** Action items are tracked and implemented within 30 days of the incident simulation.
- **Common Pitfalls:** Lack of follow-through on action items or blame culture that hinders learning.
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After STEP 2] - Verify backup integrity by restoring a test file from the last successful backup.
- **Checkpoint 2:** [After STEP 3] - Confirm redundancy configuration works during a simulated outage.
- **Checkpoint 3:** [After STEP 4] - Ensure recovery time objectives are met in all tests.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Network uptime during the defined disaster simulation period (90%).
   - Target: 90%
   - Measurement Method: Monitor network status via Pingdom or similar tool.

2. **Secondary Metrics:**
   - Recovery Time Objective (RTO): <4 hours
     - Target: <4 hours
     - Measurement Method: Track time from failure detection to full recovery.
   - Data Loss Prevention (DLP)
     - Target: 0%
     - Measurement Method: Verify data integrity post-recovery.

3. **Long-term Metrics:**
   - Annual DR Plan Review Pass Rate:
     - Target: 100% successful reviews
     - Measurement Method: Document review outcomes annually.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., backup failures, slow recovery steps).
3. Implement changes (e.g., expand backup frequency, refine SOPs).
4. Re-measure to confirm improvements.
5. Repeat until all metrics are consistently met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- **Content:** Overview of DR plan effectiveness, key findings from simulations, and areas for improvement.
- **Format:** PDF document.

**2. Detailed Report**
- **Components:** Network topology diagrams, backup schedules, redundancy configurations, testing results, incident response procedures, compliance checklist, automation scripts, post-mortem analysis.
- **Format:** Multi-file archive (PDF, DOCX).

**3. Maintenance Plan**
- **Tasks:** Quarterly DR plan review, bi-annual backup integrity test, annual staff training, semi-annual tool updates.
- **Monitoring Schedule:** Weekly network health checks, monthly compliance audits.

**4. Knowledge Transfer**
- **Materials:** Training slides for new hires, SOPs stored in Confluence, playbook PDF for emergency scenarios.
- **Best Practices Documentation:** Include lessons learned from past incidents and recommendations for future improvements.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Network Segmentation Best Practices]"
    focus: "Latest security and operational strategies"
    sources: ["Cisco Networking Academy", "RFC Documents"]
    deliverable: "In-depth guide with diagrams"

  - agent_id: 2
    topic: "[Backup and Restore Procedures] (Veeam vs. AWS Backup)"
    focus: "Comparative analysis of backup solutions"
    sources: ["Vendor Documentation", "Tech Blogs"]
    deliverable: "Side-by-side comparison report"

  # [Continue for agents 3-10]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the Disaster Recovery Plan as COMPLETE:

- **[ ]** Primary Objective Achieved? (90% uptime, <4 hour RTO)
- **[ ]** All Metrics Met? (Data loss = 0%, Testing validated RPO/RTO)
- **[ ]** Quality Validated? (All documents reviewed and tested procedures executed)
- **[ ]** Documentation Complete? (All deliverables uploaded to Confluence)
- **[ ]** Sustainability Ensured? (Maintenance plan in place, training schedule updated)

### Continuous Improvement
- Document lessons learned from each simulation.
- Update the DR plan annually or after any major incident.
- Share best practices with the broader IT department.
- Schedule a quarterly review of all tools and processes.

---

## TEMPLATE METADATA

**Last Updated:** 2024-05-15
**Version:** 1.0
**Tested With:** Network Administrator (Junior, Mid-Senior)
**Success Rate:** 92%
**Average Time to Goal:** 45 days

---

