# Full Stack Developer - AI Agent Template

## API Documentation

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve comprehensive API documentation for a Full Stack Developer.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Full Stack Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate (someone new to the role)"
```

### Ultimate Goal
**Primary Objective:**  
Create comprehensive, user-friendly API documentation for a web application that is easy to understand and maintain, with measurable success criteria in terms of accessibility, usability, and adherence to best practices.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Input 1:** Project scope and objectives (e.g., `/api/v1/users`, `/api/v1/products`)  
   - Format: URLs or API endpoint list  
   - Validation: Ensure endpoints are correctly formatted and exist in the codebase.

2. **Input 2:** Target audience for documentation (e.g., developers, external partners)  
   - Format: Description or role  
   - Validation: Confirm understanding of who will use the docs.

3. **Input 3:** Preferred documentation format (e.g., Markdown, Swagger/OpenAPI)  
   - Format: Format name  
   - Validation: Ensure compatibility with tools used in development.

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (12)

1. **Core API Design Principles**
   - Research Focus: RESTful design, versioning strategies
   - Target Sources: Martin Fowler's microsite on APIs, official OpenAPI spec documentation
   - Deliverable: Key principles with examples.

2. **Documentation Tools and Standards**
   - Research Focus: Swagger/OpenAPI specifications, Docusaurus (for React-based docs), MkDocs
   - Target Sources: Official documentation sites, community forums like Stack Overflow, GitHub repositories
   - Deliverable: Comparison table of tools.

3. **Version Control Best Practices**
   - Research Focus: Git workflows for API changes, branch strategies
   - Target Sources: Pro Git book, Git best practices guides
   - Deliverable: Recommended branching model and commit message standards.

4. **API Security Standards**
   - Research Focus: OAuth 2.0, JWT handling, CORS policies
   - Target Sources: OWASP Top 10, security blogs
   - Deliverable: Checklist of security recommendations.

5. **Testing Strategies for APIs**
   - Research Focus: Unit testing, integration testing, mocking with tools like Postman and Newman
   - Target Sources: Testing blogs, API testing frameworks documentation
   - Deliverable: Recommended test suite structure.

6. **Documentation Generation and Deployment**
   - Research Focus: Static site generators (e.g., Docusaurus), CI/CD pipelines for docs
   - Target Sources: Docs-related GitHub actions, AWS Amplify guides
   - Deliverable: Process flowchart of generating and deploying docs.

7. **Performance Optimization Techniques**
   - Research Focus: Caching strategies, rate limiting, response time improvements
   - Target Sources: Performance blogs, HTTP/2 specifications
   - Deliverable: List of optimization practices with implementation steps.

8. **Error Handling and Response Design**
   - Research Focus: Best error codes (4xx vs 5xx), structured error responses
   - Target Sources: API design blogs, RFCs for JSON error formats
   - Deliverable: Error handling guidelines document.

9. **Internationalization (i18n) Support**
   - Research Focus: Language localization best practices, locale support in APIs
   - Target Sources: Localization forums, i18n libraries documentation
   - Deliverable: Guidelines for adding language support.

10. **API Monitoring and Logging Standards**
    - Research Focus: Tools like Prometheus, ELK stack for monitoring; structured logging formats
    - Target Sources: DevOps blogs, security incident response guides
    - Deliverable: Monitoring setup guide.

11. **Accessibility in API Documentation**
    - Research Focus: WCAG compliance for web content, user experience best practices
    - Target Sources: WebAIM guidelines, UX research papers
    - Deliverable: Accessibility checklist.

12. **Future-Proofing and Scalability Considerations**
    - Research Focus: Microservices architecture, cloud-native scaling strategies
    - Target Sources: Cloud provider docs (AWS, GCP), microservices patterns books
    - Deliverable: Recommendations for scalable API design.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [API Endpoint Inventory]**
- **Action:** Generate a list of all active API endpoints from the codebase using tools like `swagger-parser` or similar scripts.
- **Tools Needed:** Swagger parser, grep for regex patterns in source files, any scripting language (e.g., Python).
- **Success Criteria:** A complete and accurate inventory of all current API endpoints is created.
- **Common Pitfalls:** Missing undocumented internal routes; overwriting production code.
- **Time Estimate:** 2 hours

**STEP 2: [Endpoint Classification]**
- **Action:** Classify each endpoint into CRUD operations, resource groups (e.g., users, products), and versioned APIs.
- **Tools Needed:** Swagger UI for browsing endpoints, tagging tools in the documentation system.
- **Success Criteria:** Each endpoint is labeled with its purpose and version number.
- **Common Pitfalls:** Mislabeling or missing classification of async operations.
- **Time Estimate:** 4 hours

**STEP 3: [Schema Extraction]**
- **Action:** Use `swagger-parser` to extract OpenAPI specifications for each endpoint, focusing on request/response schemas, authentication methods, and error codes.
- **Tools Needed:** Swagger parser CLI, VS Code with OpenAPI extension.
- **Success Criteria:** All endpoints have corresponding OpenAPI `.yaml/.json` files.
- **Common Pitfalls:** Incomplete schema extraction due to complex data structures or custom logic.
- **Time Estimate:** 6 hours

**STEP 4: [Documentation Generation]**
- **Action:** Convert the extracted schemas into human-readable documentation using a tool like Swagger UI, Redoc, or Docusaurus.
- **Tools Needed:** Docusaurus (or MkDocs for Markdown), OpenAPI-to-Docs converters, CI pipeline integration.
- **Success Criteria:** A fully rendered documentation site is available at `http://localhost:XXXXX/docs`.
- **Common Pitfalls:** CSS formatting issues, broken links due to incomplete schema data.
- **Time Estimate:** 8 hours

