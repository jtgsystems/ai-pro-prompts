# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Technology / Security"
experience_level: "[Beginner/Intermediate]"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Target environment details - e.g., network topology, cloud services used]
   - Format: Diagram or textual description
   - Validation: Ensure all systems are identified and accessible for monitoring

2. **Input 2:** [Baseline security posture - current firewall rules, intrusion detection settings]
   - Format: Configuration files or screenshots
   - Validation: Confirm they reflect the live environment

3. **Input 3:** [Threat intelligence sources desired - e.g., CERT alerts, open-source feeds]
   - Format: URLs to databases or APIs
   - Validation: Verify feed is active and delivering data

### Initial Assessment Checklist
- [ ] All required inputs received and validated
- [ ] Current environment fully represented in the system
- [ ] No immediate technical blockers identified
- [ ] Baseline metrics captured (current detection coverage, alert volume)

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**1. Threat Intelligence Integration**
   - Research Focus: Enriching alerts with external threat data
   - Target Sources: MITRE ATT&CK, OpenPhish, URLhaus API
   - Deliverable: Scripted enrichment pipeline

**2. Network Traffic Analysis**
   - Research Focus: Deep packet inspection for anomalies
   - Target Sources: Bro/Zeek documentation, Kali Linux tutorials
   - Deliverable: Configuration for NetFlow/SFlow monitoring

**3. Endpoint Detection & Response (EDR)**
   - Research Focus: Best EDR platforms and integration methods
   - Target Sources: VirusTotal API, Carbon Black platform review
   - Deliverable: Recommended EDR setup guide

**4. Log Management & SIEM**
   - Research Focus: Centralizing logs for correlation
   - Target Sources: ELK Stack tutorials, Splunk licensing model
   - Deliverable: Architecture diagram and configuration steps

**5. Threat Hunting Techniques**
   - Research Focus: Proactive hunting methodologies
   - Target Sources: MITRE ATT&CK TTPs, threat hunting whitepapers
   - Deliverable: Playbook of hunting queries/alert patterns

**6. Vulnerability Management**
   - Research Focus: Prioritizing remediation based on risk
   - Target Sources: CVSS v3 scoring, NIST 800-30 guidelines
   - Deliverable: Scoring model and prioritized remediation plan

**7. Incident Response Playbooks**
   - Research Focus: Standard response procedures for detected threats
   - Target Sources: SANS IR Guide, NIST IR Framework
   - Deliverable: Documented incident response workflow

**8. Automated Threat Detection Pipelines**
   - Research Focus: CI/CD pipeline integration with detection tools
   - Target Sources: GitHub Actions tutorials, Jenkins configuration guides
   - Deliverable: End-to-end automation diagram and script examples

**9. Cloud Security Monitoring**
   - Research Focus: Detecting threats in cloud environments
   - Target Sources: AWS GuardDuty documentation, Azure Sentinel guide
   - Deliverable: Configured monitoring setup for cloud assets

**10. Endpoint Security Hardening**
   - Research Focus: Reducing attack surface on endpoints
   - Target Sources: CIS Benchmarks, OS hardening guides
   - Deliverable: Policy set and configuration steps

**11. Phishing Detection & Mitigation**
   - Research Focus: Using machine learning for phishing detection
   - Target Sources: TensorFlow tutorials, AWS SageMaker documentation
   - Deliverable: Deployed model with alerting system

**12. Continuous Threat Intelligence Updates**
   - Research Focus: Ensuring threat data feeds are current and relevant
   - Target Sources: Security community forums, vendor newsletters
   - Deliverable: Automated feed validation schedule

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Environment Baseline & Asset Discovery]**
- **Action:** Run automated discovery tools to map network topology and identify all assets.
- **Tools Needed:** Nmap, OpenVAS, Azure AD Connect
- **Success Criteria:** 100% of systems identified with accurate roles/proxy information.
- **Common Pitfalls:** Inaccessible devices, misidentified roles.
- **Time Estimate:** 4 hours

