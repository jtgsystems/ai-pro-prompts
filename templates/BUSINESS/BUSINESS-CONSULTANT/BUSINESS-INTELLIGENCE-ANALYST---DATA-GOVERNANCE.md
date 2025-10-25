# Business Intelligence Analyst - AI Agent Template
## Data Governance

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve data governance as a Business Intelligence Analyst.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Business Intelligence Analyst"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Establish and maintain robust data governance framework that ensures data quality, security, compliance, accessibility, and usability across all business intelligence processes.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Organizational data catalog]
   - Format: CSV/Excel or database schema
   - Validation: Ensure completeness of data lineage and ownership

2. **Input 2:** [Data quality standards and KPIs]
   - Format: Defined by organization (e.g., 95% accuracy)
   - Validation: Documented in business intelligence policy documents

3. **Input 3:** [Regulatory requirements for data governance]
   - Format: GDPR, HIPAA, etc.
   - Validation: Verified against latest regulations from year 2024

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Data Lineage and Provenance
- Research Focus: Techniques for tracing data origins through transformations
- Target Sources: Apache Atlas, Talend Open Studio documentation
- Deliverable: Mapping of data lineage diagrams with provenance metadata

**Topic 2:** Master Data Management (MDM)
- Research Focus: Strategies for defining and governing master records
- Target Sources: MDM platforms like Informatica MDM or IBM InfoSphere MDM
- Deliverable: Proposed MDM framework with governance board structure

**Topic 3:** Data Quality Framework
- Research Focus: Metrics, processes, and tools for assessing data quality
- Target Sources: Data quality software reviews (e.g., Talend Data Quality)
- Deliverable: KPI dashboard template and implementation plan

**Topic 4:** Security and Access Control
- Research Focus: Encryption standards, role-based access control, audit trails
- Target Sources: NIST Cybersecurity Framework, HashiCorp Vault documentation
- Deliverable: Secure data storage architecture diagram with access policy matrix

**Topic 5:** Data Privacy Compliance
- Research Focus: GDPR, CCPA, industry-specific privacy laws
- Target Sources: Legal counsel, regulatory body guidelines
- Deliverable: Compliance checklist and remediation plan for non-compliant data

**Topic 6:** Data Stewardship Practices
- Research Focus: Roles, responsibilities, stewardship metrics
- Target Sources: Industry whitepapers, internal governance policies
- Deliverable: Stewardship role descriptions with performance indicators

**Topic 7:** Data Governance Frameworks
- Research Focus: Framework adoption strategies (e.g., ISO/IEC 21000)
- Target Sources: Academic journals, standards bodies publications
- Deliverable: Framework implementation roadmap with training plan

**Topic 8:** Master Data Management Tools
- Research Focus: Compare capabilities for data profiling, cleansing, and reconciliation
- Target Sources: G2.com, Capterra, vendor whitepapers
- Deliverable: Shortlisted tool list with feature matrix and cost analysis

**Topic 9:** Metadata Management Solutions
- Research Focus: Options for capturing, storing, and analyzing metadata
- Target Sources: Confluence documentation reviews, open-source metadata repositories (e.g., Amundsen)
- Deliverable: Proposed metadata management architecture diagram

**Topic 10:** Data Lineage Tools
- Research Focus: Technologies for visualizing data flow across systems
- Target Sources: Apache Atlas evaluation notes, Talend Lineage reports
- Deliverable: Selected tool with integration plan into existing ETL pipelines

**Topic 11:** Automated Quality Checks
- Research Focus: Implementing real-time validation and monitoring of data quality metrics
- Target Sources: Data quality software vendor demos, community examples (e.g., Great Expectations)
- Deliverable: Automation workflow design for continuous data profiling

**Topic 12:** Incident Response Protocols
- Research Focus: Procedures for handling data breaches or governance violations
- Target Sources: Industry incident response guides, legal counsel input
- Deliverable: Updated incident response playbook with test scenarios and responsibilities matrix

**Topic 13:** Data Lifecycle Management
- Research Focus: Strategies for managing data from creation through archiving/deletion
- Target Sources: Lifecycle management best practices (e.g., IBM InfoSphere)
- Deliverable: Data lifecycle policy template with retention schedules

**Topic 14:** Role-Based Access Control Implementation
- Research Focus: Configuring RBAC in platforms like Snowflake, Redshift, or BigQuery
- Target Sources: Vendor documentation, security whitepapers
- Deliverable: RBAC matrix mapping user roles to data access permissions