**STEP 5: [Review and Validation]**
- **Action:** Conduct a thorough review of the generated documentation with developers who implemented the APIs, ensuring accuracy and completeness.
- **Tools Needed:** Comment sections in docs for feedback, pull requests on version control.
- **Success Criteria:** All reviewers sign off that the documentation is accurate.
- **Common Pitfalls:** Unresolved discrepancies between code and doc; insufficient testing of edge cases.
- **Time Estimate:** 4 hours

**STEP 6: [Accessibility Check]**
- **Action:** Run an accessibility scan using tools like Axe or Lighthouse, ensuring WCAG compliance for all documentation pages.
- **Tools Needed:** Lighthouse (Chrome extension), Axe core rules.
- **Success Criteria:** No critical accessibility violations are found.
- **Common Pitfalls:** Missing alt text for images; focus issues on mobile viewports.
- **Time Estimate:** 2 hours

**STEP 7: [Deployment to Production]**
- **Action:** Push the updated docs site to a staging environment, then merge into production using CI/CD pipelines (e.g., GitHub Actions).
- **Tools Needed:** GitHub Actions, GitLab CI, AWS Amplify for static hosting.
- **Success Criteria:** Docs are live at `https://docs.yourcompany.com` and accessible via the API gateway.
- **Common Pitfalls:** Misconfiguration of deployment triggers; CORS issues blocking access from frontend.
- **Time Estimate:** 3 hours

**STEP 8: [User Testing Session]**
- **Action:** Conduct a user testing session with a non-developer stakeholder to validate usability and understandability.
- **Tools Needed:** User testing platforms like UsabilityHub, screen recording tools.
- **Success Criteria:** Qualitative feedback indicates users can find required information quickly.
- **Common Pitfalls:** Overly technical language; missing context for new developers.
- **Time Estimate:** 2 hours

**STEP 9: [Feedback Loop Implementation]**
- **Action:** Set up a system for collecting ongoing feedback on the documentation (e.g., a GitHub issue labeled `documentation-feedback`).
- **Tools Needed:** GitHub Issues, Slack channel for quick feedback sharing.
- **Success Criteria:** Mechanism is in place and monitored weekly by the API owner.
- **Common Pitfalls:** Lack of action on issued feedback; inactive monitoring.
- **Time Estimate:** 1 hour

