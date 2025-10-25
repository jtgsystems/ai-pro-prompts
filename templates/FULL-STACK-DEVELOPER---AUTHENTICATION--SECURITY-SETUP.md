# Full Stack Developer - AI Agent Template
## Authentication & Security Setup

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve robust authentication and security setup for a full stack developer.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Full Stack Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Establish a secure, scalable, and user-friendly authentication system that meets industry standards for a full stack application.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Input 1:** Project requirements document URL or path.
2. **Input 2:** List of authorized users (with roles).
3. **Input 3:** Database schema and connection details.
4. **Input 4:** Hosting platform type (e.g., AWS, Heroku).
5. **Input 5:** Existing security measures in place.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (10-20 Topics)
**Topic 1:** Authentication Frameworks  
   - Research Focus: Latest frameworks for implementing authentication (e.g., OAuth, JWT).
   - Target Sources: Auth0 blog, MDN Web Docs.
   - Deliverable: List of recommended libraries with use cases.

**Topic 2:** Security Best Practices  
   - Research Focus: OWASP Top 10 recommendations, encryption standards.
   - Target Sources: OWASP documentation, NIST guidelines.
   - Deliverable: Checklist of security measures.

**Topic 3:** Role-Based Access Control (RBAC)  
   - Research Focus: Implementing RBAC in front-end and back-end systems.
   - Target Sources: Security blogs, GitHub repositories for RBAC examples.
   - Deliverable: Implementation strategy with code snippets.

**Topic 4:** Data Encryption Techniques  
   - Research Focus: Encrypting sensitive data at rest and in transit.
   - Target Sources: OpenSSL documentation, security-focused articles.
   - Deliverable: Recommended encryption algorithms and libraries.

**Topic 5:** Secure API Development  
   - Research Focus: Best practices for building secure APIs (e.g., rate limiting, CORS).
   - Target Sources: Node.js API guides, AWS API Gateway best practices.
   - Deliverable: Secure API design principles.

**Topic 6:** Multi-Factor Authentication (MFA)  
   - Research Focus: Implementing MFA using TOTP or SMS-based systems.
   - Target Sources: Auth0 tutorials, Duo Security documentation.
   - Deliverable: Recommended libraries and implementation steps.

**Topic 7:** Session Management  
   - Research Focus: Secure session handling for user sessions.
   - Target Sources: Express.js documentation, cookie security guides.
   - Deliverable: Best practices for managing active sessions.

**Topic 8:** Dependency Management & Updates  
   - Research Focus: Keeping all project dependencies secure and up-to-date.
   - Target Sources: npm audit reports, Snyk vulnerability alerts.
   - Deliverable: Automated dependency update process.

**Topic 9:** Logging and Monitoring Tools  
   - Research Focus: Implementing logging solutions for security events.
   - Target Sources: ELK Stack documentation, Splunk tutorials.
   - Deliverable: Recommended tools for real-time monitoring of security incidents.

**Topic 10:** Compliance Requirements  
   - Research Focus: GDPR, CCPA, PCI DSS compliance for authentication systems.
   - Target Sources: Legal databases, industry articles.
   - Deliverable: Checklist of compliance requirements and implementation steps.

#### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on security posture.
4. Create a master action plan for implementation.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process
**STEP 1: [Foundation Setup]**
- **Action:** Design the authentication architecture based on research findings (e.g., OAuth2 with JWT).
- **Tools Needed:** Visual Studio Code, Git, Docker.
- **Success Criteria:** Architecture diagram approved by stakeholders and documented in a README file.
- **Common Pitfalls:** Inadequate documentation or misaligned stakeholder expectations.
- **Time Estimate:** 5 days.

**STEP 2: [Back-end Implementation]**
- **Action:** Implement authentication logic using Node.js/Express with Passport.js for OAuth2 and JWT.
- **Tools Needed:** Express, Passport.js, MongoDB (for user data), bcrypt for hashing passwords.
- **Success Criteria:** Successful login functionality implemented and tested across all environments.
- **Common Pitfalls:** Improper handling of session management leading to security vulnerabilities.
- **Time Estimate:** 7 days.

**STEP 3: [Front-end Integration]**
- **Action:** Develop the front-end authentication UI (login, registration forms) using React or Angular.
- **Tools Needed:** React/Angular CLI, Bootstrap for styling, Formik/Radix UI for form handling.
- **Success Criteria:** Secure login/logout flows implemented with responsive design across devices.
- **Common Pitfalls:** Insecure input validation leading to XSS attacks.
- **Time Estimate:** 7 days.

