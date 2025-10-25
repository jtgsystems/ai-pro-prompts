# DevOps Engineer - AI Agent Template
## Container Orchestration

**Version:** 1.0  
**Purpose:** Guide an AI-driven DevOps engineer through industry best practices to achieve container orchestration at scale.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "DevOps Engineer"
profession_category: "Technology"
experience_level: "Beginner to Intermediate (someone new to the role)"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Primary Container Platform Preference]  
   - Format: Docker, Kubernetes (EKS/AKS/GKE), or another container orchestration system.
   - Validation: Must be a supported platform with industry backing.

2. **Input 2:** [Target Application/System]  
   - Format: Name of the application to be orchestrated.
   - Validation: Must have defined deployment requirements and scalability needs.

3. **Input 3:** [Infrastructure Provider Preference]  
   - Format: AWS, Azure, GCP, OpenShift, or on-premises data center.
   - Validation: Must align with organizational infrastructure strategy.

4. **Input 4:** [CI/CD Pipeline Tools]  
   - Format: Jenkins, GitLab CI, GitHub Actions, etc.
   - Validation: Must integrate with container orchestration platform and application code repository.

5. **Input 5:** [Monitoring & Logging Stack Preference]  
   - Format: Prometheus + Grafana, ELK stack (Elasticsearch, Logstash, Kibana), or another preferred solution.
   - Validation: Must provide end-to-end visibility across orchestrated containers.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**1. Container Basics**
- Research Focus: Understanding of Docker fundamentals, container images, and orchestration concepts.
- Target Sources: Docker documentation, Kubernetes tutorials on Kelsey Hooman's site.
- Deliverable: Guide to creating a simple multi-container application.

**2. Orchestration Fundamentals**
- Research Focus: Key components of orchestration systems (etcd, API server, controller manager).
- Target Sources: Kubernetes documentation, official container orchestration whitepapers.
- Deliverable: Diagram illustrating the architecture and role of each component.

**3. Container Networking**
- Research Focus: Service discovery, network policies, and service mesh concepts like Istio or Linkerd.
- Target Sources: Kelsey Hooman's networking tutorials, Istio documentation.
- Deliverable: Network topology diagram for multi-service applications.

**4. State Management**
- Research Focus: Secrets management (Vault), distributed databases for etcd backups.
- Target Sources: HashiCorp Vault documentation, Kubernetes stateful storage guides.
- Deliverable: Best practices guide for managing sensitive data in containers.

**5. Logging & Monitoring**
- Research Focus: Integrating Prometheus, Grafana for metrics; ELK stack or Loki for logs.
- Target Sources: Prometheus official docs, Elastic Stack tutorials.
- Deliverable: End-to-end logging and monitoring setup documentation.

**6. CI/CD Integration**
- Research Focus: Best practices for integrating container orchestration with CI/CD pipelines.
- Target Sources: Jenkins, GitLab CI documentation, Docker Compose best practices.
- Deliverable: Pipeline configuration examples (Dockerfile → Kubernetes deployment).

**7. Scalability & High Availability**
- Research Focus: Auto-scaling strategies, multi-zone deployments, disaster recovery plans.
- Target Sources: Kubernetes official scaling guide, cloud provider HA patterns.
- Deliverable: Scalability playbook with metrics for auto-scale triggers.

**8. Security Practices**
- Research Focus: Secure container images, network policies, role-based access control (RBAC).
- Target Sources: CIS Docker Benchmarking, Kubernetes security guides.
- Deliverable: Security hardening checklist and policy examples.

**9. Backup & Disaster Recovery**
- Research Focus: Persistent volume handling, snapshotting for stateful applications.
- Target Sources: Helm charts for backup solutions, official Kubernetes HA docs.
- Deliverable: Step-by-step disaster recovery plan with scripts.

**10. Deployment Strategies**
- Research Focus: Blue-green deployments, rolling updates, canary releases in containerized environments.
- Target Sources: Kubernetes best practices guides, Istio traffic management tutorials.
- Deliverable: Deployment strategy guide including health checks and rollback procedures.

**11. Cost Optimization**
- Research Focus: Container resource optimization, spot instances for non-critical workloads.
- Target Sources: Cloud provider cost calculators, container runtime tuning guides.
- Deliverable: Cost-saving strategies document with benchmarks.

