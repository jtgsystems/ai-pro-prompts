# Full Stack Developer - AI Agent Template

## Production-Ready Web Application

### 1. Critical Knowledge Areas Specific to Full Stack Developer

1. Front-end Development
   - HTML, CSS, JavaScript (ES6+)
   - Responsive Design with Media Queries
   - UI/UX Principles
   - Accessibility Standards

2. Back-end Development
   - Server-side Programming Languages (Node.js, Python, Ruby, Java)
   - RESTful API Design and Implementation
   - Asynchronous Programming
   - Authentication & Authorization (OAuth)

3. Database Management
   - SQL Databases (MySQL, PostgreSQL) vs NoSQL Databases (MongoDB)
   - Database Schema Design
   - Data Modeling Techniques

4. Web Application Architecture
   - Microservices Architecture
   - Event-Driven Systems
   - Service-Oriented Architecture (SOA)

5. DevOps Practices
   - Continuous Integration/Continuous Deployment (CI/CD) Pipelines
   - Containerization with Docker and Kubernetes
   - Infrastructure as Code (IaC) Tools

6. Testing Strategies
   - Unit Testing, Integration Testing, End-to-End Testing
   - Test Automation Frameworks (Jest, Mocha, Selenium)

7. Security Best Practices
   - Secure Coding Techniques
   - Data Encryption and Transmission Protocols
   - Vulnerability Scanning and Penetration Testing

8. Cloud Computing Fundamentals
   - Scalability and High Availability Design Patterns
   - Serverless Architectures
   - Managed Services (e.g., AWS RDS, Google Cloud Firestore)

9. API Development and Consumption
   - RESTful API Design Guidelines
   - API Versioning Strategies
   - API Documentation Tools (Swagger/OpenAPI)

10. Monitoring and Logging Solutions
    - Performance Monitoring Tools (New Relic, Datadog)
    - Centralized Logging Systems (ELK Stack, Splunk)
    - Alerting Mechanisms

11. Agile Methodologies
    - Scrum or Kanban Frameworks
    - Sprint Planning and Retrospectives
    - User Story Mapping and Backlog Management

12. Mobile App Development Basics
    - Native vs Hybrid App Approaches
    - Cross-Platform Frameworks (React Native, Flutter)

13. Deployment Automation Tools
    - GitHub Actions, GitLab CI/CD
    - AWS CodeDeploy, Azure DevOps Pipelines

14. Performance Optimization Techniques
    - Front-end Asset Management (Webpacker, Parcel)
    - Caching Strategies for Database and API Calls
    - Load Balancing Techniques

15. Data Visualization and Reporting Tools
    - Dashboards and Monitoring Solutions (Grafana, Kibana)
    - Reporting Mechanisms (Power BI, Tableau)

### 2. Detailed Execution Steps with Specific Actions

1. **Project Planning**
   - Define project scope, objectives, and success criteria.
   - Identify stakeholders and define communication channels.

2. **Requirements Gathering**
   - Conduct user interviews to gather functional requirements.
   - Document non-functional requirements (security, scalability).

3. **Architecture Design**
   - Design system architecture using UML diagrams or similar tools.
   - Define microservices boundaries if applicable.
   - Select databases based on data volume and access patterns.

4. **Front-end Development Setup**
   - Initialize a new React/Angular/Vue project using Create-React-App, Angular CLI, or Vue CLI.
   - Set up version control with Git and create a remote repository (GitHub, GitLab).

5. **Back-end API Development**
   - Design RESTful APIs using OpenAPI/Swagger specifications.
   - Implement CRUD operations for database entities in Node.js/Express.js.
   - Add authentication using JWT or OAuth 2.0.

6. **Database Implementation**
   - Set up the chosen database (e.g., PostgreSQL, MongoDB).
   - Create schemas and seed initial data with sample records.

7. **Integration Testing**
   - Write unit tests for API endpoints using Jest/Mocha.
   - Perform end-to-end testing using Selenium or Cypress.

