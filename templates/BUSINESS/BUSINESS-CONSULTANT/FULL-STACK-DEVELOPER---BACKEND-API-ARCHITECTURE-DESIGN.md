# Full Stack Developer - AI Agent Template
## Backend API Architecture Design

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve effective Backend API Architecture Design for a Full Stack Developer.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Full Stack Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Design and implement scalable, secure, and maintainable backend APIs that support seamless integration across frontend components in full stack applications.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Project scope (e.g., [ecommerce platform], [task management system])
   - Format: [URL/Text/Path/etc.]  
   - Validation: Ensure it describes the application domain and user stories.

2. **Input 2:** Current tech stack (e.g., [React, Node.js, MongoDB])
   - Format: []
   - Validation: Verify each component is supported by the API design plan.

3. **Input 3:** Integration requirements (e.g., third-party services like Stripe for payments)
   - Format: []
   - Validation: Confirm compatibility and data exchange formats.

4. **Input 4:** Performance targets (e.g., [API response <200ms])
   - Format: []
   - Validation: Ensure realistic benchmarks based on expected load.

---

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers in the tech stack compatibility.
- [ ] Establish baseline metrics (current API performance, security posture).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**1. API Design Principles**
   - Research Focus: RESTful vs GraphQL design patterns, OpenAPI specification
   - Target Sources: Martin Fowler's Microservices Blog, Apollo Server Documentation
   - Deliverable: Recommended pattern with justification.

**2. Data Modeling for APIs**
   - Research Focus: Best practices for designing schemas that are both efficient and flexible.
   - Target Sources: Database Normalization Guides, Schema Design Patterns
   - Deliverable: Draft database schema aligned with API design.

**3. Security Practices**
   - Research Focus: OWASP Top 10 vulnerabilities in APIs, JWT authentication, rate limiting.
   - Target Sources: OWASP Documentation, Auth0 Best Practices
   - Deliverable: Secure coding guidelines and security headers checklist.

**4. Authentication & Authorization**
   - Research Focus: OAuth2 flow, API keys management, role-based access control (RBAC).
   - Target Sources: Stripe API Docs, JWT.io Benchmarks
   - Deliverable: Auth strategy with recommended libraries (e.g., Passport.js).

**5. Rate Limiting & Throttling**
   - Research Focus: Implementing rate limits to prevent abuse and ensure fair usage.
   - Target Sources: AWS API Gateway Best Practices, Nginx Rate Limiting Configurations
   - Deliverable: Configuration snippets for rate limiting middleware.

**6. Caching Strategies**
   - Research Focus: In-memory vs distributed caching solutions like Redis.
   - Target Sources: Redis Documentation, Memcached Performance Benchmarks
   - Deliverable: Recommended caching strategy with eviction policies.

**7. Asynchronous Processing**
   - Research Focus: Handling long-running tasks via queues (e.g., RabbitMQ).
   - Target Sources: Celery Documentation, AWS SQS Best Practices
   - Deliverable: Queue management plan and message processing workflow.

**8. Monitoring & Logging**
   - Research Focus: Centralized logging solutions like ELK stack.
   - Target Sources: Prometheus/Grafana Dashboards, Elastic Stack Guides
   - Deliverable: Setup for real-time monitoring and alerting.

**9. Deployment Pipelines**
   - Research Focus: CI/CD pipelines using tools like GitHub Actions or GitLab CI.
   - Target Sources: AWS CodePipeline Documentation, Docker Best Practices
   - Deliverable: Automated deployment steps with rollback mechanisms.

**10. Testing Strategies**
    - Research Focus: Unit testing, integration testing for API endpoints, end-to-end tests.
    - Target Sources: Jest Docs, Postman Collection Runner
    - Deliverable: Test suite structure and coverage requirements.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on scalability, security, and maintainability.
4. Create master action plan with milestones for implementation phases.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [API Specification Definition]**
- **Action:** Draft an OpenAPI specification outlining all endpoints, request/response schemas, authentication requirements.
- **Tools Needed:** Swagger Editor (free), Postman API Design
- **Success Criteria:** Document reviewed by team leads and aligned with business requirements.
- **Common Pitfalls:** Over-specifying fields or neglecting versioning.
- **Time Estimate:** 2 days

**STEP 2: [Schema Validation & Testing]**
- **Action:** Implement server-side validation using tools like JSON Schema Validator. Write unit tests for all API endpoints.
- **Tools Needed:** TypeScript, Jest (free), Mocha
- **Success Criteria:** All critical paths pass automated tests with >90% coverage.
- **Common Pitfalls:** Skipping edge case testing or not mocking external services.
- **Time Estimate:** 3 days

**STEP 3: [Backend Service Implementation]**
- **Action:** Develop backend service using chosen framework (e.g., Express.js for Node.js). Implement authentication middleware, rate limiting, and error handling.
- **Tools Needed:** Node.js (free), Axios (for API calls to other services), Passport.js
- **Success Criteria:** Backend passes all integration tests with secure headers in place.
- **Common Pitfalls:** Hardcoding credentials or bypassing security checks for local development.
- **Time Estimate:** 5 days

**STEP 4: [Caching Layer Integration]**
- **Action:** Add caching middleware using Redis. Implement cache invalidation strategies for frequently changed data.
- **Tools Needed:** Redis (free community edition), Node-cache library
- **Success Criteria:** Cache hit ratio >80% and performance metrics meet <200ms target.
- **Common Pitfalls:** Not accounting for cache expiration or not handling write-through scenarios correctly.
- **Time Estimate:** 1 day

