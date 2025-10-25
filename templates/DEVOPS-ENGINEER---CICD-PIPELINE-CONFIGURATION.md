# DevOps Engineer - AI Agent Template
## CI/CD Pipeline Configuration

### Primary Objective: Achieve a fully automated, secure, and scalable CI/CD pipeline that integrates all development stages from code commit to production deployment with zero manual steps.

**Success Criteria (Measurable):**
- **Code Change Propagation:** Every change pushed through the pipeline is deployed to production within 15 minutes.
- **Deployment Frequency:** At least one successful release per sprint cycle (bi-weekly).
- **Mean Time to Recovery (MTTR):** <30 minutes for any failed deployment or rollback.
- **Change Failure Rate:** ≤5% of deployments result in a failure requiring immediate rollback.
- **Security Compliance:** All pipelines pass static code analysis and dependency vulnerability scans without failures.
- **Observability Coverage:** 100% coverage of key metrics (build success rate, pipeline duration, resource utilization) with real-time alerts.

### Critical Knowledge Areas for DevOps Engineer

1. **Infrastructure as Code (IaC):** Terraform, AWS CloudFormation
2. **Containerization & Orchestration:** Docker, Kubernetes (EKS/AKS/GKE)
3. **CI/CD Tools:** Jenkins, GitLab CI, GitHub Actions, Azure Pipelines
4. **Configuration Management:** Ansible, Puppet, Chef
5. **Monitoring & Observability:** Prometheus, Grafana, ELK Stack
6. **Security in DevOps:** HashiCorp Vault, Snyk, OWASP ZAP
7. **Git Workflow Models:** GitFlow, GitHub Flow
8. **Chaos Engineering:** Gremlin or Chaos Mesh for resilience testing
9. **Disaster Recovery & Backup Strategies**
10. **Multi-Region Deployment Strategies**
11. **API Gateway Management:** AWS API Gateway, Kong
12. **Software Release Automation**

### Detailed Execution Steps

**STEP 1: Repository Setup and Access Control**
- Action: Create a dedicated Git repository for the project.
- Tools Needed: GitHub/GitLab/Bitbucket, SSH keys for access control.
- Success Criteria: Repository accessible only to authorized users.
- Common Pitfalls: Incorrect permissions or branch protection rules not set.
- Time Estimate: 30 minutes

**STEP 2: CI Configuration**
- Action: Set up a Jenkins instance with Docker plugin and Kubernetes agent support.
- Tools Needed: Jenkins, Docker, GitHub Actions (optional for quick testing).
- Success Criteria: Build job triggers on every push to main branch.
- Common Pitfalls: Incorrect Docker image pull or network issues between agents.
- Time Estimate: 2 hours

**STEP 3: Code Quality Checks**
- Action: Integrate SonarQube scanner and Snyk vulnerability scan into pipeline.
- Tools Needed: SonarQube, Snyk API, GitHub Actions for quick validation.
- Success Criteria: No failed quality gates; all vulnerabilities resolved before production.
- Common Pitfalls: False positives or rate limit errors from Snyk.
- Time Estimate: 1 hour

**STEP 4: Container Image Scanning**
- Action: Scan Docker images for known vulnerabilities using Trivy or Clair.
- Tools Needed: Trivy, Clair, Docker Hub.
- Success Criteria: All scans pass; no critical vulnerabilities present.
- Common Pitfalls: Incorrect image tagging causing false negatives.
- Time Estimate: 30 minutes

**STEP 5: Build and Package**
- Action: Execute a build job that compiles code and produces artifacts (Docker images).
- Tools Needed: Dockerfile, Maven/Gradle for Java apps, npm/yarn for Node.js.
- Success Criteria: Successful artifact creation with non-zero exit status.
- Common Pitfalls: Incorrect environment variables or missing dependencies.
- Time Estimate: 1 hour

**STEP 6: Deploy to Staging**
- Action: Push the Docker image to a staging Kubernetes cluster via Helm charts.
- Tools Needed: Helm, K8s API for staging namespace setup.
- Success Criteria: Successful deployment with all pods in ready state.
- Common Pitfalls: Incorrect chart values or namespace permissions.
- Time Estimate: 1 hour

**STEP 7: Automated Testing**
- Action: Run integration and end-to-end tests against the staging environment.
- Tools Needed: Selenium, Postman, Cypress.
- Success Criteria: All tests pass; no flaky tests identified.
- Common Pitfalls: Environment mismatch or race conditions in parallel test runs.
- Time Estimate: 2 hours

**STEP 8: Deploy to Production**
- Action: Once testing passes, promote the image to a production namespace via another Helm release.
- Tools Needed: Same as staging deployment.
- Success Criteria: All pods running successfully; canary or blue-green deployment works.
- Common Pitfalls: Incorrect config maps/ secrets causing service failures.
- Time Estimate: 1 hour