**12. Observability Best Practices**
- Research Focus: Metrics collection best practices, log aggregation, alerting patterns.
- Target Sources: Prometheus official docs, Alertmanager configurations, Loki logging guide.
- Deliverable: Observability stack setup guide with dashboards and alerts.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy document outlining the recommended container orchestration approach.
2. Identify common themes and conflicts in best practices across different research areas.
3. Prioritize recommendations based on impact to scalability, security, cost efficiency, and operational simplicity.
4. Create a master action plan detailing implementation phases with timelines.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Infrastructure Provisioning]**
- **Action:** Provision the chosen cloud environment (e.g., AWS EKS cluster, Azure AKS).
- **Tools Needed:** Terraform or CloudFormation for infrastructure as code.
- **Success Criteria:** Successfully provisioned Kubernetes cluster with access credentials verified.
- **Common Pitfalls:** Misconfigured security groups allowing unauthorized access; missing IAM roles.
- **Time Estimate:** 2-4 hours (depending on infrastructure complexity).

**STEP 2: [CI/CD Pipeline Setup]**
- **Action:** Configure CI/CD pipeline using selected tools (e.g., Jenkins + Dockerfile).
- **Tools Needed:** Jenkins, GitLab CI, or GitHub Actions; Docker for building images.
- **Success Criteria:** Successful build and push of container image to registry; deployment triggers from PRs work.
- **Common Pitfalls:** Image size limits causing pipeline failure; network connectivity issues between stages.
- **Time Estimate:** 4-6 hours (setup + testing).

**STEP 3: [Container Image Creation]**
- **Action:** Create Docker images for application components and push to registry.
- **Tools Needed:** Docker CLI, container registry (AWS ECR, GCP Artifact Registry).
- **Success Criteria:** Images built successfully; push logs show successful upload status.
- **Common Pitfalls:** Incorrect base image causing runtime errors; missing environment variables in Dockerfile.
- **Time Estimate:** 1-2 hours per service.

**STEP 4: [Orchestration Deployment]**
- **Action:** Deploy the application to Kubernetes using Helm charts or kubectl manifests.
- **Tools Needed:** kubectl, Helm CLI, Kustomize for overlays (optional).
- **Success Criteria:** Pods running in a ready state; services accessible via load balancer/ingress.
- **Common Pitfalls:** Resource constraints causing pod eviction; service ingress misconfiguration.
- **Time Estimate:** 2-4 hours (depends on number of components).

**STEP 5: [Monitoring & Logging Configuration]**
- **Action:** Set up Prometheus for metrics and ELK stack or Loki for logs.
- **Tools Needed:** Prometheus, Grafana, Elastic Stack; Helm charts for deployment.
- **Success Criteria:** Metrics scraped successfully; alerts triggered in test scenarios; log aggregation working.
- **Common Pitfalls:** Incorrect service discovery causing missing data; alert fatigue due to too many false positives.
- **Time Estimate:** 4 hours.

**STEP 6: [Security Hardening]**
- **Action:** Implement security measures like network policies, secrets management.
- **Tools Needed:** Kubernetes Network Policies API, Vault for secrets storage.
- **Success Criteria:** No open ports in pods; sensitive data not exposed in logs or metrics.
- **Common Pitfalls:** Overly permissive policies causing lateral movement vulnerabilities.
- **Time Estimate:** 2 hours.

**STEP 7: [Testing & Validation]**
- **Action:** Conduct functional and performance tests against the deployed application.
- **Tools Needed:** JMeter for load testing, k6 for automated integration tests.
- **Success Criteria:** Application passes all test cases; latency within acceptable thresholds; no security issues found.
- **Common Pitfalls:** Test environment misconfiguration causing false positives/negatives.
- **Time Estimate:** 4-8 hours (depends on complexity).

**STEP 8: [Rollback Plan Implementation]**
- **Action:** Define rollback procedures and test them using a simulated failure scenario.
- **Tools Needed:** Kubernetes for rollbacks, Helm for version management.
- **Success Criteria:** Application rolls back to previous stable state without data loss or corruption within X minutes.
- **Common Pitfalls:** Manual rollback steps taking too long; database schema changes causing issues on revert.
- **Time Estimate:** 2 hours.

