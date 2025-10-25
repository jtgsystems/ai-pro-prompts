# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Cybersecurity Analyst"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

## PROFESSION DETAILS

### Ultimate Goal
**Primary Objective:** Establish a comprehensive audit logging system for all cybersecurity incidents, ensuring 100% detection and response capability within 30 minutes of an incident occurrence. Achieve measurable outcomes such as:
- **Detection Rate:** 99%+ of security events logged in real-time
- **Response Time:** Average resolution time of less than 2 hours per incident
- **False Positive Rate:** Less than 5%
- **Compliance Certification:** Meet ISO/IEC 27001, NIST CSF, and GDPR standards

### Target User
A beginner to intermediate Cybersecurity Analyst working remotely.

### Environment
Remote/computer-based work with a focus on virtualized and cloud environments.

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Network topology, Log sources (firewalls, IDS/IPS, servers), Incident response playbook]
   - Format: Diagrams or list of systems/devices
   - Validation: Ensure all major network components are represented

2. **Input 2:** [Regulatory requirements (e.g., GDPR, HIPAA), Industry standards (NIST, ISO)]
   - Format: Document links or PDFs
   - Validation: Verify compliance with relevant regulations

3. **Input 3:** [Existing logging tools and platforms (e.g., Splunk, ELK Stack), Incident response protocols]
   - Format: List of software names
   - Validation: Confirm access to all systems and permissions

### Initial Assessment Checklist
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers (e.g., missing log sources, inadequate storage)
- [ ] Establish baseline metrics (current state) such as:
  - Current detection rate
  - Average incident resolution time

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Security Event Log Management Best Practices
- Research Focus: Centralized log collection, encryption at rest and in transit, retention policies
- Target Sources: NIST Special Publication 800-171, CIS Critical Security Controls, Industry blogs

**Topic 2:** Logging Tool Comparison (Free Tools)
- **Tool 1:** ELK Stack (Elasticsearch, Logstash, Kibana) - Recommended
  - Free/Open Source
  - Primary Features: Full-text search, real-time monitoring dashboards, alerting capabilities
- **Tool 2:** Graylog Enterprise - Optional Premium Alternative ($299/month)
  - Offers advanced analytics and scalability

**Topic 3:** SIEM Implementation Guidelines
- Research Focus: Integration with threat intelligence feeds, correlation rules configuration, user behavior analytics
- Target Sources: IBM Security Samhitha Blog, SANS Institute Whitepapers

**Topic 4:** Cloud Logging Solutions
- **Tool 1:** Amazon CloudWatch Logs - Recommended
  - Free tier includes basic monitoring; pay-as-you-go for advanced features
- **Tool 2:** Google Cloud Logging (included in GCP services) - Optional Premium Alternative

**Topic 5:** Incident Response Playbooks
- Research Focus: Standardized processes, escalation procedures, post-mortem analysis templates
- Target Sources: NIST 800-61, SANS Institute Course Materials

**Topic 6:** Threat Intelligence Feeds Integration
- **Tool 1:** VirusTotal API - Recommended
  - Free tier includes basic threat intelligence; requires integration with logging solution
- **Tool 2:** Anomali Platform (Premium) - Optional Alternative

**Topic 7:** Automation and Orchestration Tools
- **Tool 1:** Phantom Labs - Recommended
  - Integrates seamlessly with ELK Stack, offers playbook automation for incident response
- **Tool 2:** Demisto XSOAR (Premium) - Optional Alternative

**Topic 8:** Security Analytics and SIEM Capabilities
- Research Focus: Machine learning for anomaly detection, behavioral analytics, threat scoring
- Target Sources: IBM QRadar Blog, Splunk Webinars

**Topic 9:** Compliance Monitoring Tools
- **Tool 1:** AuditBoard - Recommended
  - Free tool with comprehensive monitoring of access and changes across systems
- **Tool 2:** Tripwire (Premium) - Optional Alternative