**STEP 4: [Security Hardening]**
- **Action:** Implement MFA using TOTP, enable HTTPS everywhere, and configure rate limiting on API endpoints.
- **Tools Needed:** Google Authenticator integration library (e.g., node-google-authenticator), SSL certificates (Let's Encrypt).
- **Success Criteria:** Security tests pass without vulnerabilities flagged; all data transmitted over TLS.
- **Common Pitfalls:** Misconfigured certificates leading to mixed content warnings.
- **Time Estimate:** 3 days.

**STEP 5: [Testing & Validation]**
- **Action:** Conduct thorough security testing (penetration, fuzzing) and user acceptance testing.
- **Tools Needed:** OWASP ZAP for automated scanning, Burp Suite for manual testing, JMeter for load testing.
- **Success Criteria:** All critical vulnerabilities mitigated; system passes compliance audits.
- **Common Pitfalls:** Overlooking edge cases in authentication flows leading to bypass vulnerabilities.
- **Time Estimate:** 5 days.

**STEP 6: [Deployment & Monitoring]**
- **Action:** Deploy the application securely using Docker Compose and configure monitoring/logging with Prometheus/Grafana.
- **Tools Needed:** AWS CodeDeploy, Kubernetes for orchestration, Sentry/Datadog for real-time alerts.
- **Success Criteria:** System monitored in production without alert fatigue; deployment pipelines automated.
- **Common Pitfalls:** Inadequate logging leading to delayed incident response.
- **Time Estimate:** 3 days.

**STEP 7: [Documentation & Training]**
- **Action:** Document the authentication process, security policies, and maintenance procedures for future developers.
- **Tools Needed:** Confluence for wikis, Markdown files in repo, Google Meet for training sessions.
- **Success Criteria:** Documentation reviewed and approved by senior team members; at least one onboarding session conducted.
- **Common Pitfalls:** Outdated documentation leading to security misconfigurations.
- **Time Estimate:** 3 days.

#### Quality Checkpoints
- **Checkpoint 1:** After Step X - Verify architecture diagram aligns with design specifications.
- **Checkpoint 2:** After Step Y - Validate login/logout functionality works securely across all environments.
- **Checkpoint 3:** After Step Z - Confirm security tests pass without critical findings.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:
1. **Primary Metric:** Percentage of users successfully authenticated per session (target >95%).
2. **Secondary Metrics:**
   - Mean Time to Detect (MTTD) security incidents.
   - Mean Time to Respond (MTTR) to identified vulnerabilities.
3. **Long-term Metrics:**
   - Annual compliance audit score.

#### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities each quarter.
3. Implement changes such as adding new MFA options or updating encryption algorithms.
4. Re-measure and document improvements.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
**1. Executive Summary**
- [ ] Current state vs. target state.
- [ ] Key actions taken to achieve secure authentication.
- [ ] Results achieved in security tests and compliance audits.
- [ ] ROI or impact metrics on user trust and system uptime.

**2. Detailed Report**
- [ ] Complete methodology used for implementation.
- [ ] All research findings with source citations.
- [ ] Implementation details including code snippets and configuration files.
- [ ] Before/after comparisons of security posture.

**3. Maintenance Plan**
- [ ] Ongoing tasks such as dependency updates, security patching, and user feedback collection.
- [ ] Monitoring schedule (e.g., weekly penetration tests).
- [ ] Update frequency for documentation and training sessions.
- [ ] Contingency procedures for emergency rollbacks or data breaches.

**4. Knowledge Transfer**
- [ ] Training materials in the form of workshops and cheat sheets for new developers.
- [ ] Standard operating procedures documented in Confluence.
- [ ] Best practices documentation published as part of internal wiki.
- [ ] Troubleshooting guide covering common issues like session timeouts and password resets.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE
1. **Replace all [BRACKETED] items** with specific project details or preferences.
2. **Define 10-20 Critical Topics** based on the latest trends, tools, and regulatory requirements in full stack development.
3. **Map Ultimate Goal to Measurable Outcomes:** Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) to define success metrics for authentication security.

### PHASE 1: INFORMATION GATHERING
- Gather project scope, user roles, data sensitivity levels, and compliance requirements from stakeholders.
- Validate existing infrastructure capabilities to support new security measures without downtime.

### PHASE 2: RESEARCH & ANALYSIS
- Analyze the latest frameworks and libraries for implementing OAuth2, JWT, and MFA in JavaScript environments using tools like Passport.js and Google Authenticator.
- Compare different encryption methods (AES vs. RSA) suitable for encrypting sensitive data at rest in MongoDB databases.

### PHASE 3: EXECUTION WORKFLOW
1. **Foundation Setup:** Document the architecture diagram showing where authentication occurs across front-end and back-end components.
2. **Back-end Implementation:** Use Express.js with Passport.js to handle user login/logout flows securely, ensuring passwords are hashed using bcrypt before storing them in MongoDB.
3. **Frontend Integration:** Implement responsive login forms in React that validate inputs against a backend API call for authentication status.

### PHASE 4: OPTIMIZATION & REFINEMENT
- Conduct regular penetration tests with OWASP ZAP to identify vulnerabilities introduced over time.
- Update documentation after each major release or security incident to maintain transparency and compliance.

### PHASE 5: REPORTING & DOCUMENTATION
- Provide executive summaries for management on the current state of authentication security versus industry standards.
- Share detailed reports including code changes, test results from OWASP ZAP scans, and lessons learned during deployments.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Authentication Frameworks]"
    focus: "Latest authentication frameworks and libraries for full stack development"
    sources: ["Auth0 blog", "MDN Web Docs"]
    deliverable: "List of recommended libraries with use cases"

  - agent_id: 2
    topic: "[Security Best Practices]"
    focus: "OWASP Top 10 recommendations and encryption standards"
    sources: ["OWASP documentation", "NIST guidelines"]
    deliverable: "Checklist of security measures to implement"

  # [Continue for agents 3-10]
```

---

### SUCCESS VALIDATION
Before marking this task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Authentication is secure, scalable, and meets industry standards.
- [ ] **All Metrics Met?** Security tests pass without critical findings; compliance audits are successful.
- [ ] **Quality Validated?** All code passes security scans (e.g., ESLint with security plugins), documentation is up-to-date.
- [ ] **Documentation Complete?** All steps, decisions, and configurations are documented in the repository README and Confluence pages.

### Continuous Improvement
- Document lessons learned from each phase of development for future reference.
- Update this template annually to reflect new best practices or changes in regulations.
- Share findings with the developer community through blog posts or webinars.

