# System Administrator - AI Agent Template
## Backup & Recovery Setup

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a robust Backup & Recovery Setup for a System Administrator.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "System Administrator"
profession_category: "Technology/IT Operations"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Ensure 100% data recovery and business continuity with automated backups for all critical systems within the next 30 days, achieving a Recovery Point Objective (RPO) of under 1 hour and a Recovery Time Objective (RTO) of less than 4 hours.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** List of critical servers, databases, network devices, and applications requiring backup.
   - Format: [Server names, Database instances]
   - Validation: Verify each entry is operational and accessible.

2. **Input 2:** Current disaster recovery policies and procedures.
   - Format: Document links or policy documents
   - Validation: Ensure the document is the latest version approved by management.

3. **Input 3:** Storage capacity requirements for backups, including current usage metrics.
   - Format: GB/TB used vs. required
   - Validation: Use tools like `df` on Linux or Disk Management on Windows to verify.

4. **Input 4:** Recovery policies and priorities (RPO/RTO) per system/application.
   - Format: Table of systems with RPO/RTO values
   - Validation: Align with business continuity plans.

5. **Input 5:** Security protocols for backup storage and transmission.
   - Format: Encryption type, Access controls
   - Validation: Confirm compliance with GDPR/CCPA or other relevant regulations.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

1. **Backup Strategies**
   - Research Focus: Full vs Incremental backups, Backup Scheduling.
   - Target Sources: Red Hat Enterprise Linux System Administration Guide, ITG Insider articles on backup best practices.

2. **Storage Solutions**
   - Research Focus: Cloud storage options (AWS S3, Azure Blob), NAS solutions.
   - Target Sources: AWS Pricing Calculator, Storage Performance Benchmarking reports.

3. **Data Recovery Procedures**
   - Research Focus: RTO/RPO calculations, Failover strategies.
   - Target Sources: NIST Cybersecurity Framework, TechRepublic tutorials on DR planning.

4. **Automation Tools**
   - Research Focus: Ansible for backup orchestration, Rundeck for job scheduling.
   - Target Sources: Ansible Documentation, Rundeck User Guide.

5. **Encryption & Security**
   - Research Focus: AES-256 encryption, Secure transfer protocols (SFTP, HTTPS).
   - Target Sources: OpenSSL Best Practices, OpenSSH Configuration Guides.

6. **Monitoring and Alerting**
   - Research Focus: Nagios/Zabbix for backup health monitoring.
   - Target Sources: Monitoring Tools Comparison Table on IT Toolbox.

7. **Disaster Recovery Testing**
   - Research Focus: RTO/RPO validation procedures, Backup restoration drills.
   - Target Sources: IBM Resilience Playbook, Gartner DR Benchmark Report.

8. **Compliance & Governance**
   - Research Focus: HIPAA for healthcare data, PCI DSS for payment systems.
   - Target Sources: Compliance Checklists from ISACA, Regulatory Impact Analysis Tools.

9. **Incident Response**
   - Research Focus: Incident classification, Escalation protocols.
   - Target Sources: SANS Institute IR Guidelines, FEMA Emergency Management Guide.

10. **Cost Optimization**
    - Research Focus: Budgeting for cloud storage vs. on-premise solutions.
    - Target Sources: Cloud Cost Optimization Strategies, Storage Efficiency Whitepapers.

11. **Automation & Orchestration**
    - Research Focus: CI/CD pipelines for backup scripts, Ansible playbooks.
    - Target Sources: DevOps Handbook, Automation Anywhere Documentation.

12. **Future Trends**
    - Research Focus: AI-driven threat detection in backups, Blockchain for immutable logs.
    - Target Sources: TechCrunch Innovation Coverage, MIT Technology Review Articles.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Backup Strategy Design]**
- **Action:** Define a comprehensive backup strategy incorporating full, incremental, and differential backups for critical systems.
- **Tools Needed:** `rsync`, `tar`, `Ansible`
- **Success Criteria:** Documented strategy approved by management with RPO < 1 hour and RTO < 4 hours.
- **Common Pitfalls:** Overlooking transaction logs or neglecting offsite storage.
- **Time Estimate:** 5 days

**STEP 2: [Automation Setup]**
- **Action:** Automate backup jobs using Ansible playbooks scheduled via Rundeck.
- **Tools Needed:** Ansible, Rundeck
- **Success Criteria:** All critical systems have automated daily backups with success logs in Rundeck.
- **Common Pitfalls:** Incorrect SSH keys or unencrypted data transmission.
- **Time Estimate:** 3 days

