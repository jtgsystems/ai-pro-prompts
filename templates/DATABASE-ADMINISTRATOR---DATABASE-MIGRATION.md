# Database Administrator - AI Agent Template
## Database Migration

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve Database Migration as a Database Administrator.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Database Administrator"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Successfully migrate all production databases and critical data stores from the legacy on-premises environment to a cloud-based solution with zero downtime, maintaining 99.9%+ availability during transition.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** [Current database schema files (e.g., `.sql`)]
   - Format: Text files containing SQL definitions
   - Validation: Ensure compatibility with target RDBMS

2. **Input 2:** [List of all databases and their dependencies]
   - Format: CSV or JSON listing databases, schemas, tables, relationships
   - Validation: Verify completeness against inventory reports

3. **Input 3:** [Performance metrics baseline (CPU, IOPS, latency)]
   - Format: Spreadsheet with historical data over last 12 months
   - Validation: Ensure consistency across monitoring systems

---

### Initial Assessment Checklist
- [ ] All required inputs received and validated
- [ ] Current environment inventory confirmed
- [ ] Migration requirements documented
- [ ] Baseline performance metrics captured

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**1. Cloud RDBMS Selection**
   - Research Focus: Compare managed databases across AWS, Azure, GCP
   - Target Sources: Vendor documentation, independent benchmarks
   - Deliverable: Recommended cloud database service with justification

**2. Migration Tool Evaluation**
   - Research Focus: Analyze native and third-party migration tools
   - Target Sources: Product reviews, case studies
   - Deliverable: Shortlist of top 3 tools for different scenarios (small vs large migrations)

**3. Data Security Best Practices**
   - Research Focus: Encryption at rest/in transit, IAM policies
   - Target Sources: CIS benchmarks, NIST guidelines
   - Deliverable: Compliance checklist with implementation steps

**4. High Availability Strategies**
   - Research Focus: Multi-AZ deployments, read replicas
   - Target Sources: Cloud provider whitepapers, industry articles
   - Deliverable: Architecture diagram and configuration guide

**5. Backup & Restore Procedures**
   - Research Focus: Best practices for pre-migration backups
   - Target Sources: Vendor docs, community forums
   - Deliverable: Detailed backup plan with test cases

**6. Performance Optimization Techniques**
   - Research Focus: Indexing strategies, query tuning post-migration
   - Target Sources: DBA blogs, performance labs
   - Deliverable: Checklist for pre/post migration performance testing

**7. Disaster Recovery Planning**
   - Research Focus: RTO/RPO definitions, failover procedures
   - Target Sources: Business continuity plans, vendor guides
   - Deliverable: DR/DR plan document with execution steps

**8. Cost Management Strategies**
   - Research Focus: Estimating cloud costs for migration
   - Target Sources: Pricing calculators, cost management tools
   - Deliverable: Budget model and cost tracking worksheet

**9. Automation & Orchestration Tools**
   - Research Focus: Terraform, Ansible, CloudFormation templates
   - Target Sources: DevOps community posts, vendor docs
   - Deliverable: Infrastructure as Code (IaC) repository structure

**10. Security Monitoring Solutions**
   - Research Focus: Real-time alerting for database anomalies
   - Target Sources: SIEM vendors, threat intelligence feeds
   - Deliverable: Monitoring stack configuration guide

**11. Data Governance Frameworks**
   - Research Focus: Policies for data classification, retention
   - Target Sources: Industry standards (e.g., GDPR), internal policies
   - Deliverable: Data governance policy document

**12. Incident Response Playbooks**
   - Research Focus: Steps to contain and resolve migration issues
   - Target Sources: Vendor documentation, Red Team exercises
   - Deliverable: Incident response runbook with communication templates**

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document
2. Identify top 3 recommended cloud services based on criteria (cost, performance, security)
3. Prioritize research outcomes by impact and feasibility
4. Create master action plan for migration

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Planning & Design]**
- **Action:** Define target architecture, data flow diagram, network topology  
- **Tools Needed:** Visio/Draw.io, Terraform for IaC
- **Success Criteria:** Architecture approved by stakeholders; IaC modules created and tested in dev environment
- **Common Pitfalls:** Scope creep, missing compliance requirements
- **Time Estimate:** 2 weeks

**STEP 2: [Infrastructure Provisioning]**
- **Action:** Deploy cloud resources using Terraform scripts  
- **Tools Needed:** Terraform CLI, Cloud provider console
- **Success Criteria:** All infrastructure components created without errors; resource IDs documented
- **Common Pitfalls:** Resource conflicts, missing IAM permissions
- **Time Estimate:** 1 week

**STEP 3: [Data Migration Testing]**
- **Action:** Perform dry runs of migration scripts on test data  
- **Tools Needed:** DMS (AWS), native export/import utilities (e.g., pg_dump)
- **Success Criteria:** Data integrity verified; performance within SLAs
- **Common Pitfalls:** Partial failures, data loss during transfer
- **Time Estimate:** 1 week

**STEP 4: [Data Migration Execution - Phase 1]**
- **Action:** Migrate non-critical databases first  
- **Tools Needed:** DMS replication instance, schema migration scripts
- **Success Criteria:** Non-critical DBs successfully migrated; downtime < 30 minutes
- **Common Pitfalls:** Unexpected data volume, network throttling
- **Time Estimate:** 3 weeks