8. **Deployment Preparation**
   - Containerize application components using Docker.
   - Define Kubernetes deployment manifests if deploying to a cluster.
   - Configure CI/CD pipeline with GitHub Actions or GitLab CI.

9. **Monitoring and Logging Setup**
   - Implement centralized logging with ELK Stack.
   - Set up performance monitoring with New Relic or Datadog.
   - Configure alerts for critical metrics (e.g., response time, error rate).

10. **Security Hardenings**
    - Encrypt sensitive data at rest using environment variables.
    - Add CORS headers to API endpoints.
    - Implement rate limiting and IP blocking.

11. **Documentation**
    - Write comprehensive README.md with setup instructions.
    - Document APIs using Swagger/OpenAPI specifications.
    - Create deployment guides for staging and production environments.

12. **Continuous Testing**
    - Automate testing pipeline in CI/CD to run tests on every commit.
    - Use coverage reports to monitor code quality.

13. **Deployment to Production**
    - Follow the deployment checklist before going live.
    - Ensure rollback procedures are in place.

14. **Post-Deployment Monitoring**
    - Monitor application health and performance post-deployment.
    - Set up alerts for immediate issue detection during initial traffic.

15. **User Acceptance Testing (UAT)**
    - Conduct UAT with a subset of actual users to validate the app meets business requirements.
    - Gather feedback and iterate on functionality as needed.

### 3. Specific Tools, Software, and Platforms

- Front-end:
  - HTML5, CSS3, JavaScript ES6+
  - Frameworks: React.js, Angular, Vue.js
  - Preprocessors: SASS/SCSS, LESS
  - Dependency Management: npm or Yarn
  - Version Control: Git (GitHub/GitLab)

- Back-end:
  - Node.js with Express.js framework
  - Python with Flask/Django frameworks
  - Database:
    - PostgreSQL (primary)
    - MongoDB (optional alternative)
  - Authentication:
    - JSON Web Tokens (JWT) for stateless auth
    - OAuth 2.0 for third-party integration

- DevOps & Cloud:
  - Containerization: Docker, Kubernetes (Docker Compose for local development)
  - CI/CD Tools:
    - GitHub Actions or GitLab CI/CD
    - Jenkins (optional)
  - Cloud Services:
    - AWS Elastic Beanstalk, EC2
    - Google Cloud Platform, GKE
    - Azure App Service

- Testing & Monitoring:
  - Jest/Mocha for unit tests
  - Selenium/Cypress for end-to-end tests
  - New Relic or Datadog for monitoring
  - ELK Stack (Elasticsearch, Logstash, Kibana) for logging

### 4. Measurable Success Criteria for "Production-Ready Web Application"

- **Functional Completeness**
  - All user stories are implemented and tested.
  - User acceptance testing is completed with all critical features passed.