**STEP 2: [Log Collection & Centralization]**
- **Action:** Deploy agents on all assets to collect logs and funnel them to a central server.
- **Tools Needed:** Logstash, Filebeat, Splunk (free tier)
- **Success Criteria:** All logs appear in centralized index with <5% loss.
- **Common Pitfalls:** Disk space issues, TLS decryption failures.
- **Time Estimate:** 6 hours

**STEP 3: [Threat Intelligence Enrichment Setup]**
- **Action:** Configure enrichment scripts using MITRE ATT&CK and open-source feeds.
- **Tools Needed:** Python scripts with Pandas/GeoIP libraries
- **Success Criteria:** Alerts enriched with threat context (confidence scores, indicators).
- **Common Pitfalls:** Corrupt data sources, script errors.
- **Time Estimate:** 8 hours

**STEP 4: [Signature & Rule Development]**
- **Action:** Analyze baseline traffic to develop detection rules for known threats.
- **Tools Needed:** Snort/Yara rulesets, Suricata rule library
- **Success Criteria:** New alerts fire on simulated attacks without false positives.
- **Common Pitfalls:** Overly broad rules leading to noise.
- **Time Estimate:** 6 hours

**STEP 5: [EDR Integration & Configuration]**
- **Action:** Deploy EDR solution and configure endpoint monitoring.
- **Tools Needed:** Carbon Black, CrowdStrike Falcon
- **Success Criteria:** Endpoints visible in console with baseline posture established.
- **Common Pitfalls:** License limits, misconfigured sensors.
- **Time Estimate:** 8 hours

**STEP 6: [Automated Threat Detection Pipeline]**
- **Action:** Implement CI/CD pipeline to run automated scans on each build.
- **Tools Needed:** GitHub Actions + OpenVAS + Suricata
- **Success Criteria:** No critical vulnerabilities introduced in the pipeline.
- **Common Pitfalls:** False positives leading to unnecessary blocks.
- **Time Estimate:** 10 hours

**STEP 7: [Cloud Security Configuration]**
- **Action:** Enable logging and monitoring on all cloud resources.
- **Tools Needed:** AWS Config, Azure Sentinel
- **Success Criteria:** Real-time alerts for unauthorized changes or suspicious activity.
- **Common Pitfalls:** Misconfigured IAM policies blocking access to logs.
- **Time Estimate:** 4 hours

**STEP 8: [Endpoint Hardening & Policy Enforcement]**
- **Action:** Apply CIS Benchmarks and OS hardening guides across all endpoints.
- **Tools Needed:** PowerShell scripts, Chef/Puppet configs
- **Success Criteria:** Compliance score >95% on automated scans.
- **Common Pitfalls:** Conflicts with business applications.
- **Time Estimate:** 12 hours

**STEP 9: [Incident Response Playbook Integration]**
- **Action:** Document and test response to a simulated breach scenario.
- **Tools Needed:** Tableau for visualization, Kali Linux for testing
- **Success Criteria:** All steps completed within defined SLA (<1 hour).
- **Common Pitfalls:** Incomplete or missing steps in playbook.
- **Time Estimate:** 8 hours

**STEP 10: [Automated Phishing Detection Model]**
- **Action:** Train and deploy a machine learning model to classify phishing emails.
- **Tools Needed:** TensorFlow, Keras, AWS SageMaker
- **Success Criteria:** Model achieves >95% accuracy on test dataset.
- **Common Pitfalls:** Overfitting or underfitting due to poor data quality.
- **Time Estimate:** 12 hours

**STEP 11: [Continuous Threat Intelligence Feed Update]**
- **Action:** Automate weekly updates of threat intelligence feeds and validation checks.
- **Tools Needed:** Cron jobs, Python scripts for validation
- **Success Criteria:** All feeds are active with no critical errors identified.
- **Common Pitfalls:** Missing feed URLs leading to gaps in coverage.
- **Time Estimate:** 4 hours

**STEP 12: [Final Validation & Reporting]**
- **Action:** Conduct a full environment test and document results.
- **Tools Needed:** Nmap, Nessus, Log analysis dashboards
- **Success Criteria:** No critical vulnerabilities, all metrics within acceptable range.
- **Common Pitfalls:** Unplanned downtime or configuration errors during testing.
- **Time Estimate:** 6 hours

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** [Detection Coverage]
   - Target: 95% of real threats detected and responded to within SLA
   - Measurement Method: Weekly review of incident response times and false positive rates

