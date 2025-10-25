# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

## PROFESSIONAL ULTIMATE GOAL DEFINITION

**Primary Objective:** Achieve Protected System Security with 100% compliance to industry standards, zero vulnerabilities, and automated threat detection for the next 12 months.

---

## PHASE 1: INFORMATION GATHERING FOR CYBERSECURITY ANALYST ROLE

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Target Organization's System Architecture Diagram]
   - Format: Visio, Draw.io diagram or structured description
   - Validation: Ensure all systems (network, endpoints, cloud services) are accounted for

2. **Input 2:** [Current Security Policies and Procedures Document]
   - Format: PDF/Word document
   - Validation: Verify policies cover access controls, data protection, incident response

3. **Input 3:** [List of Known Vulnerabilities & Threats]
   - Format: CSV or spreadsheet
   - Validation: Ensure all include CVE identifiers and risk ratings

4. **Input 4:** [Incident Response Plan Document]
   - Format: PDF/Word document
   - Validation: Confirm it includes roles, escalation paths, and recovery steps

5. **Input 5:** [Compliance Requirements List (e.g., GDPR, HIPAA)]
   - Format: CSV or list
   - Validation: Ensure all are relevant to the organization's operations

---

## PHASE 2: RESEARCH & ANALYSIS FOR CYBERSECURITY ANALYST

### Critical Knowledge Areas for Cybersecurity Analyst (10-20 Topics)

**1. Threat Intelligence**
- Research Focus: Latest threat patterns, IOCs, and actor tactics
- Target Sources: Open-source intelligence platforms like MISP, ThreatQuotient, or commercial alternatives like Recorded Future
- Deliverable: 3 most relevant threat intel feeds

**2. Vulnerability Management**
- Research Focus: Emerging vulnerabilities, CVSS scoring trends, patch management best practices
- Target Sources: CVE database (NVD), OSVDB, Snyk premium alternative for automated scans
- Deliverable: Recommended vulnerability scanning schedule and mitigation plan

**3. Network Security Monitoring**
- Research Focus: Latest IDS/IPS signatures, anomaly detection algorithms, SIEM enhancements
- Target Sources: Documentation from commercial SIEMs like Splunk or ELK Stack alternatives (Graylog)
- Deliverable: Configurable log ingestion pipeline for real-time threat analysis

**4. Endpoint Protection Configuration**
- Research Focus: Advanced Threat Protection (ATP) configurations, application control policies, exploit prevention settings
- Target Sources: Vendor documentation from solutions like CrowdStrike, Carbon Black, or open-source alternatives like ClamAV
- Deliverable: Policy matrix for optimal endpoint protection setup

**5. Cloud Security Posture**
- Research Focus: Misconfigurations in cloud environments (AWS, Azure, GCP), Zero-Day risks, Access control models
- Target Sources: CSPM tools like AWS Config Rules, Varonis, or open-source equivalents like CloudMapper
- Deliverable: Checklist for secure cloud configuration

**6. Identity and Access Management (IAM)**
- Research Focus: Privileged access management solutions, MFA strategies, Least Privilege principles
- Target Sources: Documentation from IAM vendors like Okta, Azure AD, or OpenID Connect standards
- Deliverable: Updated IAM policy document with security controls

**7. Incident Response Procedures**
- Research Focus: NIST 800-61 guidelines, Log analysis workflows, Containment strategies for ransomware and DDoS
- Target Sources: NIST Special Publication SP 800-61, SANS Institute courses, Red Team methodologies
- Deliverable: Updated IR playbook with new threat scenarios

**8. Security Automation & Orchestration**
- Research Focus: New capabilities in SIEMs, SOAR platforms like Phantom or Demisto, Threat hunting tools
- Target Sources: Vendor whitepapers, Gartner Magic Quadrant reports for security orchestration
- Deliverable: Integration matrix of automated response workflows

**9. Compliance Framework Updates (2024-2025)**
- Research Focus: Changes in regulations affecting data protection and access control (e.g., new HIPAA guidelines)
- Target Sources: Regulatory body websites, compliance news aggregators
- Deliverable: Updated compliance checklist with 2024-2025 requirements

