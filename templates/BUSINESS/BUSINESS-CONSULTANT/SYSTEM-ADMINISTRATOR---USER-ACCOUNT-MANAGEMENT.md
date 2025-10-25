# System Administrator - AI Agent Template
## User Account Management

### Success Definition (Measurable)
**Primary Objective:** Achieve 100% accurate, secure, and compliant user account management within a remote environment using only free/open-source tools by the end of Q1 2025.

#### Measurable Success Criteria:
- **Accuracy:** All user accounts are created, modified, or deleted exactly as documented with zero discrepancies.
- **Security:** 99.9% of user accounts meet or exceed recommended security best practices (strong passwords, MFA enabled).
- **Compliance:** Full audit trail maintained for all account changes, meeting GDPR/CCPA requirements where applicable.
- **Performance:** Account creation/modification processes automated to complete within <2 minutes under normal load.

### Critical Knowledge Areas (10-20 Topics)
1. **Account Lifecycle Management**
   - Research Focus: Lifecycle stages from creation to deletion
   - Tools: LDAP/AD integration tools, ticketing systems

2. **Password Policy Enforcement**
   - Research Focus: Strength requirements, rotation frequency
   - Tools: Hashcat, John the Ripper (free), LastPass Vault alternative

3. **Multi-Factor Authentication Setup**
   - Research Focus: Types of MFA methods, compatibility with existing infrastructure
   - Tools: Google Authenticator (free), Duo Mobile (optional premium)

4. **Role-Based Access Control (RBAC)**
   - Research Focus: Best practices for defining roles and permissions
   - Tools: sudoers file management tools, RBAC plugins

5. **Audit Logging & Compliance**
   - Research Focus: Log retention policies, GDPR/CCPA requirements
   - Tools: rsyslog (free), ELK Stack alternative

6. **Automation with Scripting Languages**
   - Research Focus: Bash scripts for account creation/deletion, Python integration
   - Tools: Ansible (free), Puppet (free)

7. **Directory Services Integration**
   - Research Focus: Syncing user accounts between local and directory services
   - Tools: OpenLDAP (free), Active Directory Federation Services (optional premium)

8. **Account Recovery Procedures**
   - Research Focus: Process for password resets, account lockouts
   - Tools: Account recovery workflows

9. **Backup & Restore Strategies**
   - Research Focus: Regular backups of user data and account configurations
   - Tools: rsync (free), Duplicati alternative

10. **Incident Response Planning**
    - Research Focus: Steps to take in case of unauthorized access or data breach
    - Tools: Incident response playbook templates

### Execution Workflow
**STEP 1: [Foundation Setup]**
- **Action:** Implement a robust directory service (e.g., OpenLDAP) for centralized user account management.
- **Tools Needed:** OpenLDAP, ldapadmin GUI, LDAP browser tools
- **Success Criteria:** Directory service operational with all existing user accounts synced.
- **Common Pitfalls:** Incorrect schema configuration leading to sync failures.
- **Time Estimate:** 1 week

**STEP 2: [Password Policy Enforcement]**
- **Action:** Enforce strong password policies using Hashcat or John the Ripper for periodic audits.
- **Tools Needed:** Hashcat, John the Ripper (free), monitoring scripts
- **Success Criteria:** Audit shows all accounts meet strength requirements.
- **Common Pitfalls:** Users unable to reset passwords due to policy restrictions.
- **Time Estimate:** 2 weeks

**STEP 3: [Multi-Factor Authentication Setup]**
- **Action:** Implement Google Authenticator for MFA across all user accounts.
- **Tools Needed:** Google Authenticator (free), Duo Mobile (optional)
- **Success Criteria:** All user accounts require two-factor authentication to log in.
- **Common Pitfalls:** Users unable to set up MFA on legacy systems.
- **Time Estimate:** 3 weeks

**STEP 4: [Role-Based Access Control Configuration]**
- **Action:** Define roles and assign permissions using sudoers file or RBAC plugins.
- **Tools Needed:** sudoedit, RBAC plugin for LDAP
- **Success Criteria:** Audit shows correct permissions assigned to each role.
- **Common Pitfalls:** Overprivileged accounts leading to security vulnerabilities.
- **Time Estimate:** 1 week

**STEP 5: [Automation Development]**
- **Action:** Create automated scripts for user account lifecycle management (creation, modification, deletion).
- **Tools Needed:** Ansible or Puppet for orchestration
- **Success Criteria:** Scripts successfully manage accounts without human intervention.
- **Common Pitfalls:** Incorrect syntax leading to failed deployments.
- **Time Estimate:** 2 weeks

**STEP 6: [Audit Logging Configuration]**
- **Action:** Configure rsyslog or ELK Stack to collect and store all user account change logs.
- **Tools Needed:** rsyslog, ELK alternative
- **Success Criteria:** Logs accessible for review and compliance checks.
- **Common Pitfalls:** Log retention policies not enforced leading to data loss.
- **Time Estimate:** 1 week