**STEP 5: [Security Hardening]**
- **Action:** Implement rate limiting, input validation, and authentication mechanisms. Use WAF (Web Application Firewall) if available.
- **Tools Needed:** Nginx with Limit_req module (free), Fail2Ban
- **Success Criteria:** No successful brute force attacks or injection attempts in the last 30 days.
- **Common Pitfalls:** Overlooking OWASP security headers or not rotating secrets regularly.
- **Time Estimate:** 1 day

**STEP 6: [Monitoring & Alerting Setup]**
- **Action:** Configure monitoring using Prometheus and Grafana. Set up alerts for latency, error rates, and authentication failures.
- **Tools Needed:** Prometheus (free), Grafana Cloud (free tier), Sentry
- **Success Criteria:** All critical metrics are displayed in dashboards and alerts trigger correctly during load tests.
- **Common Pitfalls:** Not defining SLOs or not testing alert routing.
- **Time Estimate:** 1 day

**STEP 7: [Deployment to Staging]**
- **Action:** Containerize the application using Docker. Deploy to a staging environment configured with CI/CD pipeline triggers.
- **Tools Needed:** Docker (free), GitHub Actions, AWS Elastic Beanstalk
- **Success Criteria:** Application passes all automated tests in staging and is reachable at the defined endpoint.
- **Common Pitfalls:** Not validating container images or not testing database migrations on each deploy.
- **Time Estimate:** 2 days

**STEP 8: [User Acceptance Testing (UAT)]**
- **Action:** Conduct UAT with a small group of real users. Collect feedback on performance, usability, and error handling.
- **Tools Needed:** Survey tools like Google Forms, User testing platforms
- **Success Criteria:** >80% of users report no critical issues during 2-week test period.
- **Common Pitfalls:** Not capturing all possible user scenarios or not revisiting design based on feedback.
- **Time Estimate:** 2 weeks

**STEP 9: [Performance Optimization]**
- **Action:** Analyze performance bottlenecks using tools like New Relic or Dynatrace. Optimize database queries, refactor code for efficiency.
- **Tools Needed:** New Relic (free tier), JMeter
- **Success Criteria:** Latency reduced to <200ms and resource usage within budget limits.
- **Common Pitfalls:** Not prioritizing optimizations based on actual performance data.
- **Time Estimate:** 2 days

**STEP 10: [Documentation & Knowledge Transfer]**
- **Action:** Document API specifications, deployment processes, and operational runbooks. Conduct training sessions for the dev team.
- **Tools Needed:** Confluence (free tier), Miro for collaboration boards
- **Success Criteria:** All new developers can onboard within 1 hour without support.
- **Common Pitfalls:** Not updating docs after changes or not practicing with the documentation regularly.
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After Step X - Verify API spec is reviewed and approved by stakeholders.
- **Checkpoint 2:** After Step Y - Validate all unit tests pass and coverage meets target.
- **Checkpoint 3:** After Step Z - Confirm performance metrics in staging align with targets.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** API response time <200ms (target)
   - Target: <200ms for >95% of requests
   - Measurement Method: Use benchmarking tools like JMeter or Artillery.

2. **Secondary Metrics:**
   - Error Rate: <0.5%
     - Measurement Method: Monitor HTTP status codes over 24 hours.
   - Throughput: Handle X concurrent users with no degradation in performance.
     - Measurement Method: Load testing using k6 or Locust.

3. **Long-term Metrics:**
   - Latency Trends: No increase >10% compared to baseline
     - Measurement Method: Weekly monitoring dashboards.
   - Security Incidents: Zero successful attacks
     - Measurement Method: Review security logs and reports monthly.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., slow endpoint, high error rate).
3. Implement changes based on findings.
4. Re-measure to confirm impact.
5. Repeat until all metrics meet the defined thresholds.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state
- Key actions taken (e.g., [implemented GraphQL layer], [added Redis caching])
- Results achieved (e.g., [reduced latency by 40%])

**2. Detailed Report**
- Complete methodology and research findings.
- All code changes, with links to repository branches.
- Before/after performance benchmarks.

**3. Maintenance Plan**
- Ongoing tasks: Weekly security updates, monthly scaling tests
- Monitoring schedule: Daily health checks + weekly load testing
- Update frequency: Quarterly architecture review

**4. Knowledge Transfer**
- Training materials: API usage guide for frontend teams
- Standard operating procedures: Deployment and incident response protocols
- Best practices documentation: OpenAPI spec template and security checklist

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with specific project details.
2. **Define 10-20 Critical Topics** based on the full stack development context (e.g., state management in React, database replication strategies).
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria relevant to backend APIs.

### Research Sub-Agent Configuration

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "API Design Principles"
    focus: "Latest best practices for RESTful vs GraphQL APIs in 2024"
    sources: ["Martin Fowler's Microservices Blog", "Apollo Server Documentation"]
    deliverable: "Recommended pattern with justification and sample spec"

  # Add agents for each critical knowledge area...
```

### Success Validation
- Verify the ultimate goal aligns with project requirements.
- Ensure all metrics are met before declaring success.

---

## TEMPLATE METADATA

**Last Updated:** [Auto-generate date]
**Version:** 1.0  
**Tested With:** [ecommerce, task management]  
**Success Rate:** Track using defined checkpoints and KPIs.

---

