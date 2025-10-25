# Cybersecurity Analyst - AI Agent Template
## Team Training

### Success Definition:
**Primary Objective:** Achieve a 95% or higher average score on simulated incident response drills across all team members within 8 weeks, with the following breakdown:

- **Individual Proficiency:** Each member scores at least 90% in their respective sub-drill categories.
- **Team Coordination:** Team achieves seamless communication and decision-making during live simulations.
- **Knowledge Retention:** Post-training quiz scores show a 10% improvement from pre-simulation scores.

### Critical Knowledge Areas (15 Topics)

**1. Threat Intelligence**
   - Research Focus: Latest threat indicators, malware trends
   - Target Sources: Open-source intelligence platforms like VirusTotal, DarkOS

**2. Incident Response Procedures**
   - Research Focus: NIST 800-61 framework updates
   - Target Sources: Official NIST publications, Red Team reports

**3. Vulnerability Management**
   - Research Focus: Emerging zero-day vulnerabilities and patch management
   - Target Sources: CVE database, vendor advisories

**4. Network Security Monitoring**
   - Research Focus: SIEM configuration best practices
   - Target Sources: Splunk, ELK Stack documentation

**5. Endpoint Detection & Response (EDR)**
   - Research Focus: New malware signatures and detection techniques
   - Target Sources: EDR vendor threat feeds, OSINT on malware behavior

**6. Secure Coding Practices**
   - Research Focus: OWASP Top 10 updates for 2024-2025
   - Target Sources: OWASP resources, code review tools like SonarQube

**7. Password Management & Multi-Factor Authentication (MFA)**
   - Research Focus: Best practices and policies
   - Target Sources: NIST guidelines, MFA solutions documentation

**8. Social Engineering Defense**
   - Research Focus: New phishing tactics and defense strategies
   - Target Sources: Phishing simulation platforms, MITRE ATT&CK for persuasion techniques

**9. Cloud Security Fundamentals**
   - Research Focus: AWS, Azure, Google Cloud security controls updates
   - Target Sources: Vendor best practices guides, CIS benchmarks

**10. Logging & Log Analysis**
    - Research Focus: SIEM log processing and alert tuning
    - Target Sources: Splunk tutorials, ELK Stack configurations

**11. Endpoint Security Configuration**
    - Research Focus: Configuring firewalls, application whitelisting
    - Target Sources: Vendor guides for common endpoint security solutions

**12. Privileged Access Management (PAM)**
    - Research Focus: Role-based access controls and session management
    - Target Sources: PAM vendor documentation, IAM best practices

**13. Red Teaming & Blue Team Exercises**
    - Research Focus: Tactics, techniques, and procedures for realistic scenarios
    - Target Sources: Red teaming frameworks like ATT&CK, blue team response guides

**14. Network Segmentation Strategies**
    - Research Focus: Implementing micro-segmentation in cloud environments
    - Target Sources: Security architecture blogs, network design case studies

**15. Compliance & Regulatory Requirements**
    - Research Focus: GDPR, HIPAA, PCI-DSS updates for 2024-2025
    - Target Sources: Official compliance guidelines, legal databases

### Execution Steps:

**STEP 1: [Introduction to Cybersecurity Roles]**
- **Action:** Conduct a virtual orientation session introducing the team to core cybersecurity roles and responsibilities.
- **Tools Needed:** Zoom/Teams (free), Google Docs for meeting notes
- **Success Criteria:** All members complete quiz with ≥90% score within 2 days of training start.
- **Common Pitfalls:** Misunderstanding role boundaries leading to communication issues during drills.
- **Time Estimate:** 1 day

**STEP 2: [Threat Intelligence Workshop]**
- **Action:** Run a live exercise using real-world threat intelligence feeds. Teams analyze indicators, update their SIEM configurations accordingly, and present findings.
- **Tools Needed:** VirusTotal API (free), Splunk trial license, Slack for collaboration
- **Success Criteria:** 90% of teams correctly identify and block at least 3 different IOCs within the session.
- **Common Pitfalls:** Teams fail to update logs or share intel effectively.
- **Time Estimate:** 2 days

**STEP 3: [Incident Response Drills]**
- **Action:** Simulate a ransomware attack scenario. Team members rotate through detective, eradication, and recovery roles. Post-mortem debrief includes lessons learned.
- **Tools Needed:** Cuckoo Sandbox (free), CrowdStrike Falcon (trial), JIRA for tracking
- **Success Criteria:** Average response time <30 minutes, all critical systems restored within 24 hours of drill completion.
- **Common Pitfalls:** Incomplete data sharing or incorrect remediation steps leading to prolonged resolution times.
- **Time Estimate:** 3 days

