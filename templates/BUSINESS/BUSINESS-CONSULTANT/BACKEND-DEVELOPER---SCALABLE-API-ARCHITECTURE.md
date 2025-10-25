# Backend Developer - AI Agent Template
## Scalable API Architecture

### Success Definition (Measurable)
A scalable API architecture is achieved when:
- **Throughput:** Handles 10,000+ concurrent requests per second with <200ms latency under peak load.
- **Scalability:** Can horizontally scale by adding more instances without degradation in performance or availability.
- **Maintainability:** Code follows industry best practices (e.g., SOLID principles, DRY), with automated linting and testing at 95% coverage.
- **Reliability:** Demonstrates 99.9% uptime over a 30-day period with automated failover mechanisms.

### Critical Knowledge Areas for Backend Developer

1. **API Design Principles**
   - RESTful design
   - API versioning strategies
   - OpenAPI/Swagger documentation standards
2. **Microservices Architecture**
   - Service decomposition guidelines
   - Service communication patterns (sync vs async)
3. **Scalability Techniques**
   - Load balancing algorithms (L4/L7)
   - Database sharding and partitioning strategies
   - Asynchronous processing models (event-driven architecture)
4. **Caching Strategies**
   - In-memory caching with Redis/Memcached
   - Distributed cache management
5. **Message Queues & Event-Driven Systems**
   - Choosing between Kafka, RabbitMQ, or AWS SQS
   - Implementing idempotency and retry mechanisms
6. **Containerization & Orchestration**
   - Docker best practices for API containers
   - Kubernetes deployment patterns (auto-scaling, rolling updates)
7. **Monitoring & Logging**
   - Centralized logging solutions (ELK stack)
   - Metrics collection via Prometheus/Grafana
8. **Security Practices**
   - OAuth 2.0/OpenID Connect implementation
   - Secure API gateway configuration
9. **Data Serialization**
   - JSON vs Protocol Buffers performance considerations
10. **Testing Strategies**
    - Unit testing with Jest/Mocha
    - Integration testing frameworks (Postman, Cypress)
11. **CI/CD Pipelines**
    - GitHub Actions or GitLab CI for automated builds and deployments
12. **Cost Optimization**
    - Cloud resource right-sizing techniques
    - Implementing cost-aware architectures (e.g., spot instances)

### Execution Workflow

**STEP 1: [Project Setup & Infrastructure as Code]**
- **Action:** Provision cloud infrastructure using Terraform or Pulumi.
  - **Tools Needed:** Terraform, AWS/GCP/Azure accounts, CI/CD pipelines (GitHub Actions).
  - **Success Criteria:** All resources provisioned successfully without drift; environment is version-controlled.
  - **Common Pitfalls:** Misconfiguration of IAM roles, missing cost controls.
  - **Time Estimate:** 4-6 hours

**STEP 2: [API Gateway Configuration]**
- **Action:** Deploy API gateway using Kong/Traefik or AWS API Gateway.
  - **Tools Needed:** Kong/Traefik, Terraform modules for deployment.
  - **Success Criteria:** All routes defined with proper authentication (JWT/OAuth); rate limiting enabled.
  - **Common Pitfalls:** Incorrect path definitions leading to 404 errors; missing security headers.
  - **Time Estimate:** 2-3 hours

**STEP 3: [Service Containerization]**
- **Action:** Dockerize backend services and push images to a registry (e.g., AWS ECR, Docker Hub).
  - **Tools Needed:** Dockerfile templates, CI pipelines for automated build/upload.
  - **Success Criteria:** Images built without errors; can be deployed successfully in Kubernetes.
  - **Common Pitfalls:** Missing `ENTRYPOINT` configurations leading to container crashes.
  - **Time Estimate:** 2-3 hours

**STEP 4: [Service Deployment & Scaling]**
- **Action:** Deploy services to a Kubernetes cluster and configure autoscaling rules.
  - **Tools Needed:** kubectl, Helm charts for deployment, Prometheus for metrics.
  - **Success Criteria:** Services running healthily; auto-scaling adjusts based on CPU load.
  - **Common Pitfalls:** Incorrect resource requests causing throttling or over-provisioning.
  - **Time Estimate:** 3-4 hours

**STEP 5: [Database Design & Sharding Strategy]**
- **Action:** Design database schema considering scalability needs and implement sharding strategy if needed.
  - **Tools Needed:** MySQL/MariaDB, MongoDB Atlas, Redis for caching.
  - **Success Criteria:** Schema supports horizontal scaling; can demonstrate performance with increased load.
  - **Common Pitfalls:** Poor index design leading to slow queries under load.
  - **Time Estimate:** 4-6 hours

**STEP 6: [Caching & Message Queues Implementation]**
- **Action:** Set up Redis for caching and implement message queues (Kafka/RabbitMQ).
  - **Tools Needed:** Redis, Kafka Connect, RabbitMQ servers.
  - **Success Criteria:** Latency reduced by 50% or more; messages processed reliably with idempotency.
  - **Common Pitfalls:** Incorrect consumer offsets leading to message loss.
  - **Time Estimate:** 4-6 hours