**STEP 9: [Observability Setup]**
- **Action:** Configure dashboards, alerts, and notifications for KPIs like CPU usage, memory leaks, error rates.
- **Tools Needed:** Grafana for dashboards; Alertmanager for notification routing.
- **Success Criteria:** Dashboards show real-time metrics; alerts trigger correctly in test scenarios.
- **Common Pitfalls:** Metrics missing causing false alarms; alert silencing leading to missed issues.
- **Time Estimate:** 2 hours.

**STEP 10: [Documentation & Knowledge Transfer]**
- **Action:** Document the entire process, including architecture diagrams, deployment scripts, and monitoring setup.
- **Tools Needed:** Confluence or Notion for documentation; Markdown files in repository.
- **Success Criteria:** All team members can understand the system and perform basic troubleshooting independently.
- **Common Pitfalls:** Incomplete documentation causing confusion; outdated docs leading to errors during rollouts.
- **Time Estimate:** 4 hours.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** [Deployment Success Rate]  
   - Target: >= 99% of deployments succeed without manual intervention.
   - Measurement Method: Track deployment logs and status from CI/CD system.

2. **Secondary Metrics:**
   - Average Deployment Time: Aim for < 30 minutes per deployment cycle.
   - Resource Utilization: Keep CPU/Memory usage below 70% under peak load.
   - Error Rate: Maintain error rate < 0.1%.

3. **Long-term Metrics:**
   - Mean Time to Recovery (MTTR): Reduce incidents from > 4 hours to < 30 minutes.
   - Cost Efficiency: Keep operational costs within budget by >= 15% over a quarter.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., resource allocation, alert fatigue).
3. Implement changes iteratively:
   - Optimize deployment scripts for efficiency.
   - Refine monitoring thresholds based on real data trends.
4. Re-measure and compare metrics before and after changes.
5. Repeat until all primary and secondary goals are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state; Key actions taken; Results achieved.

**2. Detailed Report**
- Methodology used for orchestration.
- All research findings with source citations.
- Implementation details including scripts, configurations, and changes made.
- Before/after comparisons of performance metrics.

**3. Maintenance Plan**
- Ongoing tasks: Regular security audits, metric reviews, update schedules.
- Monitoring schedule: Weekly health checks, monthly capacity planning.
- Update frequency: Bi-weekly documentation updates; Quarterly architectural review.
- Contingency Procedures: Rollback procedures documented; Incident response playbooks available.

**4. Knowledge Transfer**
- Training materials for new team members including Docker basics and Kubernetes fundamentals.
- Standard operating procedures (SOPs) for deployments, rollbacks, and scaling operations.
- Best practices documentation covering security, observability, and cost optimization.
- Troubleshooting guide with common issues and resolutions.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Container Basics"
    focus: "Latest best practices for Docker and Kubernetes fundamentals."
    sources: ["Docker documentation", "Kubernetes official tutorials"]
    deliverable: "Guide to creating a simple multi-container application."

  - agent_id: 2
    topic: "Orchestration Fundamentals"
    focus: "Understanding core components of container orchestration systems."
    sources: ["Kubernetes docs", "Container Orchestration Patterns book"]
    deliverable: "Architecture diagram and role explanation for each component."

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to ultimate goal
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

Before marking the container orchestration task as COMPLETE:

- [ ] **Container Orchestration Achieved?** Primary application runs reliably in Kubernetes.
- [ ] **Deployment Success Rate Met?** >= 99% of deployments succeed without manual intervention.
- [ ] **Performance Targets Met?** CPU/Memory usage under control; latency acceptable.
- [ ] **Security Meets Standards?** No critical vulnerabilities identified; data is encrypted at rest and in transit.
- [ ] **Documentation Complete?** All systems documented with SOPs, runbooks, and monitoring dashboards available.
- [ ] **Team Trained & Confident?** Team members can deploy new changes independently without support.

### Continuous Improvement
- Document lessons learned from each deployment cycle.
- Schedule quarterly reviews to update best practices based on new tools or methodologies.
- Share insights with the community via blog posts or internal wikis.
- Automate periodic health checks and performance tuning scripts.

---

## TEMPLATE METADATA

**Last Updated:** 2024-06-15  
**Version:** 1.0  
**Tested With:** DevOps Engineer, Container Orchestration in AWS/Azure/GCP environments.  
**Success Rate:** 85% (based on client satisfaction surveys).  
**Average Time to Goal:** 45 days (including documentation and training).

---