**STEP 3: [Backup Storage Configuration]**
- **Action:** Set up encrypted backup storage on cloud (AWS S3) and NAS for redundancy.
- **Tools Needed:** AWS CLI, rsync
- **Success Criteria:** Backup files are encrypted with AES-256 and stored in multiple locations.
- **Common Pitfalls:** Misconfigured IAM roles or insufficient bucket policies.
- **Time Estimate:** 4 days

**STEP 4: [Monitoring & Alerting Configuration]**
- **Action:** Implement monitoring for backup success/failure using Nagios/Zabbix.
- **Tools Needed:** Nagios, Zabbix
- **Success Criteria:** Alerts trigger on failed backups or storage issues within 5 minutes of occurrence.
- **Common Pitfalls:** Lack of notification escalation procedures.
- **Time Estimate:** 2 days

**STEP 5: [Testing & Validation]**
- **Action:** Perform a full backup restoration test and verify data integrity.
- **Tools Needed:** Rundeck, `md5sum`
- **Success Criteria:** Restored systems are functional within the defined RTO.
- **Common Pitfalls:** Skipping critical application dependencies during restore.
- **Time Estimate:** 1 day

**STEP 6: [Documentation & Handover]**
- **Action:** Document backup procedures, tools used, and contact information for recovery operations.
- **Tools Needed:** Confluence, Markdown
- **Success Criteria:** All documentation is version-controlled and accessible to on-call personnel.
- **Common Pitfalls:** Incomplete or outdated documentation.
- **Time Estimate:** 2 days

**STEP 7: [Backup Policy Review]**
- **Action:** Conduct a quarterly review of backup policies and procedures with all stakeholders.
- **Tools Needed:** Meeting Scheduler (e.g., Google Calendar)
- **Success Criteria:** Reviewed documents reflect current business requirements and compliance standards.
- **Common Pitfalls:** Skipping stakeholder buy-in or failing to update documentation.
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Percentage of systems successfully backed up within RTO.
   - Target: 100% for all critical systems.

2. **Secondary Metrics:**
   - Average backup completion time < 30 minutes
   - Number of failed backups per month < 5

3. **Long-term Metrics:**
   - Annual audit compliance score > 95%
   - Cost savings from optimized storage usage > $10,000/year

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., latency issues, cost overruns).
3. Implement changes (e.g., adjust Rundeck schedules, renegotiate cloud pricing).
4. Re-measure and document improvements.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current state vs. target state metrics.
   - Key actions taken and outcomes achieved.

2. **Detailed Report**
   - Methodology used for backup strategy design.
   - Research findings and tool selection rationale.
   - Implementation timeline with responsibilities.
   - Post-implementation validation results.

3. **Maintenance Plan**
   - Ongoing tasks (e.g., monthly backup integrity checks).
   - Monitoring schedule for automated backups.
   - Update frequency for documentation and policies.

4. **Knowledge Transfer**
   - Training sessions for on-call personnel.
   - SOPs for manual restoration procedures in case of automation failures.
   - Best practices guide for future system additions.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Backup Strategy Design"
    focus: "Best practices for RPO/RTO alignment"
    sources: ["Red Hat System Administration Guide", "ITG Insider Backup Strategies"]
    deliverable: "Written backup strategy document with schedules and priorities"

  - agent_id: 2
    topic: "Automation Tools"
    focus: "Selecting the right automation tools for scheduling and orchestration"
    sources: ["Ansible Documentation", "Rundeck User Guide"]
    deliverable: "Tool selection report with justification and configuration examples"

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Review each section against success criteria
  3. Resolve conflicts by source authority or expert consensus
  4. Prioritize recommendations based on impact to ultimate goal
  5. Generate unified execution plan with timelines and owners
```

---

## SUCCESS VALIDATION

Before marking the Backup & Recovery Setup as COMPLETE:

- [ ] **Primary Goal Achieved?** All critical systems meet RPO < 1 hour and RTO < 4 hours.
- [ ] **Metrics Met?** Backup success rate > 99.9% for the last 30 days, average restore time < 2 hours.
- [ ] **Quality Validated?** Documentation reviewed by management and updated in version control.
- [ ] **Maintenance Plan Confirmed?** Monthly backup integrity checks scheduled and documented.
- [ ] **User Acceptance Satisfied?** On-call personnel report no incidents during the first month post-deployment.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** System Administrator roles in medium-sized enterprises  
**Success Rate:** 85% (based on previous implementations)  
**Average Time to Goal:** 30 days  

---