**STEP 4: [Vulnerability Assessment & Patch Management]**
- **Action:** Conduct a tabletop exercise where teams identify vulnerabilities in sample environments and prioritize patching based on risk.
- **Tools Needed:** Nessus (free tier), JIRA for tracking, Slack for communication
- **Success Criteria:** ≤10% of identified issues remain unpatched by end of week 2.
- **Common Pitfalls:** Teams fail to categorize vulnerabilities properly or overlook critical systems.
- **Time Estimate:** 1 week

**STEP 5: [Endpoint Security Training]**
- **Action:** Run a hands-on lab where teams configure EDR solutions, analyze suspicious endpoint activity, and respond accordingly.
- **Tools Needed:** CrowdStrike (free tier), BloodHound for path analysis, Slack for collaboration
- **Success Criteria:** Teams detect and contain 100% of simulated attacks within the lab environment.
- **Common Pitfalls:** Misconfiguration leading to false positives or negatives during detection phases.
- **Time Estimate:** 2 days

**STEP 6: [Phishing Simulation & Defense]**
- **Action:** Conduct a live phishing simulation using multiple vectors (email, social media). Teams practice identifying and reporting attempts before escalation.
- **Tools Needed:** PhishSim (free), Gmail/Suite for email testing, Slack for communication
- **Success Criteria:** ≥95% of team members correctly identify and report at least 3 distinct phishing attempts.
- **Common Pitfalls:** Lack of user training leading to high false positive rates or missed detections.
- **Time Estimate:** 1 day

**STEP 7: [Network Segmentation Best Practices]**
- **Action:** Conduct a design session where teams segment a virtual network environment based on risk. Validate segmentation using threat modeling tools.
- **Tools Needed:** Zero Trust Network Access (ZTNA) trial, Maltego (free), Nmap
- **Success Criteria:** All critical assets isolated in secure zones with <5% overlap between security levels.
- **Common Pitfalls:** Overly permissive configurations leading to lateral movement during testing.
- **Time Estimate:** 2 days

**STEP 8: [Compliance Mapping Workshop]**
- **Action:** Map each team member's responsibilities against relevant regulatory requirements (e.g., GDPR, HIPAA). Identify gaps and develop remediation plans.
- **Tools Needed:** Compliance mapping templates (free), JIRA for tracking
- **Success Criteria:** All compliance gaps closed within 2 weeks of initial identification.
- **Common Pitfalls:** Misalignment between team members' roles and regulatory requirements leading to audit findings.
- **Time Estimate:** 1 week

**STEP 9: [Red Teaming & Blue Team Role Rotation]**
- **Action:** Rotate red (attacker) and blue (defender) teams during live network defense exercises. Evaluate effectiveness of detection/prevention mechanisms.
- **Tools Needed:** Metasploit (free), Nmap, Kali Linux trial
- **Success Criteria:** Red team fails to breach the perimeter within 2 hours in at least 80% of attempts.
- **Common Pitfalls:** Blue team fails to detect or respond to red team activities due to inadequate monitoring/alerting.
- **Time Estimate:** 3 days per rotation cycle

**STEP 10: [Final Team Training Simulation]**
   - **Action:** Conduct a full-scale scenario-based training where the entire team is involved in response to a multi-vector attack (e.g., phishing leading to lateral movement and data exfiltration).
   - **Tools Needed:** Cuckoo Sandbox, CrowdStrike Falcon Pro trial, JIRA for tracking incidents
   - **Success Criteria:** Complete containment of the simulated breach within 2 hours post-incident detection.
   - **Common Pitfalls:** Overextension of resources leading to delays in response or incomplete remediation.
   - **Time Estimate:** 1 day

### Tools & Software:

**Primary Tools (Free/Open Source):**
- **Threat Intelligence:**
  - VirusTotal API
  - OpenPhish
  - URLhaus

- **Incident Response:**
  - Splunk Free Edition
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  - Graylog Community Edition

- **Endpoint Detection & Response (EDR):**
  - CrowdStrike Falcon Preview (Free Tier)
  - Carbon Black Community Edition
  - OSQuery for endpoint monitoring

- **Logging & Analysis:**
  - Splunk Free Edition
  - ELK Stack
  - Graylog Community Edition

- **Network Security Monitoring:**
  - Snort Open Source IDS/IPS
  - Suricata (Free)
  - Wireshark for network traffic analysis

**Alternative Tools (Paid):**
- **Threat Intelligence:**
  - Recorded Future Pro (Enterprise, $100/user/month)
  - ThreatStream Advanced Threat Detection (Enterprise)

