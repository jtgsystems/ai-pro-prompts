# Full Stack Developer - AI Agent Template
## Production-Ready Web Application

### PROFESSION CONFIGURATION
```yaml
profession_name: "Full Stack Developer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### SUCCESS DEFINITION (Production-Ready Web Application)
**Primary Objective:** Develop a fully functional, scalable, and secure web application that is deployable in production environments with zero downtime, meeting all quality standards for performance, security, and user experience.

#### Measurable Success Criteria
1. **Functional Correctness:**
   - 99% of unit tests pass (using Jest)
   - CI/CD pipeline runs successfully on every push to main branch

2. **Performance:**
   - Load time < 3 seconds for 95th percentile
   - CPU usage under 70% on production server at peak load
   - Memory footprint < 500 MB per instance

3. **Security:**
   - No high-severity vulnerabilities in OWASP Top 10 (using Snyk)
   - Rate limiting configured to prevent brute force attacks
   - Data sanitization in all user input handling

4. **Scalability:**
   - Horizontal scaling supported with zero configuration changes
   - Autoscaling works as expected under simulated load spikes

5. **Deployment Reliability:**
   - Blue-green deployment tested without data loss (using Argo Rollouts)
   - Disaster recovery plan validated through scheduled backups and restore tests

6. **Maintainability:**
   - Code coverage > 85% across all modules
   - Architecture documented in Confluence with diagrams and process flowcharts
   - Dependency issues resolved automatically via Dependabot alerts

### CRITICAL KNOWLEDGE AREAS FOR FULL STACK DEVELOPER (10-20 SPECIFIC TOPICS)
1. **Frontend Technologies:**
   - React 18 + TypeScript for component-based architecture
   - Redux Toolkit or Zustand for state management
   - Next.js SSR capabilities and API routes
   - Tailwind CSS for styling solutions

2. **Backend Development:**
   - Node.js/Express framework for server logic
   - RESTful API design principles and OpenAPI documentation
   - Database integration with MongoDB (Mongoose) or PostgreSQL
   - Authentication using JWT and OAuth 2.0 libraries

3. **Full-Stack Integration:**
   - GraphQL usage for efficient data fetching and caching strategies
   - WebSocket communication via Socket.IO for real-time updates
   - Containerization with Docker to ensure consistent environments
   - Orchestration with Kubernetes or AWS ECS Fargate

4. **DevOps Practices:**
   - Continuous Integration using GitHub Actions or GitLab CI
   - Infrastructure as Code (IaC) with Terraform or Pulumi
   - Serverless Functions on AWS Lambda for stateless operations
   - Monitoring with Prometheus + Grafana stack in production

5. **Security Best Practices:**
   - CORS policies and cross-site scripting prevention
   - HTTPS enforcement and HSTS configuration
   - Environment variable management via Vault or AWS Secrets Manager
   - Automated dependency vulnerability scanning (Snyk, Dependabot)

6. **Testing Frameworks:**
   - Unit testing with Jest for backend logic
   - Integration tests using Cypress for end-to-end scenarios
   - Performance testing with Lighthouse CI

7. **Version Control and Collaboration:**
   - Git branching strategies (GitHub Flow)
   - Code reviews enforced via Pull Request templates
   - Automated linting and formatting with ESLint + Prettier

8. **API Documentation and Client Libraries:**
   - Swagger/OpenAPI documentation for all REST endpoints
   - Typed client libraries in TypeScript/JavaScript for frontend consumption
   - Pagination, filtering, sorting options implemented per API spec

9. **Performance Optimization Techniques:**
   - Lazy loading of resources (images, videos)
   - Code splitting and dynamic imports for bundles
   - Web Workers for heavy computations off the main thread
   - CDN usage for static assets distribution globally

10. **Scalability Patterns:**
    - Microservices architecture breakdown if application grows
    - Event-driven processing with RabbitMQ or Kafka
    - Database sharding strategies for high-traffic scenarios
    - Load balancing configurations on API Gateway layer

### EXECUTION STEPS WITH SPECIFIC ACTIONS AND TOOLS

**STEP 1: Project Initialization & Setup**
- **Action:** Scaffold the project using Next.js boilerplate (with TypeScript support)
- **Tools Needed:** Visual Studio Code, Node.js LTS, Git
- **Success Criteria:** Repo initialized with proper folder structure; Dockerfile created in root directory
- **Common Pitfalls:** Forgetting to enable `client: true` on pages requiring SSR data fetching
- **Time Estimate:** 2 hours

**STEP 2: Backend API Development**
- **Action:** Create core routes (`/users`, `/posts`) using Express + Prisma ORM for database access
- **Tools Needed:** MongoDB Atlas (or PostgreSQL on AWS RDS), Prisma CLI, Supabase for authentication fallback
- **Success Criteria:** All endpoints return valid JSON responses; API Gateway configured with health checks
- **Common Pitfalls:** Incorrect data schema causing validation errors at runtime
- **Time Estimate:** 4 hours

**STEP 3: Frontend Component Development**
- **Action:** Build reusable UI components (Sidebar, Header, Modal) using React + Tailwind CSS framework
- **Tools Needed:** Next.js Pages directory (`app/`), Storybook for component isolation testing
- **Success Criteria:** Components pass accessibility tests; styled correctly per design system guidelines
- **Common Pitfalls:** Overriding global styles causing conflicts between components
- **Time Estimate:** 6 hours

**STEP 4: State Management & Async Operations**
- **Action:** Implement Redux Toolkit with time-travel debugging capabilities for complex state logic (e.g., pagination)
- **Tools Needed:** Redux DevTools Extension in VS Code, Immutable.js utilities
- **Success Criteria:** Application maintains consistent UI even when async data resolves simultaneously from multiple sources
- **Common Pitfalls:** Mutating global state directly instead of using actions/reducers pattern
- **Time Estimate:** 3 hours

**STEP 5: Authentication & Authorization**
- **Action:** Integrate JWT-based authentication flow with refresh token rotation strategy; implement role-based access control
- **Tools Needed:** NextAuth.js library, AWS Cognito for user directory integration
- **Success Criteria:** Users can log in/out without session hijacking; protected routes only accessible to authenticated users
- **Common Pitfalls:** Exposing secret keys (JWT signing key) in client code
- **Time Estimate:** 2 hours

**STEP 6: API Documentation & Client Library**
- **Action:** Generate OpenAPI spec for all endpoints; bundle with TypeScript types for developer consumption
- **Tools Needed:** Swagger UI, Typedoc CLI
- **Success Criteria:** Frontend components auto-complete against server schema; client library available at `/api-docs` endpoint
- **Common Pitfalls:** Out-of-sync between backend changes and generated documentation leading to integration errors
- **Time Estimate:** 2 hours

**STEP 7: Performance Optimization**
- **Action:** Implement code splitting for lazy-loaded modules, enable GZIP compression on server responses
- **Tools Needed:** Next.js built-in code splitting, Brotli plugin in Express
- **Success Criteria:** First Contentful Paint < 1.5s; Time to Interactive > 2.5s under realistic network conditions
- **Common Pitfalls:** Forgetting to split critical path CSS causing FOIT issues
- **Time Estimate:** 4 hours

**STEP 8: Security Hardening**
- **Action:** Enforce HTTPS, implement rate limiting at API Gateway layer; sanitize user inputs before DB storage
- **Tools Needed:** Cloudflare for SSL termination, AWS WAF for DDoS protection
- **Success Criteria:** No critical vulnerabilities found in Snyk scan; bot mitigation thresholds set appropriately
- **Common Pitfalls:** Overly permissive CORS settings leading to security risks
- **Time Estimate:** 3 hours

**STEP 9: Testing & CI/CD Pipeline**
- **Action:** Write unit tests for core business logic, integration tests for end-to-end data flows; configure GitHub Actions pipeline
- **Tools Needed:** Jest, Cypress, GitHub Actions, Docker Compose
- **Success Criteria:** All pipelines pass on every commit to main branch; failure notifications sent via Slack/Email
- **Common Pitfalls:** Test coverage not meeting target thresholds due to lack of test cases for edge scenarios
- **Time Estimate:** 5 hours

**STEP 10: Deployment & Monitoring**
- **Action:** Deploy application using Argo Rollouts with canary release strategy; set up Prometheus metrics and Grafana dashboards
- **Tools Needed:** Docker Hub, Kubernetes Cluster (EKS/GKE), Prometheus Operator, Grafana Cloud
- **Success Criteria:** Zero downtime deployments verified through automated smoke tests post-deployment; alerts configured for CPU/memory saturation
- **Common Pitfalls:** Missing health checks causing automatic rollbacks in CI pipeline
- **Time Estimate:** 4 hours

### TOOLING RECOMMENDATION (PRIMARY TOOLS LISTED FIRST)

**CORE DEVELOPMENT**
- **IDE:** Visual Studio Code (free, recommended)
- **JavaScript/TypeScript Runtime:** Node.js LTS (free)
- **Frontend Framework:** Next.js (React framework) - free
- **CSS Library:** Tailwind CSS - free

**BACKEND FRAMEWORK & ORCHESTRATION**
- **Framework:** Express.js (Node.js web server framework) - free
- **ORM/Database:** Prisma or Sequelize for SQL databases; Mongoose for MongoDB - free
- **Containerization:** Docker - free
- **Orchestration:** Kubernetes on EKS/GKE, Amazon ECS Fargate (optional/paid)

**SECURITY & DEPENDENCY MANAGEMENT**
- **Dependency Scanner:** Snyk (free tier available) or Dependabot (GitHub feature)
- **Secrets Management:** AWS Secrets Manager (optional paid component of AWS services)
- **Rate Limiting:** AWS API Gateway Rate Limits

**CI/CD & CONTINUOUS INTEGRATION**
- **Build Server:** GitHub Actions (free for public repos, free on private up to 2 concurrent jobs)
- **Testing Frameworks:** Jest, Cypress
- **Container Registry:** Docker Hub or Amazon ECR (free tier available)

**MONITORING AND OBSERVABILITY**
- **Metrics:** Prometheus + Grafana Cloud (free tier available)
- **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana) - free with Docker Compose setup
- **Alerting:** PagerDuty integration for critical alerts

**DEPLOYMENT STRATEGIES**
- **Canary Deployments:** Argo Rollouts or Helm rolling updates
- **Blue-Green Deployments:** Kubernetes deployment strategies
- **Disaster Recovery:** Automated snapshots via S3/Blob Storage with cross-region replication options

### TIMELINE TO ACHIEVE PRODUCTION-READY WEB APPLICATION

| Phase | Duration | Key Milestones |
|-------|----------|----------------|
| Research & Planning | 1 week | Define project scope, select tech stack, create initial repo structure |
| Development Sprint 1 | 2 weeks | Core backend API with authentication; frontend routing set up |
| Development Sprint 2 | 2 weeks | Implement main application features (CRUD operations); UI components developed |
| Quality Assurance & Testing | 1 week | Write tests covering >80% of critical paths; run full CI pipeline |
| Security Hardening & Monitoring Setup | 3 days | Enable HTTPS, rate limiting, set up Prometheus/Grafana monitoring |
| Deployment Preparation | 2 days | Configure Kubernetes manifests, write deployment scripts (Argo Rollouts) |
| Launch & Post-Launch Optimization | Ongoing | Monitor performance metrics; iterate on user feedback |

**TOTAL ESTIMATED TIME:** ~4 weeks for initial development and setup phase

### COMMON TRAFFIC JAMPOINTS AND HOW TO AVOID THEM

#### Frontend Issues
- **Problem:** Components not loading due to circular dependencies or missing typings.
  - **Solution:** Enforce single source of truth; use TypeScript with strict mode.

- **Problem:** State synchronization issues leading to stale UI data.
  - **Solution:** Utilize Redux Toolkit's createSlice and immer for pure state transformations.

#### Backend Issues
- **Problem:** Database schema changes causing migration conflicts.
  - **Solution:** Use Prisma Migrate or Sequelize CLI version control migrations; test rollbacks thoroughly.

- **Problem:** API endpoint not handling large payloads correctly.
  - **Solution:** Implement size limits in Express middleware; log oversized requests for investigation.

#### Deployment Issues
- **Problem:** Rollback due to unexpected error during deployment.
  - **Solution:** Use GitOps approach with immutable deployments; keep previous Docker images available post-deployment.

- **Problem:** Inconsistent environment variables between dev/staging/prod leading to runtime errors.
  - **Solution:** Centralize environment configuration using AWS Secrets Manager or GitHub Actions secrets.

### TROUBLESHOOTING GUIDE FOR COMMON ISSUES

#### Application Crashes on Start
1. Check Docker logs for image loading failures (e.g., `npm ERR!`).
2. Verify all service ports are correctly mapped in Kubernetes manifests.
3. Ensure environment variables loaded via K8s ConfigMaps.

#### Slow Load Times
1. Review bundle size using Webpack Bundle Analyzer; consider code splitting.
2. Check Cloudflare cache settings for frontend assets.
3. Enable HTTP/2 in your cloud provider's load balancer settings.

#### Authentication Failures
1. Verify JWT secret key matches between client and server configurations.
2. Confirm user roles correctly mapped to backend permissions schema.
3. Inspect CORS headers if using cross-origin resources properly.

#### Deployment Errors
1. Check Argo Rollout status for failed tasks (e.g., container image pull failures).
2. Ensure Helm chart values correctly set in GitHub Actions environment variables.
3. Review Kubernetes pod conditions; look for `imagePullBackOff` or `ErrImagePull`.

### RECOMMENDED TOOL STACK FOR 2024-2025

**PRIMARY TOOLS (FREE)**
- **IDE:** Visual Studio Code
- **JavaScript/TypeScript Runtime:** Node.js LTS
- **Frontend Framework:** Next.js
- **CSS Library:** Tailwind CSS
- **Backend Framework:** Express.js
- **ORM/Database:**
  - Prisma for database access (free)
  - Mongoose for MongoDB integration (free)
- **Containerization & Orchestration:**
  - Docker (Docker Hub registry free tier)
  - Kubernetes on EKS/GKE or AWS ECS Fargate (optional paid component of AWS services)
- **CI/CD:** GitHub Actions
- **Testing Frameworks:** Jest, Cypress
- **Monitoring:** Prometheus + Grafana Cloud (free tier available)
- **Logging:** ELK Stack setup in Docker Compose
- **Deployment Strategies:** Argo Rollouts

**OPTIONAL/PAYMENT-REQUIRED TOOLS**
- **Secrets Management:** AWS Secrets Manager (optional paid component of AWS services)
- **API Gateway Rate Limiting:** AWS API Gateway Pro tier
- **Container Registry:** Amazon ECR with advanced features
- **Cloud Deployment Services:** Google Kubernetes Engine (GKE) Pro tier or Azure AKS Enterprise

**BEST PRACTICES FOR REMOTE WORK AS A FULL STACK DEVELOPER**

1. **Set Up a Dedicated Workspace**
   - Use a dual-monitor setup for code, documentation, and testing environments side-by-side
   - Ensure noise-canceling headphones are available for focused work sessions

2. **Implement Access Control Protocols**
   - Two-factor authentication on all cloud accounts (AWS/GCP/Azure)
   - VPN with strong encryption (OpenVPN or WireGuard)

3. **Adopt Collaborative Tools Efficiently**
   - Use Slack channels for real-time collaboration; keep main development channel #dev
   - Integrate GitHub Actions notifications directly into your primary messaging app

4. **Maintain Regular Rhythm**
   - Schedule daily standups via Zoom or Google Meet to discuss progress and blockers
   - Set up weekly sprint retrospectives to improve workflow and tooling

5. **Document Everything**
   - Keep all documentation in Confluence linked from GitHub README files
   - Use Markdown for clear, version-controlled notes on architecture decisions and tech stack rationale

