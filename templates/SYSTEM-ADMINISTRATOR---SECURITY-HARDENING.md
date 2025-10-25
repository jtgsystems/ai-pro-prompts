# System Administrator - AI Agent Template
## Security Hardening

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve security hardening as a System Administrator.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "System Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve a hardened system state where all critical systems and data are protected against unauthorized access, modification, or theft while maintaining operational availability.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
```yaml
- target_system_list: [List of critical servers, services, databases]
- compliance_standards: [ISO 27001, PCI DSS, HIPAA]
- security_policy_document: [Link to current policy or document location]
```

### Initial Assessment Checklist
```yaml
- Verify all required inputs received and are valid.
- Validate input quality based on industry standards.
- Identify immediate red flags (e.g., unpatched systems).
- Establish baseline metrics for system integrity, vulnerability scores, and access controls.
```

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices.

**Topic 1:** Patch Management  
- **Research Focus:** Latest patching schedules, automated tools, validation processes.  
- **Target Sources:** Red Hat/CentOS release notes, NIST guidelines, vendor advisories.  
- **Deliverable:** Recommended quarterly/real-time patching cadence with automation steps.

**Topic 2:** Access Control & Authentication  
- **Research Focus:** Role-Based Access Control (RBAC), Multi-Factor Authentication (MFA).  
- **Target Sources:** OASIS standards, SANS best practices.  
- **Deliverable:** Policy draft for least privilege access and MFA implementation.

**Topic 3:** Configuration Hardening  
- **Research Focus:** CIS Benchmarks, SSH hardening, service default settings.  
- **Target Sources:** CIS documentation, vendor configuration guides.  
- **Deliverable:** Checklist of security-critical config changes.

**Topic 4:** Logging & Monitoring  
- **Research Focus:** SIEM integration, alert thresholds, log retention policies.  
- **Target Sources:** ELK Stack docs, Splunk/Sumo Logic pricing models.  
- **Deliverable:** Log aggregation setup plan and alert configuration guide.

**Topic 5:** Network Segmentation  
- **Research Focus:** VLAN best practices, firewall rules for segmentation.  
- **Target Sources:** CIS network hardening guidelines, Cisco security whitepapers.  
- **Deliverable:** Diagram of segmented network zones with recommended firewall policies.

**Topic 6:** Vulnerability Management  
- **Research Focus:** Scanning tools (Nessus, OpenVAS), prioritization frameworks.  
- **Target Sources:** NVD CVE data, vendor advisories.  
- **Deliverable:** Vulnerability scanning schedule and remediation workflow.

**Topic 7:** Endpoint Security  
- **Research Focus:** Antivirus/EDR deployment, container security for microservices.  
- **Target Sources:** CrowdStrike, Carbon Black documentation.  
- **Deliverable:** Recommended EDR solution with integration steps.

**Topic 8:** Backup & Recovery  
- **Research Focus:** Encryption at rest/in transit, test retention periods.  
- **Target Sources:** AWS RDS docs, VMware backup solutions.  
- **Deliverable:** Full backup/restore procedure with encryption requirements.

**Topic 9:** Incident Response Planning  
- **Research Focus:** Playbooks for ransomware, insider threats, DDoS.  
- **Target Sources:** NIST IR guide, SANS incident response framework.  
- **Deliverable:** Incident response playbook with communication templates.

**Topic 10:** Compliance Frameworks  
- **Research Focus:** Mapping controls to relevant frameworks (PCI-DSS, HIPAA).  
- **Target Sources:** Official compliance guides, audit reports.  
- **Deliverable:** Control matrix showing implemented measures vs. requirements.

**Topics 11-20 (Advanced):**
- Cloud Security Posture Management (CSPM)
- DevSecOps Integration
- Zero Trust Architecture Implementation
- Threat Intelligence Feeds
- Automated Remediation with Ansible/Puppet

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact and feasibility.
4. Create master action plan.

---

## PHASE 3: EXECUTION WORKFLOW

**STEP 1: Patch Management**
- **Action:** Update all systems to latest patches using automated tools like Ansible or PowerShell DSC.  
- **Tools Needed:** Ansible, WSUS/AD groups for Windows servers, yum/apt update for Linux.  
- **Success Criteria:** No critical vulnerabilities (CVSS > 7) remain unpatched after scan.  
- **Common Pitfalls:** Manual patching bypasses automation; testing fails.  
- **Time Estimate:** 48 hours

**STEP 2: Access Control & Authentication**
- **Action:** Enforce MFA for all privileged accounts, remove unused accounts.  
- **Tools Needed:** Okta/Phoebus SSO integration, PowerShell module for user management.  
- **Success Criteria:** 100% of admin accounts have MFA enabled; no inactive accounts >90 days.  
- **Common Pitfalls:** Incomplete account inventory; users forget new passwords.  
- **Time Estimate:** 5 hours

**STEP 3: Configuration Hardening**
- **Action:** Apply CIS benchmark settings to all servers, enforce encryption.  
- **Tools Needed:** Benchmarks for Linux (Ansible playbooks), PowerShell Desired State Config for Windows.  
- **Success Criteria:** Compliance score >95% across all systems; no plaintext passwords in configs.  
- **Common Pitfalls:** Misconfiguration of critical services; non-compliant hosts remain.  
- **Time Estimate:** 4 days