- **Performance Metrics**
  - Load test passes: <200ms response time under expected load (e.g., JMeter or k6).
  - Database query performance within acceptable thresholds (e.g., PostgreSQL's EXPLAIN ANALYZE).

- **Security Compliance**
  - No open ports except those defined in the security group.
  - All sensitive data is encrypted at rest and in transit.

- **Scalability**
  - The application can handle increased load without degradation of performance or functionality.
  - Horizontal scaling tested across multiple instances with minimal downtime.

- **Observability**
  - Logs are centralized, searchable, and alerting works as configured.
  - Application metrics (CPU usage, memory) are monitored in real-time dashboards.

### 5. Troubleshooting Section for Common Issues

1. **Deployment Failures**
   - *Issue:* Docker image build fails due to missing dependencies.
     - *Solution:* Verify package.json or requirements.txt lists all necessary packages.
   - *Issue:* Kubernetes deployment fails with pod errors.
     - *Solution:* Check logs using `kubectl describe pod <pod-name>` for specific error messages.

2. **Performance Bottlenecks**
   - *Issue:* High latency in API responses.
     - *Solution:* Profile code with tools like Chrome DevTools or Node.js profiler to identify slow functions.
   - *Issue:* Database connection pool exhausted under load.
     - *Solution:* Increase max_connections setting, optimize queries.

3. **Security Vulnerabilities**
   - *Issue:* Sensitive data exposed in logs or error messages.
     - *Solution:* Mask sensitive data before logging (e.g., JWT tokens).
   - *Issue:* Exploitable XSS vulnerability.
     - *Solution:* Sanitize user input using libraries like DOMPurify.

4. **Dependency Conflicts**
   - *Issue:* Multiple versions of same package causing errors.
     - *Solution:* Use `npm dedupe` or `yarn resolutions` to enforce single version globally.
   - *Issue:* Version conflict in Dockerfile (e.g., Node.js v18 with npm v6).
     - *Solution:* Pin specific versions in the environment and CI/CD pipeline.

### 6. Recommended Tool Stack with Pricing

- **Version Control & Collaboration**
  - GitHub: Free for public repositories, $7 per user/month for private repos.
  
- **Front-end Development**
  - React/Angular/Vue.js (frameworks): Open-source
  - npm/yarn (package managers): Open-source
  
- **Back-end Development**
  - Node.js with Express.js: Open-source
  - PostgreSQL, MongoDB: Free, open-source databases
  
- **Database Management & Migration**
  - pgAdmin (for PostgreSQL), Compass (MongoDB UI): Web-based tools are free; desktop versions available for purchase.

- **API Design & Documentation**
  - Swagger/OpenAPI Editor: Free web tool
  - Postman (optional alternative): $12 per user/month
  
  
### 7. Realistic Timeline to Achieve Production-Ready Web Application

**Assumptions**: A team of one Full Stack Developer working full-time.

| Phase                 | Duration |
|-----------------------|----------|
| Project Planning      | 1 week  |
| Requirements Gathering| 2 weeks |
| Architecture Design   | 3 days   |
| Front-end Development Setup | 1 day |
| Back-end API Development | 4-6 weeks (depending on complexity) |
| Database Implementation| 2-3 days |
| Integration Testing   | 5-7 days |
| Deployment Preparation | 1 week  |
| Monitoring & Logging Setup | 2 days |
| Security Hardenings   | Ongoing throughout development |
| Documentation         | Ongoing until release |
| Continuous Testing     | Ongoing |
| Deployment to Production | 1 day (with rollback procedures) |
| Post-Deployment Monitoring | Ongoing |
| UAT                   | 3-5 days |

**Total Estimated Time**: Approximately **2 months** from project initiation.

### 8. Troubleshooting Section for Common Issues

1. **Docker Build Fails**
   - *Error:* `docker build: failed to cache layer`
   - *Solution:* Ensure Dockerfile uses `COPY` instead of `ADD` for static assets and that files are not excluded unintentionally.
   
2. **Database Connection Errors**
   - *Error:* `pool is exhausted`
   - *Solution:* Verify max_connections setting in your database configuration (PostgreSQL: `max_connections = 150`, MongoDB: `maxPoolSize = 10`). Increase if needed.

3. **API Rate Limit Exceeded**
   - *Error:* HTTP 429 response
   - *Solution:* Implement rate limiting middleware on the server-side and configure API Gateway to handle throttling.

4. **Environment Variable Errors**
   - *Error:* `Cannot read property 'setInterval' of null`
   - *Solution:* Ensure all environment variables are correctly set in `.env` file and that they match the variable names used in code.

5. **Dependency Version Conflicts**
   - *Error:* Incompatible package versions
   - *Solution:* Use `npm dedupe` or `yarn resolutions` to enforce specific version requirements globally.
   
By following this comprehensive template, a Full Stack Developer can systematically approach building and deploying a production-ready web application in 2024-2025. The emphasis on using open-source tools ensures cost-effectiveness while maintaining high standards of quality and security.

