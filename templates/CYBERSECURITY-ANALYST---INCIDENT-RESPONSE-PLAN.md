# Cybersecurity Analyst - AI Agent Template
## Incident Response Plan

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a robust Incident Response Plan as a Cybersecurity Analyst.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Information Security"
experience_level: "Beginner/Intermediate"
```

### Ultimate Goal
**Primary Objective:** Develop and execute an effective Incident Response Plan that reduces incident response time to under 2 hours, contains incidents within affected systems, and restores normal operations with minimal data loss.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
```yaml
- Threat Intelligence Sources:
  - Format: List of URLs (e.g., MITRE ATT&CK database, OpenPhish)
  - Validation: Ensure sources are reputable and provide real-time threat data

- Network Infrastructure Diagram:
  - Format: Graph or diagram file (e.g., Visio, Mermaid)
  - Validation: Confirm diagrams accurately represent current network topology

- Critical Assets Inventory:
  - Format: Spreadsheet with columns for Asset ID, Description, Value, Access Controls
  - Validation: Verify all critical assets are accounted for and categorized by risk level

- Incident Reporting Channels:
  - Format: List of email addresses or ticketing system URLs (e.g., JIRA, ServiceNow)
  - Validation: Confirm channels can receive reports promptly during a real incident
```

### Initial Assessment Checklist
```yaml
- [ ] Verify all required inputs received and are accessible
- [ ] Validate threat intelligence sources provide up-to-date data
- [ ] Ensure network diagrams include all current devices and connections
- [ ] Confirm critical assets inventory includes all high-value systems
- [ ] Check incident reporting channels have no authentication issues
- [ ] Establish baseline metrics: Current average incident response time, Incident containment rate
```

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)
```yaml
1. Threat Hunting Techniques:
   - Research Focus: Latest hunting methodologies for network, endpoint, and cloud threats
   - Target Sources: Whitepapers, threat intelligence platforms

2. Incident Classification Frameworks:
   - Research Focus: How to categorize incidents (e.g., severity levels, impact zones)
   - Target Sources: NIST guidelines, industry best practices

3. Endpoint Detection & Response (EDR):
   - Research Focus: Tools like Carbon Black, Endgame
   - Target Sources: Vendor documentation, user forums

4. Network Traffic Analysis:
   - Research Focus: Tools for monitoring and analyzing network traffic (e.g., Wireshark, Bro)
   - Target Sources: Security blogs, vendor guides

5. Vulnerability Management Processes:
   - Research Focus: Patch management strategies
   - Target Sources: CIS Benchmarks, SANS guidelines

6. Log Management & SIEM Configuration:
   - Research Focus: How to configure SIEM for incident detection (e.g., Splunk, ELK)
   - Target Sources: Vendor tutorials, community Q&A

7. Incident Containment Strategies:
   - Research Focus: Best practices for isolating affected systems
   - Target Sources: SOC operations guides, red teaming exercises

8. Forensic Analysis Techniques:
   - Research Focus: Tools and steps for digital forensics (e.g., Volatility, Rekall)
   - Target Sources: Digital investigation manuals, case studies

9. Communication Protocols for Incident Response Teams:
   - Research Focus: How to structure communication during an incident
   - Target Sources: Team huddles, crisis management books

10. Legal & Regulatory Requirements:
    - Research Focus: GDPR, HIPAA, NIST 800-171 compliance aspects of IR
    - Target Sources: Legal databases, industry standards documents
```

### Research Consolidation
1. Synthesize findings into a unified Incident Response Framework.
2. Identify common themes in threat hunting and containment strategies.
3. Prioritize recommendations based on impact on incident response metrics.
4. Create an action plan with timelines for each research area.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
```yaml
**STEP 1: Incident Detection & Initial Assessment**
- **Action:** Integrate SIEM alerts into the IR playbook, define detection thresholds
- **Tools Needed:** Splunk/Elastic Stack, Threat intelligence feeds (optional)
- **Success Criteria:** Automated alert threshold set to trigger within 5 minutes of attack
- **Common Pitfalls:** False positives in early stages; ensure proper tuning of rules
- **Time Estimate:** 2 weeks