**10. Emerging Threats & AI Integration**
- Research Focus: New ransomware families, supply chain attacks, integration of AI for predictive analytics in threat detection
- Target Sources: Dark web monitoring platforms like VirusTotal, research from MITRE ATT&CK framework
- Deliverable: Strategy document on leveraging AI for improved threat intelligence

**11. Endpoint Detection & Response (EDR)**
- Research Focus: New EDR solutions, behavioral analysis techniques, response automation capabilities
- Target Sources: Vendor demos, security blogs, case studies of successful breaches
- Deliverable: Recommended EDR solution with deployment plan

**12. Network Traffic Analysis (NTA)**
- Research Focus: Advanced NTA tools for detecting lateral movement and exfiltration attempts
- Target Sources: Reviews from Gartner Peer Insights, vendor documentation
- Deliverable: Comparison table of top NTA solutions

**13. Log Management Best Practices**
- Research Focus: Elastic log pipelines, data lake architectures for security analytics
- Target Sources: Documentation from ELK Stack (Elasticsearch, Logstash, Kibana) and commercial alternatives like Splunk
- Deliverable: Optimal log storage solution with retention policy

**14. Security Operations Center (SOC) Workflow Optimization**
- Research Focus: Reducing MTTD/MTTD in incident response, enhancing threat hunting processes
- Target Sources: SOC manager guidelines from SANS Institute, industry whitepapers
- Deliverable: Optimized workflow diagram and SOPs for the SOC team

**15. Phishing Simulation Programs**
- Research Focus: Best practices for simulated phishing campaigns to assess employee security awareness
- Target Sources: Frameworks like ATT&CK's T1566 (Phishing), training platforms reviews
- Deliverable: Simulated campaign plan with KPI tracking metrics

---

### Research Consolidation Phase 2.1

After all sub-agents complete:
1. Synthesize findings into unified strategy for Protected System Security
2. Identify conflicts or contradictions in best practices across research areas
3. Prioritize recommendations by impact to ultimate goal (measured in reduced vulnerabilities and incidents)
4. Create master action plan with milestones aligned to the 12-month timeline

---

## PHASE 3: EXECUTION WORKFLOW FOR CYBERSECURITY ANALYST

### Step-by-Step Process for Achieving Protected System Security

**STEP 1: [Baseline Vulnerability Assessment]**
- **Action:** Conduct comprehensive vulnerability scanning across all systems using tools like Nessus (free alternative) or OpenVAS. Prioritize findings based on CVSS scores.
- **Tools Needed:** Nessus, OpenVAS
- **Success Criteria:** Complete scan report with top 10 critical vulnerabilities identified and prioritized for remediation.
- **Common Pitfalls:** Overlooking cloud resources or third-party dependencies.
- **Time Estimate:** 2 weeks

**STEP 2: [Network Segmentation & Access Control Hardening]**
- **Action:** Implement network segmentation using VLANs/ACLs. Enforce strict access controls based on the principle of least privilege across all systems.
- **Tools Needed:** Cisco ASA firewalls, AWS VPC security groups
- **Success Criteria:** 100% compliance with segmented network zones and reduced lateral movement paths for attackers.
- **Common Pitfalls:** Misconfigured ACLs or overly permissive permissions.
- **Time Estimate:** 3 weeks

**STEP 3: [Endpoint Protection Deployment]**
- **Action:** Deploy Endpoint Detection & Response (EDR) solutions like Carbon Black or CrowdStrike on all endpoints. Configure real-time protection and automated response policies.
- **Tools Needed:** Carbon Black, CrowdStrike
- **Success Criteria:** Endpoints monitored with <5% false positives in alerts. Automated containment rules tested and validated.
- **Common Pitfalls:** Overwhelming security teams with alert noise.
- **Time Estimate:** 1 week

**STEP 4: [Threat Intelligence Integration]**
- **Action:** Integrate threat intelligence feeds into SIEM (Security Information and Event Management) to enrich log data with IOCs. Develop automated alerts for known indicators.
- **Tools Needed:** Splunk, ELK Stack
- **Success Criteria:** New threat detections integrated within 24 hours of IOC publication. Automated response rules trigger <1% false positives.
- **Common Pitfalls:** Incomplete integration leading to blind spots in detection.
- **Time Estimate:** 2 weeks