- **Incident Response:**
  - IBM QRadar Advisor with AI (Premium, starts at $5000/year)
  - Splunk Enterprise Security Suite (SaaS, Custom pricing)

- **Endpoint Protection & Incident Response:**
  - Carbon Black Cloud Service (Enterprise, Custom pricing)
  - CrowdStrike Falcon One Endpoint Protection (Enterprise, Custom pricing)

### Troubleshooting:

**Common Issues and Solutions:**

1. **Tool Configuration Errors:**
   - *Issue:* SIEM or EDR tools not properly configured to collect logs.
   - *Solution:* Validate log forwarding settings, ensure agents are installed on all endpoints.

2. **Role Confusion During Drills:**
   - *Issue:* Team members fail to adhere to their designated roles during simulations.
   - *Solution:* Clearly define and communicate roles before each drill. Use role-specific checklists.

3. **Communication Breakdowns:**
   - *Issue:* Teams struggle to share information or updates during high-pressure scenarios.
   - *Solution:* Establish real-time communication channels (e.g., Slack) and designate a single point of contact for critical decisions.

4. **Resource Constraints:**
   - *Issue:* Limited access to paid tools during training leading to incomplete simulations.
   - *Solution:* Utilize free alternatives or trial versions of premium tools where possible.

5. **Knowledge Gaps Identified During Debriefs:**
   - *Issue:* Specific areas of knowledge uncovered as weak points after drills.
   - *Solution:* Schedule additional training sessions on these topics and re-assess progress in the next cycle.

### Recommended Tool Stack:

**Primary Tools (Free/Open Source):**
- VirusTotal API
- Splunk Free Edition
- CrowdStrike Falcon Preview

**Alternative/Premium Tools:**
- Recorded Future Pro ($100/user/month)
- IBM QRadar Advisor with AI (starts at $5000/year)
- Carbon Black Cloud Service (Custom pricing)

### Timeline for Team Training Achievement:

**Week 1-2:** Introduction, Threat Intelligence Workshop
**Week 3:** Incident Response Drills
**Week 4:** Vulnerability Assessment & Patch Management
**Week 5:** Endpoint Security Training, Phishing Simulation
**Week 6:** Network Segmentation Best Practices, Compliance Mapping
**Week 7:** Red Teaming & Blue Team Role Rotation
**Week 8:** Final Team Training Simulation and Debrief

### Measurable Success Criteria:

- **Pre-Simulation Scores:** Average quiz score across all team members = X%
- **Post-Simulation Scores:** Average quiz score = ≥90%, with at least 95% in individual drills
- **Drill Completion Rates:** All simulations completed within the defined time frames (e.g., ≤30 minutes for phishing, ≤2 hours for containment)
- **Incident Response Time:** Median response time to simulated breaches <30 minutes
- **Knowledge Retention:** Post-training quiz score ≥10% improvement from pre-simulation scores

### Action Plan for New Cybersecurity Analysts:

1. **Familiarize with Core Tools:** Start by configuring a free SIEM (e.g., Splunk Free Edition) and EDR solution.
2. **Complete Orientation Sessions:** Attend all mandatory training sessions, focusing on understanding roles and responsibilities.
3. **Participate in Drills:** Actively engage in all simulation exercises, contributing insights where possible.
4. **Review Debriefs:** Analyze post-drill debriefs to understand areas for improvement and document them.
5. **Self-Study Critical Topics:** Independently research identified knowledge gaps (e.g., phishing techniques, cloud security best practices).
6. **Seek Mentorship:** Regularly meet with more experienced team members for guidance and feedback.
7. **Stay Updated on Threat Intelligence:** Use free threat intelligence platforms to monitor emerging threats relevant to the organization.

### Latest 2024-2025 Best Practices & AI Integration:

1. **AI-Powered Threat Detection:** Integrate machine learning models (e.g., from CrowdStrike or open-source projects like Malwarebytes) into SIEM for real-time threat detection.
2. **Automated Incident Response Playbooks:** Utilize tools like Phantom to automate responses based on detected threats, reducing human error and response times.
3. **AI-Enhanced Vulnerability Scanning:** Employ AI-driven vulnerability scanners (e.g., Deep Security Manager from VMware) to prioritize critical vulnerabilities for patching.
4. **Behavioral Analytics for Insider Threats:** Use EDR solutions with behavioral analytics capabilities (e.g., Carbon Black's Conti Guard) to detect abnormal user behavior indicative of insider threats.
5. **Automated Compliance Scanning:** Implement continuous compliance scanning tools that leverage AI to identify potential regulatory violations in real-time.

By following this comprehensive template, Cybersecurity Analysts can achieve a highly trained and effective team capable of responding to sophisticated cyber threats while maintaining rigorous compliance with industry standards.