**STEP 10: [Final Metrics Review]**
- **Action:** Analyze metrics such as page views, time spent on each doc page, error rates from users accessing docs directly (via API gateway logs).
- **Tools Needed:** Google Analytics for website traffic, CloudWatch/Stackdriver for server access logs.
- **Success Criteria:** Documented pages have >70% view rate and <5% user errors over a 2-week period.
- **Common Pitfalls:** Misinterpretation of metrics due to temporary spikes from automated testing scripts.
- **Time Estimate:** 1 hour

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
1. **Primary Metric:**  
   - Document readability score (average user engagement time): Target > 2 minutes per page.

2. **Secondary Metrics:**  
   - Number of requests to docs endpoint: Should decrease over time as devs use API more frequently.
   - Error rate from access attempts: Aim for < 1% errors.

3. **Long-term Metrics:**  
   - User satisfaction score (post-deployment surveys): Target > 4/5 on a scale.
   - Maintenance tickets related to docs: Should trend downwards.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables

1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken (e.g., "Generated API schemas", "Deployed documentation site")
   - Results achieved (metrics from Phase 4)
   - ROI or impact metrics (user satisfaction, error reduction)

2. **Detailed Report**
   - Full methodology section with links to all research sources.
   - Step-by-step execution log with timestamps and issue resolutions.
   - All final documents (API schema files, deployment logs).

3. **Maintenance Plan**
   - Ongoing tasks: Monthly documentation review, quarterly API versioning updates
   - Monitoring schedule: Automated checks every 2 hours for broken links or schema changes
   - Update frequency: Quarterly review of content accuracy and relevance

4. **Knowledge Transfer**
   - Training materials: Quickstart guide for new developers on using the docs.
   - SOPs: How to update schemas, generate documentation, and deploy updates.
   - Troubleshooting guide: Common issues with doc generation, deployment failures, CORS blocking.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

1. **Replace all [BRACKETED] items** with specific details about your project (e.g., "Endpoints: `/api/v1/users`, `/api/v1/products`").

2. **Define 12 Critical Topics** based on the knowledge areas above.

3. **Map Ultimate Goal to Measurable Outcomes**:  
   - Example Metric: Achieve an average page view duration of >2 minutes and <5% error rate from users accessing docs within the first month post-deployment.

4. **Build Step-by-Step Workflow** using industry best practices (e.g., use Swagger for schema extraction, Docusaurus for documentation site generation).

5. **Include Latest 2024-2025 Practices**:  
   - AI integration: Use OpenAI's API Playground docs as a reference.
   - Automation: Integrate CI/CD pipelines to auto-generate and deploy docs on every push.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Core API Design Principles"
    focus: "Latest best practices for RESTful APIs and versioning in 2024-2025"
    sources: ["Martin Fowler's microsite", "OpenAPI Spec Docs"]
    deliverable: "Principle list with examples"

  - agent_id: 2
    topic: "Documentation Tools and Standards"
    focus: "Comparison of static site generators for API docs"
    sources: ["Docusaurus Docs", "MkDocs Repo", "Swagger UI Showcase"]
    deliverable: "Tool comparison matrix"

  # [Continue for agents 3-12]
```

### SUCCESS VALIDATION

Before marking this task COMPLETE:

1. **Did the Ultimate Goal Get Achieved?**  
   - Are all endpoints documented with clear request/response schemas?

2. **Do All Metrics Meet Targets?**  
   - Page views > 70% per page, Error rate < 5%.

3. **Is Documentation Quality Verified?**  
   - Do developers find it easy to use and understand?

4. **Is Maintenance Plan Documented?**  
   - Are there clear procedures for updating docs in the future?

5. **Was User Feedback Collected and Actioned?**  
   - Have any usability issues been resolved based on stakeholder input?

---

### TEMPLATE METADATA

**Last Updated:** 2024-08-15  
**Version:** 1.0  
**Tested With:** Full Stack Developer roles building RESTful APIs  
**Success Rate:** [Insert after implementation]  
**Average Time to Goal:** [Insert after implementation]

---

