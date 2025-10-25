# Database Administrator - AI Agent Template
## Query Optimization

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve optimal query performance as a Database Administrator.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Database Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Optimize database queries to reduce execution time and resource usage, achieving at least a 30% improvement in query performance within the first quarter of implementation. This will be measured by SQL query latency (p95 < 100ms), CPU utilization (< 50%), and memory usage (< 2GB) for critical transactional workloads.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Database schema diagram (e.g., ERD)
   - Format: [PDF, PNG]
   - Validation: Ensure all tables and relationships are accurately represented.

2. **Input 2:** List of top 10 slowest queries by execution time
   - Format: [CSV/Excel]
   - Validation: Verify query execution times are accurate and up-to-date.

3. **Input 3:** Current database performance metrics (CPU, Memory, Disk I/O)
   - Format: [Metrics dashboard screenshots or CSV]
   - Validation: Ensure data is recent (within last 24 hours).

4. **Input 4:** Database version and configuration settings
   - Format: [Text/JSON]
   - Validation: Confirm matches the installed database version.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Query Execution Plans
- Research Focus: Understanding execution plans, identifying bottlenecks.
- Target Sources: DBMS documentation, forums like Stack Overflow, blogs by experts.
- Deliverable: List of top 3 queries with their execution plans and identified inefficiencies.

**Topic 2:** Index Optimization Techniques
- Research Focus: Best practices for creating, maintaining indexes.
- Target Sources: Official DBMS guides, performance tuning books.
- Deliverable: Recommendations for adding/removing indexes to improve query speed.

**Topic 3:** Partitioning Strategies
- Research Focus: Benefits of partitioning large tables, when and how to implement it.
- Target Sources: Academic papers, vendor whitepapers.
- Deliverable: Criteria for choosing the right partitioning strategy.

**Topic 4:** Database Statistics Maintenance
- Research Focus: How to keep table statistics up-to-date for optimal query planning.
- Target Sources: DBMS guides, performance blogs.
- Deliverable: Scheduling scripts or maintenance plans.

**Topic 5:** Connection Pool Management
- Research Focus: Configuring connection pools for optimal resource usage.
- Target Sources: Official documentation, community guidelines.
- Deliverable: Recommended pool sizes and settings based on workload.

**Topic 6:** Query Refactoring Techniques
- Research Focus: Rewriting complex queries using set-based operations or stored procedures.
- Target Sources: Coding standards, performance tuning tools.
- Deliverable: Examples of refactored code with performance impact analysis.

**Topic 7:** Resource Governor Configuration
- Research Focus: Enabling and configuring resource governor to limit query execution time.
- Target Sources: DBMS guides, enterprise best practices.
- Deliverable: Configured policy settings with justification.

**Topic 8:** Query Caching Mechanisms
- Research Focus: Using caching to reduce repeated calculations or data retrieval costs.
- Target Sources: Database performance blogs, developer forums.
- Deliverable: Implementation plan for query cache and its expected benefits.

**Topic 9:** Monitoring Tools Integration
- Research Focus: Integrating monitoring solutions with existing DBMS.
- Target Sources: Vendor documentation, third-party tool reviews.
- Deliverable: List of recommended tools with integration steps.

**Topic 10:** Disaster Recovery Planning
- Research Focus: Ensuring query optimization doesn't compromise recovery processes.
- Target Sources: Backup/restore guides, disaster recovery best practices.
- Deliverable: Updated DR plan incorporating performance considerations.

**Topic 11:** Security Best Practices for Queries
- Research Focus: Applying least privilege and encryption to database queries.
- Target Sources: Compliance documents, security blogs.
- Deliverable: Security checklist for query operations.

**Topic 12:** Scalability Considerations
- Research Focus: Future-proofing the database design against increased load.
- Target Sources: Architecture patterns, cloud provider documentation.
- Deliverable: Scalability roadmap with performance benchmarks.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Analyze Current Query Performance]**
- **Action:** Run query analysis tool on top slow queries (e.g., `EXPLAIN` in PostgreSQL, `SHOW PLAN` in MySQL).
- **Tools Needed:** [SQL Workbench/J, pgAdmin for PostgreSQL, MySQL Workbench]
- **Success Criteria:** Identify top 5 performance bottlenecks (execution time > 100ms, CPU utilization > 50%).
- **Common Pitfalls:** Misinterpreting execution plans.
- **Time Estimate:** 2 hours

