# Network Administrator - AI Agent Template  
## Router/Firewall Configuration  

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve Router/Firewall Configuration as a Network Administrator.

---

## PROFESSION CONFIGURATION  

### Basic Information
```yaml
profession_name: "Network Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal  
**Primary Objective:** Configure and optimize a router/firewall to securely manage network traffic, enforce security policies, and maintain high availability with 99.9% uptime over a defined period of testing.

---

## PHASE 1: INFORMATION GATHERING  

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Network topology diagram (device list & connections)
   - Format: Diagram image or text description
   - Validation: All core network devices accounted for

2. **Input 2:** Current firewall ruleset and policy
   - Format: Configuration files, CSV export
   - Validation: Rules cover all traffic planes (inbound/outbound) and are up-to-date

3. **Input 3:** Security requirements & compliance standards
   - Format: Policy documents, regulatory frameworks
   - Validation: Documents signed off by appropriate stakeholders

4. **Input 4:** Performance targets
   - Format: Throughput, latency, availability percentages
   - Validation: Targets reflect current business needs

5. **Input 5:** Maintenance schedule & backup policy
   - Format: Calendar entries, maintenance windows
   - Validation: Aligns with operational cycles

### Initial Assessment Checklist
- [ ] Verify all required inputs received and properly formatted
- [ ] Validate input quality (complete device lists, up-to-date configs)
- [ ] Identify immediate red flags or blockers in current config
- [ ] Establish baseline metrics for throughput, latency, security events

---

## PHASE 2: RESEARCH & ANALYSIS  

### Critical Knowledge Areas (10-20 Topics)  
**Research Agent Deployment:** Launch 12 parallel sub-agents to research latest practices.

**Topic 1:** Modern Firewall Architectures
- Research Focus: Next-gen firewalls, microsegmentation, application visibility
- Target Sources: Cisco UCS blog, Fortinet whitepapers, Bro blogs

**Topic 2:** Network Security Policies  
- Research Focus: CIS Controls, NIST 800-53, industry standards
- Target Sources: SANS Institute publications, ISO 27001 frameworks

**Topic 3:** Traffic Management Techniques  
- Research Focus: QoS algorithms, BGP peering best practices  
- Target Sources: Cisco Networking Academy guides, Juniper TechDocs

**Topic 4:** Configuration Best Practices  
- Research Focus: Redundancy models, change management processes
- Target Sources: IT Governance Institute reports, Purdue DevOps Handbook

**Topic 5:** Security Monitoring Tools  
- Research Focus: SIEM integration, IDS/IPS tuning  
- Target Sources: Splunk documentation, ELK Stack guides

**Topic 6:** Automation & Orchestration  
- Research Focus: Ansible playbooks, TFTP scripts for config backups
- Target Sources: HashiCorp Vault tutorials, Ansible Tower best practices

**Topic 7:** Cloud-Native Network Security  
- Research Focus: Software-defined networking (SDN), network functions virtualization (NFV)
- Target Sources: VMware NSX guides, AWS VPC whitepapers

**Topic 8:** Zero Trust Architecture Implementation
- Research Focus: Microsegmentation, identity-based policies, multi-factor authentication
- Target Sources: Palo Alto Networks Zero Trust Playbook, Gartner research reports

**Topic 9:** Network Segmentation Strategies  
- Research Focus: VLAN design, DMZ segmentation best practices
- Target Sources: RFC documents, industry case studies on segmented networks

**Topic 10:** High Availability & Failover Configurations  
- Research Focus: Active/active vs. active/passive models, HA clustering
- Target Sources: Cisco ASAs failover guide, Barracuda Load Balancer articles

**Topic 11:** Compliance Scanning Tools  
- Research Focus: Vulnerability scanners like Nessus, compliance checkers
- Target Sources: Qualys documentation, OpenVAS guides

**Topic 12:** Incident Response Playbooks  
- Research Focus: Steps for containment, eradication, recovery post-breach
- Target Sources: MITRE ATT&CK framework, SOC response guides

### Research Consolidation  
After all sub-agents complete:
1. Synthesize findings into a unified strategy document
2. Identify conflicting recommendations and prioritize by impact
3. Create a master action plan with milestones for each phase

---

## PHASE 3: EXECUTION WORKFLOW  

### Step-by-Step Process  

**STEP 1: [Architecture Redesign]**
- **Action:** Review current topology, propose optimized design considering microsegmentation & cloud integration  
- **Tools Needed:** Cisco UCS Manager (free), GNS3 or Packet Tracer (free) for simulation  
- **Success Criteria:** Updated diagram approved by network manager; documented security enhancements  
- **Common Pitfalls:** Overlooking critical path dependencies; not aligning with existing infrastructure  
- **Time Estimate:** 4 weeks

**STEP 2: [Policy Implementation]**
- **Action:** Translate compliance requirements into firewall rules, apply to all relevant interfaces  
- **Tools Needed:** Cisco ASA command-line interface (CLI), Fortinet FortiGate GUI  
- **Success Criteria:** Ruleset passes automated testing; no open ports in vulnerability scan results  
- **Common Pitfalls:** Incorrectly configured ACLs; rules not applied globally  
- **Time Estimate:** 1 week

**STEP 3: [Segmentation Deployment]**
- **Action:** Implement VLAN structure, apply security policies to each segment  
- **Tools Needed:** Cisco Switch CLI, NetScout network discovery tool (free) for validation  
- **Success Criteria:** Segments isolated in logs; no cross-segment traffic without explicit allow rules  
- **Common Pitfalls:** Inconsistent configuration across devices  
- **Time Estimate:** 1 week

**STEP 4: [Automation Setup]**
- **Action:** Configure Ansible playbooks to automate config backups, updates, and validation  
- **Tools Needed:** Ansible Tower (free), GitLab for version control  
- **Success Criteria:** Playbook runs without errors; configs are stored in a secure repository  
- **Common Pitfalls:** Syntax errors in playbook scripts; permissions issues on storage devices  
- **Time Estimate:** 3 days

**STEP 5: [Monitoring Configuration]**
- **Action:** Integrate firewall logs with SIEM system for real-time analysis  
- **Tools Needed:** Splunk (free tier available), Elasticsearch  
- **Success Criteria:** Logs appear in SIEM within minutes; alerts generated on suspicious activity  
- **Common Pitfalls:** Incorrect field mappings between systems  
- **Time Estimate:** 1 week

**STEP 6: [Testing & Validation]**
- **Action:** Conduct comprehensive penetration testing, validate performance under load  
- **Tools Needed:** Metasploit (free), Wireshark for traffic analysis  
- **Success Criteria:** All security rules pass without vulnerabilities; throughput meets SLA targets  
- **Common Pitfalls:** Not using real-world traffic patterns; not simulating DDoS attacks  
- **Time Estimate:** 2 weeks

**STEP 7: [Documentation Update]**
- **Action:** Create/Update runbooks, diagrams, and SOPs reflecting new config  
- **Tools Needed:** Confluence (free tier), Lucidchart for diagrams  
- **Success Criteria:** All documentation version controlled; accessible to all team members  
- **Common Pitfalls:** Outdated links in docs; missing contact information for critical staff  
- **Time Estimate:** 1 week

**STEP 8: [Rollout & Training]**
- **Action:** Deploy new config to production, train on changes and new tools used  
- **Tools Needed:** Zoom or Teams (free), LMS platform like Moodle (free)  
- **Success Criteria:** Staff trained; no critical errors in first week post-deployment  
- **Common Pitfalls:** Inadequate training sessions; not tracking completion of training modules  
- **Time Estimate:** 1 week

**STEP 9: [Continuous Optimization]**
- **Action:** Schedule quarterly reviews to refine policies, add new features  
- **Tools Needed:** Jira for task management (free tier), GitLab CI/CD pipelines  
- **Success Criteria:** Quarterly review completed; documented improvements implemented  
- **Common Pitfalls:** No set schedule; not tracking improvement metrics  
- **Time Estimate:** Ongoing

**STEP 10: [Backup Strategy Implementation]**
- **Action:** Configure automated daily backups of config to secure cloud storage  
- **Tools Needed:** AWS S3 (free tier), Ansible for backup scripts  
- **Success Criteria:** Backups run without errors; restores possible within SLA  
- **Common Pitfalls:** Incorrect access permissions; not testing restore procedures regularly  
- **Time Estimate:** 1 week

**STEP 11: [Failover Testing]**
- **Action:** Simulate failover to secondary router, verify automatic route propagation and security rules apply  
- **Tools Needed:** Cisco Prime GRC (free tier), Network simulator tools like GNS3  
- **Success Criteria:** Failover completes within defined RTO; no configuration drift post-failure  
- **Common Pitfalls:** Not testing in production environment; not verifying all dependent services are restarted  
- **Time Estimate:** 2 days

**STEP 12: [Documentation Review & Sign-off]**
- **Action:** Final review of all documentation, obtain sign-off from key stakeholders  
- **Tools Needed:** Google Docs (free), DocuSign for e-signatures  
- **Success Criteria:** All documents reviewed; approved by network manager and security officer  
- **Common Pitfalls:** Not tracking reviewer status; not including required signatures  
- **Time Estimate:** 1 week

### Quality Checkpoints  
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify architecture diagram reflects all changes
- **Checkpoint 2:** [After Step Y] - Validate that firewall rules meet compliance requirements
- **Checkpoint 3:** [After Step Z] - Confirm automated backup scripts run without errors

---

## PHASE 4: OPTIMIZATION & REFINEMENT  

### Performance Metrics  
Define how to measure success:

1. **Primary Metric:** Uptime over 30-day period
   - Target: ≥ 99.9%
   - Measurement Method: Monitoring platform (Nagios, Zabbix) reports

2. **Secondary Metrics:**
   - Firewall rule effectiveness measured by logs showing < 0.1% false positives
   - Security event response time ≤ 5 minutes during simulated attacks
   - Configuration drift detection rate ≥ 99%

3. **Long-term Metrics:**
   - Annual compliance audit score ≥ 95%
   - Reduction in security incidents by X% year-over-year

### Iterative Improvement Loop  
1. Measure current performance against targets for each metric  
2. Identify top 5 improvement opportunities based on metrics that fall below thresholds  
3. Implement changes (e.g., tighter rules, additional monitoring)  
4. Re-measure and document results  
5. Repeat annually or after major incidents

---

## PHASE 5: REPORTING & DOCUMENTATION  

### Deliverables  

**1. Executive Summary**
- Current state vs. target state
- Key actions taken
- Results achieved (metrics above)
- ROI impact on security posture

**2. Detailed Report**
- Complete methodology used for redesign and testing
- All research findings with source links
- Implementation details including scripts, configs, diagrams
- Before/after performance comparisons

**3. Maintenance Plan**
- Ongoing tasks: Quarterly reviews, weekly backups verification  
- Monitoring schedule: Daily status reports, monthly compliance scans  
- Update frequency: Every 6 months or after major incidents  
- Contingency procedures: RTO/RPO documentation for failover scenarios

**4. Knowledge Transfer**
- Training materials uploaded to LMS with completion tracking
- SOPs stored in Confluence and version controlled on GitLab
- Best practices documented in internal wiki page
- Troubleshooting guide created as a searchable knowledge base article