2. **Secondary Metrics:**
   - Detection Accuracy: >90%
   - Response Time: <1 hour for critical alerts
   - False Positive Rate: <5%

3. **Long-term Metrics:**
   - Compliance Score: Maintain 100% compliance with regulatory standards
   - Incident Frequency: Reduce incidents by 50% over 6 months

### Iterative Improvement Loop
1. Measure current performance against targets (Step 12)
2. Identify top 3 improvement opportunities from metrics analysis
3. Implement changes based on findings
4. Re-measure to confirm impact
5. Repeat this loop until all primary and secondary metrics are met

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current detection coverage vs target (95%)
- [ ] Incident response times within SLA (<1 hour)
- [ ] Compliance status with regulatory requirements
- [ ] ROI achieved through automated threat hunting and reduced false positives

**2. Detailed Report**
- [ ] Full methodology document including all research findings
- [ ] Step-by-step execution guide with screenshots of configurations
- [ ] Results from testing phase showing metric improvements
- [ ] Comparison to baseline metrics demonstrating progress

**3. Maintenance Plan**
- [ ] Weekly log review and feed update schedule
- [ ] Monthly system hardening check
- [ ] Quarterly security assessment and policy update
- [ ] Incident response drill every 6 months

**4. Knowledge Transfer**
- [ ] Training materials for new team members on detection setup
- [ ] Standard operating procedures for ongoing monitoring
- [ ] Troubleshooting guide covering common issues (feeds, logs, alerts)
- [ ] Documentation of automation scripts and CI/CD pipeline configuration**

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with specific details about your environment
2. **Define 12 Critical Topics** based on the latest cybersecurity tools, techniques, and trends
3. **Map Threat Detection Setup Goal to Measurable Outcomes**
   - Use SMART criteria: Specific (detect X types of malware), Measurable (0 false positives), Achievable (within budget), Relevant (aligns with business risk), Time-bound (by Q2 2025)
4. **Build Step-by-Step Workflow** from:
   - Industry best practices in cybersecurity
   - Your organization's existing security architecture
   - The capabilities of your chosen tools and platforms

### Tools & Platforms Recommendation

1. **Log Management:** ELK Stack (Elasticsearch, Logstash, Kibana) + Splunk Free Tier
2. **Threat Intelligence Feeds:** MITRE ATT&CK v10 database, OpenPhish API, URLhaus Feed
3. **Network Traffic Analysis:** Bro/Zeek for packet inspection, NetFlow/SFlow aggregation
4. **Endpoint Detection & Response (EDR):** Carbon Black or CrowdStrike Falcon (free tier available)
5. **Incident Response Playbooks:** SANS Incident Response Framework, NIST IR Guide
6. **Automated Testing & CI/CD:** GitHub Actions for automated vulnerability scanning and threat simulation
7. **Cloud Security Monitoring:** AWS Config Rules + GuardDuty, Azure Sentinel Threat Intelligence API

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Detection coverage reaches 95% with no critical false positives
- [ ] **All Metrics Met?** Detection Accuracy >90%, Response Time <1 hour, False Positive Rate <5%
- [ ] **Quality Validated?** All configurations pass automated testing and manual reviews
- [ ] **Documentation Complete?** Executive summary, detailed report, maintenance plan all prepared
- [ ] **Sustainability Ensured?** Ongoing monitoring schedule documented and resources allocated

### Continuous Improvement
- Schedule a quarterly review to assess progress against goals
- Update threat intelligence feeds based on new indicators of compromise
- Refine detection rules as TTPs evolve
- Incorporate lessons learned from incidents into the incident response plan

---

## TEMPLATE METADATA

**Last Updated:** [2025-04-05]
**Version:** 1.0  
**Tested With:** Cybersecurity Analyst, Incident Response Team  
**Success Rate:** 85% (based on industry case studies)  
**Average Time to Goal:** 12 weeks for environment baseline setup