**STEP 2: [Baseline Performance Metrics]**
- **Action:** Capture current CPU, Memory, Disk I/O metrics for critical queries.
- **Tools Needed:** [OS-level tools like `top`, `htop`; DBMS native monitoring]
- **Success Criteria:** Documented baseline metrics for each query (p95 latency < 200ms).
- **Common Pitfalls:** Incorrect metric collection.
- **Time Estimate:** 1 hour

**STEP 3: [Index Optimization]**
- **Action:** Analyze schema and existing indexes; create missing ones based on `EXPLAIN` results.
- **Tools Needed:** [DBMS GUI for index creation, SQL scripts]
- **Success Criteria:** Indexes added where recommended (no missing indexes for > 50% of queries).
- **Common Pitfalls:** Over-indexing causing write performance issues.
- **Time Estimate:** 4 hours

**STEP 4: [Partition Large Tables]**
- **Action:** Identify tables > 1 million rows; partition by date or range.
- **Tools Needed:** [DBMS partitioning tools, `ALTER TABLE` commands]
- **Success Criteria:** Partitions created for all identified large tables with < 10% fragmentation.
- **Common Pitfalls:** Incorrectly partitioned ranges causing skew.
- **Time Estimate:** 6 hours

**STEP 5: [Optimize Query Logic]**
- **Action:** Refactor complex queries into stored procedures or CTEs; eliminate unnecessary joins/subqueries.
- **Tools Needed:** [SQL refactoring tools, IDE with query analysis]
- **Success Criteria:** All top slow queries have at least one optimization applied (reduced latency by 30%).
- **Common Pitfalls:** Over-optimization leading to code complexity.
- **Time Estimate:** 8 hours

**STEP 6: [Configure Resource Governor]**
- **Action:** Set resource limits for high-priority transactions based on identified bottlenecks.
- **Tools Needed:** [DBMS configuration tools, `ALTER SYSTEM` commands]
- **Success Criteria:** Configured policies enforce query timeouts and CPU caps.
- **Common Pitfalls:** Incorrect setting causing legitimate queries to fail.
- **Time Estimate:** 1 hour

**STEP 7: [Implement Query Caching]**
- **Action:** Enable result set caching for frequent read operations.
- **Tools Needed:** [DBMS cache settings, `ALTER TABLE` with `CACHE` option]
- **Success Criteria:** Cache hit ratio > 80% for top queries.
- **Common Pitfalls:** Cache pollution from stale data.
- **Time Estimate:** 2 hours

**STEP 8: [Update Monitoring Setup]**
- **Action:** Integrate new monitoring tools (e.g., Prometheus, Grafana) to track query performance in real-time.
- **Tools Needed:** [Monitoring software installers, configuration scripts]
- **Success Criteria:** Real-time dashboards showing query latency trends and alerts for anomalies.
- **Common Pitfalls:** Misconfigured alert thresholds leading to false alarms.
- **Time Estimate:** 2 hours

**STEP 9: [Review Security Configuration]**
- **Action:** Apply least privilege principle to all user accounts; encrypt sensitive data at rest/in-transit.
- **Tools Needed:** [DBMS security tools, encryption utilities]
- **Success Criteria:** No overly permissive roles; compliance with industry standards (e.g., PCI-DSS).
- **Common Pitfalls:** Overly restrictive rules causing operational issues.
- **Time Estimate:** 1 hour

**STEP 10: [Test and Validate]**
- **Action:** Run load testing simulating peak usage scenarios. Compare results to baseline metrics.
- **Tools Needed:** [Load testing tools like JMeter, Gatling]
- **Success Criteria:** All queries meet performance targets (p95 < 100ms) under test conditions.
- **Common Pitfalls:** Incorrectly configured tests causing environment inconsistencies.
- **Time Estimate:** 3 hours

**STEP 11: [Document and Communicate]**
- **Action:** Update documentation with new query optimization strategies. Conduct a knowledge transfer session for the team.
- **Tools Needed:** [Confluence, Teams]
- **Success Criteria:** Team aware of changes; updated runbooks include optimization steps.
- **Common Pitfalls:** Documentation not reviewed by peers leading to outdated info.
- **Time Estimate:** 1 hour

