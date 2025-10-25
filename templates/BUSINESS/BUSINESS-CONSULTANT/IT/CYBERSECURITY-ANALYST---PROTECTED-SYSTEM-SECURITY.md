# Cybersecurity Analyst - AI Agent Template

## Protected System Security

### 1. Critical Knowledge Areas

1. Network Security
2. Endpoint Security
3. Identity and Access Management (IAM)
4. Threat Intelligence & Research
5. Vulnerability Management
6. Incident Response & Handling
7. Compliance & Regulatory Standards (e.g., GDPR, HIPAA, PCI-DSS)
8. Penetration Testing & Red Teaming
9. Malware Analysis & Reverse Engineering
10. Security Information and Event Management (SIEM)
11. Cryptography & Data Protection
12. Cloud Security Architecture
13. Application Security
14. Physical Security

### 2. Execution Steps with Actions

1. **Conduct a Comprehensive System Audit**: Use `Nessus`, an open-source vulnerability scanner, to identify all systems and software components.
   
   - Action: Run Nessus scans across all network segments and document findings.

2. **Implement Strong Access Controls**: Utilize `FreeIPA` or `OpenVAS` for managing user access with robust IAM policies.

   - Action: Set up group policies using FreeIPA and enforce multi-factor authentication (MFA).

3. **Deploy Endpoint Security Solutions**: Install lightweight, free endpoint security solutions like `ClamAV`, `Whonix`, and configure them to run scans daily/weekly.

   - Action: Configure ClamAV for real-time scanning of emails and files.

4. **Configure Firewalls & Network Segments**: Use `iptables` or the open-source `Uncomplicated Firewall (UFW)` for firewall rules that prevent unauthorized access.

   - Action: Define strict inbound/outbound rules based on least privilege principle.

5. **Implement Logging and Monitoring**: Set up `ELK Stack` (Elasticsearch, Logstash, Kibana) to aggregate logs from all systems into a searchable dashboard.

   - Action: Configure ELK for real-time log analysis and alerting on suspicious activities.

6. **Train Staff on Security Awareness**: Create phishing simulations using tools like `Cobalt Strike` or use free resources such as `PhishMe`.

   - Action: Regularly distribute simulated phishing emails to employees and analyze their responses.

7. **Develop an Incident Response Plan**: Define procedures for containment, eradication, recovery, and post-incident activities.

   - Action: Document incident response steps with clear roles and responsibilities.

8. **Continuously Update Security Knowledge**: Follow security blogs like `Krebs on Security` or subscribe to newsletters such as `Threatpost`.

   - Action: Allocate 2 hours per week for reading industry news and articles.

### 3. Tools, Software, and Platforms

- **Network Monitoring & Scanning**:
  - Nessus (free)
  - OpenVAS
- **Endpoint Security**:
  - ClamAV
  - Qubes OS (for isolation)
- **Firewalls**:
  - iptables or UFW
- **Logging & SIEM**:
  - ELK Stack (Elasticsearch, Logstash, Kibana)
- **Incident Response & Pen Testing**:
  - Cobalt Strike (optional for advanced red teaming)
  - Metasploit (for penetration testing)

### 4. Success Criteria

- **Zero Critical Vulnerabilities**: All systems scanned free tools like Nessus and OpenVAS show no critical or high vulnerabilities.
  
- **100% MFA Implementation**: 100% of users enrolled in the IAM solution with MFA activated.

- **Log Coverage**: Full coverage of system, network, and application logs within ELK dashboard without gaps.

- **Incident Response Drills**: Successful completion of tabletop exercises at least twice a year demonstrating effective response to simulated incidents.

### 5. Troubleshooting Common Issues

1. **False Positives in Logs**:
   - Verify the source by checking system services.
   - Ensure that all systems and applications are configured correctly within ELK.

2. **Access Denied Errors**:
   - Check IAM policies for user roles and permissions.
   - Validate group memberships if using FreeIPA or similar solutions.

3. **Endpoint Security Alerts False Negative**:
   - Update signature databases in ClamAV regularly.
   - Test alerts against known malware samples.

### 6. Recommended Tool Stack with Pricing

- **Primary Tools (FREE)**:
  - Nessus
  - OpenVAS
  - ClamAV
  - iptables/UFW
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  
- **Alternative / Premium Tools**:
  - Cobalt Strike ($2990 per year)
  - Metasploit Pro ($1499 per year)

### 7. Timeline to Achieve Protected System Security

1. **Weeks 1-2**: Initial Audit and Vulnerability Scanning
   - Conduct initial system audit.
   - Deploy Nessus/OpenVAS scans.

2. **Weeks 3-4**: Implement Access Controls and Endpoint Solutions
   - Enforce MFA using FreeIPA or UFW.
   - Install ClamAV and configure for real-time scanning.

3. **Weeks 5-6**: Set Up Logging and Monitoring
   - Configure ELK Stack for log aggregation and monitoring.

4. **Weeks 7-8**: Develop Incident Response Plan and Conduct Training
   - Create IR plan with clear steps.
   - Run phishing simulations using Cobalt Strike or PhishMe alternatives.

5. **Ongoing**: Continuous Monitoring, Updates, and Training
   - Regularly update tools and configurations based on new threats.
   - Schedule quarterly security awareness training for staff.

### 8. Realistic Timeline

- **Short-term (0-3 months)**: Focus on initial setup of critical security controls like access management, endpoint protection, and logging systems.
  
- **Medium-term (3-12 months)**: Develop and refine incident response procedures, establish a culture of security awareness among staff, and continuously monitor for vulnerabilities.

- **Long-term (1-2 years)**: Establish a robust threat intelligence program to stay ahead of emerging threats. Implement advanced analytics and machine learning tools for better anomaly detection in logs.

### 9. Best Practices and AI Integration

- **Automation**: Use automation scripts via `Ansible` or similar platforms to enforce security configurations across systems post-initial setup.
  
- **AI-Powered Threat Detection**: Integrate AI models using open-source libraries like TensorFlow or PyTorch for detecting anomalies in network traffic, logs, and system behavior.

- **Regular Updates**: Schedule automatic updates for all software components using tools like `Unattended Upgrades` on Debian-based systems.

- **Collaboration with AI Security Platforms**: Consider leveraging AI-driven security platforms (e.g., AWS GuardDuty) to enhance detection capabilities while maintaining compliance with free tool recommendations where possible.