**STEP 7: [Backup Strategy Implementation]**
- **Action:** Set up regular backups of user account data using rsync or Duplicati.
- **Tools Needed:** rsync, Duplicati (optional)
- **Success Criteria:** Backup restores show all accounts and configurations intact.
- **Common Pitfalls:** Incomplete backups due to lack of scheduled jobs.
- **Time Estimate:** Ongoing

**STEP 8: [Incident Response Plan Creation]**
- **Action:** Develop a comprehensive incident response plan for unauthorized access or data breaches.
- **Tools Needed:** Incident response playbook templates
- **Success Criteria:** Team trained on and can execute the plan within defined timeframes.
- **Common Pitfalls:** Lack of clear escalation procedures leading to confusion during incidents.
- **Time Estimate:** 1 week

**STEP 9: [Security Audits & Testing]**
- **Action:** Conduct regular security audits using Hashcat and John the Ripper, test MFA with Duo Mobile.
- **Tools Needed:** Hashcat, John the Ripper (free), Duo Mobile testing
- **Success Criteria:** All accounts pass audit requirements without exceptions.
- **Common Pitfalls:** Skipping regular audits leading to unpatched vulnerabilities.
- **Time Estimate:** Monthly

**STEP 10: [User Training & Documentation]**
- **Action:** Provide users with training on account creation, password resets, and MFA setup. Document all processes in a centralized wiki.
- **Tools Needed:** LMS (Learning Management System), Confluence/DokuWiki
- **Success Criteria:** Users can create accounts and reset passwords independently without assistance.
- **Common Pitfalls:** Documentation not updated leading to outdated procedures.
- **Time Estimate:** Ongoing

### Troubleshooting Common Issues
**1. User Account Sync Failures**
- Check directory service connectivity
- Verify schema compatibility between systems
- Restart LDAP replication process

**2. Password Reset Failures**
- Ensure users have enabled MFA on their accounts
- Check for locked out account due to multiple incorrect login attempts
- Review password policy settings in the directory service

**3. MFA Setup Issues**
- Confirm Duo Mobile app installed and connected
- Verify user enrolled with a second factor method (SMS OTP, push notification)
- Test failover mechanism if primary factor fails

**4. Automation Failures**
- Check script syntax for errors or missing dependencies
- Ensure Ansible/Puppet agent is running on all target systems
- Review inventory of managed hosts in the orchestration tool

**5. Audit Log Loss**
- Verify log rotation settings are correctly configured
- Check storage space on log server
- Test writing to logs with a sample user account change event

### Recommended Tool Stack (2024-2025 Best Practices)
#### Primary Tools (Free/Open Source)
1. **Directory Service:** OpenLDAP
2. **Password Auditing:** Hashcat, John the Ripper
3. **MFA Management:** Google Authenticator (free), Duo Mobile (optional premium)
4. **Role-Based Access Control:** sudoers file management, LDAP RBAC plugins
5. **Automation:** Ansible or Puppet
6. **Audit Logging:** rsyslog, ELK Stack alternative
7. **Backup:** rsync
8. **Incident Response:** Incident response playbook templates

#### Optional Paid Alternatives
1. **Directory Service:** Active Directory Federation Services (optional premium)
2. **Password Auditing:** Hashcat Pro Edition (optional), John the Ripper Pro Edition (optional)
3. **MFA Management:** Duo Security Enterprise (premium alternative)
4. **RBAC:** Keycloak (open-source with enterprise support)
5. **Automation Orchestration:** Ansible Tower or Red Hat Ansible Automation Platform
6. **Audit Logging:** Splunk Enterprise (paid), ELK Stack Enterprise (paid)
7. **Backup & Recovery:** Veeam Backup & Replication (paid alternative)

### Timeline to Achieve User Account Management

**Phase 1: Research and Planning (Weeks 1-2)**
- Define critical knowledge areas
- Select research tools
- Draft initial workflow

**Phase 2: Implementation (Weeks 3-10)**
- Set up directory service and automated synchronization
- Enforce password policies and enable MFA
- Configure RBAC based on roles and responsibilities
- Develop automation scripts for account lifecycle management
- Establish audit logging and backup strategies
- Create incident response plan

**Phase 3: Testing and Validation (Weeks 11-14)**
- Conduct security audits using Hashcat and John the Ripper
- Test MFA setup with different users
- Validate automation workflows through scripted scenarios
- Review audit logs for completeness and integrity
- Simulate incidents to test response plans

**Phase 4: Training and Documentation (Weeks 15-16)**
- Train all system administrators on new processes
- Update documentation in the centralized wiki
- Provide user guides for account management tasks
- Conduct knowledge transfer sessions with team leads

