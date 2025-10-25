# DevOps Engineer - AI Agent Template
## Infrastructure as Code Setup

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a secure, scalable, and maintainable cloud infrastructure setup using Infrastructure as Code (IaC).

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "DevOps Engineer"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve a fully automated, version-controlled, and scalable cloud infrastructure setup that supports continuous deployment pipelines with 99.9% uptime and zero manual configuration drift.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** Target Cloud Provider (AWS, Azure, Google Cloud)
   - Format: String (e.g., AWS, Azure)
   - Validation: Must be a valid cloud provider listed by industry standards.
2. **Input 2:** Desired Region/Availability Zone(s) for deployment
   - Format: List of regions or AZs
   - Validation: Must match supported regions for the selected cloud provider.

3. **Input 3:** Current Application Architecture (e.g., microservices, monolith)
   - Format: Description in YAML/JSON format
   - Validation: Must align with industry standards for your application type.
4. **Input 4:** Deployment Frequency Requirements (Daily, Weekly, Continuous)
   - Format: String (Daily, Weekly, Continuous)
   - Validation: Must be achievable within the selected cloud provider's CI/CD capabilities.

---

### Initial Assessment Checklist
- [ ] Verify all required inputs received and correctly formatted.
- [ ] Validate that the target cloud region(s) are available for requested resources.
- [ ] Identify immediate red flags such as unsupported services or licensing issues.
- [ ] Establish baseline metrics like current infrastructure uptime, deployment frequency, and mean time to recovery (MTTR).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Infrastructure as Code Tools
- Research Focus: Latest open-source IaC solutions and their capabilities.
- Target Sources: GitHub trending repos, official documentation, community forums.
- Deliverable: List of top tools with comparison matrix.

**Topic 2:** Version Control Integration
- Research Focus: Best practices for integrating IaC scripts with version control systems (e.g., Git).
- Target Sources: DevOps blogs, CI/CD tool docs.
- Deliverable: Recommended branching strategy and commit message standards.

**Topic 3:** Security Configuration Standards
- Research Focus: Compliance requirements (e.g., PCI-DSS, GDPR) and secure configuration best practices.
- Target Sources: Regulatory bodies, security frameworks.
- Deliverable: Checklist of security controls for infrastructure.

**Topic 4:** Automation Tools & Pipelines
- Research Focus: CI/CD platforms that support IaC workflows.
- Target Sources: Vendor documentation, user reviews.
- Deliverable: Recommended pipeline architecture and tooling stack.

**Topic 5:** Monitoring & Logging Solutions
- Research Focus: Real-time monitoring of infrastructure changes and performance metrics.
- Target Sources: Observability vendor pages, tech blogs.
- Deliverable: List of recommended tools with integration methods.

**Topic 6:** Cost Management Strategies
- Research Focus: Techniques for optimizing cloud spend in IaC setups.
- Target Sources: Cloud provider cost calculators, budgeting frameworks.
- Deliverable: Best practices for tagging resources and setting budgets.

**Topic 7:** Disaster Recovery & High Availability Designs
- Research Focus: Design patterns for fault tolerance and disaster recovery using IaC.
- Target Sources: Architecture guides from cloud providers.
- Deliverable: Recommended configuration patterns.

**Topic 8:** Multi-Account/Multi-Region Strategies
- Research Focus: Best practices for managing infrastructures across multiple accounts or regions.
- Target Sources: Industry case studies, multi-account management docs.
- Deliverable: Template configurations and governance models.

**Topic 9:** Policy as Code (PaaS)
- Research Focus: Tools that allow defining infrastructure policies declaratively.
- Target Sources: GitHub repos, community discussions.
- Deliverable: List of policy frameworks with examples.

**Topic 10:** Testing IaC Scripts
- Research Focus: Unit testing and validation strategies for IaC code.
- Target Sources: Test automation blogs, CI tooling docs.
- Deliverable: Recommended test framework setup.

**Topic 11:** Cost Optimization Techniques
- Research Focus: Detailed breakdown of how to reduce infrastructure costs through IaC practices.
- Target Sources: Cloud provider cost optimization guides, budget management articles.
- Deliverable: Actionable steps for continuous cost reduction.