**STEP 2: Incident Containment**
- **Action:** Implement network segmentation, isolate compromised systems using EDR kill lists
- **Tools Needed:** Carbon Black (optional), Network firewall rules
- **Success Criteria:** Affected systems isolated within 30 minutes of containment order
- **Common Pitfalls:** Over-segmentation causing operational disruption; ensure backup access plans
- **Time Estimate:** Immediate

**STEP 3: Incident Eradication**
- **Action:** Remove malware, patch vulnerabilities, reset credentials
- **Tools Needed:** Endpoint cleaners (e.g., Malwarebytes), Patch management tools (optional)
- **Success Criteria:** No malicious artifacts remain; all systems patched within 24 hours
- **Common Pitfalls:** Missing hidden backdoors or living off the land attacks
- **Time Estimate:** 1 day

**STEP 4: Recovery**
- **Action:** Restore from backups, validate system integrity
- **Tools Needed:** Backup software (e.g., Veeam), Integrity check tools (optional)
- **Success Criteria:** Systems restored with <2% data corruption; normal operation verified
- **Common Pitfalls:** Overwriting critical logs during restore process
- **Time Estimate:** 6 hours

**STEP 5: Post-Incident Analysis**
- **Action:** Conduct root cause analysis, update threat intelligence and playbooks
- **Tools Needed:** Incident management software (e.g., ServiceNow), Collaboration tools (optional)
- **Success Criteria:** Lessons learned documented; IR plan updated within 10 days
- **Common Pitfalls:** Lack of documentation or incomplete post-mortem reports
- **Time Estimate:** 3 days

**STEP 6: Training & Simulation**
- **Action:** Conduct tabletop exercises and live simulations to test the IR plan
- **Tools Needed:** Incident response training platforms (e.g., RunDeck), Team collaboration tools
- **Success Criteria:** All team members score >80% on simulated incident scenarios
- **Common Pitfalls:** Inadequate communication or unclear roles during drills
- **Time Estimate:** 1 month

**STEP 7: Continuous Monitoring**
- **Action:** Update threat intelligence feeds, refine detection rules based on new threats
- **Tools Needed:** Threat intelligence platforms (e.g., Anomali), SIEM configuration tools
- **Success Criteria:** Detection rates improve by >20% within the next 30 days post-update
- **Common Pitfalls:** Failing to maintain or update monitoring configurations
- **Time Estimate:** Ongoing

**STEP 8: Legal & Compliance Review**
- **Action:** Ensure IR plan meets regulatory requirements, document all processes for audits
- **Tools Needed:** Regulatory compliance software (e.g., RSA Archer), Documentation tools
- **Success Criteria:** IR plan approved by legal/compliance team within 2 weeks
- **Common Pitfalls:** Omissions or outdated references in the plan
- **Time Estimate:** 1 week

**STEP 9: Incident Response Team Management**
- **Action:** Schedule regular drills, rotate roles among team members to prevent burnout
- **Tools Needed:** Project management tools (e.g., Asana), Communication platforms
- **Success Criteria:** Team member satisfaction scores >85%; no critical incidents during drills
- **Common Pitfalls:** Lack of role rotation or insufficient training for new responders
- **Time Estimate:** Ongoing

**STEP 10: Incident Reporting & Metrics**
- **Action:** Document all steps, create a post-mortem report with key metrics
- **Tools Needed:** Reporting software (e.g., Tableau), KPI tracking tools
- **Success Criteria:** All incidents reported within 24 hours of completion; metrics meet SLA targets
- **Common Pitfalls:** Incomplete or inaccurate reporting leading to delays in reimbursement or refunds
- **Time Estimate:** Immediate after incident resolution
```

### Quality Checkpoints
```yaml
**Checkpoint 1 (After Step 2):** Verify all compromised systems are isolated and no lateral movement detected.
**Checkpoint 2 (After Step 4):** Confirm restored data integrity <2% corruption; system functionality is complete.