**STEP 9: Rollback Procedure**
- Action: Implement a rollback mechanism using Helm's rollback command and Prometheus alerts.
- Tools Needed: Helm, Alertmanager in Prometheus, GitHub Actions for test runs.
- Success Criteria: Ability to roll back within the defined MTTR threshold (<30 mins).
- Common Pitfalls: Incorrect revision numbers or alert fatigue.
- Time Estimate: 30 minutes

**STEP 10: Monitoring & Alerts**
- Action: Set up dashboards and alerts using Prometheus, Grafana, and Loki for logs.
- Tools Needed: Prometheus, Grafana, Loki, Alertmanager.
- Success Criteria: All critical metrics collected; alerts fire on real anomalies.
- Common Pitfalls: Missing alerts due to incorrect threshold settings.
- Time Estimate: 2 hours

**STEP 11: Security Hardenments**
- Action: Implement Vault for secrets management and integrate with CI pipeline via dynamic credentials.
- Tools Needed: HashiCorp Vault, Vault Agent Injector.
- Success Criteria: No static credentials in the code; secret rotation logs available.
- Common Pitfalls: Incorrect policy definitions leading to denied requests.
- Time Estimate: 1 hour

**STEP 12: Chaos Testing**
- Action: Inject failures (CPU spike, network latency) into running services during a production window.
- Tools Needed: Gremlin or Chaos Mesh.
- Success Criteria: System recovers automatically; no data loss reported.
- Common Pitfalls: Unexpected system shutdowns due to chaos injection.
- Time Estimate: 1 hour

**STEP 13: Documentation and Knowledge Transfer**
- Action: Document the entire pipeline architecture, config files, and runbooks in a shared wiki.
- Tools Needed: Confluence, Markdown editor for documentation.
- Success Criteria: All team members can reproduce the pipeline from scratch within 15 minutes.
- Common Pitfalls: Outdated documentation causing confusion during handovers.
- Time Estimate: Ongoing

### Recommended Tool Stack (2024-2025)

**Primary Tools (Free/Open Source):**
1. **Version Control:** GitHub/GitLab
2. **CI/CD:** Jenkins, GitHub Actions
3. **Containerization:** Docker
4. **Orchestration:** Kubernetes (EKS/AKS/GKE)
5. **Infrastructure as Code:** Terraform
6. **Monitoring:** Prometheus + Grafana + Loki
7. **Logging:** Fluentd -> Elasticsearch
8. **Configuration Management:** Ansible/Puppet/Chef
9. **Secrets Management:** HashiCorp Vault (free tier available)
10. **Static Analysis:** SonarQube (cloud or self-hosted)

**Optional Premium Tools:**
1. **Advanced Monitoring & Alerting:** Datadog, New Relic
2. **Service Mesh:** Istio/Linkerd (commercial support options)
3. **Container Security:** Aqua Security, Twistlock
4. **Chaos Engineering:** Gremlin Pro Plan
5. **API Management:** Kong Enterprise

### Troubleshooting Guide for Common Issues

**Deployment Fails with "Permission Denied"**
- Check Kubernetes service account permissions.
- Ensure Helm release is scoped to the right namespace.

**Build Fails Due to "Image Push Error"**
- Verify Docker daemon logs for network errors or registry connectivity issues.
- Retry build after clearing Docker cache.

**Tests Fail in Staging/Production**
- Check environment parity between staging and production (especially secrets).
- Review recent changes in configuration files that might have triggered the failure.

**Rollback Not Working**
- Ensure Helm release revision numbers are correct.
- Test rollback manually from a previous working revision.

**Monitoring Alerts Firing Without Issues**
- Verify Alertmanager routing rules.
- Check if Prometheus scrape targets are healthy.

### Realistic Timeline

| Phase          | Duration |
|----------------|----------|
| Repository Setup & Access Control | 1 Day |
| CI Configuration                | 2 Days |
| Code Quality Checks             | 1 Day |
| Container Image Scanning        | 0.5 Day |
| Build and Package               | 1 Day |
| Deploy to Staging              | 1 Day |
| Automated Testing              | 2 Days |
| Deploy to Production            | 1 Day |
| Monitoring & Alerts Setup      | 2 Days |
| Security Hardenments           | 1 Day |
| Chaos Testing                  | 1 Day |
| Documentation and Knowledge Transfer | Ongoing |
**Total:** Approximately **8-10 Business Days**

### Final Checklist for Success

Before declaring the CI/CD pipeline configuration complete:

- [ ] All phases executed without critical errors.
- [ ] Deployment frequency achieved (e.g., at least one release per sprint).
- [ ] MTTR < 30 minutes for failures.
- [ ] Change failure rate ≤ 5%.
- [ ] Security scans passed with no critical findings.
- [ ] Observability metrics cover all key components (build success, pipeline duration, resource utilization).
- [ ] All team members can successfully reproduce the entire process.
- [ ] Documentation updated and reviewed by stakeholders.

**Continuous Improvement:**
- Schedule a post-mortem review after each deployment cycle to identify bottlenecks or improvements.
- Automate documentation generation from CI/CD configuration files whenever changes are detected.
- Periodically run chaos tests in non-production environments to validate resilience.

