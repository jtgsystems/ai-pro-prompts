# Computer Technician - AI Agent Template
## Security Configuration

### Success Definition (Measurable)
**Primary Objective:** Achieve a state where all systems adhere to industry-standard security configurations with 100% compliance across all endpoints.

- **Compliance Rate:** 100% of devices pass internal and external vulnerability scans.
- **Vulnerability Count:** Zero critical vulnerabilities, <5 major, <10 minor per scan cycle.
- **Patch Management:** All critical patches applied within 24 hours of release.
- **User Access:** Role-based access controls in place with no privileged escalation incidents.

### Critical Knowledge Areas

1. **Operating System Hardening**
   - Focus: Best practices for securing Windows, Linux, and macOS systems
   - Tools: Security Configuration Wizard (Windows), Lynis Audit Tool (Linux), macOS Security Guide

2. **Endpoint Protection**
   - Focus: Implementing and managing antivirus/antimalware solutions
   - Tools: ESET NOD32 Antivirus (free), Bitdefender Total Security (premium alternative)

3. **Firewall Configuration**
   - Focus: Configuring network firewalls to block unauthorized access while allowing legitimate traffic
   - Tools: Windows Defender Firewall, pfSense (open-source firewall), Cisco ASA

4. **Access Control Policies**
   - Focus: Implementing and managing user account controls, session timeouts, and privilege escalation protections
   - Tools: Active Directory Group Policy Objects (GPOs), LDAP Security Bindings

5. **Patch Management Systems**
   - Focus: Automating the deployment of security patches across all endpoints
   - Tools: SCCM (System Center Configuration Manager), Ansible Playbooks (free), WSUS (Windows Server Update Services)

6. **Network Segmentation**
   - Focus: Dividing network into secure zones to prevent lateral movement in case of breach
   - Tools: VLANs, Subnet Masks, Network ACLs

7. **Secure Remote Access**
   - Focus: Implementing VPNs and other secure remote access solutions
   - Tools: OpenVPN (free), Cisco AnyConnect Secure Mobility Client (premium)

8. **Data Encryption**
   - Focus: Protecting data at rest and in transit using encryption methods
   - Tools: BitLocker (Windows), LUKS2 (Linux), FileVault (macOS)

9. **User Training & Awareness**
   - Focus: Educating users about phishing, malware, and social engineering threats
   - Tools: PhishSim (free training tool), KnowBe4 (premium threat awareness platform)

10. **Logging & Monitoring**
    - Focus: Implementing systems to log security events and monitor for anomalies
    - Tools: SIEM Solutions like Splunk Enterprise Security (free tier), ELK Stack, OSSEC

11. **Backup & Recovery Strategy**
    - Focus: Ensuring data can be restored securely in case of ransomware or other attacks
    - Tools: Veeam Backup & Replication (premium alternative), rsync, Acronis True Image

12. **Disaster Recovery Planning**
    - Focus: Preparing for major incidents that could compromise the entire network
    - Tools: DR Playbooks, NIST Cybersecurity Framework

### Execution Workflow

**STEP 1: Inventory & Baseline Assessment**
- Action: Conduct a comprehensive inventory of all endpoints and remote systems.
- Tools Needed: CMDB (Configuration Management Database), SCCM (System Center Configuration Manager)
- Success Criteria: 100% of devices accounted for with current OS/version, hardware specs captured.

**Common Pitfalls:** Missing devices due to unmanaged BYOD or rogue systems.  
**Time Estimate:** 2 weeks

**STEP 2: Baseline Security Policy Creation**
- Action: Develop a security policy template based on NIST/ISO standards.
- Tools Needed: Word Processor (free), Secure Configuration Guides
- Success Criteria: Approved by IT leadership and documented in the Knowledge Base.

**Common Pitfalls:** Lack of stakeholder buy-in.  
**Time Estimate:** 1 week

**STEP 3: Implement Operating System Hardening**
- Action: Apply hardening configurations to all systems following the policy.
- Tools Needed: Security Configuration Wizard, Lynis Audit Tool
- Success Criteria: Automated compliance scans show >95% pass rate.

**Common Pitfalls:** Over-hardening causing functional issues.  
**Time Estimate:** 2 weeks per platform

**STEP 4: Install & Configure Endpoint Protection**
- Action: Deploy antivirus/antimalware solutions and configure real-time scanning.
- Tools Needed: ESET NOD32 Antivirus, Bitdefender Total Security
- Success Criteria: No new malware detected in a controlled phishing test.

**Common Pitfalls:** User bypassing protections due to false positives.  
**Time Estimate:** 1 week

**STEP 5: Configure Firewalls**
- Action: Set up rules to block all inbound traffic except for necessary services.
- Tools Needed: Windows Defender Firewall, pfSense
- Success Criteria: No open ports detected by external scan tools.

**Common Pitfalls:** Incorrectly configured NAT or routing causing connectivity issues.  
**Time Estimate:** 1 week

**STEP 6: Implement Access Controls**
- Action: Enforce strong password policies and MFA for privileged accounts.
- Tools Needed: Active Directory, LDAP Security Bindings
- Success Criteria: No account can be accessed without proper credentials.