**Topic 15:** Data Lineage Visualization Techniques
- Research Focus: Building dashboards for visualizing complex data flows and lineage
- Target Sources: Tableau, Power BI tutorials, D3.js examples
- Deliverable: Prototype dashboard showcasing key data flows with drill-through capabilities

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Data Governance Framework Setup**
- **Action:** Document and publish the chosen governance framework (e.g., ISO/IEC 21000)
- **Tools Needed:** Confluence, Google Docs
- **Success Criteria:** Framework approved by leadership team within 2 weeks
- **Common Pitfalls:** Lack of stakeholder buy-in; incomplete documentation
- **Time Estimate:** 1 week

**STEP 2: Data Lineage and Provenance Mapping**
- **Action:** Use Apache Atlas or Talend Open Studio to map data lineage across systems
- **Tools Needed:** Apache Atlas, Talend, Visio for diagramming
- **Success Criteria:** At least 90% of key data flows mapped with provenance metadata attached
- **Common Pitfalls:** Incomplete mapping due to undocumented integrations; inaccurate provenance tags
- **Time Estimate:** 2 weeks

**STEP 3: Data Quality Framework Implementation**
- **Action:** Define KPIs for data quality (e.g., accuracy, completeness, consistency)
- **Tools Needed:** Talend Data Quality, Great Expectations
- **Success Criteria:** Automated checks deployed to monitor at least 70% of critical data sets with <1% error rate
- **Common Pitfalls:** Overly aggressive threshold settings causing false positives; lack of escalation process for quality issues
- **Time Estimate:** 3 weeks

**STEP 4: Security and Access Control Configuration**
- **Action:** Implement encryption at rest/in transit, RBAC policies across platforms
- **Tools Needed:** HashiCorp Vault, Snowflake roles, AWS IAM
- **Success Criteria:** All sensitive data encrypted; no overly permissive access granted in audit
- **Common Pitfalls:** Inconsistent encryption settings across environments; complex role hierarchies causing permission creep
- **Time Estimate:** 2 weeks

**STEP 5: Data Stewardship Program Launch**
- **Action:** Identify and train designated stewards for each data domain
- **Tools Needed:** Slack channels, JIRA tickets for training sessions, Confluence pages for knowledge sharing
- **Success Criteria:** At least 80% of key data domains have assigned stewards; training completion rate >90%
- **Common Pitfalls:** Stewards overwhelmed with responsibilities; lack of ongoing engagement and refreshers
- **Time Estimate:** Ongoing

**STEP 6: Compliance Review and Remediation Plan**
- **Action:** Conduct a gap analysis against GDPR/CCPA requirements
- **Tools Needed:** Compliance checklists (e.g., NIST), Data protection impact assessments (DPIAs)
- **Success Criteria:** All identified gaps remediated with documented mitigation plans; audit compliance score >95%
- **Common Pitfalls:** Non-compliant data stored in unmonitored locations; incomplete DPIA documentation
- **Time Estimate:** 1 month

**STEP 7: Metadata Management System Deployment**
- **Action:** Implement metadata repository and tagging strategy
- **Tools Needed:** Amundsen, Confluence, DataHub
- **Success Criteria:** At least 85% of datasets tagged with relevant metadata; automated ingestion of new data into the system
- **Common Pitfalls:** Inconsistent metadata definitions; low adoption by data consumers
- **Time Estimate:** 2 weeks

**STEP 8: Automated Quality Checks and Monitoring**
- **Action:** Set up real-time quality monitoring using Great Expectations or Talend
- **Tools Needed:** Great Expectations, Grafana dashboards, PagerDuty for alerts
- **Success Criteria:** Alerts triggered on data breaches with automatic escalation to incident response team; <5% of checks failing over 30 days
- **Common Pitfalls:** Alert fatigue from too many thresholds; lack of clear ownership for alert responders
- **Time Estimate:** Ongoing

**STEP 9: Incident Response and Data Breach Procedures**
- **Action:** Develop and test incident response playbook for data breaches or governance violations
- **Tools Needed:** JIRA tickets, Tableau dashboards for monitoring, Slack notifications for real-time updates
- **Success Criteria:** Incident response drills completed quarterly; time to respond to a breach < 1 hour
- **Common Pitfalls:** Incomplete runbooks; lack of regular practice leading to knowledge decay
- **Time Estimate:** Ongoing

**STEP 10: Data Lifecycle Management Policy Implementation**
- **Action:** Define and document policies for data creation, use, archiving, and deletion
- **Tools Needed:** Confluence, GRC tools (e.g., RSA Archer)
- **Success Criteria:** Policies approved by governance board; documented processes integrated into workflows
- **Common Pitfalls:** Overly complex policies causing resistance; lack of automation in enforcement
- **Time Estimate:** 2 weeks

**STEP 11: Data Governance Training and Awareness**
- **Action:** Conduct training sessions for data owners, stewards, and end-users on new governance practices
- **Tools Needed:** Teams meetings, LMS platforms (e.g., Moodle), Knowledge Base articles
- **Success Criteria:** Training completion rate >90%; post-training assessment shows knowledge retention >80%
- **Common Pitfalls:** Lack of follow-up assessments; limited participation due to scheduling conflicts
- **Time Estimate:** 1 month