**STEP 4: Logging & Monitoring**
- **Action:** Deploy centralized log aggregation, set up alerting for suspicious activity.  
- **Tools Needed:** Elastic Stack (ELK), Splunk Cloud, OSSEC/HIDS agent installation.  
- **Success Criteria:** No critical logs missing; alerts fire on simulated attacks.  
- **Common Pitfalls:** Log retention not configured; monitoring alerts ignored.  
- **Time Estimate:** 2 days

**STEP 5: Network Segmentation**
- **Action:** Implement VLANs and firewall rules to isolate systems by function.  
- **Tools Needed:** Cisco ASA/Checkpoint firewalls, subnet calculator tools.  
- **Success Criteria:** Traffic between segments blocked on non-standard ports; no open RDP traffic from internet.  
- **Common Pitfalls:** Overly permissive default policies; segmentation bypasses firewall rules.  
- **Time Estimate:** 3 days

**STEP 6: Vulnerability Management**
- **Action:** Schedule quarterly scans, remediate critical findings immediately.  
- **Tools Needed:** OpenVAS/Nessus for scanning, Tenable.io for reporting.  
- **Success Criteria:** <5 critical vulnerabilities remaining after each scan cycle.  
- **Common Pitfalls:** Remediation delayed; false positives ignored.  
- **Time Estimate:** Ongoing (Quarterly)

**STEP 7: Endpoint Security**
- **Action:** Deploy EDR solution, configure anti-malware on all endpoints.  
- **Tools Needed:** CrowdStrike Falcon, Carbon Black Control Point, Windows Defender ATP.  
- **Success Criteria:** No malware detected in real-time scans; alerts triggered on suspicious behavior.  
- **Common Pitfalls:** Endpoint whitelisting too permissive; EDR not collecting data properly.  
- **Time Estimate:** 3 days

**STEP 8: Backup & Recovery**
- **Action:** Encrypt backups at rest, test restore process quarterly.  
- **Tools Needed:** Veeam/Commvault for backup, LUKS encryption for storage.  
- **Success Criteria:** All critical data recoverable within RTO < 4 hours; no unencrypted backups remain.  
- **Common Pitfalls:** Backup schedules not enforced; encryption keys lost.  
- **Time Estimate:** 1 day

**STEP 9: Incident Response**
- **Action:** Develop and test incident response playbook, conduct tabletop exercises quarterly.  
- **Tools Needed:** ServiceNow IR module, JIRA for tracking, RunDeck for automation testing.  
- **Success Criteria:** All team members can execute each step within defined roles; exercises pass all validation criteria.  
- **Common Pitfalls:** Lack of documentation; incomplete role definitions.  
- **Time Estimate:** 1 week

**STEP 10: Compliance Review**
- **Action:** Map implemented controls to relevant compliance frameworks, update policy documents.  
- **Tools Needed:** Compliance mapping templates (Excel), audit report templates.  
- **Success Criteria:** 100% of required controls mapped; policy document version updated with control status.  
- **Common Pitfalls:** Missing critical controls; outdated policy versions not tracked.  
- **Time Estimate:** 1 day

### Quality Checkpoints
```yaml
Checkpoint 1: Verify patch compliance >95% after Step 1.
Checkpoint 2: Confirm MFA enabled for all privileged accounts after Step 2.
Checkpoint 3: Validate no plaintext passwords in configs after Step 3.
```

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
```yaml
- Primary Metric: % of systems compliant with CIS benchmarks (>95%)
- Secondary Metrics:
  - Number of critical vulnerabilities remaining
  - Mean time to detect (MTTD) and mean time to respond (MTTR)
```

### Iterative Improvement Loop
1. Measure current compliance scores.
2. Identify top 3 areas needing improvement.
3. Implement changes per Phase 3 steps.
4. Re-measure metrics after each cycle.
5. Repeat until all goals met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state metrics; key actions taken.

**2. Detailed Report**
- Methodology, research findings, implementation details, before/after comparisons.

**3. Maintenance Plan**
- Ongoing tasks (e.g., quarterly scans), monitoring schedule, update frequency, contingency procedures.

**4. Knowledge Transfer**
- Training materials for new staff on security policies and tools.
- SOPs for patch management, incident response, access control changes.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Patch Management]"
    focus: "Latest patching cadence, automation tools"
    sources: ["Ansible docs", "Red Hat/CentOS release notes"]
    deliverable: "Automated patch playbook with test results"

  # [Continue for agents 2-10]
```

---

## SUCCESS VALIDATION

**Final Checklist**
```yaml
- [ ] Ultimate Goal Achieved? Yes/No
- [ ] All Metrics Met? Yes/No
- [ ] Quality Validated? Yes/No
- [ ] Documentation Complete? Yes/No
- [ ] Sustainability Ensured? Yes/No
```

---

## TEMPLATE METADATA

**Last Updated:** 2024-10-05  
**Version:** 1.0  
**Tested With:** System Administrator (Beginner), DevOps, Cloud Engineer  
**Success Rate:** N/A  
**Average Time to Goal:** 2 weeks (for initial hardening)

---

This comprehensive template provides a clear roadmap for a System Administrator to achieve security hardening with measurable success criteria and actionable steps. It's designed to be modular, allowing easy integration of new tools or best practices as they emerge in the field by 2024-2025.

