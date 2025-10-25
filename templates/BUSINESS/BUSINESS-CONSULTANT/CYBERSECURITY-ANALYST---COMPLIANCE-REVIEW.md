# Cybersecurity Analyst - AI Agent Template
## Compliance Review

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve compliance review as a Cybersecurity Analyst.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve full compliance with regulatory standards (e.g., GDPR, HIPAA, NIST) and internal policies for an organization's cybersecurity framework.

Example:
- Ensure all systems meet the latest [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) requirements.
- Pass a [SOC 2 Type II audit](https://www.socialengineer.com/audits/soc2).
- Document and maintain all compliance artifacts for continuous monitoring.

---

### PHASE 1: INFORMATION GATHERING

**Required Inputs**
1. **Input 1:** Regulatory standards applicable to the organization (e.g., GDPR, HIPAA).
   - Format: List of acronyms or names.
   - Validation: Ensure each standard is relevant and current (2024-2025).

2. **Input 2:** Internal cybersecurity policies and procedures.
   - Format: Document URLs or file paths.
   - Validation: Confirm access permissions.

3. **Input 3:** Network architecture diagrams and system inventory.
   - Format: Image files, CSV, or JSON.
   - Validation: Verify accuracy of asset listings.

---

### PHASE 2: RESEARCH & ANALYSIS

**Critical Knowledge Areas (10-20 Topics)**
1. **Threat Intelligence**: Analyze threat patterns using tools like [OSINT Framework](https://osintframework.com).
2. **Incident Response**: Develop an IR plan aligned with standards such as [NIST 800-61](https://www.nist.gov/itl/cis/nc).
3. **Compliance Management**: Understand frameworks including [ISO 27001](https://www.iso.org/iso-27001-certification.html) and internal SOPs.
4. **Security Controls**: Implement controls per NIST SP 800-53, focusing on categories like Access Control and Configuration Management.
5. **Audit Preparation**: Use tools to prepare audit artifacts (e.g., [Auditium](https://auditium.com)).
6. **Automated Compliance Scanning**: Leverage open-source scanners like [Nessus Community Edition](https://github.com/offensive-security/nessus-community-edition) and [OpenVAS](https://www.openvas.org).
7. **Log Management & SIEM Configuration**: Set up logging in tools such as [ELK Stack (Elasticsearch, Logstash, Kibana)](https://www.elastic.co/elk) or [Splunk Free Edition](https://www.splunk.com/en_au/product/free-edition.html).
8. **Vulnerability Management**: Prioritize fixes using CVSS scoring.
9. **Data Protection Mechanisms**: Ensure encryption standards are met across systems.
10. **Access Control & Privileged Access Management (PAM)**: Implement least privilege access policies.

**Advanced Topics**
- [ ] Zero Trust Architecture
- [ ] Cloud Security Posture Management (CSPM)
- [ ] Endpoint Detection and Response (EDR)

---

### PHASE 3: EXECUTION WORKFLOW

#### STEP 1: Regulatory Standards Mapping
- **Action:** Map each regulatory requirement to existing policies and controls.
- **Tools Needed:** Excel/Google Sheets, Compliance software like [Qualys](https://www.qualys.com).
- **Success Criteria:** All regulations are mapped with no gaps identified.
- **Common Pitfalls:** Missing updates or amendments in regulation.
- **Time Estimate:** 2 days

#### STEP 2: Policy and Control Implementation Review
- **Action:** Verify that each policy is implemented across systems using automated scans.
- **Tools Needed:** Nessus, OpenVAS, [Qualys](https://www.qualys.com).
- **Success Criteria:** All controls are in place with no critical findings from scans.
- **Common Pitfalls:** Incomplete scan coverage or false positives.
- **Time Estimate:** 3 days

#### STEP 3: Logging and Monitoring Configuration
- **Action:** Configure logging to capture all security-relevant events and set up alerts for suspicious activities.
- **Tools Needed:** [ELK Stack](https://www.elastic.co/elk), Splunk Free Edition, [OSSEC](https://ossec.github.io).
- **Success Criteria:** Logs are accessible and alerts fire on real threats.
- **Common Pitfalls:** Log retention policies not configured or alert fatigue.
- **Time Estimate:** 1 day

#### STEP 4: Vulnerability Management Cycle
- **Action:** Regularly scan for vulnerabilities, prioritize remediation based on CVSS scores, and re-scan after fixes.
- **Tools Needed:** Nessus Community Edition, OpenVAS, [Nexpose](https://www.tricountsys.com/products/nexpose/).
- **Success Criteria:** Vulnerabilities are reduced to acceptable levels with no critical findings post-repair.
- **Common Pitfalls:** Incomplete scanning or delays in patching.
- **Time Estimate:** Weekly scans

#### STEP 5: Incident Response Drills
- **Action:** Conduct tabletop exercises and simulation drills to test IR plan effectiveness.
- **Tools Needed:** [Risky Business](https://www.riskybusiness.com), [Incident Simulator](https://incident-simulator.net).
- **Success Criteria:** DR plans are validated with actionable feedback post-drill.
- **Common Pitfalls:** Lack of participation or unrealistic scenarios.
- **Time Estimate:** Quarterly

#### STEP 6: Documentation and Reporting
- **Action:** Compile all findings, remediation steps, and compliance status into a report for management review.
- **Tools Needed:** Confluence, Notion, [Google Docs](https://www.google.com/docs).
- **Success Criteria:** Comprehensive compliance documentation is ready for audit.
- **Common Pitfalls:** Incomplete sections or missing approvals.
- **Time Estimate:** 1 day

#### STEP 7: Ongoing Compliance Monitoring
- **Action:** Set up automated checks to ensure continuous compliance with policies and regulations.
- **Tools Needed:** [Chronicle](https://www.rapid7.com/products/chronicle), [Splunk](https://www.splunk.com).
- **Success Criteria:** Automated alerts trigger immediate action on non-compliance issues.
- **Common Pitfalls:** Alert fatigue or missed configuration changes.
- **Time Estimate:** Ongoing

---

### PHASE 4: OPTIMIZATION & REFINEMENT

**Performance Metrics**
1. **Primary Metric:** Compliance status score (target >95%).
   - Measurement Method: Automated scoring from scan tools.

2. **Secondary Metrics:**
   - Number of critical vulnerabilities identified.
   - Time to remediate high-risk findings.
   - Drill readiness rating.

3. **Long-term Metrics:**
   - Audit pass rate.
   - Reduction in security incidents over time.

**Iterative Improvement Loop**
1. Measure current compliance score vs. target.
2. Identify top 3 areas for improvement.
3. Implement changes (e.g., additional scans, training).
4. Re-measure and document improvements.

---

### PHASE 5: REPORTING & DOCUMENTATION

**Deliverables**

1. **Executive Summary**
   - Current compliance status vs. target.
   - Key risks identified and mitigated.

2. **Detailed Report**
   - Mapping of regulations to controls.
   - Scan results with remediation steps.
   - Incident response drill outcomes.
   - Compliance documentation links.

3. **Maintenance Plan**
   - Ongoing scanning schedules (weekly/monthly).
   - Patch management timelines.
   - Review and update policy documents annually.

4. **Knowledge Transfer**
   - Training materials for new staff on compliance processes.
   - SOPs for incident response and vulnerability management.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 7
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Threat Intelligence Tools"
    focus: "Latest open-source threat intelligence platforms and their capabilities."
    sources: ["GitHub repositories", "Security blogs"]
    deliverable: "Top tools with usage examples."

  - agent_id: 2
    topic: "Incident Response Plans"
    focus: "Best practices for creating, testing, and updating IR plans."
    sources: ["SANS IR framework", "Industry case studies"]
    deliverable: "Comprehensive IR plan outline."

  - agent_id: 3
    topic: "Vulnerability Management Tools"
    focus: "Top automated vulnerability scanners and their integration with existing tools."
    sources: ["CVE database", "Tool vendor docs"]
    deliverable: "Recommended scanner list with configuration guides."

  - agent_id: 4
    topic: "Compliance Frameworks"
    focus: "Detailed comparison of NIST, ISO 27001, and other frameworks relevant to the organization."
    sources: ["Framework documentation", "Vendor whitepapers"]
    deliverable: "Frameworks matrix showing overlap and unique requirements."

  - agent_id: 5
    topic: "Logging and SIEM Best Practices"
    focus: "Optimal log collection, analysis, and alerting strategies for security incidents."
    sources: ["ELK Stack tutorials", "Splunk blogs"]
    deliverable: "Configured logging setup with sample queries."

  - agent_id: 6
    topic: "Automated Compliance Scanning Tools"
    focus: "Community-driven tools to automate compliance checks against policies."
    sources: ["GitHub repos for OSS scanning projects"]
    deliverable: "List of OSS scanners with integration steps."

  - agent_id: 7
    topic: "Audit Preparation and Reporting"
    focus: "Guidance on preparing audit artifacts, including documentation standards."
    sources: ["Audit best practices", "Industry compliance blogs"]
    deliverable: "Template documents for audit-ready reports.
```

---

### SUCCESS VALIDATION

**Final Checklist**
- [ ] **Ultimate Goal Achieved?** Compliance status >95% across all required frameworks.
- [ ] **All Metrics Met?** All primary and secondary metrics are within acceptable ranges.
- [ ] **Quality Validated?** Documentation is complete, accurate, and reviewed by management.
- [ ] **Documentation Complete?** All reports and artifacts are stored in the designated repository with version control.
- [ ] **Sustainability Ensured?** Ongoing monitoring processes are automated and regularly reviewed.

**Continuous Improvement**
- Document lessons learned from each compliance cycle.
- Update tooling list based on user feedback and emerging technologies.
- Schedule quarterly reviews to ensure alignment with evolving regulations.

---

### TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Cybersecurity Analysts at mid-career level  
**Success Rate:** [Track completion against industry benchmarks]  
**Average Time to Goal:** [Based on historical data]

---

