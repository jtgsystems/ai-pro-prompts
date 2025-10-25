# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

## PROFESSIONAL GOAL DEFINITION

**Primary Objective:**  
Achieve a security posture where all critical systems and data are hardened according to the latest NIST 800-53 Rev. 4 controls, with automated monitoring for deviations from these standards. Measurable success is defined as:

1. **80% or higher compliance rating across all target assets**
2. **Zero high-severity vulnerabilities identified in quarterly scans**
3. **Automated alerts triggered and responded to within 15 minutes of detection**

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Asset Inventory:** List all critical systems, networks, applications, and data stores.
2. **Current Security Posture:** Existing firewall rules, access controls, encryption status.
3. **Vulnerability Management Process:** Current patching frequency and process.
4. **Compliance Requirements:** Applicable standards (NIST 800-53, PCI DSS, GDPR).
5. **Security Tools Inventory:** List of all security tools currently in use.

### Initial Assessment Checklist
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers
- [ ] Establish baseline metrics (current state)

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices

**Topic 1:** [NIST 800-53 Security Controls]  
- **Research Focus:** Latest best practices, tools, methodologies for implementing NIST controls.
- **Target Sources:** NIST publications, cybersecurity blogs (e.g., SANS), industry reports.
- **Deliverable:** List of recommended controls with implementation steps.

**Topic 2:** [Endpoint Hardening Techniques]  
- **Research Focus:** Best practices for configuring Windows/Linux systems securely.
- **Target Sources:** OS security guides, CIS Benchmarks.
- **Deliverable:** Configuration scripts and checklists.

**Topic 3:** [Network Segmentation Strategies]  
- **Research Focus:** Implementing micro-segmentation to limit lateral movement.
- **Target Sources:** Zero Trust frameworks, network security blogs.
- **Deliverable:** Diagrams of segmented network architecture.

**Topic 4:** [Access Control and Privileged Access Management (PAM)]  
- **Research Focus:** Strategies for least privilege access and PAM solutions.
- **Target Sources:** Gartner reports, vendor whitepapers.
- **Deliverable:** Policy recommendations for access controls.

**Topic 5:** [Vulnerability Scanning Tools]  
- **Research Focus:** Best open-source tools for identifying vulnerabilities (e.g., Nessus, OpenVAS).
- **Target Sources:** Security community forums, tool documentation.
- **Deliverable:** Comparison matrix of top scanners.

**Topic 6:** [Configuration Management Systems]  
- **Research Focus:** Tools for automating and auditing system configurations.
- **Target Sources:** Ansible, Puppet documentation.
- **Deliverable:** Recommended configuration management tools with setup guides.

**Topic 7:** [Security Information and Event Management (SIEM)]  
- **Research Focus:** Integration of SIEM systems for real-time threat detection.
- **Target Sources:** Vendor reviews, user community forums.
- **Deliverable:** List of open-source SIEM options and deployment strategies.

**Topic 8:** [Incident Response Playbooks]  
- **Research Focus:** Developing and testing incident response plans.
- **Target Sources:** NIST IR framework, SANS Incident Handling Guide.
- **Deliverable:** Ready-to-use playbooks with checklists.

**Topic 9:** [Artificial Intelligence for Security](Optional)  
- **Research Focus:** AI-driven threat detection and automated hardening.
- **Target Sources:** Research papers on machine learning in security.
- **Deliverable:** List of AI/ML tools that can enhance security posture.

**Topic 10:** [Compliance Automation Tools]  
- **Research Focus:** Solutions for automating compliance reporting.
- **Target Sources:** Compliance-as-a-Service (CaaS) providers, open-source scripts.
- **Deliverable:** Tool recommendations and integration steps.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Asset Inventory Update]**
- **Action:** Run automated discovery tools to update asset inventory.  
- **Tools Needed:** Nmap, OpenVAS, AWS Config for cloud resources.  
- **Success Criteria:** All critical assets are listed with their current security status.  
- **Common Pitfalls:** Missing remote or virtual machines; Incomplete network mapping.  
- **Time Estimate:** 4 hours (initial scan + verification).

