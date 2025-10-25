# Network Administrator - AI Agent Template
## User Access Management

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve User Access Management in a Network Administrator role.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Network Administrator"
profession_category: "Technology"
experience_level: "Beginner/Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve 100% secure, compliant, and efficient user access management across all network resources with zero unauthorized access incidents.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** Network infrastructure details (e.g., firewall configurations, VPN settings)
   - Format: [Firewall rules, VPN endpoints]
   - Validation: Verify connectivity and configuration through network scans.
2. **Input 2:** User account inventory (active vs inactive)
   - Format: [CSV/Database listing with user ID, role, access level]
   - Validation: Cross-reference against Active Directory/LDAP.
3. **Input 3:** Access policy documents
   - Format: [PDF/Word document]
   - Validation: Ensure policies are up-to-date and signed by management.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags (e.g., stale accounts, overly permissive access).
- [ ] Establish baseline metrics (current state of access control).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**1. Identity and Access Management (IAM)**
   - Research Focus: Implementing IAM solutions for centralized user authentication.
   - Target Sources: AWS, Azure, Google Cloud documentation.

**2. Role-Based Access Control (RBAC)**
   - Research Focus: Designing RBAC policies to limit privileges based on job function.
   - Target Sources: NIST guidelines, internal policy docs.

**3. Least Privilege Principle**
   - Research Focus: Granting users only the minimum permissions needed for their role.
   - Target Sources: Security frameworks (e.g., CIS).

**4. Multi-Factor Authentication (MFA)**
   - Research Focus: Implementing MFA across all critical systems.
   - Target Sources: Duo, Okta, Google Authenticator.

**5. Privileged Access Management (PAM)**
   - Research Focus: Securing admin credentials and session monitoring.
   - Target Sources: CyberArk, BeyondTrust.

**6. Identity Governance and Administration (IGA)**
   - Research Focus: Managing user lifecycle events (onboarding/offboarding).
   - Target Sources: Active Directory Rights Management Services.

**7. Secure Authentication Protocols**
   - Research Focus: Implementing Kerberos, LDAP, SAML.
   - Target Sources: RFCs, vendor docs.

**8. Access Monitoring and Auditing Tools**
   - Research Focus: Real-time monitoring of access logs for anomalies.
   - Target Sources: Splunk, ELK Stack, LogRhythm.

**9. Network Segmentation**
   - Research Focus: Segmenting network to limit lateral movement in case of breach.
   - Target Sources: Zero Trust Architecture guides.

**10. Secure Configuration Management**
    - Research Focus: Automating secure configurations for servers and endpoints.
    - Target Sources: Ansible, Puppet, Chef.

**11. Patch Management Process**
    - Research Focus: Ensuring all systems are patched within a defined timeframe.
    - Target Sources: NIST 800-30, CIS Benchmarks.

**12. Incident Response Plan**
    - Research Focus: Steps to contain and remediate access-related security incidents.
    - Target Sources: SANS Institute guidelines.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy for user access management.
2. Identify conflicts or contradictions in best practices (e.g., between MFA and legacy systems).
3. Prioritize recommendations by impact on security posture and operational efficiency.
4. Create master action plan.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
**STEP 1: [Define Access Policy Framework]**
- **Action:** Draft a comprehensive access policy document outlining roles, permissions, MFA requirements.
- **Tools Needed:** Google Docs/Word, version control (Git).
- **Success Criteria:** Approved by management and documented in the system.

**STEP 2: [Implement IAM Solution]**
- **Action:** Deploy an IAM solution like Azure AD or Okta to centralize user authentication.
- **Tools Needed:** Azure AD Setup Wizard, Okta Admin Console.
- **Success Criteria:** All users can log in using MFA-enabled credentials; SSO working for critical apps.

**STEP 3: [Configure RBAC and Least Privilege]**
- **Action:** Assign roles based on job function. Remove unnecessary permissions from user accounts.
- **Tools Needed:** Active Directory, LDAP client.
- **Success Criteria:** Audit shows no more than 5% of users have admin rights.

**STEP 4: [Enable Multi-Factor Authentication (MFA)]**
- **Action:** Enforce MFA for all remote access and privileged accounts.
- **Tools Needed:** Duo Security, Okta MFA settings.
- **Success Criteria:** Dashboard shows >95% compliance with MFA.

**STEP 5: [Set Up Privileged Access Management (PAM)]**
- **Action:** Implement PAM solution to secure admin credentials.
- **Tools Needed:** CyberArk, BeyondTrust.
- **Success Criteria:** Admins can request temporary access tokens without sharing passwords.

**STEP 6: [Implement Identity Governance and Administration]**
- **Action:** Automate user lifecycle management (onboarding/offboarding).
- **Tools Needed:** Azure IGA, Active Directory Rights Management Services.
- **Success Criteria:** All new hires onboarded within 48 hours; terminated accounts removed within 72 hours.