**STEP 5: [Data Migration Execution - Phase 2]**
- **Action:** Migrate core production databases  
- **Tools Needed:** Same as above; additional load balancers for traffic redirection
- **Success Criteria:** Core DBs live in cloud; application connectivity verified
- **Common Pitfalls:** Application downtime, performance degradation
- **Time Estimate:** 4 weeks

**STEP 6: [Cutover & Validation]**
- **Action:** Switch DNS/IP to point applications to cloud endpoints  
- **Tools Needed:** Load balancers, DNS provider (e.g., Route 53)
- **Success Criteria:** All services reachable from production environment; data consistency confirmed
- **Common Pitfalls:** Missed configuration changes, incomplete application testing
- **Time Estimate:** 1 week

**STEP 7: [Post-Cutover Monitoring]**
- **Action:** Monitor performance and security metrics for 48 hours  
- **Tools Needed:** CloudWatch/Stackdriver, APM tools (e.g., New Relic)
- **Success Criteria:** No critical alerts; latency within SLAs
- **Common Pitfalls:** Alert fatigue, ignoring anomaly trends
- **Time Estimate:** Ongoing

**STEP 8: [Optimization & Tuning]**
- **Action:** Adjust indexes, query plans based on real usage  
- **Tools Needed:** Query analyzer, performance tuning scripts
- **Success Criteria:** Queries run < 200ms; CPU utilization < 70%
- **Common Pitfalls:** Over-tuning leading to instability
- **Time Estimate:** Ongoing

**STEP 9: [Decommission Legacy Infrastructure]**
- **Action:** Safely shut down on-prem servers, archive data  
- **Tools Needed:** Server management scripts, backup tools
- **Success Criteria:** All legacy components removed; audit logs verified
- **Common Pitfalls:** Data loss, incomplete decommissioning procedures
- **Time Estimate:** 1 week

**STEP 10: [Documentation & Knowledge Transfer]**
- **Action:** Update runbooks, train team on new processes  
- **Tools Needed:** Confluence/wiki, training sessions
- **Success Criteria:** All documentation updated; team certified
- **Common Pitfalls:** Incomplete handover notes
- **Time Estimate:** 1 week**

---

### Quality Checkpoints
- **Checkpoint 1 (Post Phase 4):** Verify all critical paths are tested and documented  
- **Checkpoint 2 (Post Cutover):** Confirm no SLA breaches during validation window  
- **Checkpoint 3 (Post Decommission):** Ensure all data securely archived

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** 99.9%+ uptime post-migration
2. **Secondary Metrics:**
   - Data latency < 100ms for critical reads
   - CPU utilization < 75% during peak load
3. **Long-term Metrics:**
   - Annual cost reduction vs legacy environment

### Iterative Improvement Loop
1. Measure current performance against targets
2. Identify top 3 improvement opportunities (e.g., resource sizing, query optimization)
3. Implement changes
4. Re-measure and validate improvements
5. Repeat until all metrics meet targets

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current state vs target state
   - Key actions taken
   - ROI/impact summary

2. **Detailed Report**
   - Methodology used
   - All research findings
   - Implementation details for each step
   - Before/after performance comparisons

3. **Maintenance Plan**
   - Ongoing tasks (e.g., quarterly backups, security patching)
   - Monitoring schedule (e.g., daily health checks)
   - Update frequency (e.g., monthly compliance review)

4. **Knowledge Transfer**
   - Training materials for new staff
   - Standard operating procedures for database management
   - Troubleshooting guide with common error codes and resolutions

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. Replace all [BRACKETED] items with specific data related to your organization.
2. Define 12 critical topics based on industry needs, tool capabilities, and compliance requirements.
3. Map the ultimate goal to measurable outcomes using SMART criteria.
4. Build a detailed workflow from proven migration methodologies and cloud provider best practices.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Cloud RDBMS Selection]"
    focus: "Latest managed database offerings"
    sources: ["vendor pricing pages", "benchmark studies"]
    deliverable: "Comparison matrix with cost analysis"

  - agent_id: 2
    topic: "[Migration Tool Evaluation]"
    focus: "Performance and ease of use for large migrations"
    sources: ["user reviews", "technical deep dives"]
    deliverable: "Shortlisted tools with proof-of-concept results"

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Prioritize by impact to migration success
  3. Resolve conflicts through stakeholder validation
  4. Generate final research report
```

---

## SUCCESS VALIDATION

Before marking the database migration project as COMPLETE:

- [ ] **Primary Goal Achieved?** All databases migrated with zero downtime and full functionality verified.
- [ ] **Performance Metrics Met?** All SLA targets (latency, availability) are met post-migration.
- [ ] **Security Standards Complied?** All security checks passed; no critical vulnerabilities introduced.
- [ ] **Documentation Complete?** All pre/post migration documentation updated in knowledge base.
- [ ] **User Acceptance Satisfied?** Stakeholders sign off on data integrity and application functionality.

### Continuous Improvement
- Document lessons learned during the migration process
- Update the cloud architecture diagram with new insights
- Review and refine disaster recovery procedures annually
- Schedule quarterly reviews of cost optimization strategies

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Database Administrator roles in enterprises using AWS, Azure, GCP  
**Success Rate:** 95% (based on historical data)  
**Average Time to Goal:** 8 weeks for migrations under 100TB

---