**STEP 12: Continuous Improvement and Monitoring**
- **Action:** Establish a governance council to review performance metrics quarterly and identify areas for improvement
- **Tools Needed:** GRC software, Power BI dashboards, JIRA tickets for continuous improvement projects
- **Success Criteria:** Identified initiatives implemented within 3 months; measurable improvements in data quality scores >10%
- **Common Pitfalls:** Lack of regular council meetings; escalation delays causing prolonged issues
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Data Governance Scorecard
   - Target: 90% compliance with governance framework
   - Measurement Method: Quarterly scorecard using GRC tools (e.g., RSA Archer)

2. **Secondary Metrics:**
   - **Data Quality Index:** Aim for >95% accuracy and completeness across key metrics
     - Measurement Method: Automated quality checks from Great Expectations
   - **Security Posture Score:** Maintain 0 critical vulnerabilities in annual audits
     - Measurement Method: Security audit reports, penetration testing results
   - **Stewardship Engagement Rate:** >80% of stewards participating in quarterly knowledge sharing sessions

3. **Long-term Metrics:**
   - **Data Drift Detection Rate:** Measure number of data quality issues detected before they impact downstream processes
     - Measurement Method: Logs from automated quality monitoring tools
   - **Incident Response Time:** Average time to respond and contain a breach
     - Measurement Method: Incident response logs, SLA compliance

### Iterative Improvement Loop
1. Measure current performance against targets quarterly
2. Identify top 3 improvement opportunities through governance council reviews
3. Implement changes (e.g., new quality checks, enhanced training)
4. Re-measure to confirm improvements achieved
5. Repeat annually or as needed based on organizational changes

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Data Governance Framework Documentation**
- Current state vs. target state assessment
- Full framework documentation with ownership assigned

**2. Data Quality Dashboard**
- Live dashboard showing real-time quality metrics (accuracy, completeness)
- Trend analysis of data quality over time

**3. Security Posture Report**
- Inventory of all sensitive data elements and encryption status
- Summary of security findings from last audit and remediation progress

**4. Compliance Audit Report**
- Detailed report showing compliance with GDPR/CCPA requirements
- Action items for any identified gaps with timelines

**5. Governance Council Minutes**
- Regular meeting minutes capturing decisions, action items, and updates on key metrics
- Distribution list of all stakeholders

**6. Training Records**
- Attendance sheets and assessment scores from training sessions
- Updated curriculum reflecting latest governance practices

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content.
2. **Define 15 Critical Topics** based on:
   - Industry standards and certifications (e.g., CIPP, CAGI)
   - Latest trends in data governance tools and technologies
   - Regulatory requirements specific to industry verticals
   - Methodology best practices from leading frameworks

3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria.
4. **Build Step-by-Step Workflow** incorporating:
   - Industry playbooks (e.g., NIST Cybersecurity Framework)
   - Expert practitioner processes shared through webinars and conferences
   - Tool vendor best practices for their platforms

5. **Include Latest 2024-2025 Practices** such as:
   - Integration of AI/ML models into data quality monitoring
   - Real-time lineage tracking using streaming technologies (e.g., Apache Kafka)
   - Dynamic access control based on behavior analytics

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Data Lineage and Provenance"
    focus: "Latest techniques for tracing data origins through transformations"
    sources: ["Apache Atlas documentation", "Talend Open Studio tutorials"]
    deliverable: "Lineage diagrams with provenance metadata"

  - agent_id: 2
    topic: "Master Data Management (MDM)"
    focus: "Strategies for defining and governing master records"
    sources: ["IBM InfoSphere MDM guides", "Industry case studies"]
    deliverable: "Proposed MDM framework with governance board structure"

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority (e.g., academic research > vendor documentation)
  4. Prioritize recommendations by impact to governance framework and feasibility
  5. Generate unified recommendation report with implementation roadmap
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this template as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Data governance framework operational across all data domains
- [ ] **All Metrics Met?** Governance Scorecard >90%, Data Quality Index >95%, Security Posture Score 0 critical findings
- [ ] **Quality Validated?** All documentation reviewed by leadership and audit team; testing completed on automated processes
- [ ] **Documentation Complete?** All deliverables (framework docs, dashboards, reports) stored in approved repository with version control
- [ ] **Sustainability Ensured?** Training records updated; governance council schedule established with clear meeting cadence

### Continuous Improvement
- Document lessons learned from each quarterly review in a knowledge base
- Update the template annually to reflect new regulations and technologies
- Share best practices and insights with peer organizations through webinars or blogs
- Schedule periodic (quarterly) re-evaluation of success metrics against business objectives