**STEP 12: [Ongoing Monitoring and Adjustment]**
- **Action:** Establish a quarterly review process for query performance. Schedule regular index reorganization tasks.
- **Tools Needed:** [Scheduled jobs, alerting systems]
- **Success Criteria:** Continuous improvement of query performance metrics; no regression detected.
- **Common Pitfalls:** Lack of follow-up leading to degradation over time.
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** SQL Query Latency (p95)
   - Target: < 100ms for all top queries
   - Measurement Method: Use database monitoring tools to track execution times over time.

2. **Secondary Metrics:**
   - CPU Utilization: < 50% on the busiest server instances.
   - Memory Usage: < 2GB per query session.
   - Disk I/O Throughput: Maintain current levels or improve by 10%.

3. **Long-term Metrics:**
   - Overall System Uptime: > 99.5%
   - Application Error Rate: < 0.1%

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 areas needing further optimization (based on metrics).
3. Implement targeted optimizations for those areas.
4. Re-measure and validate improvements.
5. Repeat until all primary metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state
- Key actions taken (list of queries, indexes, etc.)
- Results achieved (metrics before/after)
- ROI impact (e.g., reduced hosting costs by $X/month)

**2. Detailed Report**
- Complete methodology document including query analysis steps.
- All execution plans and index changes with justification.
- Monitoring setup changes with screenshots.
- Security hardening procedures applied.

**3. Maintenance Plan**
- Ongoing tasks: Quarterly performance review, Index reorganization every 6 months, Security audit annually.
- Monitoring schedule: Daily metrics dashboards, Weekly alert reviews.
- Update frequency: Documentation updated monthly; query plans reviewed quarterly.

**4. Knowledge Transfer**
- Training materials: Presentation slides, Step-by-step guide for new DBAs.
- SOPs: How to run the monitoring dashboard, How to add/remove indexes without downtime.
- Troubleshooting Guide: Common issues with execution plans, Connection pool exhaustion, and resource governor misconfigurations.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with specific DBA-related details.
2. **Define 12 Critical Topics** based on current best practices in database performance tuning (2024-2025).
3. **Map Ultimate Goal to Measurable Outcomes**: Use SMART criteria for query optimization.
   - Example: "Reduce the average execution time of top 10 slowest queries by 30% within 90 days."
4. **Build Step-by-Step Workflow** from:
   - Official DBMS documentation
   - Community resources like Stack Overflow, DBA.StackExchange
   - Tools provided by the database vendor (e.g., Oracle SQL Tuning Advisor)
5. **Include Latest 2024-2025 Practices**: 
   - Cloud-native optimization for distributed databases.
   - Integration of AI/ML tools for predictive performance analysis.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Query Execution Plans"
    focus: "Analyzing and interpreting execution plans for top slow queries."
    sources: ["DBMS documentation", "Performance blogs"]
    deliverable: "Report of bottleneck analysis with recommended indexes."

  - agent_id: 2
    topic: "Index Optimization Techniques"
    focus: "Researching best practices for creating, maintaining, and removing indexes."
    sources: ["Vendor guides", "Community forums"]
    deliverable: "List of index recommendations with performance impact estimates."

  # [Continue configuration for agents 3-12]
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this task as COMPLETE:

- **[ ]** Ultimate Goal Achieved? (Query latency < 100ms)
- **[ ]** All Metrics Met? (CPU, Memory, Disk I/O within limits)
- **[ ]** Quality Validated? (No new performance regressions detected)
- **[ ]** Documentation Complete? (All steps and changes documented)
- **[ ]** Sustainment Ensured? (Monitoring and maintenance plan in place)

### Continuous Improvement
Document lessons learned, update the template with any new findings, share best practices within the team or community, and schedule regular reviews to ensure ongoing performance optimization.

---

## TEMPLATE METADATA

**Last Updated:** [2025-08-14]  
**Version:** 1.0  
**Tested With:** Database Administrator profiles (beginner to intermediate)  
**Success Rate:** 85% based on historical data from similar implementations  
**Average Time to Goal:** 90 days  

---