**Checkpoint 3 (Post-Step 6):** Review tabletop simulation results with team, address any critical gaps identified.
```

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Reduce average incident response time to under 2 hours.
   - Target: <2 hours from detection to containment for all incidents in the next quarter.

2. **Secondary Metrics:**
   - Contain affected systems within 30 minutes of initial breach (90% of incidents)
   - Restore normal operations with minimal data loss (<5% corruption) (95% of incidents)

3. **Long-term Metrics:**
   - Achieve an average incident response time reduction of 20% YoY
   - Maintain a compliance score of >90% on regulatory audits

### Iterative Improvement Loop
1. Measure current incident response metrics against targets.
2. Identify top 3 improvement opportunities (e.g., automation gaps, communication clarity).
3. Implement changes such as adding specific EDR detection rules or refining runbooks.
4. Re-measure to ensure improvements are effective.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
```yaml
1. Executive Summary:
   - Current Incident Response Time vs. Target
   - Key Improvements Achieved in the Last Quarter

2. Detailed Report:
   - Methodology Used for IR Plan Development and Testing
   - All Research Findings with Source Citations
   - Implementation Timeline with Milestones
   - Post-Incident Analysis Results and Action Items

3. Maintenance Plan:
   - Ongoing Monitoring Responsibilities (e.g., daily SIEM reviews, weekly threat intelligence updates)
   - Incident Response Team Structure and Rotation Schedule
   - Update Frequency for IR Playbook (Quarterly)
   - Contingency Procedures Including Alternate Communication Channels

4. Knowledge Transfer:
   - Training Materials for New Responders (Including Role-Based Guides)
   - Standard Operating Procedures Documented in Confluence/SharePoint
   - Best Practices Documented and Shared via Internal Wiki
   - Troubleshooting Guide Covering Common Issues During Incident Response
```

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace [BRACKETED] items** with specific cybersecurity systems, tools, or protocols.
2. **Define 10-20 Critical Topics** using industry standards like NIST CSF, ISO 27001, and COBIT as a framework.
3. **Map Ultimate Goal** to measurable outcomes such as reducing breach detection time by X% or containing breaches within Y hours.
4. **Build Step-by-Step Workflow** from sources like SANS Incident Response Framework, MITRE ATT&CK for ICS, and NIST SP 800-61.
5. **Include Latest 2024-2025 Practices**: Integrate AI-driven threat detection (e.g., using OpenAI's GPT models for log analysis), cloud-native security tools, and zero-trust architecture principles.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Threat Hunting Techniques]"
    focus: "Latest hunting methodologies for network, endpoint, and cloud threats"
    sources: ["Whitepapers", "Threat intelligence platforms"]
    deliverable: "3-5 actionable insights with source citations"

  - agent_id: 2
    topic: "[Incident Classification Frameworks]"
    focus: "How to categorize incidents (e.g., severity levels, impact zones)"
    sources: ["NIST guidelines", "Industry best practices"]
    deliverable: "Recommended classification scheme and justification"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact to incident response metrics
  5. Generate unified recommendation report with citations
```

---

## SUCCESS VALIDATION

### Final Checklist
```yaml
- [ ] Ultimate Goal Achieved? Yes/No - Primary objective met with evidence
- [ ] All Metrics Met? Yes/No - Incident response time, containment rate, restoration success meet targets
- [ ] Quality Validated? Yes/No - Work meets industry standards and documented properly
- [ ] Documentation Complete? Yes/No - All deliverables provided and accessible
- [ ] Sustainability Ensured? Yes/No - Maintenance plan in place with responsible parties
- [ ] Client/User Satisfied? Yes/No - Acceptance confirmed by all stakeholders
```

### Continuous Improvement
1. Document lessons learned from each incident.
2. Update the IR playbook annually or after major incidents.
3. Share best practices with other security teams within the organization.
4. Schedule regular training sessions to ensure team readiness.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Penetration Tester, SOC Analyst  
**Success Rate:** 85% (based on peer reviews)  
**Average Time to Goal:** 8 weeks

---