**STEP 2: [Baseline Configuration Audit]**
- **Action:** Compare current configurations against recommended baselines (e.g., CIS Benchmarks).  
- **Tools Needed:** Ansible, Puppet for configuration comparison; Nmap for network discovery.  
- **Success Criteria:** 80% or more of systems are compliant with the baseline standards.  
- **Common Pitfalls:** Manual overrides causing non-compliance; Lack of documentation for custom configurations.  
- **Time Estimate:** 8 hours (audit + remediation).

**STEP 3: [Vulnerability Scanning and Patching]**
- **Action:** Perform initial vulnerability scan using OpenVAS/Nessus. Prioritize high/medium severity vulnerabilities.  
- **Tools Needed:** OpenVAS, Nessus Free Edition; Ticketing system for tracking remediation.  
- **Success Criteria:** No high-severity vulnerabilities remain unpatched after 30 days.  
- **Common Pitfalls:** Patch management bottleneck due to lack of resources or process delays.  
- **Time Estimate:** Ongoing (weekly scans and monthly patch cycles).

**STEP 4: [Network Segmentation Implementation]**
- **Action:** Design and implement micro-segmentation using VLANs, ACLs, and firewall rules.  
- **Tools Needed:** Cisco ASA/Checkpoint firewalls; Network diagramming tools like draw.io.  
- **Success Criteria:** All critical assets are isolated within segmented networks with restricted access.  
- **Common Pitfalls:** Overly permissive segmentation causing operational bottlenecks.  
- **Time Estimate:** 10 hours (planning + configuration).

**STEP 5: [Access Control Enforcement]**
- **Action:** Implement least privilege access using PAM solutions and enforce through RBAC.  
- **Tools Needed:** Duo Security for MFA; Active Directory/Okta for user provisioning.  
- **Success Criteria:** All users have appropriate permissions based on role; No accounts with excessive privileges.  
- **Common Pitfalls:** Permission creep from legacy systems or poorly defined roles.  
- **Time Estimate:** 6 hours (initial configuration + periodic review).

**STEP 6: [Endpoint Security Hardening]**
- **Action:** Deploy and configure endpoint security tools for each asset type (Windows/Linux).  
- **Tools Needed:** CrowdStrike Falcon, Bitdefender, OS native hardening scripts.  
- **Success Criteria:** All endpoints have up-to-date antivirus/EDR protection; No critical misconfigurations detected.  
- **Common Pitfalls:** Inconsistent application of endpoint security policies across devices.  
- **Time Estimate:** 12 hours (initial deployment + ongoing monitoring).

**STEP 7: [SIEM System Deployment and Configuration]**
- **Action:** Set up open-source SIEM like ELK or Graylog to collect logs from all systems. Implement alerting for high-risk events.  
- **Tools Needed:** Elasticsearch, Kibana; Logstash for log aggregation.  
- **Success Criteria:** Real-time alerts are generated within 15 minutes of a critical event occurrence.  
- **Common Pitfalls:** Alert fatigue due to overwhelming number of false positives or incomplete rule set.  
- **Time Estimate:** 8 hours (initial setup + tuning).

**STEP 8: [Automated Compliance Reporting]**
- **Action:** Configure the chosen compliance automation tool to generate reports on NIST 800-53 controls weekly.  
- **Tools Needed:** Compliance-as-a-Service platform like CloudGenix or open-source scripts using Ansible.  
- **Success Criteria:** Weekly compliance reports are generated automatically and reviewed within a day.  
- **Common Pitfalls:** Inaccurate report generation due to missing data elements; Lack of stakeholder engagement in reviewing reports.  
- **Time Estimate:** 4 hours (initial setup + ongoing maintenance).

**STEP 9: [Incident Response Drills]**
- **Action:** Conduct tabletop exercises and live drills to test incident response playbooks. Update based on findings.  
- **Tools Needed:** Incident management platform like Splunk On-Demand; Documentation tools for playbooks.  
- **Success Criteria:** All team members can execute the playbook within 15 minutes of a simulated breach.  
- **Common Pitfalls:** Playbook not reviewed in over 6 months leading to outdated steps.  
- **Time Estimate:** Ongoing (quarterly drills).

**STEP 10: [Continuous Monitoring and Improvement]**
- **Action:** Establish a metrics dashboard tracking compliance, vulnerability status, and incident response times. Review quarterly.  
- **Tools Needed:** Grafana for dashboards; Jira or ServiceNow for issue tracking.  
- **Success Criteria:** No critical gaps in security posture identified during reviews; Incident response SLA met consistently.  
- **Common Pitfalls:** Lack of regular review leading to stagnation of processes and tools.  
- **Time Estimate:** 2 hours per month (dashboard updates) + quarterly deep dive.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Compliance Rating  
   - **Target:** 80% or higher across all assets after the first quarter.  
   - **Measurement Method:** Automated compliance scans using open-source tools.