**Common Pitfalls:** Weak passwords due to user resistance.  
**Time Estimate:** Ongoing

**STEP 7: Patch Management Setup**
- Action: Configure automated patch deployment for all systems.
- Tools Needed: SCCM, Ansible Playbooks
- Success Criteria: <5 critical vulnerabilities remaining post-deployment.

**Common Pitfalls:** Incomplete patch rollout or missed updates.  
**Time Estimate:** 2 weeks setup

**STEP 8: Network Segmentation**
- Action: Divide network into zones based on function (DMZ, Internal, Guest).
- Tools Needed: VLAN Configuration, Subnetting Calculators
- Success Criteria: No traffic flows between zones without proper routing.

**Common Pitfalls:** Misconfigured subnets causing data leakage.  
**Time Estimate:** 1 week

**STEP 9: Secure Remote Access**
- Action: Deploy and configure VPN for remote access.
- Tools Needed: OpenVPN, Cisco AnyConnect
- Success Criteria: Users can connect securely without authentication errors.

**Common Pitfalls:** Weak VPN configurations or no client software available.  
**Time Estimate:** 1 week

**STEP 10: Implement Data Encryption**
- Action: Encrypt data at rest on all devices and in transit over the network.
- Tools Needed: BitLocker, LUKS2, FileVault
- Success Criteria: All critical files can be restored securely.

**Common Pitfalls:** Incompatible encryption formats causing restore issues.  
**Time Estimate:** 1 week

**STEP 11: Conduct Penetration Testing**
- Action: Perform internal and external security assessments.
- Tools Needed: Metasploit (free), OWASP ZAP, Nmap
- Success Criteria: All critical vulnerabilities patched.

**Common Pitfalls:** False positives leading to unnecessary work.  
**Time Estimate:** 1 month

**STEP 12: Train Users**
- Action: Conduct phishing simulations and security awareness training.
- Tools Needed: PhishSim (free), KnowBe4
- Success Criteria: Users score >90% in simulated attacks.

**Common Pitfalls:** User fatigue or lack of engagement.  
**Time Estimate:** Ongoing

**STEP 13: Implement Backup & Recovery**
- Action: Set up automated backups for critical systems.
- Tools Needed: Veeam Backup & Replication, rsync
- Success Criteria: Data can be restored within RTO (Recovery Time Objective) < 1 hour.

**Common Pitfalls:** Incomplete backup schedules or untested restores.  
**Time Estimate:** 2 weeks

**STEP 14: Develop Disaster Recovery Plan**
- Action: Document processes for recovering from major incidents.
- Tools Needed: DR Playbooks, Business Impact Analysis Software
- Success Criteria: RPO (Recovery Point Objective) < 4 hours.

**Common Pitfalls:** Lack of clear roles or testing procedures.  
**Time Estimate:** Ongoing

### Troubleshooting Common Issues

1. **Compliance Failures**
   - Check if the policy version matches what's being scanned.
   - Verify that configuration changes are synced across all systems.

2. **Patch Rollout Errors**
   - Ensure SCCM agents are installed and running on target machines.
   - Check for network or firewall blocks preventing patch downloads.

3. **Access Denials**
   - Confirm the user has been added to the correct group policy.
   - Verify password and MFA credentials if applicable.

4. **VPN Connectivity Issues**
   - Check firewall rules allow outbound traffic from VPN client.
   - Ensure users have entered correct connection parameters.

5. **Backup Failures**
   - Look for disk space issues or permissions errors on backup locations.
   - Verify that the backup schedule is active and correctly configured.

### Recommended Tool Stack

- **Primary Tools (Free/Open Source):**
  - Windows Defender Firewall
  - Lynis Audit Tool
  - SCCM Configuration Manager
  - BitLocker Full Disk Encryption
  - OSSEC Intrusion Detection System

- **Alternative Tools (Paid/Premium):**
  - ESET NOD32 Antivirus
  - pfSense Enterprise Firewall
  - Cisco AnyConnect Secure Mobility Client
  - Veeam Backup & Replication
  - PhishSim Training Tool

### Realistic Timeline to Achieve Security Configuration

| Phase | Duration |
|-------|----------|
| Inventory & Baseline | 2 weeks |
| Policy Creation | 1 week |
| OS Hardening | 2-3 weeks per platform |
| Endpoint Protection Setup | 1 week |
| Firewall Configurations | 1 week |
| Access Controls Implementation | Ongoing |
| Patch Management Deployment | 2 weeks |
| Network Segmentation | 1 week |
| Remote Access Security | 1 week |
| Encryption Implementation | 1 week |
| Penetration Testing | 1 month |
| User Training & Awareness | Ongoing |
| Backup and Recovery Setup | 2 weeks |
| Disaster Recovery Planning | Ongoing |

**Total Estimated Time:** Approximately **6-8 months**, depending on the size of the organization and complexity of existing infrastructure.

---

This template provides a comprehensive roadmap for achieving robust security configurations as a Computer Technician. It emphasizes best practices, measurable outcomes, and continuous improvement while leveraging both free and premium tools to ensure optimal protection against cyber threats.