**STEP 7: [Configure Access Monitoring and Auditing Tools]**
- **Action:** Set up logs for access monitoring. Configure alerts for suspicious activity.
- **Tools Needed:** Splunk, ELK Stack.
- **Success Criteria:** Alerts fire on unusual login attempts or changes to privileged accounts.

**STEP 8: [Segment Network Using Least Privilege Principles]**
- **Action:** Divide network into zones based on functionality (e.g., DMZ, internal).
- **Tools Needed:** Cisco ASA, Juniper SRX.
- **Success Criteria:** Segmentation policy validated through penetration testing.

**STEP 9: [Implement Secure Authentication Protocols]**
- **Action:** Deploy Kerberos for authentication and SAML for single sign-on.
- **Tools Needed:** AD Kerberos configuration, Okta SAML settings.
- **Success Criteria:** Internal users can log in without passwords to critical systems.

**STEP 10: [Establish Patch Management Process]**
- **Action:** Automate patch deployment across servers and endpoints.
- **Tools Needed:** Ansible Playbooks, SCCM.
- **Success Criteria:** Weekly report shows <1% of critical systems are non-compliant with patches.

**STEP 11: [Define Incident Response Plan for Access Issues]**
- **Action:** Document steps to revoke access in case of compromise.
- **Tools Needed:** Confluence page.
- **Success Criteria:** Tested plan is reviewed and approved by all stakeholders.

**STEP 12: [Ongoing Policy Review and Update Cycle]**
- **Action:** Schedule quarterly reviews of access policies with legal/compliance teams.
- **Tools Needed:** Calendar invites, meeting notes.
- **Success Criteria:** Updated policy version deployed within the next quarter; sign-off recorded.**

---

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1 (After Step X):** Verify all users can log in using MFA-enabled credentials.
- **Checkpoint 2 (After Step Y):** Run a compliance audit showing >95% of accounts adhere to least privilege.
- **Checkpoint 3 (After Step Z):** Conduct a penetration test on network segmentation.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:
1. **Primary Metric:** Zero privileged account access incidents in the past quarter.
   - Target: [0]
   - Measurement Method: Incident response logs and audit trails.

2. **Secondary Metrics:**
   - Percentage of users compliant with MFA: [95%+]
   - Number of privilege escalation attempts blocked per month
   - Time to detect and respond to access incidents

3. **Long-term Metrics:**
   - Annual compliance scorecard against industry standards (e.g., NIST 800-53)
   - User satisfaction with access management tools (NPS)

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities.
3. Implement changes.
4. Re-measure and iterate until all metrics met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state.
- Key actions taken.
- Results achieved (e.g., no MFA incidents).

**2. Detailed Report**
- Complete methodology.
- All research findings.
- Implementation details for each step.
- Before/after access control audits.

**3. Maintenance Plan**
- Ongoing tasks to maintain results.
- Monitoring schedule (daily, weekly, monthly).
- Update frequency of policies and tools.
- Contingency procedures for policy changes or breaches.

**4. Knowledge Transfer**
- Training materials for IT staff on new processes.
- SOPs for managing access lifecycle events.
- Best practices documentation in Confluence/SharePoint.
- Troubleshooting guide for common issues (e.g., MFA enrollment failures).

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace all [BRACKETED] items** with specific network infrastructure names and user account details.
2. **Define 12 Critical Topics** based on the latest 2024-2025 technologies (e.g., Zero Trust, SASE).
3. **Map Ultimate Goal** to measurable outcomes using SMART criteria.

### Example Customization
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Identity and Access Management (IAM)"
    focus: "Latest 2024-2025 IAM solutions"
    sources: ["AWS IAM docs", "Okta blog", "NIST frameworks"]
    deliverable: "Recommended IAM solution with integration plan"

  # [Continue for agents 2-10]
```

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Identity and Access Management (IAM)"
    focus: "Latest 2024-2025 IAM solutions"
    sources: ["AWS IAM docs", "Okta blog", "NIST frameworks"]
    deliverable: "Recommended IAM solution with integration plan"

  # [Continue for agents 2-12]
```

---

## SUCCESS VALIDATION

Before marking the task COMPLETE:

- [ ] **Primary Goal Achieved?** All users have secure, compliant access.
- [ ] **All Metrics Met?** No incidents; compliance metrics hit targets.
- [ ] **Quality Validated?** Access management processes documented and auditable.
- [ ] **Documentation Complete?** All deliverables stored in the shared repository.
- [ ] **Sustainability Ensured?** Maintenance tasks assigned to IT staff.

### Continuous Improvement
- Document lessons learned after each quarter.
- Update templates with new tools or regulatory changes.
- Share best practices at internal security meetings.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Network Administrator, Cybersecurity Analyst  
**Success Rate:** [To be updated]  
**Average Time to Goal:** [To be updated]

---

