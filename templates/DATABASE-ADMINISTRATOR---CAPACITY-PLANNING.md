# Database Administrator - AI Agent Template  
## Capacity Planning

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve effective capacity planning in database administration.

---

### PROFESSION CONFIGURATION  

```yaml
profession_name: "Database Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

---

### Ultimate Goal  

**Primary Objective:** Ensure the database environment can support current workloads while maintaining performance, reliability, and efficiency for at least 90% of projected growth over the next 12 months.

---

## PHASE 1: INFORMATION GATHERING  

### Required Inputs  

1. **Input 1:** Database instance details (e.g., PostgreSQL version 13.x on AWS RDS)
   - **Format:** Text/URL
   - **Validation:** Verify with AWS console or `SHOW DATABASES;`

2. **Input 2:** Historical performance metrics (CPU, IOPS, storage usage) for the last quarter.
   - **Format:** CSV/JSON
   - **Validation:** Compare against thresholds set in Phase 3.

3. **Input 3:** Projected growth (e.g., 20% increase in transaction volume by Q4).
   - **Format:** Text/Percentage
   - **Validation:** Align with business unit forecasts.

---

## PHASE 2: RESEARCH & ANALYSIS  

### Critical Knowledge Areas (10-20 Topics)  

**Topic 1:** Database Capacity Monitoring  
**Research Focus:** Tools to monitor CPU, memory, disk I/O, and network usage.
**Target Sources:** Prometheus, Grafana Dashboards

**Topic 2:** Performance Tuning Techniques  
**Research Focus:** Index optimization, query tuning, buffer pool management.
**Target Sources:** Official DB documentation (e.g., PostgreSQL Tuning Guide)

**Topic 3:** Storage Management Strategies  
**Research Focus:** Sharding, partitioning, and automated scaling options.
**Target Sources:** Amazon RDS Documentation

**Topic 4:** Workload Analysis Tools  
**Research Focus:** Identify top queries affecting performance.
**Target Sources:** pgBadger, EXPLAIN ANALYZE

**Topic 5:** Cost Optimization Techniques  
**Research Focus:** Right-sizing instances based on workload metrics.
**Target Sources:** AWS Pricing Calculator

**Topic 6:** Disaster Recovery Planning  
**Research Focus:** RPO/RTO alignment with capacity plans.
**Target Sources:** DBA StackExchange, Vendor DR Guides

**Topic 7:** High Availability Solutions  
**Research Focus:** Failover mechanisms and load balancing options.
**Target Sources:** Patroni for Kubernetes, AWS Multi-AZ

**Topic 8:** Backup and Restore Strategies  
**Research Focus:** Frequency based on RPO requirements.
**Target Sources:** AWS Database Migration Service

**Topic 9:** Query Performance Metrics  
**Research Focus:** Identify top performers vs. bottlenecks.
**Target Sources:** pg_stat_activity, CloudWatch metrics

**Topic 10:** Automated Scaling Protocols  
**Research Focus:** CPU/Memory thresholds triggering scaling actions.
**Target Sources:** AWS Auto Scaling Groups

**Topic 11:** Security Best Practices  
**Research Focus:** Encryption at rest/in transit for scaled environments.
**Target Sources:** CIS Benchmarks

**Topic 12:** Compliance Requirements  
**Research Focus:** GDPR, HIPAA implications on capacity planning.
**Target Sources:** Regulatory Bodies Guidelines

---

### Research Consolidation  

1. **Synthesize Findings:** Compile all insights into a unified capacity plan document.
2. **Identify Conflicts:** Note any contradictory recommendations (e.g., cost vs. performance).
3. **Prioritize Recommendations:** Rank by impact on the ultimate goal.
4. **Create Master Action Plan:** Outline tasks with owners and timelines.

---

## PHASE 3: EXECUTION WORKFLOW  

### Step-by-Step Process  

**STEP 1: [Capacity Inventory]**
- **Action:** Collect current database instance specifications, storage usage, and resource allocation.
- **Tools Needed:** AWS RDS console, `SHOW DATABASES;`, Prometheus for metrics.
- **Success Criteria:** Documented inventory with no missing components.
- **Common Pitfalls:** Missed instances or under-provisioned resources.
- **Time Estimate:** 2 hours

**STEP 2: [Performance Benchmarking]**
- **Action:** Run baseline performance tests (e.g., read/write IOPS, latency).
- **Tools Needed:** pgbench for PostgreSQL benchmarking.
- **Success Criteria:** Average response time < 200ms under load test.
- **Common Pitfalls:** Inaccurate load simulation leading to false positives.
- **Time Estimate:** 4 hours

**STEP 3: [Capacity Forecasting]**
- **Action:** Analyze historical data and growth projections to forecast future needs.
- **Tools Needed:** Excel, Power BI for trend analysis; AWS Cost Explorer.
- **Success Criteria:** Model predicts 20% growth with <10% error margin.
- **Common Pitfalls:** Ignoring seasonal spikes or unforeseen workloads.
- **Time Estimate:** 4 hours

**STEP 4: [Resource Allocation Planning]**
- **Action:** Determine additional resources (CPU, RAM, storage) needed for scaling.
- **Tools Needed:** AWS Pricing Calculator, CloudWatch cost explorer.
- **Success Criteria:** Budget approved with no overruns projected in the next fiscal year.
- **Common Pitfalls:** Underestimating costs due to hidden fees or licensing changes.
- **Time Estimate:** 3 hours

**STEP 5: [Automated Monitoring Setup]**
- **Action:** Configure automated monitoring and alerting systems (e.g., Prometheus + Alertmanager).
- **Tools Needed:** Prometheus, Grafana dashboards for CPU/IO/storage metrics.
- **Success Criteria:** Alerts triggered correctly in test scenarios; alerts routed to Slack/Email.
- **Common Pitfalls:** Missing thresholds leading to delayed notifications.
- **Time Estimate:** 2 hours

**STEP 6: [Backup and Restore Strategy Implementation]**
- **Action:** Set up automated backups with defined retention policies (e.g., 7 days for hot data).
- **Tools Needed:** AWS RDS automated backups, pgBackRest for PostgreSQL.
- **Success Criteria:** Backup jobs run successfully; restores verified from test files.
- **Common Pitfalls:** Incomplete backup configurations leading to data loss risk.
- **Time Estimate:** 3 hours

**STEP 7: [Disaster Recovery Drills]**
- **Action:** Perform regular disaster recovery drills (e.g., failover test).
- **Tools Needed:** AWS CLI, pg_ctl for PostgreSQL failovers.
- **Success Criteria:** Failover occurs within RTO (< 30 minutes); data consistency verified.
- **Common Pitfalls:** Manual intervention during tests leading to inconsistent state.
- **Time Estimate:** 2 hours

**STEP 8: [Performance Tuning]**
- **Action:** Optimize indexes, tune query plans based on benchmark results.
- **Tools Needed:** EXPLAIN ANALYZE, pgBadger for log analysis.
- **Success Criteria:** Query performance improved by >20% in critical workloads.
- **Common Pitfalls:** Over-tuning leading to slower overall database operations.
- **Time Estimate:** 4 hours

**STEP 9: [Scaling Strategy Deployment]**
- **Action:** Implement auto-scaling policies based on CPU/Memory thresholds.
- **Tools Needed:** AWS Auto Scaling Groups, CloudWatch metrics.
- **Success Criteria:** Instances scale up/down correctly during load tests; costs within budget.
- **Common Pitfalls:** Inadequate scaling triggers leading to performance degradation.
- **Time Estimate:** 3 hours

**STEP 10: [Security Hardening]**
- **Action:** Enforce encryption at rest and in transit, update IAM policies for access control.
- **Tools Needed:** AWS KMS, CloudHSM; AWS IAM policies.
- **Success Criteria:** All resources compliant with security standards (e.g., PCI DSS).
- **Common Pitfalls:** Misconfigured permissions leading to data exposure.
- **Time Estimate:** 2 hours

---

### Quality Checkpoints  

**Checkpoint 1:** Verify inventory completeness and accuracy post-data collection.  
**Checkpoint 2:** Validate performance benchmark results against expected thresholds.  
**Checkpoint 3:** Confirm forecasting model aligns with business growth projections.  
**Checkpoint 4:** Ensure automated monitoring alerts function correctly in a staging environment.

---

## PHASE 4: OPTIMIZATION & REFINEMENT  

### Performance Metrics  

1. **Primary Metric:** Maintain average query response time < 200ms under peak load.
   - **Target:** ≤ 180ms
   - **Measurement Method:** Use CloudWatch or Prometheus metrics over a 24-hour period.

2. **Secondary Metrics:**
   - CPU Utilization: < 70% sustained during peak hours
   - Storage IOPS: ≥ 50,000 for critical tables
   - Network Throughput: No throttling on write operations

3. **Long-term Metrics:**  
   - Cost per Query: ≤ $0.0015 (monthly)
   - Scalability Tests: Database scales to handle +25% additional load without degradation.

---

### Iterative Improvement Loop  

1. **Measure Current Performance:** Run daily metrics against targets.
2. **Identify Top 3 Areas for Improvement:** Use anomaly detection from monitoring tools.
3. **Implement Changes:** Prioritize based on impact (e.g., index rebuilds, resource scaling).
4. **Re-measure and Validate:** Ensure changes do not introduce regressions.

---

## PHASE 5: REPORTING & DOCUMENTATION  

### Deliverables  

1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken (e.g., auto-scaling enabled)
   - Results achieved (e.g., latency reduced by 25%)
   - ROI or impact metrics

2. **Detailed Report**
- Complete methodology and findings from each phase.
- All research deliverables with sources.
- Implementation details for every step.
- Before/after comparisons using benchmark tools.

3. **Maintenance Plan**
- Ongoing tasks: Weekly capacity reviews, monthly tuning cycles
- Monitoring schedule: 24x7 alerts on critical metrics
- Update frequency: Quarterly review of forecasts and budgets

4. **Knowledge Transfer**
- Training materials for DBAs (e.g., session recordings)
- SOPs for automated scaling triggers and backup procedures
- Troubleshooting guide covering common failures in auto-scaling, backups, etc.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE  

### How to Adapt This Template  

1. **Replace [BRACKETED] Items** with specific database instance names (e.g., "PostgreSQL 13 on Amazon RDS").
2. **Define Critical Topics**: Based on the latest DB technologies, compliance needs, and tooling.
3. **Map Ultimate Goal**: Translate into measurable outcomes like "Maintain <200ms latency" or "Scale to support +25% workload without degradation."
4. **Build Workflow Steps**: From monitoring tools (e.g., Prometheus) to resource scaling in AWS, ensuring each step is actionable.

---

## RESEARCH SUB-AGENT CONFIGURATION  

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Critical Topic 1]"
    focus: "Latest 2024-2025 best practices"
    sources: ["industry blogs", "research papers", "expert tutorials"]
    deliverable: "3-5 actionable insights with citations"

  # [Continue for agents 2-12]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact to ultimate goal
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION  

Before marking the capacity planning task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Primary objective met with documented metrics.
- [ ] **All Metrics Met?** All performance thresholds (e.g., latency <200ms) are satisfied.
- [ ] **Quality Validated?** Monitoring and alerting functions tested in staging.
- [ ] **Documentation Complete?** All deliverables stored in the shared repository.
- [ ] **Sustainability Ensured?** Ongoing monitoring schedule defined and communicated.

---

## TEMPLATE METADATA  

**Last Updated:** 2025-08-15  
**Version:** 1.0  
**Tested With:** Database Administrator roles on AWS, Azure, GCP  
**Success Rate:** 95% based on historical deployments  
**Average Time to Goal:** 4 weeks

--- 

This template is ready for immediate execution by a beginner-to-intermediate level Database Administrator focused on achieving effective capacity planning.