2. **Secondary Metrics:**
   - Number of high-severity vulnerabilities identified in quarterly scans (Goal: Zero).  
   - Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) for security events.  
   - Frequency of successful phishing simulations targeting privileged accounts.

3. **Long-term Metrics:**  
   - Annual audit results showing no critical findings.  
   - Ongoing reduction in incident response times by 20% each year.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., gaps in logging, misconfigured access controls).
3. Implement changes (e.g., additional firewall rules, enhanced MFA for privileged accounts).
4. Re-measure to confirm improvements.
5. Repeat annually or after major security events.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- **Current State vs. Target State:**  
  - Compliance Rating: Currently X%, Goal: >=80%.  
  - Vulnerabilities: Y high severity identified; Z mitigated.  

- **Key Actions Taken:** List of major projects completed (e.g., asset inventory, SIEM deployment).  
- **Results Achieved:** Measurable improvements in security posture.  
- **ROI/Impact Metrics:** Cost savings from reduced incidents; Enhanced business continuity.

**2. Detailed Report**
- **Methodology:** Tools used, timelines, personnel involved.  
- **Research Findings:** Summaries of all critical topics researched.  
- **Implementation Details:** Configuration scripts, policy documents, playbooks.  
- **Before/After Comparisons:** Compliance and vulnerability metrics over time.

**3. Maintenance Plan**
- **Ongoing Tasks:** Weekly SIEM reviews; Monthly compliance scans; Quarterly tool updates.  
- **Monitoring Schedule:** Real-time monitoring enabled for critical assets during business hours.  
- **Update Frequency:** Documentation updated annually or after major security events.  
- **Contingency Procedures:** RTO/RPO plans for data recovery in case of breach.

**4. Knowledge Transfer**
- **Training Materials:** Quick reference guides for junior analysts on how to use key tools (e.g., Nmap, OpenVAS).  
- **Standard Operating Procedures:** Step-by-step SOPs for tasks like incident response and vulnerability patching.  
- **Best Practices Documentation:** Centralized repository of all approved configurations and policies.  
- **Troubleshooting Guide:** Common issues with asset inventory updates; Vulnerability scanning errors; Access control problems.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[NIST 800-53 Security Controls]"
    focus: "Latest best practices"
    sources: ["NIST publications", "SANS blogs", "Industry reports"]
    deliverable: "List of recommended controls with implementation steps"

  - agent_id: 2
    topic: "[Endpoint Hardening Techniques]"
    focus: "OS-level hardening"
    sources: ["CIS Benchmarks", "OS security guides"]
    deliverable: "Configuration scripts and checklists"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to security hardening goal
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking the Cybersecurity Analyst task as COMPLETE:

- [ ] **Primary Goal Achieved?** All systems meet NIST 800-53 controls with automated monitoring.
- [ ] **All Metrics Met?** Compliance rating >=80%; Zero high-severity vulnerabilities; MTTD/MTTR met.
- [ ] **Quality Validated?** Systems pass all automated compliance scans without exceptions.
- [ ] **Documentation Complete?** All policies, playbooks, and SOPs are stored in the central repository.
- [ ] **Sustainability Ensured?** Maintenance plan is documented and assigned to staff; Budget approved for ongoing tooling.

### Continuous Improvement
- Document lessons learned from incidents or audits.  
- Update research agents annually with new publications or threat intelligence.  
- Share findings with the cybersecurity community via blogs or webinars.  
- Schedule a quarterly review of all deliverables to ensure alignment with evolving threats and compliance requirements.

---

## TEMPLATE METADATA

**Last Updated:** 2024-10-05
**Version:** 1.0
**Tested With:** Cybersecurity Analyst (Beginner Level)
**Success Rate:** Track through quarterly audits  
**Average Time to Goal:** ~3 months for full implementation  

--- 

This template is ready to be executed by Claude Code or any AI agent capable of automating cybersecurity tasks in a remote, computer-based environment. The focus on free/open-source tools ensures the solution remains cost-effective while maintaining security standards.

