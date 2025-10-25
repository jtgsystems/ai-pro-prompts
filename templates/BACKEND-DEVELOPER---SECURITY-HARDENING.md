# Backend Developer - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Backend Developer"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

---

## PHASE 1: INFORMATION GATHERING

**Required Inputs**
```yaml
- target_platform: [e.g., Cloud, On-Premise]
- deployment_environment: [e.g., AWS, Azure, Kubernetes]
- security_standards: [e.g., OWASP, CIS, GDPR]
- existing_security_controls: []
```

**Initial Assessment Checklist**
```markdown
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers
- [ ] Establish baseline metrics (current state)
```

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Container Security Practices
- **Research Focus:** Best practices for securing Docker/Kubernetes environments, image scanning, secret management
- **Target Sources:** Docker security guide, Kubernetes CIS benchmarks, Trivy documentation
- **Deliverable:** Secure container deployment checklist

**Topic 2:** API Hardening Techniques
- **Research Focus:** OWASP Top 10 API vulnerabilities, rate limiting, authentication mechanisms (OAuth2/JWT)
- **Target Sources:** OWASP API Cheat Sheet, Auth0 blog, JWT security guidelines
- **Deliverable:** API hardening checklist and code examples

**Topic 3:** Serverless Security Risks
- **Research Focus:** Cold start attacks, function execution vulnerabilities, permission creep in AWS Lambda/CFN
- **Target Sources:** Serverless Framework best practices, AWS Well-Architected Tool
- **Deliverable:** Serverless security audit template

**Topic 4:** Database Hardening Strategies
- **Research Focus:** SQL injection prevention, least privilege access for DB users, encrypted storage (TLS)
- **Target Sources:** PostgreSQL security guide, OWASP SQL Injection Prevention Cheat Sheet
- **Deliverable:** Database hardening checklist with configuration examples

**Topic 5:** Logging and Monitoring Standards
- **Research Focus:** Centralized logging architecture, log encryption at rest/in transit, alerting best practices
- **Target Sources:** ELK Stack documentation, Splunk best practices guide
- **Deliverable:** Logging and monitoring implementation plan

**Topic 6:** Dependency Management Security
- **Research Focus:** Vulnerability scanning for third-party libraries, using tools like Snyk or Dependabot
- **Target Sources:** OWASP Dependency Check guide, GitHub Dependabot documentation
- **Deliverable:** Automated dependency vulnerability management workflow

**Topic 7:** Identity and Access Management (IAM)
- **Research Focus:** Role-based access control, least privilege principles, multi-factor authentication
- **Target Sources:** AWS IAM best practices, Azure AD security guide
- **Deliverable:** IAM policy template for secure backend deployment

**Topic 8:** Encryption Practices
- **Research Focus:** Data at rest encryption, TLS/SSL implementation for APIs and services
- **Target Sources:** OpenSSL documentation, Let's Encrypt guide
- **Deliverable:** End-to-end encryption strategy document

**Topic 9:** Secure Coding Standards
- **Research Focus:** OWASP Secure Coding Practices, input validation, output encoding
- **Target Sources:** OWASP Cheat Sheet Series, secure coding guidelines for Java/Node.js/etc.
- **Deliverable:** Secure code review checklist and automated static analysis config

**Topic 10:** Threat Modeling Techniques
- **Research Focus:** STRIDE threat modeling methodology, identifying vulnerabilities in backend architecture
- **Target Sources:** NIST Cybersecurity Framework, OWASP Threat Modeling guide
- **Deliverable:** Threat model diagram and associated mitigation plan

**Topic 11:** Incident Response Planning
- **Research Focus:** Developing a response playbook for security incidents affecting the backend system
- **Target Sources:** SANS incident response framework, CIS Critical Security Controls
- **Deliverable:** Incident response procedure document with roles/responsibilities

**Topic 12:** Compliance and Auditing Procedures
- **Research Focus:** Ensuring compliance with relevant standards (e.g., PCI DSS, HIPAA) and audit requirements
- **Target Sources:** Relevant regulatory guidelines, SOC 2 audit checklist
- **Deliverable:** Compliance matrix and audit readiness documentation

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Container Image Hardening**
```markdown
- **Action:** Scan Docker images with Trivy for vulnerabilities
- **Tools Needed:** Trivy (free), Docker CLI
- **Success Criteria:** All critical/high vulnerabilities mitigated or patched
- **Common Pitfalls:** Ignoring CVEs marked as "unfixed" despite no current exploitation evidence
- **Time Estimate:** 30 minutes per image scan
```