**Topic 10:** Incident Response Training Resources
- Research Focus: Virtual labs, scenario-based exercises, certification prep materials
- Target Sources: SANS Institute Online Courses, Cybrary Free Tutorials

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy prioritizing tools with best compliance and integration capabilities.
2. Identify conflicts or contradictions in tool recommendations (e.g., budget constraints vs. feature needs).
3. Prioritize recommendations by impact on detection, response time, and regulatory compliance.

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Infrastructure Setup]**
- **Action:** Configure logging pipelines to capture data from all identified sources (firewalls, IDS/IPS, servers).
- **Tools Needed:** ELK Stack, CloudWatch Logs, AuditBoard
- **Success Criteria:** All log sources are ingested within a minute of data generation.
- **Common Pitfalls:** Missing TLS encryption for data in transit; insufficient storage capacity.
- **Time Estimate:** 2 hours

**STEP 2: [Initial Log Collection]**
- **Action:** Deploy agents on all critical systems to forward logs to the centralized log repository (ELK Stack).
- **Tools Needed:** Filebeat Agent, AuditD daemon
- **Success Criteria:** Logs are flowing into ELK within real-time indexing limits.
- **Common Pitfalls:** Network firewalls blocking outbound traffic; misconfigured file permissions.
- **Time Estimate:** 4 hours

**STEP 3: [Log Analysis and Alert Configuration]**
- **Action:** Set up dashboards for anomaly detection, configure alert thresholds (e.g., failed login attempts >5 within 10 minutes).
- **Tools Needed:** Kibana UI, Phantom Labs Automation
- **Success Criteria:** Alerts trigger correctly in response to simulated incidents.
- **Common Pitfalls:** Overly broad alerts causing false positives; lack of escalation procedures.
- **Time Estimate:** 6 hours

**STEP 4: [SIEM Integration and Correlation Rules]**
- **Action:** Integrate ELK with SIEM (Splunk) for advanced analytics, define correlation rules to detect multi-vector attacks.
- **Tools Needed:** Splunk Universal Forwarder, Phantom Labs
- **Success Criteria:** Complex attack patterns are detected within the logging system.
- **Common Pitfalls:** Inadequate rule tuning causing high false positive rates; insufficient data normalization.
- **Time Estimate:** 8 hours

**STEP 5: [Threat Intelligence Feeds]**
- **Action:** Subscribe to VirusTotal and Anomali threat feeds, configure real-time alerts for known indicators of compromise (IOCs).
- **Tools Needed:** VirusTotal API Integration, Anomali Threat Intelligence Feed
- **Success Criteria:** Immediate alerting on detected IOCs across all systems.
- **Common Pitfalls:** Subscription limits causing data truncation; misconfigured feed parsing.
- **Time Estimate:** 3 hours

**STEP 6: [Automated Response Playbooks]**
- **Action:** Develop and test playbooks in Phantom Labs for common incident types (e.g., malware detection, unauthorized access).
- **Tools Needed:** Phantom Labs Automation Platform
- **Success Criteria:** Automated response actions (e.g., isolate system) are executed successfully.
- **Common Pitfalls:** Incomplete or missing dependencies in playbook scripts; insufficient testing of edge cases.
- **Time Estimate:** 4 hours

**STEP 7: [Incident Response Workflow Integration]**
- **Action:** Connect logging and SIEM systems to incident response platform (e.g., Demisto).
- **Tools Needed:** Demisto XSOAR Integration
- **Success Criteria:** Incident tickets are automatically created in Demisto from detected logs.
- **Common Pitfalls:** Mismatched identifiers between systems causing ticket duplication or loss.
- **Time Estimate:** 2 hours

**STEP 8: [Compliance Verification]**
- **Action:** Run compliance scans using AuditBoard to ensure logging practices meet ISO/IEC 27001, NIST CSF, and GDPR requirements.
- **Tools Needed:** AuditBoard Compliance Scanning Module
- **Success Criteria:** Zero non-compliant findings in audit reports.
- **Common Pitfalls:** Missing logs for critical systems; unencrypted storage of personal data.
- **Time Estimate:** 2 hours

**STEP 9: [Performance Testing]**
- **Action:** Simulate a range of cyber incidents (e.g., ransomware, phishing) and measure detection and response times.
- **Tools Needed:** Metasploit for penetration testing, Splunk Query Language
- **Success Criteria:** Detection rate >=99% within the first 5 minutes; resolution time <2 hours per incident.
- **Common Pitfalls:** Overly aggressive alerting causing false positives; insufficient logging depth during test.
- **Time Estimate:** 8 hours