**STEP 5: [Incident Response Drills]**
- **Action:** Conduct tabletop exercises simulating ransomware and DDoS attacks. Evaluate response times, containment effectiveness, and recovery procedures.
- **Tools Needed:** No specific tool required
- **Success Criteria:** All key stakeholders can execute response steps within predefined timeframes (<30 minutes for initial detection, <2 hours for containment).
- **Common Pitfalls:** Lack of clear roles or communication protocols in the IR plan.
- **Time Estimate:** Ongoing quarterly drills

**STEP 6: [Compliance Validation]**
- **Action:** Perform compliance scans against relevant regulations (e.g., GDPR, HIPAA). Address any non-compliant configurations identified.
- **Tools Needed:** Compliance scanners like Nessus Compliance or Varonis for data protection policies
- **Success Criteria:** Zero critical findings from compliance checks. All gaps remediated within defined timelines.
- **Common Pitfalls:** Assuming manual documentation is sufficient without automated validation tools.
- **Time Estimate:** Monthly scans

**STEP 7: [Automated Vulnerability Remediation]**
- **Action:** Implement an automated patch management system using tools like Ansible or Chef to deploy fixes for identified vulnerabilities.
- **Tools Needed:** Ansible, Chef
- **Success Criteria:** Automated deployment of patches with <1% failures. All systems scanned weekly without critical findings.
- **Common Pitfalls:** Overlooking dependencies that break during automation.
- **Time Estimate:** 2 weeks setup, then ongoing

**STEP 8: [Continuous Monitoring & Alert Tuning]**
- **Action:** Regularly review alert volumes and tune SIEM rules to reduce noise. Establish baselines for normal network activity.
- **Tools Needed:** Splunk, ELK Stack
- **Success Criteria:** False positive rate below 5%. Key alerts (e.g., brute force attempts) trigger immediate escalation.
- **Common Pitfalls:** Ignoring critical alerts due to overwhelming noise.
- **Time Estimate:** Ongoing

**STEP 9: [Security Awareness Training Program]**
- **Action:** Develop and deliver phishing simulation campaigns. Provide regular security awareness training sessions for staff.
- **Tools Needed:** Phishing simulation tools like KnowBe4, SentinelOne
- **Success Criteria:** Employee click-through rate on simulated phishing emails below industry average (<30%). Post-training assessments show improvement in knowledge retention (>80%).
- **Common Pitfalls:** Lack of engagement or perceived irrelevance by employees.
- **Time Estimate:** Quarterly campaigns

**STEP 10: [Annual Review & Process Optimization]**
- **Action:** Conduct a full review of the security posture. Identify areas for improvement and implement new processes based on emerging threats.
- **Tools Needed:** No specific tool required
- **Success Criteria:** Updated risk assessment, refined incident response plan, enhanced compliance status.
- **Common Pitfalls:** Neglecting to document changes or update SOPs.
- **Time Estimate:** Annual

---

### Quality Checkpoints for Cybersecurity Analyst Workflow

**Checkpoint 1 (After Step 2):** Verify all network segmentation rules are correctly applied and logs show reduced traffic between segments.

**Checkpoint 2 (After Step 4):** Validate that threat intelligence feeds populate SIEM in real-time without delays.

**Checkpoint 3 (After Step 7):** Ensure automated patch deployment completes successfully on at least 95% of systems during a test window.

**Checkpoint 4 (End of Phase 3):** Conduct a full system scan for compliance and security configurations. All findings should be remediated before proceeding to Phase 4.

---

## PHASE 4: OPTIMIZATION & REFINEMENT FOR CYBERSECURITY ANALYST

### Performance Metrics Definition

1. **Primary Metric:** Zero critical vulnerabilities identified in quarterly scans.
   - Target: Achieve <5% false positives in alerts from the SIEM system.
   - Measurement Method: Automated vulnerability scan reports and alert analytics.

2. **Secondary Metrics:**
   - Time to Detect (TTD): Average time from threat detection to alert generation should be under 15 minutes.
   - Time to Respond (TTR): Average time from alert acknowledgment to containment action should be under 30 minutes.
   - Phishing Click Rate: Employee click-through on phishing simulations should remain below 20% month-over-month.