**STEP 2: API Gateway Configuration**
```markdown
- **Action:** Implement rate limiting and authentication at the API gateway layer using Kong or AWS API Gateway
- **Tools Needed:** Kong (free), AWS Console, JWT library for Node.js/Java/etc.
- **Success Criteria:** Rate limit policies enforced without affecting legitimate traffic; 99.9% successful authentications
- **Common Pitfalls:** Overly permissive rate limits leading to DoS vulnerabilities
- **Time Estimate:** 1 hour for initial configuration
```

**STEP 3: Serverless Function Hardening**
```markdown
- **Action:** Enable least privilege IAM roles and implement function invocation logging
- **Tools Needed:** AWS Lambda console, CloudWatch Logs, AWS IAM Access Analyzer
- **Success Criteria:** Functions only access required resources; all executions logged and monitored
- **Common Pitfalls:** Using default execution roles with overly broad permissions
- **Time Estimate:** 2 hours for configuration of multiple functions
```

**STEP 4: Database Security Configuration**
```markdown
- **Action:** Enforce TLS encryption, restrict network access to DB instances
- **Tools Needed:** AWS RDS console, PgBouncer or similar connection pooling tool
- **Success Criteria:** All connections to DB enforce TLS; only authorized IPs can reach DB ports
- **Common Pitfalls:** Leaving default open ports without firewall rules
- **Time Estimate:** 1 hour per database instance
```

**STEP 5: Dependency Scanning and Updates**
```markdown
- **Action:** Run Snyk or Dependabot scans weekly; automatically create PRs for CVE fixes
- **Tools Needed:** Snyk (free tier), Dependabot (GitHub Actions)
- **Success Criteria:** No critical vulnerabilities in dependencies; all security patches applied within 24 hours
- **Common Pitfalls:** Ignoring low-severity alerts that later become high-risk
- **Time Estimate:** Ongoing - automated, but initial setup requires 2 hours
```

**STEP 6: IAM Policy Review and Restructuring**
```markdown
- **Action:** Conduct a full review of IAM policies to ensure least privilege is enforced
- **Tools Needed:** AWS IAM Access Analyzer, IAM Policy Simulator
- **Success Criteria:** No overly permissive policies; all roles/services have only required permissions
- **Common Pitfalls:** Missing implicit permissions granted through group memberships
- **Time Estimate:** 4 hours for a typical backend stack
```

**STEP 7: Logging and Monitoring Setup**
```markdown
- **Action:** Implement centralized logging with ELK/EFK stack; configure alerting for anomalous patterns
- **Tools Needed:** Docker/Elasticsearch, Logstash/Kibana/Frontend, Prometheus/Grafana for metrics
- **Success Criteria:** All logs forwarded to central store; alerts fire correctly in test scenarios
- **Common Pitfalls:** Logs not being shipped due to network/firewall misconfigurations
- **Time Estimate:** 2 days setup, ongoing maintenance
```

**STEP 8: Secure Coding Practices Enforcement**
```markdown
- **Action:** Integrate SAST tools (e.g., SonarQube) into CI/CD pipeline; enforce secure coding guidelines
- **Tools Needed:** SonarQube (free community edition), GitHub Actions/GitLab CI, ESLint with security plugins
- **Success Criteria:** No critical/static analysis issues in production code; 100% of PRs must pass SAST check
- **Common Pitfalls:** Skipping SAST for hotfixes or emergency releases
- **Time Estimate:** Continuous - initial setup takes 2 days
```

**STEP 9: Threat Modeling Exercise**
```markdown
- **Action:** Conduct a STRIDE threat model on the current backend architecture
- **Tools Needed:** Threat modeling tool (e.g., PASTA), whiteboard or digital collaboration platform
- **Success Criteria:** All identified threats have corresponding mitigations; risk rating low for all high-risk items
- **Common Pitfalls:** Assuming third-party services are secure without verification
- **Time Estimate:** 4 hours initial model, ongoing updates
```

**STEP 10: Incident Response Drills**
```markdown
- **Action:** Perform tabletop exercises simulating security incidents; review and update response plan
- **Tools Needed:** Confluence or similar documentation platform for playbook
- **Success Criteria:** All team members can execute the incident response steps within defined timeframes
- **Common Pitfalls:** Incomplete playbooks or unclear ownership of tasks
- **Time Estimate:** 2 hours per drill, monthly review
```

