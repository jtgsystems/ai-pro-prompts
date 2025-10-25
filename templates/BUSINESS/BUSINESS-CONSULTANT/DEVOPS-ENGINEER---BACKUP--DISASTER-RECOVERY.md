# DevOps Engineer - AI Agent Template

## Backup & Disaster Recovery

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve effective Backup & Disaster Recovery for a DevOps Engineer.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "DevOps Engineer"
profession_category: "Technology/Engineering"
experience_level: "[Beginner/Intermediate]"
```

#### Ultimate Goal
**Primary Objective:** Implement a robust, automated Backup & Disaster Recovery (BDR) solution that restores all critical systems and data within 2 hours of an incident, with 99.9% recovery success rate over the past year.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Target Environment:** List of cloud platforms (AWS/Azure/GCP), container orchestration tools (Kubernetes), and application architectures.
2. **Critical Data Sources:** Database types, file servers, logs, configuration files.
3. **Recovery Time Objective (RTO):** Maximum acceptable downtime for each system component.
4. **Recovery Point Objective (RPO):** Maximum data loss tolerance.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received and correctly formatted.
- [ ] Validate that the target environment is defined with correct cloud provider, region settings.
- [ ] Confirm RTO/RPO metrics are measurable and realistic for the business.
- [ ] Establish baseline metrics: current downtime frequency, data loss incidents.

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (12 Topics)

**1. Cloud Backup Strategies**
   - **Research Focus:** Best practices for cloud-native backup solutions in AWS, Azure, GCP.
   - **Target Sources:** AWS Backup Service Documentation, Azure Recovery Services, GCP Storage Solutions.

**2. Data Replication Techniques**
   - **Research Focus:** Real-time vs asynchronous replication methods for databases and file systems.
   - **Target Sources:** PostgreSQL WAL shipping docs, MongoDB Atlas replication guides.

**3. Automated Disaster Recovery (DR) Testing**
   - **Research Focus:** Frameworks for automating DR drills using Terraform or Ansible.
   - **Target Sources:** AWS Well-Architected Framework, ITIL disaster recovery processes.

**4. Version Control Systems**
   - **Research Focus:** Integrating backup solutions with Git for change management.
   - **Target Sources:** GitHub Actions, GitLab CI/CD pipelines.

**5. Infrastructure as Code (IaC) Tools**
   - **Research Focus:** Best IaC practices for consistent deployment of BDR infrastructure.
   - **Target Sources:** Terraform Registry, AWS CloudFormation Templates.

**6. Monitoring and Alerting**
   - **Research Focus:** Tools to monitor backup success rates and alert on failures.
   - **Target Sources:** Prometheus + Grafana dashboards, Datadog APM.

**7. Encryption & Compliance**
   - **Research Focus:** Ensuring data-at-rest and in-transit encryption meet regulatory standards (GDPR, HIPAA).
   - **Target Sources:** OpenSSL docs, AWS KMS documentation.

**8. Backup Orchestration Tools**
   - **Research Focus:** Centralized management of backup jobs across environments.
   - **Target Sources:** Restic, Rclone, Bacula Enterprise.

**9. Data Archiving Strategies**
   - **Research Focus:** Tiered storage solutions for long-term retention and cost optimization.
   - **Target Sources:** Lifecycle policies in S3, Azure Archive Storage.

**10. Failover/Fallback Mechanisms**
   - **Research Focus:** Redundant architectures that automatically switch to backup environments during failure.
   - **Target Sources:** Kubernetes StatefulSets, DNS failover solutions.

**11. Cost Optimization Techniques**
   - **Research Focus:** Balancing storage costs with data protection needs.
   - **Target Sources:** AWS Storage Costs Calculator, Azure Reserved Instances pricing.

**12. Emerging Trends (2024-2025)**
   - **Research Focus:** Integration of AI for predictive backups and anomaly detection in recovery processes.
   - **Target Sources:** Papers on AI-driven backup solutions, vendor blogs.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: Infrastructure Provisioning**
- **Action:** Deploy cloud-based infrastructure using Terraform with separate resources for primary and secondary environments.
- **Tools Needed:** Terraform (free), AWS/Azure/GCP Console, Git Repository.
- **Success Criteria:** All infra components are up and running in both regions without manual intervention.
- **Common Pitfalls:** Misconfigured VPC peering or IAM policies; Missing resource tagging.
- **Time Estimate:** 2 days

**STEP 2: Backup Policy Configuration**
- **Action:** Define backup schedules (daily, weekly), retention periods (7/30/90 days), and encryption settings using Restic for data at rest.
- **Tools Needed:** Restic CLI (free), AWS S3 Bucket Policies, Azure Storage ACLs.
- **Success Criteria:** Automated backups run successfully with 0 errors; Encryption keys are stored securely in KMS.
- **Common Pitfalls:** Overlapping backup jobs causing resource contention.
- **Time Estimate:** 1 day

**STEP 3: Data Replication Setup**
- **Action:** Configure asynchronous replication of databases (e.g., PostgreSQL) to secondary region using native tools or third-party services like Zerto.
- **Tools Needed:** pglogical extension, Zerto (optional premium), Cloud provider cross-region replication.
- **Success Criteria:** Replication lag < 5 minutes; Data integrity verified through checksum comparison.
- **Common Pitfalls:** Network bandwidth throttling causing delayed syncs.
- **Time Estimate:** 2 days

**STEP 4: Automated DR Testing**
- **Action:** Implement a monthly automated test using Ansible to failover from primary to secondary environment and verify data restoration.
- **Tools Needed:** Ansible (free), JUnit tests for validation, Terraform state management.
- **Success Criteria:** Test completes within scheduled window; All critical services operational in DR location.
- **Common Pitfalls:** Environment drift causing test failures; Incomplete rollback scripts.
- **Time Estimate:** 1 day

**STEP 5: Monitoring & Alerting**
- **Action:** Set up Prometheus alerts for backup job status, storage utilization, and replication health. Integrate with PagerDuty for incident response.
- **Tools Needed:** Prometheus + Grafana (free), PagerDuty (optional premium), Slack notifications.
- **Success Criteria:** Alerts trigger correctly during simulated failures; Teams respond within SLA timeframes.
- **Common Pitfalls:** Alert fatigue due to too many thresholds; False positives from benign issues.
- **Time Estimate:** 2 days

**STEP 6: Encryption & Compliance Verification**
- **Action:** Generate encryption keys in AWS KMS/ Azure Key Vault and verify they are used during backup jobs. Conduct a compliance audit checklist.
- **Tools Needed:** AWS KMS (free), Azure Key Vault (free), Cloud Compliance Toolkit.
- **Success Criteria:** All backups encrypted with validated key IDs; Audit shows no critical findings.
- **Common Pitfalls:** Keys misconfigured or deleted; Non-compliant storage locations used.
- **Time Estimate:** 1 day

**STEP 7: Version Control Integration**
- **Action:** Commit backup scripts, Terraform configurations, and Ansible playbooks to Git. Use pull requests for code review before deployment.
- **Tools Needed:** GitHub/GitLab (free), CI/CD pipeline integration, Code signing keys.
- **Success Criteria:** All changes pass automated linting; Deployment runs without manual intervention.
- **Common Pitfalls:** Uncommitted changes leading to incomplete deployments; Branch merging conflicts.
- **Time Estimate:** 1 day

**STEP 8: Documentation & Knowledge Transfer**
- **Action:** Document the entire BDR process, including SOPs for failover/fallback procedures, escalation paths, and data restoration steps. Conduct a knowledge transfer session with team members.
- **Tools Needed:** Confluence (optional premium), Markdown files in Git repo, Training sessions via Zoom/WebEx.
- **Success Criteria:** Team can independently execute at least one failover drill; Documentation version is locked.
- **Common Pitfalls:** Outdated documentation; Lack of hands-on training for new hires.
- **Time Estimate:** 1 day

**STEP 9: Cost Optimization Review**
- **Action:** Analyze storage costs and data transfer charges. Implement lifecycle policies to move older backups to cheaper tiered storage (e.g., Glacier).
- **Tools Needed:** AWS Cost Explorer, Azure Cost Management, Lifecycle policies in S3.
- **Success Criteria:** Monthly storage cost reduction by X%; Data stored appropriately across tiers based on access frequency.
- **Common Pitfalls:** Underestimating data growth; Over-relying on free tier limits.
- **Time Estimate:** 1 day

**STEP 10: Incident Response Plan Update**
- **Action:** Revise the incident response playbook to include BDR procedures. Conduct a tabletop exercise with relevant stakeholders.
- **Tools Needed:** Incident Response Template (free), Tabletop Exercise Simulations.
- **Success Criteria:** All participants can identify roles, execute steps within defined timeframes; Post-mortem action items are documented and tracked.
- **Common Pitfalls:** Lack of clear ownership; Inadequate communication channels during testing.
- **Time Estimate:** 1 day

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
1. **Primary Metric:** Mean Time to Recovery (MTTR) for failed systems should be ≤ 2 hours.
   - Target: < 120 minutes per incident in the last quarter.
   - Measurement Method: Track recovery completion time via monitoring dashboards.

2. **Secondary Metrics:**
   - Backup Success Rate: ≥ 99.9%
     - Measurement: Number of successful backups vs total attempts over a month.
   - Data Integrity Verification: All restores pass checksum validation tests.
     - Measurement: Automated verification scripts post-recovery.

3. **Long-term Metrics:**
   - Cost Efficiency Index (CEI): Total BDR-related costs as % of budget.
     - Measurement: Annual cost divided by allocated budget.

#### Iterative Improvement Loop
1. Measure current performance against targets for the past 30 days.
2. Identify top 3 improvement opportunities based on metric gaps.
3. Implement changes (e.g., adjust RTO/RPO, update encryption policies).
4. Re-measure to confirm improvements.
5. Repeat quarterly until all metrics meet or exceed targets.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
1. **Executive Summary**
   - Current State vs Target: Brief overview of existing BDR capabilities and desired outcomes.
   - Key Actions Taken: List of major changes implemented during the project.
   - Results Achieved: Quantitative data on improved recovery times, cost savings.

2. **Detailed Report**
   - Methodology Overview
   - Research Findings (with citations)
   - Implementation Steps with Screenshots/Diagrams
   - Testing Results and Metrics

3. **Maintenance Plan**
   - Ongoing Tasks: Weekly backup verification scripts; Monthly cost review.
   - Monitoring Schedule: Automated alerts for critical metrics; Daily status dashboard.
   - Update Frequency: Quarterly audit of policies; Bi-annual technology refresh.

4. **Knowledge Transfer**
   - Training Materials: Step-by-step guides, cheat sheets for team members.
   - SOPs: Standard Operating Procedures stored in Confluence with version control.
   - Troubleshooting Guide: Common issues and their resolutions documented.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

1. **Replace All [BRACKETED] Items** with concrete examples from the DevOps Engineer's role, such as AWS S3 Buckets, Kubernetes Clusters, Terraform Modules.
2. **Define 12 Critical Topics** based on actual tools and practices used in 2024-2025:
   - Cloud Backup for IaC environments
   - Real-time Replication of Docker/Kubernetes State
   - Automated DR Testing with Chaos Engineering
   - Encryption as a Service (EFS) Integration
   - Version Control Best Practices for Infrastructure Changes
   - Monitoring with Open Source Stack
   - Compliance Automation via Policy-as-Code

3. **Map Ultimate Goal to Measurable Outcomes**:
   - "Restore 100% of application data within 2 hours during scheduled DR drills" (SMART: Specific, Measurable, Achievable, Relevant, Time-bound).

4. **Build Step-by-Step Workflow** from industry playbooks such as AWS Well-Architected Framework and ITIL v4.
5. **Include Latest 2024-2025 Practices**:
   - AI-driven backup analytics using open-source tools like Kubeflow for model training on backup data patterns.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Cloud Backup Strategies]"
    focus: "Evaluate cloud-native backup solutions"
    sources: ["AWS Backup Service Documentation", "Azure Recovery Services", "GCP Storage Solutions"]
    deliverable: "Comparative analysis with cost and compliance scorecard"

  # [Continue for agents 2-12]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to ultimate goal
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

**Final Checklist**
- [ ] **Primary Goal Achieved?** Restore all critical systems within 2 hours.
- [ ] **Metrics Met:** Average MTTR < 120 minutes, Backup Success Rate ≥ 99.9%.
- [ ] **Quality Validated:** All scripts pass linting; Documentation reviewed by peers.
- [ ] **Documentation Complete:** All SOPs, Dashboards, and Incident Playbooks stored in version control.
- [ ] **Sustainability Ensured:** Ongoing monitoring schedule added to CI/CD pipeline.

**Continuous Improvement**
- Document lessons learned from each DR test in a shared Confluence page.
- Update the cost optimization strategy quarterly based on actual usage data.
- Schedule an annual review with stakeholders to refresh encryption policies and compliance checks.

---

### TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** DevOps Engineer (AWS, Azure), Kubernetes, Terraform  
**Success Rate:** Aim for ≥ 95% successful recoveries per DR test