**STEP 7: [Security Hardening]**
- **Action:** Implement OAuth/OpenID Connect, enforce HTTPS, and configure rate limiting.
  - **Tools Needed:** AWS WAF/Azure Front Door, TLS certificates (Let's Encrypt).
  - **Success Criteria:** All endpoints require authentication; no insecure routes exposed.
  - **Common Pitfalls:** Misconfigured CORS policies causing cross-origin requests to fail.
  - **Time Estimate:** 2-3 hours

**STEP 8: [Testing & Validation]**
- **Action:** Write unit and integration tests covering critical API flows. Deploy to staging environment for load testing.
  - **Tools Needed:** Jest, Mocha, Postman collections, k6 or JMeter for load testing.
  - **Success Criteria:** All tests pass; system handles target load with acceptable latency (<200ms).
  - **Common Pitfalls:** Missing edge case scenarios in test suites leading to failures in production.
  - **Time Estimate:** 4-6 hours

**STEP 9: [Monitoring & Alerting Setup]**
- **Action:** Configure Prometheus metrics, Grafana dashboards, and alert rules for latency, error rates, and resource utilization.
  - **Tools Needed:** Prometheus exporters, Grafana dashboards, Alertmanager.
  - **Success Criteria:** Alerts trigger correctly during simulated load spikes or failures.
  - **Common Pitfalls:** Missed alerts due to incorrect threshold settings.
  - **Time Estimate:** 2-3 hours

**STEP 10: [Documentation & Knowledge Transfer]**
- **Action:** Document API contracts, deployment procedures, and operational runbooks. Conduct walkthroughs with team members.
  - **Tools Needed:** Swagger/OpenAPI docs, Confluence/Notion pages for documentation, Zoom/Teams for training sessions.
  - **Success Criteria:** All critical systems documented; at least one peer has completed the knowledge transfer session.
  - **Common Pitfalls:** Documentation not updated after changes leading to operational confusion.
  - **Time Estimate:** Ongoing

### Tools & Software Stack (2024-2025)

#### Primary Tools (Free/Open Source)
1. **Terraform** for Infrastructure as Code
2. **Docker** and **Kubernetes** for containerization
3. **PostgreSQL** or **MySQL** for relational databases
4. **MongoDB Atlas** for NoSQL needs
5. **Redis** for caching
6. **Kafka** for message queuing (using Confluent Cloud free tier)
7. **GitHub Actions** for CI/CD
8. **Swagger/OpenAPI** for API documentation
9. **Jest/Mocha** for testing
10. **Prometheus + Grafana** for monitoring

#### Optional Paid Tools (Premium Alternatives)
1. **AWS API Gateway** or **Azure API Management** (optional)
2. **Grafana Cloud Pro** for enhanced monitoring features
3. **Datadog** or **New Relic** for advanced application performance monitoring
4. **Docker Hub Enterprise** for private registries (if needed)

### Troubleshooting Guide

#### Common Issues & Solutions
1. **Deployment Fails**
   - Check container images are built and pushed to registry.
   - Verify Helm chart values match your environment variables.
2. **Service Not Scaling**
   - Ensure HorizontalPodAutoscaler is correctly configured with target CPU utilization.
3. **Database Performance Degradation**
   - Review query performance; add indexes if necessary.
   - Consider read replicas for scaling reads.
4. **Message Queue Lag**
   - Check consumer offsets are being committed after processing messages.
5. **Security Alerts (e.g., OWASP Top 10 vulnerabilities)**
   - Run automated security scans on CI pipeline.
   - Review API endpoints for input validation.

### Realistic Timeline to Achieve Scalable API Architecture

**Week 1-2: Infrastructure Setup & Provisioning**
- Complete provisioning of cloud infrastructure using Terraform (Day 3).
- Set up Docker registry and configure CI/CD pipelines (Days 5-6).

**Week 3-4: Core Service Deployment & Initial Load Testing**
- Deploy core backend services to Kubernetes.
- Implement initial API routes with basic authentication.
- Perform load testing at 50% of expected peak traffic (Day 10).
- Scale services horizontally based on test results.

**Week 5-6: Advanced Features & Security Hardening**
- Implement caching layer using Redis.
- Set up message queues for asynchronous processing.
- Harden security configuration (OAuth/OpenID Connect) (Days 11-14).

**Week 7-8: Monitoring, Alerting, and Documentation**
- Configure Prometheus/Grafana stack for real-time monitoring.
- Establish alerting rules based on latency and error rates.
- Document API contracts and operational procedures. Conduct knowledge transfer sessions.

**Post-Implementation Phase (Ongoing)**
- Regularly review performance metrics; adjust scaling policies as needed.
- Update documentation with any changes to architecture or deployment process.
- Schedule quarterly security audits and penetration testing.

### Final Checklist Before Marking Complete
- [ ] Scalable Architecture Achieved: System meets throughput and latency requirements under peak load tests (10,000+ concurrent requests).
- [ ] Monitoring in Place: All critical metrics monitored; alerts configured and tested.
- [ ] Documentation Updated: API contracts, deployment scripts, runbooks are current.
- [ ] Knowledge Transfer Completed: Team members have completed training sessions.
- [ ] Security Best Practices Followed: No critical vulnerabilities identified during security audit.

### Continuous Improvement Plan
1. **Review Performance Weekly:** Analyze metrics; identify bottlenecks and optimize services.
2. **Update Documentation Monthly:** Ensure all documentation reflects current state of the system.
3. **Run Quarterly Security Assessments:** Conduct penetration testing and vulnerability scans.
4. **Refactor Code Annually:** Review code for maintainability and performance improvements.

---

*This template is designed to be followed step-by-step by a Backend Developer new to the profession, ensuring they build a scalable API architecture with the latest tools and practices available.*

