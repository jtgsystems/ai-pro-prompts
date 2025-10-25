# Backend Developer - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Backend Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate (someone new to the role)"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Project scope and requirements for RESTful API development  
   - Format: Detailed documentation or list of endpoints, data models, authentication methods
   - Validation: Must include primary functionality description and user stories

2. **Input 2:** Target platforms (e.g., mobile app, web service)  
   - Format: List of target client applications
   - Validation: Each platform's supported protocols and capabilities documented

3. **Input 3:** Preferred programming language for API development (usually [e.g., Python, Node.js])  
   - Format: Language name
   - Validation: Must be one supported by the project stack

4. **Input 4:** Version control system preference (e.g., Git)  
   - Format: System name
   - Validation: Must support code branching and deployment workflows

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Research Agent Deployment:** Launch 8 parallel sub-agents to research latest practices

**Topic 1:** RESTful API design best practices  
- Research Focus: Naming conventions, versioning strategies, stateless interactions
- Target Sources: RFC 7231, OWASP API Security Guide, Industry blogs
- Deliverable: Design patterns and naming convention guide

**Topic 2:** Popular Backend frameworks for the chosen language (e.g., Express.js for Node.js)  
- Research Focus: Ecosystem maturity, community support, feature set
- Target Sources: Framework documentation, GitHub activity metrics, Stack Overflow trends
- Deliverable: Comparative matrix of top 3 frameworks

**Topic 3:** Authentication and authorization strategies (OAuth2, JWT)  
- Research Focus: Standards compliance, security best practices, implementation complexity
- Target Sources: Security research papers, API security forums
- Deliverable: Recommended auth strategy with code examples

**Topic 4:** Database selection for RESTful services (SQL vs NoSQL)  
- Research Focus: Data modeling fit, performance benchmarks, ecosystem maturity
- Target Sources: DB benchmarking studies, community reviews
- Deliverable: Database comparison chart with suitability analysis

**Topic 5:** API testing tools and methodologies  
- Research Focus: Automated testing frameworks, mocking capabilities, coverage metrics
- Target Sources: Testing blogs, conference recordings, tool documentation
- Deliverable: Recommended test suite with example scripts

**Topic 6:** Monitoring and logging best practices for APIs  
- Research Focus: Metrics to track (latency, errors), tools for real-time monitoring, log aggregation strategies
- Target Sources: Ops research papers, SaaS provider case studies
- Deliverable: Monitoring setup guide with recommended tooling

**Topic 7:** CI/CD pipeline configuration for API projects  
- Research Focus: Build processes, deployment automation, rollback procedures
- Target Sources: DevOps blogs, open-source pipeline examples
- Deliverable: Sample GitHub Actions or Jenkinsfile for API pipelines

**Topic 8:** Containerization and orchestration (Docker/Kubernetes)  
- Research Focus: Benefits of containerizing APIs, best practices for Kubernetes deployment
- Target Sources: Docker documentation, Kubernetes community guides
- Deliverable: Dockerfile template and basic Kubernetes manifest

**Topic 9:** Microservices architecture considerations for RESTful APIs  
- Research Focus: Service boundaries, inter-service communication patterns, data consistency strategies
- Target Sources: Microservices design books, case studies from industry giants
- Deliverable: High-level microservice diagram with API interaction map

**Topic 10:** Emerging technologies impacting RESTful development (GraphQL, OpenAPI)  
- Research Focus: How these technologies can be integrated into existing APIs
- Target Sources: Tech blogs, conference talks
- Deliverable: Integration guide showing before/after code examples

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document covering design, implementation, testing, deployment
2. Identify conflicts or contradictions in best practices and resolve them with prioritized recommendations
3. Create master action plan mapping research insights to development tasks

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Project Setup]**
- **Action:** Initialize project repository, set up version control, create CI/CD pipeline  
- **Tools Needed:** Git (GitHub/GitLab), GitHub Actions/Jenkins for CI/CD, Docker
- **Success Criteria:** Repo cloned locally, build and test workflows pass in CI environment
- **Common Pitfalls:** Incorrect branch configuration, missing environment variables
- **Time Estimate:** 30 minutes

**STEP 2: [API Design]**
- **Action:** Define API endpoints, request/response models using OpenAPI specification  
- **Tools Needed:** Swagger Editor or Redoc, code editor (VS Code)
- **Success Criteria:** Fully documented API spec reviewed and approved
- **Common Pitfalls:** Ambiguous field names, missing error handling
- **Time Estimate:** 2 hours

