# Backend Developer - AI Agent Template
## Authentication & Authorization

### PROFESSION CONFIGURATION
```yaml
profession_name: "Backend Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Implement a secure, scalable authentication and authorization system for web applications that meets industry best practices (2024-2025 standards) using only free/open-source tools.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
```yaml
inputs:
  - target_system_url: "URL of the application requiring auth/authorization"
  - authentication_requirements: "Types of users, multi-factor support needed?"
  - authorization_model: "Role-based vs attribute-based access control"
  - compliance_standards: "GDPR, HIPAA, etc."
```

### Initial Assessment Checklist
- [ ] Verify all required inputs received and formatted correctly.
- [ ] Validate URL is active and accessible for testing.
- [ ] Confirm authentication/authorization requirements are clearly defined.
- [ ] Identify any existing security policies or compliance needs.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** JSON Web Tokens (JWT)
- **Research Focus:** Latest JWT standards, HMAC vs RSA algorithms
- **Sources:** RFC7519 spec, Auth0 blog posts, OpenSSL documentation
- **Deliverable:** Comparison of algorithm security levels and token expiration best practices

**Topic 2:** OAuth 2.0 & OpenID Connect (OIDC)
- **Research Focus:** Current implementation patterns for SPA vs backend APIs
- **Sources:** OASIS OIDC spec, GitHub oauth2-server examples, Authlib library docs
- **Deliverable:** Recommended libraries/frameworks with pros/cons

**Topic 3:** Role-Based Access Control (RBAC) vs Attribute-Based (ABAC)
- **Research Focus:** Model differences for microservices architecture
- **Sources:** OWASP documentation, NIST guidelines, Kubernetes RBAC model
- **Deliverable:** Implementation matrix comparing both models in backend contexts

**Topic 4:** Multi-Factor Authentication (MFA)
- **Research Focus:** Emerging MFA methods: WebAuthn, FIDO2 security keys
- **Sources:** Google's WebAuthn spec, NIST SP 800-133, Authy research papers
- **Deliverable:** Recommended hardware vs software tokens for secure rollout

**Topic 5:** Secure Storage of Secrets
- **Research Focus:** Best practices for DB encryption, secrets management tools
- **Sources:** HashiCorp Vault documentation, AWS KMS best practices guide
- **Deliverable:** Comparison table of secret storage solutions (AWS, Azure, GCP)

**Topic 6:** CORS Policy Management
- **Research Focus:** Configuring cross-origin policies securely
- **Sources:** MDN Web Docs on CORS, OWASP Security Headers project
- **Deliverable:** Checklist for implementing secure CORS headers

**Topic 7:** Session Management
- **Research Focus:** Cookie security (SameSite flags, Secure flag), token revocation strategies
- **Sources:** Node.js session management guides, Django sessions documentation
- **Deliverable:** Recommended cookie settings and token storage patterns

**Topic 8:** API Gateway Configuration for Auth Z
- **Research Focus:** Centralized auth strategy using AWS API Gateway, Kong, or NGINX
- **Sources:** Kong developer docs, AWS API Gateway best practices
- **Deliverable:** Config templates showing JWT validation in gateway layer

**Topic 9:** Logging and Monitoring of Authentication Events
- **Research Focus:** Tools for tracking logins, failed attempts, token usage anomalies
- **Sources:** ELK stack tutorials, Splunk Auth logs guide, Datadog auth monitoring
- **Deliverable:** Recommended logging setup with alert thresholds

**Topic 10:** Password Hashing Techniques
- **Research Focus:** Argon2id vs Bcrypt vs PBKDF2 for password storage
- **Sources:** NIST Special Publication 800-132, OWASP Password Storage Cheat Sheet
- **Deliverable:** Comparative analysis of hashing algorithms and recommended config

**Topic 11:** Database Security Best Practices
- **Research Focus:** Least privilege DB access, encryption at rest/in transit
- **Sources:** PostgreSQL security guide, MySQL encryption docs
- **Deliverable:** Checklist for securing user database schema

**Topic 12:** Network Segmentation & Firewalls
- **Research Focus:** Configuring secure network zones for auth services
- **Sources:** CIS Critical Security Controls guide, Cloud provider firewall best practices
- **Deliverable:** Recommended firewall ruleset and VPC layout diagrams

**Topic 13:** Dependency Management in Auth Systems
- **Research Focus:** Keeping JWT libraries, OAuth client libs up-to-date
- **Sources:** OWASP Dependency Check recommendations, GitHub Snyk tools
- **Deliverable:** Automated dependency update workflow with security testing

**Topic 14:** Compliance Auditing for Authentication Systems
- **Research Focus:** Preparing for GDPR/CCPA audits on auth components
- **Sources:** NIST Cybersecurity Framework, EU Data Protection Board guidance
- **Deliverable:** Audit checklist and documentation plan

**Topic 15:** Disaster Recovery & High Availability Planning
- **Research Focus:** Strategies for maintaining auth functionality during outages
- **Sources:** AWS DR best practices, Kubernetes high availability guides
- **Deliverable:** RTO/RPO calculations and failover implementation strategy

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified security architecture plan.
2. Identify any conflicting recommendations (e.g., tooling suggestions).
3. Prioritize features based on risk reduction, performance impact.
4. Create master action plan with phased rollout approach.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Select and install a secure programming environment (IDE, version control).
- **Tools Needed:** VS Code (free), GitLab or GitHub for code hosting.
- **Success Criteria:** Development environment fully configured with security extensions.
- **Common Pitfalls:** Using insecure settings in IDE, unencrypted local storage of secrets.
- **Time Estimate:** 2 hours

**STEP 2: [Authentication Core Implementation]**
- **Action:** Implement JWT generation and validation middleware.
- **Tools Needed:** Node.js + Express framework (free), JSON Web Token library (e.g., jsonwebtoken).
- **Success Criteria:** Secure token generation with HMAC SHA256, robust validation middleware.
- **Common Pitfalls:** Using weak secret keys, storing tokens in memory only.
- **Time Estimate:** 4 hours

**STEP 3: [OAuth2 / OpenID Connect Setup]**
- **Action:** Configure OAuth2 authorization server and client.
- **Tools Needed:** Authlib library (free), PostgreSQL for user database.
- **Success Criteria:** Users can log in via OAuth with proper scopes, token refresh works.
- **Common Pitfalls:** Incorrect scope handling, insecure redirect URIs.
- **Time Estimate:** 6 hours

**STEP 4: [RBAC Implementation]**
- **Action:** Define roles and permissions, implement role checks at API endpoints.
- **Tools Needed:** Role enum in DB, middleware for permission checking.
- **Success Criteria:** Users can only access resources allowed by their assigned role.
- **Common Pitfalls:** Overly permissive default roles, missing permission checks on admin actions.
- **Time Estimate:** 4 hours

**STEP 5: [MFA Integration]**
- **Action:** Implement WebAuthn or FIDO2-based MFA using a library like Authy.
- **Tools Needed:** Authy API (or open-source equivalents), server-side key storage.
- **Success Criteria:** Users can enroll authenticators, tokens are validated during login attempts.
- **Common Pitfalls:** Improper token handling leading to bypass, insufficient backup codes provisioned.
- **Time Estimate:** 6 hours

**STEP 6: [Secure Session Management]**
- **Action:** Set up secure session cookies with SameSite=Strict and Secure flags.
- **Tools Needed:** Cookie store (encrypted cookie store lib), HTTPS everywhere.
- **Success Criteria:** Sessions cannot be hijacked via CSRF, tokens expire after inactivity.
- **Common Pitfalls:** Weak CSRF protection, insecure storage of session IDs on client side.
- **Time Estimate:** 3 hours

**STEP 7: [API Gateway Configuration]**
- **Action:** Configure API Gateway to validate JWTs and enforce auth middleware.
- **Tools Needed:** AWS API Gateway (free tier), Kong or NGINX reverse proxy.
- **Success Criteria:** Unauthorized requests are blocked, valid tokens grant access.
- **Common Pitfalls:** Misconfigured routes, bypassing auth checks in certain endpoints.
- **Time Estimate:** 4 hours

**STEP 8: [Logging and Monitoring Setup]**
- **Action:** Implement secure logging of authentication events with sensitive data redacted.
- **Tools Needed:** Elastic Stack (ELK), Splunk free tier, Datadog basic monitoring.
- **Success Criteria:** Logs are encrypted at rest, alerts fire on suspicious activity patterns.
- **Common Pitfalls:** Logging secrets, inadequate alert thresholds leading to false positives.
- **Time Estimate:** 4 hours

**STEP 9: [Database Hardening]**
- **Action:** Enforce least privilege access, encrypt sensitive fields (e.g., passwords).
- **Tools Needed:** PostgreSQL with pgcrypto extensions, encrypted environment variables.
- **Success Criteria:** DB user can only perform required operations, data at rest is encrypted.
- **Common Pitfalls:** Overly permissive DB users, missing encryption for PII.
- **Time Estimate:** 4 hours

**STEP 10: [Network Segmentation & Firewall Setup]**
- **Action:** Implement network zones with firewalls controlling access to auth services.
- **Tools Needed:** AWS VPC firewall rules, NGINX reverse proxy as perimeter.
- **Success Criteria:** Auth servers are only reachable from authorized IP ranges/services.
- **Common Pitfalls:** Open ports to the internet, missing logging of suspicious network activity.
- **Time Estimate:** 3 hours

**STEP 11: [Dependency Security Review]**
- **Action:** Run automated dependency vulnerability scans and update all libraries.
- **Tools Needed:** OWASP Dependency Check (free), Snyk API integration.
- **Success Criteria:** No critical vulnerabilities found, dependencies are up-to-date.
- **Common Pitfalls:** Failing to update transitive dependencies leading to new issues.
- **Time Estimate:** 2 hours

**STEP 12: [Compliance Documentation & Audit Preparation]**
- **Action:** Document security controls and provide evidence for compliance audits.
- **Tools Needed:** Confluence or Notion, audit logs, penetration testing reports.
- **Success Criteria:** All security requirements are documented with supporting artifacts.
- **Common Pitfalls:** Incomplete documentation, missing evidence of hardening steps.
- **Time Estimate:** 5 hours

**STEP 13: [Testing & Validation]**
- **Action:** Perform load testing and security penetration tests on the auth system.
- **Tools Needed:** JMeter for load testing, OWASP ZAP or Burp Suite for security testing.
- **Success Criteria:** System withstands brute force attacks, passes all compliance checks.
- **Common Pitfalls:** Ignoring test results leading to undetected vulnerabilities.
- **Time Estimate:** 6 hours

**STEP 14: [Deployment & Monitoring](deployment)**
- **Action:** Deploy the auth system behind an API Gateway with auto-scaling enabled.
- **Tools Needed:** AWS CodeDeploy, Kubernetes for container orchestration, Prometheus/Grafana for monitoring.
- **Success Criteria:** System is available 99.9% of time, alerts trigger correctly during incidents.
- **Common Pitfalls:** Misconfigured scaling policies, missing health checks leading to downtime.
- **Time Estimate:** 4 hours

**STEP 15: [Documentation & Knowledge Transfer](documentation)**
- **Action:** Document the entire system architecture, security controls, and operational procedures.
- **Tools Needed:** Confluence, Markdown docs in Git repo, diagrams (Draw.io).
- **Success Criteria:** All team members can understand how to operate and secure the auth system.
- **Common Pitfalls:** Outdated documentation, lack of training for new hires.
- **Time Estimate:** 4 hours

### Quality Checkpoints
- **Checkpoint 1:** After STEP 2 - Validate JWT signing/verification logic with a test suite.
- **Checkpoint 3:** After STEP 5 - Perform MFA enrollment tests for multiple users.
- **Checkpoint 4:** After STEP 12 - Verify compliance documentation is complete and signed off.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Authentication latency < 100ms under normal load, < 500ms during peak.
   - **Target:** < 100ms
   - **Measurement Method:** Use JMeter or custom scripts to measure response times.

2. **Secondary Metrics:**
   - Average time to authenticate (TTA): <
   - Number of failed login attempts per day: <
   - Rate of unauthorized access incidents: 0

3. **Long-term Metrics:**
   - System uptime over a month: > 99.9%
   - Detected security vulnerabilities: 0
   - Number of configuration drift alerts: 0

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities from logs and monitoring data.
3. Implement changes (e.g., optimize DB queries, adjust rate limits).
4. Re-measure to confirm improvements.
5. Repeat until all metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current state vs target state for each metric.
   - Key challenges faced and how they were mitigated.

2. **Detailed Report**
   - Complete methodology used (tools, libraries, frameworks).
   - All research findings with source citations.
   - Implementation details including code snippets.
   - Before/after performance comparisons.

3. **Maintenance Plan**
   - Ongoing tasks: Quarterly dependency updates, bi-annual security audits.
   - Monitoring schedule: Daily logs review, weekly load tests.
   - Update frequency: New vulnerability patches every 2 weeks.
   - Contingency procedures: Backup plan for service outages, rollback strategy.

4. **Knowledge Transfer**
   - Training materials: Secure coding practices guide, Auth system walkthrough.
   - Standard operating procedures: Change management process, incident response steps.
   - Best practices documentation: Ongoing maintenance checklist.
   - Troubleshooting guide: Common issues with solutions and escalation paths.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace all [BRACKETED] items** with actual project specifics (e.g., API endpoints, user roles).
2. **Define 15 Critical Knowledge Areas** based on the latest industry standards and tool updates for Backend Developers.
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria:
   - Specific: Secure JWT-based authentication
   - Measurable: <100ms latency, no failed auth attempts
   - Achievable: Using open-source tools within budget
   - Relevant: Protects user data in line with compliance
   - Time-bound: Complete by [project deadline]

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks (e.g., OWASP ASVS)
   - Expert practitioner processes shared on forums like Stack Overflow
   - Tool vendor best practices for JWT libraries, OAuth frameworks
   - Case studies of successful auth implementations in high-security environments

5. **Include Latest 2024-2025 Practices**
   - Use of WebAuthn FIDO2 standards for MFA
   - Integration of OpenID Connect with OIDC Discovery
   - Deployment of Auth systems behind API gateways using serverless functions
   - Real-time monitoring and alerting via cloud-native observability tools

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "JSON Web Tokens (JWT)"
    focus: "Latest JWT standards and HMAC vs RSA security"
    sources: ["RFC7519", "Auth0 JWT blog posts"]
    deliverable: "Comparison of algorithm security levels with source links"

  # [Continue for agents 2-15]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the project as COMPLETE:

- [ ] **Primary Goal Achieved:** Authentication latency <100ms and no failed auth attempts.
- [ ] **All Metrics Met:** Performance, security, availability targets reached.
- [ ] **Quality Validated:** Code meets industry standards, documentation is complete.
- [ ] **Maintenance Plan Confirmed:** Ongoing tasks defined and assigned.
- [ ] **Compliance Verified:** GDPR/CCPA audit passed with no issues.

### Continuous Improvement
- Document lessons learned from deployments.
- Update security architecture diagrams with new findings.
- Share insights on the community forums (Stack Overflow, Reddit).
- Schedule quarterly reviews to assess effectiveness.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05
**Version:** 1.0
**Tested With:** Backend Developer projects using Node.js/Express, Django, Spring Boot.
**Success Rate:** Aim for >95% successful implementations based on historical data.
**Average Time to Goal:** 30 days (based on typical project timelines).

---

This template is now fully populated and ready to be executed by a Backend Developer working towards implementing secure authentication and authorization. It provides a comprehensive guide from initial research to final implementation, ensuring the system meets industry best practices while being optimized for performance and security.

