# Network Administrator - AI Agent Template
## Secure Network Infrastructure

### Ultimate Goal Definition (Success Criteria)
**Primary Objective:** Achieve a Zero Trust Security Model for all network infrastructure components within 90 days.

- **Specific:** Implement multi-factor authentication (MFA) on all user accounts, including admin credentials.
- **Measurable:** Deploy 100% MFA across all systems with <1% false positive rate in audit logs.
- **Achievable:** Utilize existing IAM solutions and phased rollout strategy.
- **Relevant:** Aligns with industry best practices for network security and regulatory compliance (e.g., GDPR, HIPAA).
- **Time-bound:** Complete within 90 days.

### Critical Knowledge Areas
1. Network Segmentation Best Practices
2. Zero Trust Architecture Principles
3. Multi-Factor Authentication Implementation
4. Endpoint Security Configuration
5. Firewall Rule Optimization
6. Intrusion Detection System (IDS) Tuning
7. Vulnerability Management Workflow
8. Regular Security Audits and Penetration Testing
9. Incident Response Planning
10. Secure Remote Access Protocols

### Execution Steps with Tools & Success Criteria

**STEP 1: Network Segmentation Implementation**
- **Action:** Design and implement network segmentation using VLANs, VPNs, and access control lists (ACLs).
- **Tools Needed:** Cisco ASA Firewalls, VMware NSX Manager.
- **Success Criteria:** Achieve ≥80% network segment isolation with <5% misconfiguration errors identified in audit logs.

**STEP 2: Zero Trust Architecture Deployment**
- **Action:** Configure micro-segmentation and enforce least privilege access policies.
- **Tools Needed:** Cisco Identity Services Engine (ISE), PAN-OS Firewalls, Azure Sentinel for monitoring.
- **Success Criteria:** Deploy zero trust model with <10% exceptions to default policies.

**STEP 3: MFA Rollout**
- **Action:** Enable MFA for all user accounts using TOTP or U2F protocols.
- **Tools Needed:** Okta Identity Provider, Duo Security integration with AD.
- **Success Criteria:** Achieve 100% MFA adoption with <1% account lockouts due to authentication failures.

**STEP 4: Endpoint Security Hardening**
- **Action:** Configure endpoint detection and response (EDR) solutions on all workstations and servers.
- **Tools Needed:** CrowdStrike, Carbon Black, SysInternals tools for Windows systems.
- **Success Criteria:** Identify >90% of malicious activity in real-time with <5 false positives.

**STEP 5: Firewall Rule Optimization**
- **Action:** Review and optimize existing firewall rules to eliminate unnecessary open ports/services.
- **Tools Needed:** Palo Alto PAN-OS, Fortinet FortiGate Management Console.
- **Success Criteria:** Reduce attack surface by ≥70% as measured through vulnerability scans.

**STEP 6: IDS/IPS Tuning**
- **Action:** Configure Intrusion Detection and Prevention Systems (IDS/IPS) to block known threats.
- **Tools Needed:** Snort, Suricata, Zeek for open-source solutions; Cisco Stealthwatch or AlienVault OTX for managed services.
- **Success Criteria:** Detect ≥95% of test malware with <1 false positive rate.

**STEP 7: Vulnerability Management Process**
- **Action:** Implement a continuous vulnerability scanning and patch management workflow using automated tools.
- **Tools Needed:** Nessus, OpenVAS, Red Canary.
- **Success Criteria:** Reduce critical vulnerabilities by ≥85% over the first quarter.

**STEP 8: Security Audit Preparation**
- **Action:** Prepare for quarterly security audits with documentation of all configurations and policies.
- **Tools Needed:** AWS Config Rules, Azure Policy Compliance Checker.
- **Success Criteria:** Pass third-party audit checklist with minor findings only.

**STEP 9: Incident Response Drills**
- **Action:** Conduct regular incident response drills simulating breach scenarios.
- **Tools Needed:** Tabletop exercises using documented playbooks; Digital forensics tools for investigation analysis.
- **Success Criteria:** Complete drill within 4 hours and document lessons learned.

**STEP 10: Secure Remote Access Deployment**
- **Action:** Implement secure VPN access with strong encryption protocols (e.g., OpenVPN, WireGuard).
- **Tools Needed:** Cisco AnyConnect, open-source alternatives like FreeIPA for authentication.
- **Success Criteria:** Achieve 100% remote connection compliance with MFA and encrypted tunneling.

### Recommended Tool Stack
**Primary Tools (Free/Open Source):**
1. **Cisco ASA Firewalls** (free configuration tools)
2. **VMware NSX Manager** (for network virtualization)
3. **Identity Services Engine (ISE)** - Free community edition available
4. **Palo Alto PAN-OS** for firewall management
5. **CrowdStrike Falcon Platform** (cloud-delivered endpoint protection)
6. **Snort or Suricata IDS/IPS**
7. **Nessus Scanning Tool** (free version with limited plugins)

**Alternative / Paid Tools:**
1. **Okta Identity Provider** - Advanced MFA features
2. **Duo Security Mobile App** - Stronger authentication options
3. **Azure Sentinel** or **AWS GuardDuty** for advanced threat detection
4. **Carbon Black Endpoint Protection** (paid, with advanced analytics)
5. **Red Canary Threat Detection** (subscription-based monitoring)

### Troubleshooting Common Issues
- **Issue:** MFA configuration errors resulting in authentication failures.
  - **Solution:** Verify that the Identity Provider is correctly federated with Active Directory and that device registration is complete.

- **Issue:** Firewall rules causing connectivity issues between segmented networks.
  - **Solution:** Use firewall logging to trace traffic paths and adjust ACLs accordingly, ensuring least privilege access.

- **Issue:** IDS alerts generating too many false positives.
  - **Solution:** Tune signature sets based on threat intelligence feeds; whitelist known benign activity patterns.

- **Issue:** Endpoint security tools not detecting malicious activity.
  - **Solution:** Update EDR signatures and conduct a full system scan, focusing on recently compromised vulnerabilities.

### Recommended Learning Path
1. **Fundamentals:**
   - CompTIA Network+ Certification (covers network architecture, protocols)
   - ITIL Foundation for Service Management

2. **Advanced:**
   - Certified Information Systems Security Professional (CISSP) Exam Prep
   - Zero Trust Architecture Whitepaper Review

3. **Hands-On Labs:**
   - Cisco CCNA Security Certification
   - Red Team/Blue Team Exercises via CTF platforms like CaptureTheFlag101

### Timeline to Achieve Secure Network Infrastructure
**Phase 1:** Initial Assessment & Planning (Weeks 1-2)
- Define security goals and baseline network state.
- Identify key stakeholders and communication channels.

**Phase 2:** Implementation of Core Security Controls (Weeks 3-6)
- Deploy segmentation, MFA, and endpoint protection.
- Conduct initial configuration reviews.

**Phase 3:** Optimization & Tuning (Weeks 7-10)
- Refine firewall rules, IDS signatures, and access policies.
- Perform vulnerability scans and patch prioritization.

**Phase 4:** Continuous Improvement & Auditing (Ongoing)
- Schedule quarterly security audits and penetration tests.
- Update documentation based on findings and new threats.

**Total Estimated Time to Achieve Goal:** 90 days

---

This template provides a comprehensive roadmap for Network Administrators to secure their network infrastructure with measurable outcomes. It is structured around industry best practices, incorporates the latest tools and techniques from 2024-2025, and focuses on tasks that can be executed remotely by someone new to the role but looking to advance in network security expertise.