**STEP 3: [Framework Selection & Setup]**
- **Action:** Choose backend framework based on research, scaffold project structure  
- **Tools Needed:** Selected framework CLI (e.g., `express-generator`), package manager (npm/yarn)
- **Success Criteria:** Project initialized with all dependencies installed
- **Common Pitfalls:** Choosing a framework without considering team expertise
- **Time Estimate:** 1 hour

**STEP 4: [Authentication Implementation]**
- **Action:** Implement JWT-based authentication flow, create middleware for protected routes  
- **Tools Needed:** Auth library (e.g., Passport.js), database for storing tokens
- **Success Criteria:** Users can authenticate and access only authorized endpoints
- **Common Pitfalls:** Token expiration handling, session fixation vulnerabilities
- **Time Estimate:** 3 hours

**STEP 5: [Database Integration]**
- **Action:** Set up database schema based on API models, implement CRUD operations  
- **Tools Needed:** Database client (e.g., Sequelize for Node.js), ORM library
- **Success Criteria:** Endpoints correctly perform create/read/update/delete actions
- **Common Pitfalls:** Data validation issues, race conditions in transactions
- **Time Estimate:** 4 hours

**STEP 6: [API Testing]**
- **Action:** Write automated tests covering all endpoints and edge cases  
- **Tools Needed:** Jest/Mocha for testing framework, Postman for manual testing
- **Success Criteria:** All tests pass, test coverage >80%
- **Common Pitfalls:** Overlooking important edge cases, not maintaining tests as code evolves
- **Time Estimate:** 4 hours

**STEP 7: [Monitoring and Logging Setup]**
- **Action:** Configure monitoring dashboards (e.g., Prometheus + Grafana) and logging to central system  
- **Tools Needed:** Prometheus for metrics collection, Elastic Stack or Splunk for logs
- **Success Criteria:** Real-time visibility into API performance and errors
- **Common Pitfalls:** Missing alerts for critical failures, log data loss
- **Time Estimate:** 2 hours

**STEP 8: [Deployment to Production]**
- **Action:** Push code to production environment via CI/CD pipeline, configure serverless functions if needed  
- **Tools Needed:** Docker for containerization, Kubernetes or AWS ECS for orchestration, API Gateway
- **Success Criteria:** API fully operational in production with zero downtime
- **Common Pitfalls:** Environment variable mismatches, port conflicts
- **Time Estimate:** 2 hours

**STEP 9: [Documentation and Handover]**
- **Action:** Update README with usage instructions, generate API docs using Redoc/Swagger  
- **Tools Needed:** Markdown editor, Swagger UI or Redoc
- **Success Criteria:** All developers can understand how to use the API and its limits
- **Common Pitfalls:** Outdated documentation, missing authentication details
- **Time Estimate:** 1 hour

**STEP 10: [Post-Live Review]**
- **Action:** Monitor API performance for first 24 hours, collect feedback from users  
- **Tools Needed:** Monitoring dashboards, user feedback tools (e.g., SurveyMonkey)
- **Success Criteria:** No critical errors detected, positive feedback on functionality
- **Common Pitfalls:** Ignoring early issues that surface in production
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify API spec documents are reviewed and approved by team lead
- **Checkpoint 2:** [After Step Y] - Validate all tests pass and coverage metrics meet threshold
- **Checkpoint 3:** [After Step Z] - Confirm monitoring dashboards show no critical anomalies

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** API response time <200ms for 99% of requests  
   - Target: ≤200ms
   - Measurement Method: APM tools (Datadog, New Relic) or Prometheus metrics

2. **Secondary Metrics:**  
   - Error rate <0.5% across all endpoints  
     - Target: ≤0.5%
     - Measurement Method: Monitoring dashboards for error counts
   - Throughput >10k requests/second during peak load testing  
     - Target: ≥10k rps
     - Measurement Method: Load testing tools (k6, JMeter)

### Iterative Improvement Loop
1. Measure current performance against targets at the end of each sprint
2. Identify top 3 areas for improvement based on metrics
3. Implement changes (e.g., caching layer, database indexing)
4. Re-measure to confirm improvements
5. Repeat until all primary and secondary metrics are met

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current state vs. target state for API performance and functionality
- [ ] Key actions taken during development cycle
- [ ] Results achieved from testing and monitoring phases
- [ ] ROI or impact metrics (e.g., reduced latency by X%)

**2. Detailed Report**
- [ ] Complete methodology document with links to all research artifacts
- [ ] All code repositories with commit history showing progress
- [ ] API design documents and version control changes
- [ ] Test coverage reports and monitoring dashboards snapshots