**Topic 12:** Integration with Existing CI/CD Pipelines
- Research Focus: How to integrate new IaC workflows into existing CI/CD pipelines without disruption.
- Target Sources: Migration case studies, user forums.
- Deliverable: Step-by-step migration guide and best practices.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy prioritizing tools with the highest community adoption and feature alignment with the ultimate goal.
2. Identify conflicts in tool recommendations (e.g., one tool being open-source but another offering premium support).
3. Prioritize recommendations by impact to achieving the primary objective, focusing on security, scalability, and maintainability first.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Choose primary IaC tooling based on research (e.g., Terraform, AWS CloudFormation).
   - Tools Needed: Terraform CLI, Git repository for code management.
   - Success Criteria: Tool is installed and version of the script matches a known good state from community standards.
   - Common Pitfalls: Using unsupported versions or configurations that are not aligned with best practices.
   - Time Estimate: 2 hours

**STEP 2: [Infrastructure Configuration]**
- **Action:** Define core infrastructure components such as VPC, subnets, security groups, and IAM roles.
   - Tools Needed: Terraform configuration files (.tf), CI/CD pipeline for deployment.
   - Success Criteria: Infrastructure is fully provisioned in the target cloud region with no errors during apply phase.
   - Common Pitfalls: Misconfigured network settings leading to connectivity issues or overly permissive security groups.
   - Time Estimate: 4 hours

**STEP 3: [Resource Provisioning]**
- **Action:** Add application-specific resources like EC2 instances, RDS databases, and load balancers.
   - Tools Needed: Terraform modules for each resource type, monitoring tools (e.g., CloudWatch).
   - Success Criteria: All components are correctly provisioned with appropriate tags and permissions.
   - Common Pitfalls: Missing dependencies causing resource creation failures or incorrect IAM policies leading to access issues.
   - Time Estimate: 6 hours

**STEP 4: [Testing & Validation]**
- **Action:** Run tests on the infrastructure configuration to ensure everything is set up as intended.
   - Tools Needed: Terratest, Jenkins/GitHub Actions for automated testing.
   - Success Criteria: All tests pass without critical failures and security policies are enforced correctly.
   - Common Pitfalls: Skipping integration tests leading to runtime errors in production.
   - Time Estimate: 2 hours

**STEP 5: [Deployment & Verification]**
- **Action:** Deploy the infrastructure to the target cloud environment and verify all components are operational.
   - Tools Needed: Terraform apply, automated health checks (e.g., using Prometheus).
   - Success Criteria: Infrastructure is live with no critical errors in monitoring dashboards.
   - Common Pitfalls: Manual deployment steps leading to drift from the coded state.
   - Time Estimate: 3 hours

**STEP 6: [Monitoring & Alerting Setup]**
- **Action:** Configure real-time monitoring and alerting for all resources using tools like Prometheus, Grafana, or native cloud services (e.g., CloudWatch).
   - Tools Needed: Prometheus exporters, Grafana dashboards, PagerDuty/Slack alerts.
   - Success Criteria: Alerts trigger correctly in test scenarios and metrics are collected without errors.
   - Common Pitfalls: Missing critical alerts leading to delayed incident response.
   - Time Estimate: 3 hours

**STEP 7: [Security Hardening & Compliance Checks]**
- **Action:** Apply security configurations, enable encryption at rest/in transit, and run compliance scans (e.g., CIS benchmarks).
   - Tools Needed: AWS Config Rules, HashiCorp Sentinel, OpenSCAP.
   - Success Criteria: All resources meet the defined security standards with no violations identified.
   - Common Pitfalls: Overlooking sensitive data exposure leading to potential breaches.
   - Time Estimate: 4 hours

**STEP 8: [Disaster Recovery & Failover Testing]**
- **Action:** Simulate disaster scenarios such as region failure or instance loss and verify the system recovers automatically.
   - Tools Needed: Chaos Engineering tools (e.g., Gremlin), DR testing scripts.
   - Success Criteria: Systems recover within SLA without data loss or service interruption.
   - Common Pitfalls: Inadequate backup strategies leading to data loss during recovery tests.
   - Time Estimate: 4 hours

**STEP 9: [Cost Optimization Review]**
- **Action:** Analyze cloud spend and identify opportunities for optimization based on the final IaC deployment.
   - Tools Needed: Cloud provider cost explorer, budget alerts.
   - Success Criteria: Budget is met or exceeded by a predefined margin with no manual overrides needed.
   - Common Pitfalls: Ignoring dynamic pricing models leading to unexpected costs.
   - Time Estimate: 2 hours