3. **Long-term Metrics:**
   - Annual Compliance Score: Achieve >95% compliance with industry regulations post-implementation.
   - Incident Frequency Reduction: Reduce the number of security incidents by at least 50% compared to baseline over a year.

---

## PHASE 5: REPORTING & DOCUMENTATION FOR CYBERSECURITY ANALYST

### Deliverables for Cybersecurity Analyst Workflow

**1. Executive Summary**
- Current State vs. Target State
- Key Actions Taken
- Results Achieved (e.g., zero critical vulnerabilities, <5% false positives)
- Impact Metrics (e.g., reduced TTD and TTR)

**2. Detailed Report**
- Methodology Overview
- All Research Findings Documented with Sources
- Implementation Steps with Screenshots/Logs
- Pre- and Post-Implementation Comparison Tables

**3. Maintenance Plan**
- Ongoing Tasks: Quarterly vulnerability scans, Annual policy reviews, Continuous monitoring of threat intelligence feeds
- Monitoring Schedule: Weekly SIEM alerts review, Monthly compliance checks
- Update Frequency: Every 6 months or upon major regulatory change
- Contingency Procedures: Documented in IR playbook with version control

**4. Knowledge Transfer**
- Training Materials: Phishing simulation reports, Vulnerability remediation guides
- SOPs: Incident response playbooks, Patch management procedures
- Best Practices Documentation: Updated security policies and configurations
- Troubleshooting Guide: Common issues (e.g., alert fatigue, patch failures) with step-by-step resolution

---

## RESEARCH SUB-AGENT CONFIGURATION FOR CYBERSECURITY ANALYST

### Agent Deployment Template for Cybersecurity Analyst Research

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "5 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Threat Intelligence Feeds"
    focus: "Latest threat intelligence sources and their integration into security platforms"
    sources: ["MISP", "ThreatQuotient", "SANS Open Threat Exchange"]
    deliverable: "Comparative analysis of top 5 feeds with scoring matrix"

  - agent_id: 2
    topic: "Vulnerability Management Tools"
    focus: "Evaluation of vulnerability scanning solutions for accuracy and coverage"
    sources: ["NVD", "OSVDB", "Rapid7 InsightVM"]
    deliverable: "Benchmark report with cost-benefit analysis"

  - agent_id: 3
    topic: "Endpoint Protection Solutions"
    focus: "Performance comparison of EDR tools across various attack scenarios"
    sources: ["EDR Reviews", "Gartner Peer Insights"]
    deliverable: "Pricing model and deployment recommendation matrix"

  # [Continue for agents 4-15]
```

---

## SUCCESS VALIDATION FOR CYBERSECURITY ANALYST ROLE

### Final Checklist Before Completion

Before marking the Cybersecurity Analyst workflow as COMPLETE:

- [ ] **Primary Objective Achieved:** Zero critical vulnerabilities detected in quarterly scans.
- [ ] **All Metrics Met:** TTD < 15 minutes, TTR < 30 minutes, Phishing Click Rate < 20%.
- [ ] **Quality Validated:** All documentation reviewed and approved by senior security team.
- [ ] **Maintenance Plan Confirmed:** SOPs updated with new findings and responsibilities assigned.

### Continuous Improvement Process

1. Measure current performance against targets (TTD, TTR, Phishing Click Rate).
2. Identify top 3 improvement opportunities based on metrics.
3. Implement changes in the next sprint cycle.
4. Re-measure and document outcomes.
5. Repeat annually or after major incident.

---

## TEMPLATE METADATA FOR CYBERSECURITY ANALYST

**Last Updated:** [2025-06-20]
**Version:** 1.0
**Tested With:** Cybersecurity Analyst (Beginner to Intermediate)
**Success Rate:** Track completion based on meeting all success criteria above.
**Average Time to Goal:** Typically achieved within 12 months following this framework.

---

This comprehensive template is now fully customized for a Cybersecurity Analyst with the ultimate goal of Protected System Security. It includes specific knowledge areas, detailed execution steps, tools and software recommendations, measurable success criteria, and an actionable timeline for achievement. The content is designed to be immediately applicable for someone new to the profession while also providing direction for those with more experience looking to refine their expertise.