**3. Maintenance Plan**
- [ ] Ongoing tasks: Weekly performance reviews, monthly security audits
- [ ] Monitoring schedule: Grafana dashboard alerts configured for error rates >0.5%
- [ ] Update frequency: API documentation regenerated after any breaking change
- [ ] Contingency procedures: Step-by-step rollback plan in case of critical failures

**4. Knowledge Transfer**
- [ ] Training materials: Short video walkthroughs for onboarding new team members
- [ ] Standard operating procedures: Documented deployment process and incident response steps
- [ ] Best practices documentation: API design patterns and security recommendations
- [ ] Troubleshooting guide: Common issues encountered during development and resolution

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content  
   - Example: Replace "Project scope" with "Specific domain knowledge required for API (e.g., Finance, Healthcare)"

2. **Define 10-20 Critical Topics** based on:
   - Industry standards and certifications relevant to backend development
   - Latest trends in cloud computing, containerization, and microservices architecture
   - Regulatory requirements if the API handles sensitive data
   - Tool and platform updates (e.g., new versions of Node.js, Docker)
   - Methodology innovations like DevOps practices

3. **Map Ultimate Goal to Measurable Outcomes**  
   - Use SMART criteria: For instance, "Develop a RESTful API that processes 10k requests/second with <200ms latency and zero critical errors"

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks for building scalable backend systems
   - Expert practitioner processes for version control in microservices architectures
   - Tool vendor best practices (e.g., GitHub Actions CI workflows)
   - Case studies of successful RESTful API deployments

5. **Include Latest 2024-2025 Practices**  
   - AI/ML integration: Implementing API endpoints that utilize machine learning models
   - Automation possibilities: Using serverless functions for specific operations to reduce cost and complexity
   - New tool capabilities: Leveraging GraphQL for more efficient data fetching in certain projects

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 8
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "RESTful API design best practices"
    focus: "Naming conventions, versioning strategies, stateless interactions"
    sources: ["RFC 7231", "OWASP API Security Guide"]
    deliverable: "Design patterns and naming convention guide"

  - agent_id: 2
    topic: "Popular Backend frameworks for chosen language"
    focus: "Ecosystem maturity, community support, feature set"
    sources: ["GitHub activity metrics", "Stack Overflow trends"]
    deliverable: "Comparative matrix of top 3 frameworks"

  - agent_id: 3
    topic: "Authentication and authorization strategies"
    focus: "Standards compliance, security best practices, implementation complexity"
    sources: ["Security research papers"]
    deliverable: "Recommended auth strategy with code examples"

  - agent_id: 4
    topic: "Database selection for RESTful services"
    focus: "Data modeling fit, performance benchmarks, ecosystem maturity"
    sources: ["DB benchmarking studies", "Community reviews"]
    deliverable: "Database comparison chart with suitability analysis"

  - agent_id: 5
    topic: "API testing tools and methodologies"
    focus: "Automated testing frameworks, mocking capabilities, coverage metrics"
    sources: ["Testing blogs", "Conference recordings"]
    deliverable: "Recommended test suite with example scripts"

  - agent_id: 6
    topic: "Monitoring and logging best practices for APIs"
    focus: "Metrics to track (latency, errors), tools for real-time monitoring, log aggregation strategies"
    sources: ["Ops research papers", "SaaS provider case studies"]
    deliverable: "Monitoring setup guide with recommended tooling"

  - agent_id: 7
    topic: "CI/CD pipeline configuration for API projects"
    focus: "Build processes, deployment automation, rollback procedures"
    sources: ["DevOps blogs", "Open-source pipeline examples"]
    deliverable: "Sample GitHub Actions or Jenkinsfile for API pipelines"

  - agent_id: 8
    topic: "Containerization and orchestration (Docker/Kubernetes)"
    focus: "Benefits of containerizing APIs, best practices for Kubernetes deployment"
    sources: ["Docker documentation", "Kubernetes community guides"]
    deliverable: "Dockerfile template and basic Kubernetes manifest

---

## SUCCESS VALIDATION

### Final Checklist
Before marking profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [API fully functional, meets all performance and security requirements]
- [ ] **All Metrics Met?** [Latency <200ms for 99% of requests, error rate <0.5%, throughput >10k rps]
- [ ] **Quality Validated?** [Code passes all tests with coverage >80%, documentation is up-to-date]
- [ ] **Documentation Complete?** [All deliverables (design docs, testing plan, monitoring setup) are documented and accessible]
- [ ] **Sustainability Ensured?** [Maintenance plan includes regular performance reviews and updates to security patches]

### Continuous Improvement
- Document lessons learned from the development process
- Update the template with new best practices identified during implementation
- Share knowledge gained with the team through training sessions
- Schedule a review meeting after 6 months to assess ongoing compliance