**STEP 10: [Documentation & Knowledge Transfer]**
- **Action:** Document the entire setup process, including IaC scripts, monitoring configurations, and disaster recovery plans.
   - Tools Needed: Confluence/Notion for documentation, Markdown templates for code comments.
   - Success Criteria: All team members can reproduce the setup with minimal guidance.
   - Common Pitfalls: Incomplete or outdated documentation leading to operational issues.
   - Time Estimate: 3 hours

---

### Quality Checkpoints
- **Checkpoint 1:** After Step 2 - Verify that all core components are correctly defined and conflict-free.
- **Checkpoint 2:** After Step 5 - Validate deployment status against predefined success criteria.
- **Checkpoint 3:** After Step 7 - Ensure compliance with security standards using automated scans.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** System Uptime
   - Target: >99.9%
   - Measurement Method: Cloud provider uptime guarantees and monitoring data.
2. **Secondary Metrics:**
   - Deployment Frequency: Achieve continuous deployments without manual intervention.
   - Resource Utilization: Maintain optimal CPU, memory, and network usage.
   - Cost Efficiency: Keep spend within 10% of budgeted amount.

### Iterative Improvement Loop
1. Measure current performance against primary metric targets.
2. Identify top 3 improvement opportunities (e.g., cost overruns, security gaps).
3. Implement changes such as adjusting instance types or tightening IAM policies.
4. Re-measure to ensure metrics are improved without regression.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state for each metric.
- Key actions taken and their impact on achieving the ultimate goal.

**2. Detailed Report**
- Full methodology document including research findings, tool selection rationale, and implementation steps.
- Comprehensive list of all IaC scripts with version history.
- Monitoring and alerting configurations with sample dashboards.

**3. Maintenance Plan**
- Weekly reviews of infrastructure health metrics.
- Monthly security compliance scans.
- Quarterly cost optimization review meetings.

**4. Knowledge Transfer**
- Training sessions for onboarding new team members.
- Standard operating procedures (SOPs) for routine maintenance tasks.
- Troubleshooting guide covering common issues encountered during setup and deployment.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE
1. **Replace all [BRACKETED] items** with the specifics of your target environment.
2. **Define 12 Critical Topics** based on your industry's latest trends, such as serverless architectures or edge computing.
3. **Map Ultimate Goal to Measurable Outcomes**: Define how you will measure success in terms of uptime, security compliance scores, and cost efficiency.

### Tool Stack Recommendations
- **Primary Tools (Free/Open-source):**
  - Terraform (for IaC)
  - Git for version control
  - Jenkins or GitHub Actions for CI/CD
  - Prometheus + Grafana for monitoring
  - OpenSCAP for compliance scanning

- **Optional/Premium Alternatives:**
  - AWS CloudFormation (optional premium alternative for AWS environments)
  - Azure Resource Manager Templates (ARM) (optional premium alternative for Azure)
  - GCP Deployment Manager (optional premium alternative for Google Cloud)

---

### Timeline to Achieve Infrastructure as Code Setup
**Week 1:** Research and Tool Selection  
- Spend first week gathering research, comparing tools, and documenting findings.

**Weeks 2-3:** Foundation & Core Configuration  
- Set up version control repository and select primary IaC tool (e.g., Terraform).

**Weeks 4-5:** Resource Provisioning & Testing  
- Define resources needed for your application and start provisioning them via scripts.

**Week 6:** Deployment, Monitoring, and Security Hardening  
- Deploy the infrastructure, configure monitoring/alerting systems, and enforce security policies.

**Weeks 7-8:** Optimization & Cost Review  
- Optimize cloud spend, review configurations against budgets, and implement any necessary changes.

**Week 9:** Documentation and Knowledge Transfer  
- Document everything thoroughly and conduct training sessions for team members.

**Week 10:** Continuous Improvement Planning
- Establish processes for ongoing monitoring, optimization, and incident response planning.

---

### Final Checklist Before Completion

- [ ] Ultimate goal of Infrastructure as Code Setup achieved.
- [ ] All metrics (uptime, cost efficiency) met or exceeded.
- [ ] Security compliance validated through automated scans.
- [ ] Documentation updated with current configurations and procedures.
- [ ] Knowledge transfer completed with all team members trained.

### Continuous Improvement
- Schedule regular reviews to update documentation and tooling based on new research or industry changes.
- Share findings with the broader DevOps community for feedback and improvement.
- Document lessons learned in migration from traditional setup methods.