**STEP 11: Compliance and Audit Readiness**
```markdown
- **Action:** Verify all security controls align with PCI DSS/HIPAA requirements; conduct a mock audit
- **Tools Needed:** Checkmarx for compliance scanning, internal audit checklist
- **Success Criteria:** All compliance gaps identified and remediated; audit score 90% or higher
- **Common Pitfalls:** Misinterpreting regulatory language leading to incomplete controls
- **Time Estimate:** Ongoing - initial gap analysis takes 3 days
```

**STEP 12: Documentation and Knowledge Transfer**
```markdown
- **Action:** Document all security configurations, policies, and procedures; train team members
- **Tools Needed:** Confluence or Notion for documentation, Zoom/Teams for training sessions
- **Success Criteria:** All security processes are documented in central repository; at least 80% of team can explain each process
- **Common Pitfalls:** Documentation not updated when changes occur
- **Time Estimate:** Ongoing - initial documentation takes 4 days
```

---

## PHASE 4: OPTIMIZATION & REFINEMENT

**Performance Metrics**
```markdown
1. **Primary Metric:** No critical vulnerabilities detected in 3 consecutive scans (Trivy, Snyk)
   - Target: 0
   - Measurement Method: Automated vulnerability scanning reports weekly

2. **Secondary Metrics:**
   - [ ] Percentage of logs ingested into central system: 100%
   - [ ] Average time to detect and respond to security incidents: <1 hour
   - [ ] Compliance score (PCI DSS/HIPAA): 95% or higher
```

**Iterative Improvement Loop**
```markdown
1. Measure current performance against targets
2. Identify top 3 improvement opportunities (e.g., missing logs, unpatched deps)
3. Implement changes in next sprint (e.g., add logging for new service)
4. Re-measure until all metrics meet targets
```

---

## PHASE 5: REPORTING & DOCUMENTATION

**Deliverables**
```markdown
1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken
   - Results achieved (e.g., number of critical vulnerabilities mitigated)

2. **Detailed Report**
   - Complete methodology used for security hardening
   - All research findings, including links to source documents
   - Implementation details for each step
   - Before/after metrics demonstrating improvement

3. **Maintenance Plan**
   - Ongoing tasks (e.g., weekly scans, monthly audits)
   - Monitoring schedule (e.g., Grafana dashboards showing security metrics)
   - Update frequency of documentation and playbooks

4. **Knowledge Transfer**
   - Training materials for team on new security practices
   - SOPs for handling security incidents
   - Best practices document stored in version-controlled repo
```

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Container Security Practices"
    focus: "Latest 2024-2025 best practices for Docker/Kubernetes security"
    sources: ["Docker documentation", "Kubernetes CIS benchmarks", "Trivy user guide"]
    deliverable: "Secure container deployment checklist with scanning tools"

  - agent_id: 2
    topic: "API Hardening Techniques"
    focus: "OWASP Top 10 API vulnerabilities and mitigation strategies"
    sources: ["OWASP API Cheat Sheet", "Auth0 blog on API security", "JWT documentation"]
    deliverable: "API hardening checklist with code examples for rate limiting and auth"

  # [Continue for agents 3-12]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency across topics
  3. Resolve conflicts by checking multiple authoritative sources (e.g., OWASP > NIST)
  4. Prioritize recommendations based on risk impact and implementation effort
  5. Generate unified security hardening recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this template COMPLETE:

- [ ] **Ultimate Goal Achieved?** The backend system has been hardened to industry best practices with no critical vulnerabilities detected.
- [ ] **All Metrics Met?** All defined performance metrics (vulnerability detection, response time, compliance score) are met or exceeded.
- [ ] **Quality Validated?** Code reviews and security testing show all recommended practices are implemented.
- [ ] **Documentation Complete?** All policies, procedures, and training materials are stored in version control and accessible to the team.
- [ ] **Sustainability Ensured?** A maintenance plan is in place with defined ownership for ongoing compliance and updates.

### Continuous Improvement
- Document lessons learned from the hardening process
- Update the template annually with new best practices (e.g., AI-powered threat detection)
- Share findings with the broader security community to promote industry-wide improvements

---