**STEP 10: [Training and Knowledge Transfer]**
- **Action:** Conduct training sessions for onboarding new analysts, create SOPs for daily operations.
- **Tools Needed:** Training modules (IBM Security Samhitha), Confluence Documentation
- **Success Criteria:** New analysts can independently operate logging system within a week of onboarding.
- **Common Pitfalls:** Incomplete documentation; lack of hands-on training exercises.
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step 3] - Verify that all alert thresholds are correctly tuned with no false positives in test logs.
- **Checkpoint 2:** [After Step 5] - Ensure threat intelligence feeds are properly ingested and alerts trigger on known IOCs.
- **Checkpoint 3:** [After Step 8] - Confirm compliance with regulatory standards using automated scanning tools.

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Detection Rate
   - Target: >=99% within first 5 minutes of incident
   - Measurement Method: Automated analysis of alert metrics over a full operational week

2. **Secondary Metrics:**
   - Average Incident Resolution Time (Target <2 hours)
     - Measurement Method: Dashboard tracking time from alert to resolution closure
   - False Positive Rate (Target <5%)
     - Measurement Method: Weekly review of false positive alerts in Kibana UI

3. **Long-term Metrics:**
   - Compliance Certification Status (Annual Review)
     - Measurement Method: Quarterly compliance scans with AuditBoard

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., tuning thresholds, adding missing log sources).
3. Implement changes using the defined workflow.
4. Re-measure and document improvements.

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state metrics
- Key actions taken to achieve goals
- ROI or impact metrics (e.g., reduction in breach incidents)

**2. Detailed Report**
- Methodology used for logging and SIEM implementation
- All research findings, tool selections, configuration details
- Before/After comparisons of detection and response times

**3. Maintenance Plan**
- Ongoing tasks to maintain audit logs (e.g., log rotation, security updates)
- Monitoring schedule (daily, weekly, monthly)
- Update frequency for playbooks and threat intelligence feeds

**4. Knowledge Transfer**
- Training materials shared via Confluence
- SOPs documented in incident response playbook templates
- Best practices documented in a wiki page with version control

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content.
2. **Define 10-20 Critical Topics** based on:
   - Industry standards and certifications
   - Latest trends and technologies
   - Regulatory requirements
   - Tool and platform updates
   - Methodology innovations

3. **Map Ultimate Goal to Measurable Outcomes**
   - Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
   - Define clear success metrics
   - Establish acceptable ranges

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks
   - Expert practitioner processes
   - Tool vendor best practices
   - Case studies of successful implementations

5. **Include Latest 2024-2025 Practices**
   - AI/ML integration opportunities (e.g., anomaly detection)
   - Automation possibilities (e.g., orchestration with Phantom Labs)
   - New tool capabilities (e.g., cloud-native logging solutions)

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Security Event Log Management Best Practices]"
    focus: "Centralized log collection, encryption at rest and in transit, retention policies"
    sources: ["NIST Special Publication 800-171", "CIS Critical Security Controls Blog"]
    deliverable: "3-5 actionable insights with source citations"

  - agent_id: 2
    topic: "[Logging Tool Comparison]"
    focus: "Tools comparison for centralized logging and SIEM integration"
    sources: ["ELK Stack Documentation", "Splunk Pricing Page"]
    deliverable: "Recommended toolset with justification table including cost analysis"

  # [Continue for agents 3-10]
```

## SUCCESS VALIDATION

### Final Checklist
Before marking this profession task as COMPLETE:

- **[ ]** Ultimate Goal Achieved? (Detection Rate >=99%, Resolution Time <2 hours)
- **[ ]** All Metrics Met? (Compliance, False Positive Rate, Performance Benchmarks)
- **[ ]** Quality Validated? (System performs correctly under test scenarios)
- **[ ]** Documentation Complete? (All deliverables in place)
- **[ ]** Sustainability Ensured? (Maintenance plan defined and resources allocated)

### Continuous Improvement
1. Document lessons learned from each iteration.
2. Update the template with new best practices identified during Phase 4.
3. Share insights with peers through forums or knowledge bases.
4. Schedule periodic reviews to assess ongoing relevance.

## TEMPLATE METADATA

**Last Updated:** [2025-06-20]
**Version:** 1.0
**Tested With:** Cybersecurity Analyst (Beginner/Intermediate)
**Success Rate:** N/A
**Average Time to Goal:** N/A

---

*This master template should be copied and customized for each specific profession. The framework remains constant, but the details within each section are profession-specific.*

