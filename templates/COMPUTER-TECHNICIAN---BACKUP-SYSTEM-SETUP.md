# Computer Technician - AI Agent Template
## Backup System Setup

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a reliable backup system setup for computer technicians.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "Beginner to Intermediate (new to the role)"
```

### Ultimate Goal
**Primary Objective:** Set up a fully functional, automated backup system for all critical data on client devices, ensuring 100% recovery capability within 24 hours of any failure.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information is needed to start:

1. **Input 1:** List of client systems (devices) that need backups.
   - Format: [Device ID]
   - Validation: Verify each device's IP or MAC address exists in the system database.

2. **Input 2:** Backup requirements:
   - Frequency (daily, weekly)
   - Retention period
   - Priority level (critical vs. non-critical data)

3. **Input 3:** Destination for backups:
   - Local network share path
   - Cloud storage provider and bucket name

4. **Input 4:** Access credentials for destination.
   - Format: [Username, Password]
   - Validation: Ensure credentials are valid.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness (no missing device IDs or invalid paths).
- [ ] Identify immediate red flags or blockers (e.g., incompatible devices).
- [ ] Establish baseline metrics (current backup status, data loss risk).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Cloud Storage Options
- Research Focus: Best cloud providers for security and cost.
- Target Sources: Pricing calculators, customer reviews.

**Topic 2:** Network Infrastructure
- Research Focus: Bandwidth requirements, latency impact on backup speed.
- Target Sources: ISP bandwidth limits, network performance reports.

**Topic 3:** Encryption Standards
- Research Focus: AES encryption best practices for data at rest and in transit.
- Target Sources: NIST guidelines, vendor documentation.

**Topic 4:** Backup Scheduling Tools
- Research Focus: Automation tools that support recurring backups.
- Target Sources: Vendor comparison sites, user forums.

**Topic 5:** Data Deduplication Techniques
- Research Focus: Reducing storage needs without data loss risk.
- Target Sources: Tech blogs, vendor whitepapers.

**Topic 6:** Failover Strategies
- Research Focus: Mechanisms to switch to a secondary backup if primary fails.
- Target Sources: Disaster recovery guides, industry case studies.

**Topic 7:** Compliance and Regulatory Requirements
- Research Focus: GDPR, HIPAA, or other regulations affecting data backups.
- Target Sources: Legal databases, compliance checklists.

**Topic 8:** Security Best Practices
- Research Focus: Protecting backup systems from ransomware and unauthorized access.
- Target Sources: Cybersecurity reports, vendor security features.

**Topic 9:** Monitoring and Alerting Tools
- Research Focus: Systems to track backup success/failure status.
- Target Sources: Review sites, technical blogs.

**Topic 10:** Scalability Solutions
- Research Focus: How to expand backups for large networks or growing data volumes.
- Target Sources: Cloud provider scalability docs, vendor whitepapers.

**Topic 11:** Automated Remediation Scripts
- Research Focus: PowerShell/Batch scripts that restore from backup in case of failure.
- Target Sources: Script repositories (GitHub), vendor tutorials.

**Topic 12:** Network Security Protocols
- Research Focus: Firewalls and VPNs needed to secure backup traffic.
- Target Sources: Firewall configuration guides, security blogs.

**Topic 13:** Data Integrity Checks
- Research Focus: Methods to verify data is correctly restored after a restore test.
- Target Sources: Recovery testing frameworks, vendor documentation.

**Topic 14:** Role-Based Access Control (RBAC)
- Research Focus: How to limit access to backup systems based on user roles.
- Target Sources: RBAC best practice articles, security standards.

**Topic 15:** Cost Optimization Strategies
- Research Focus: Balancing storage needs with budget constraints.
- Target Sources: Budgeting tools, cost comparison sites.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Network Configuration]**
- **Action:** Set up a secure network path to the backup destination.
- **Tools Needed:** PowerShell (Windows) or SSH client (Linux).
- **Success Criteria:** Successful initial connection test (ping/SSH login).

**STEP 2: [Backup Software Installation]**
- **Action:** Install an open-source, free backup solution like Duplicati or Restic.
- **Tools Needed:** Duplicati CLI or Restic CLI.
- **Success Criteria:** Backup software runs without errors.

**STEP 3: [Initial Data Transfer]**
- **Action:** Perform a full data transfer to the backup location.
- **Tools Needed:** Selected backup software (Duplicati/Restic).
- **Success Criteria:** All devices backed up successfully with zero errors.

**STEP 4: [Automation Setup]**
- **Action:** Schedule recurring backups based on client requirements.
- **Tools Needed:** Task Scheduler (Windows) or cron jobs (Linux).
- **Success Criteria:** Backups run automatically at scheduled times without manual intervention.

**STEP 5: [Encryption Implementation]**
- **Action:** Encrypt all data during transfer and at rest using AES-256 encryption.
- **Tools Needed:** Duplicati/Restic with built-in encryption, or open-source tools like OpenSSL.
- **Success Criteria:** Data remains encrypted when in transit and on the backup server.

**STEP 6: [Backup Verification]**
- **Action:** Test restoring a small sample of data to ensure integrity.
- **Tools Needed:** Backup software restore feature.
- **Success Criteria:** Successfully restored data matches original data byte-for-byte.

**STEP 7: [Failover Configuration]**
- **Action:** Set up an alternative backup destination for failover scenarios.
- **Tools Needed:** Additional cloud storage or local drive.
- **Success Criteria:** Ability to switch between primary and secondary backups without data loss.

**STEP 8: [Security Hardening]**
- **Action:** Implement firewall rules, VPN connections, and RBAC policies.
- **Tools Needed:** Firewall configuration tools (Windows Defender Firewall), OpenVPN client.
- **Success Criteria:** Only authorized personnel can access the backup system.

**STEP 9: [Monitoring & Alerting Setup]**
- **Action:** Configure alerts for backup success/failure status.
- **Tools Needed:** Monitor software like NAGIOS or Zabbix.
- **Success Criteria:** Real-time notifications sent on backup failures.

**STEP 10: [Documentation and Training]**
- **Action:** Document the entire process and train support staff.
- **Tools Needed:** Confluence, Google Docs.
- **Success Criteria:** All team members can execute the backup procedure without assistance.

### Quality Checkpoints
Insert checkpoints between major steps:

**Checkpoint 1:** Verify successful network connection (after Step 1).
**Checkpoint 2:** Confirm backup software runs correctly (after Step 3).
**Checkpoint 3:** Validate encryption settings are active (after Step 4).
**Checkpoint 4:** Ensure automated backups trigger as scheduled.
**Checkpoint 5:** Check restore functionality after Step 6.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Backup Success Rate
   - Target: >99% successful backup attempts per month.
   - Measurement Method: Log retention rates from backup software.

2. **Secondary Metrics:**
   - Average time for full backups (daily, weekly).
   - Data integrity check results (checksum match).
   - Frequency of restore tests passed vs. failed.

3. **Long-term Metrics:**
   - Monthly client satisfaction survey score.
   - Number of security incidents related to backup system.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., bandwidth issues, restore failures).
3. Implement changes based on findings.
4. Re-measure results and adjust until metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state of backup system vs. target state.
- Key actions taken to achieve the goal.
- Results achieved with measurable KPIs.

**2. Detailed Report**
- Complete methodology and process documentation.
- All research findings, including tool comparisons.
- Implementation details for each step.
- Before/after comparison metrics (e.g., downtime before vs. after).

**3. Maintenance Plan**
- Ongoing tasks to maintain backups (regular verification).
- Monitoring schedule (daily/weekly reports).
- Update frequency of backup software and policies.

**4. Knowledge Transfer**
- Training materials for staff on using the new backup system.
- SOPs detailing how to perform restores, updates, and audits.
- Troubleshooting guide covering common issues like encryption failures or restore errors.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace All [BRACKETED] Items** with specific data such as actual device IDs from client inventory systems.
2. **Define 15 Critical Topics** based on the technician's role and tools:
   - Cloud Storage Options (AWS, Azure, Google Cloud)
   - Network Infrastructure (bandwidth tests, latency analysis)
   - Encryption Standards (AES-256 compliance)
   - Backup Scheduling Tools (cron jobs vs. Task Scheduler)
   - Data Deduplication Techniques (WORM storage)
   - Failover Strategies (active-passive clustering)
   - Compliance and Regulatory Requirements (HIPAA for healthcare)
   - Security Best Practices (multi-factor authentication)
   - Monitoring and Alerting Tools (Nagios, Splunk)
   - Scalability Solutions (distributed cloud backup)
   - Automated Remediation Scripts (PowerShell runbooks)
   - Network Security Protocols (TLS 1.3 encryption)
   - Data Integrity Checks (checksum validation)

3. **Define Ultimate Goal** with specific metrics:
   - Success Metric: Achieve 99% uptime of backups over a 30-day period.
   - Time-Bound: Complete setup within 4 business days.

4. **Build Step-by-Step Workflow** from:
   - Backup software vendor documentation (e.g., Restic, Duplicati).
   - Network performance reports from ISPs.
   - Security frameworks like NIST CSF.
   - Case studies of successful cloud backup implementations in small businesses.

5. **Include Latest 2024-2025 Practices**:
   - Use AI to predict potential failures based on historical data.
   - Integrate with Azure Sentinel for real-time alerting and incident response.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "5 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Cloud Storage Options]"
    focus: "Best cloud providers for cost and security"
    sources: ["AWS Pricing Calculator", "Azure Pricing", "Google Cloud Pricing"]
    deliverable: "Recommended provider with justification"

  - agent_id: 2
    topic: "[Network Infrastructure Analysis]"
    focus: "Bandwidth requirements analysis"
    sources: ["ISP bandwidth reports", "network performance tools"]
    deliverable: "Optimal network path for backups"

  # [Continue for agents 3-15]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the task COMPLETE:

- [ ] **Primary Metric Achieved?** Backup success rate >99%.
- [ ] **Backup Frequency Met?** All devices backed up according to schedule.
- [ ] **Encryption Validated?** Data encrypted during transfer and at rest.
- [ ] **Failover Tested?** Failover mechanism works in a simulated environment.
- [ ] **Security Audited?** Backup system passes penetration tests.
- [ ] **Documentation Complete?** All steps documented with screenshots.

### Continuous Improvement
- Document lessons learned from each backup test.
- Update tools and processes based on new regulations (e.g., GDPR 2024).
- Share best practices with the team through monthly knowledge sessions.

