# Data Analyst - AI Agent Template
## Data Governance Implementation

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve Data Governance Implementation as a Data Analyst.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Data Analyst"
profession_category: "Technology/Analytics"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve comprehensive data governance that ensures compliance, quality, security, and accessibility of all datasets used by the organization.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** List of critical datasets in use (e.g., `/data/raw/employee_data.csv`, `/data/processed/customer_transactions.parquet`)
   - Format: File paths or database schemas
   - Validation: Ensure all file/directory exist and can be accessed.

2. **Input 2:** Data usage policies from stakeholders (e.g., marketing team's CRM usage)
   - Format: Document URLs or internal policy documents.
   - Validation: Confirm they are the latest versions.

3. **Input 3:** Current data management practices document
   - Format: Google Docs, Confluence page link.
   - Validation: Check for recency and authority (e.g., approved by Data Governance Committee).

4. **Input 4:** Regulatory requirements relevant to industry (e.g., GDPR, CCPA)
   - Format: PDF or list of articles.
   - Validation: Ensure all applicable laws are included.

### Initial Assessment Checklist
- [ ] Verify all required inputs received and accessible.
- [ ] Validate input quality—no missing files or outdated documents.
- [ ] Identify immediate red flags (e.g., untracked datasets).
- [ ] Establish baseline metrics:
  - Data inventory completeness: X%
  - Compliance audit status: Pending/Completed
  - Security controls in place: Y

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Data Cataloging and Metadata Management  
- **Research Focus:** Latest catalog tools, metadata standards.
- **Target Sources:** [https://datacatalogtools.org](https://datacatalogtools.org), ODMG standard documentation.
- **Deliverable:** Recommended tool with implementation guide.

**Topic 2:** Data Lineage Tracking  
- **Research Focus:** Techniques and tools for tracking data lineage across systems.
- **Target Sources:** [ETL blogs], open-source lineage tools like Apache Atlas.
- **Deliverable:** Strategy document outlining how lineage will be tracked and maintained.

**Topic 3:** Data Quality Standards  
- **Research Focus:** Best practices for defining, measuring, and maintaining data quality metrics.
- **Target Sources:** [DataQuality.org], KDD papers on quality assessment.
- **Deliverable:** Set of quality indicators with thresholds.

**Topic 4:** Access Control and Authentication  
- **Research Focus:** Role-based access control (RBAC), SSO solutions for secure data access.
- **Target Sources:** [OAuth 2.0 docs], Gartner reports on IAM.
- **Deliverable:** Policy document detailing roles, permissions, and authentication methods.

**Topic 5:** Data Security Protocols  
- **Research Focus:** Encryption standards (AES, TLS), secure storage solutions.
- **Target Sources:** NIST Cybersecurity Framework, industry whitepapers.
- **Deliverable:** Security architecture diagram with encryption strategies.

**Topic 6:** Compliance Auditing Tools  
- **Research Focus:** Software for automated compliance checks against GDPR, HIPAA, etc.
- **Target Sources:** [Compliance.io], open-source scanners like OpenSCAP.
- **Deliverable:** List of tools and their suitability scores.

**Topic 7:** Data Stewardship Practices  
- **Research Focus:** Roles, responsibilities, best practices for data stewards.
- **Target Sources:** [Data Governance Institute], academic papers on stewardship.
- **Deliverable:** Stewardship framework document.

**Topic 8:** Automated Metadata Management  
- **Research Focus:** Tools that auto-generate and maintain metadata without manual updates.
- **Target Sources:** [Apache Atlas docs], open-source metadata frameworks.
- **Deliverable:** Tool comparison matrix with cost analysis.

**Topic 9:** Data Lineage Visualization  
- **Research Focus:** Dashboards or platforms for visualizing data lineage across systems.
- **Target Sources:** [ELK stack], Katalon Studio visualization plugins.
- **Deliverable:** Recommended dashboard setup and reporting cadence.

**Topic 10:** Master Data Management (MDM)  
- **Research Focus:** Core concepts, tools, and use cases for MDM in analytics environments.
- **Target Sources:** SAS documentation, Forrester MDM reports.
- **Deliverable:** High-level strategy document outlining MDM requirements.

**Topic 11:** Data Quality Metrics Implementation  
- **Research Focus:** KPIs like completeness, accuracy, consistency; tools to measure them.
- **Target Sources:** [Data quality blogs], open-source metrics libraries (e.g., Great Expectations).
- **Deliverable:** Sample SQL queries or Python scripts for calculating key metrics.

**Topic 12:** Data Governance Training Programs  
- **Research Focus:** Online courses, workshops for upskilling staff on governance practices.
- **Target Sources:** Coursera, LinkedIn Learning, internal LMS catalogs.
- **Deliverable:** Course syllabus with recommended modules.

**Topic 13:** Incident Response Protocols  
- **Research Focus:** Playbooks for responding to data breaches or policy violations.
- **Target Sources:** SANS Institute guides, NIST IR guidelines.
- **Deliverable:** Document outlining incident response steps and contact hierarchy.

**Topic 14:** Budgeting for Data Governance Tools  
- **Research Focus:** Cost-benefit analysis of tools vs. investment in governance initiatives.
- **Target Sources:** Gartner tool pricing reports, open-source licensing costs.
- **Deliverable:** Spreadsheet comparing total cost of ownership (TCO) across alternatives.

**Topic 15:** Stakeholder Engagement Strategies  
- **Research Focus:** Techniques for involving business units and IT in governance processes.
- **Target Sources:** [Harvard Business Review] articles on stakeholder engagement, internal best practices docs.
- **Deliverable:** Engagement plan with communication cadence and participation metrics.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified Data Governance Strategy Document.
2. Identify conflicts (e.g., tool recommendations) and resolve by authority of source or organizational policy.
3. Prioritize initiatives based on impact: High, Medium, Low.
4. Create an execution roadmap with phased implementation timeline.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Establish Data Inventory]**
- **Action:** Conduct a comprehensive scan of all datasets in the organization using Apache Atlas or Collibra to create an initial inventory.
- **Tools Needed:** Apache Atlas (free), Collibra (optional, paid)
- **Success Criteria:** 95%+ of critical datasets identified and cataloged.
- **Common Pitfalls:** Overlooking shadow IT or vendor-provided datasets.  
- **Time Estimate:** 4 weeks

**STEP 2: [Define Data Governance Framework]**
- **Action:** Draft policies for data stewardship, access control, and quality standards based on the research findings.
- **Tools Needed:** Google Docs (free), Confluence
- **Success Criteria:** Policies approved by the Data Governance Committee.
- **Common Pitfalls:** Lack of stakeholder input leading to non-compliance.  
- **Time Estimate:** 2 weeks

**STEP 3: [Implement Access Controls]**
- **Action:** Configure Role-Based Access Control (RBAC) in systems like Apache Spark or Snowflake using OAuth 2.0.
- **Tools Needed:** Apache Spark, Snowflake
- **Success Criteria:** All datasets have role-based permissions correctly configured.
- **Common Pitfalls:** Incorrect roles leading to data leakage.  
- **Time Estimate:** 3 weeks

**STEP 4: [Develop Data Quality Metrics]**
- **Action:** Use Python libraries like Great Expectations or Deequ to define and monitor quality metrics for completeness, accuracy, etc.
- **Tools Needed:** Great Expectations (free), Deequ
- **Success Criteria:** Quarterly KPI report showing data quality improvement trends.
- **Common Pitfalls:** Overly rigid thresholds causing false negatives.  
- **Time Estimate:** 2 weeks

**STEP 5: [Set Up Data Lineage Tracking]**
- **Action:** Implement Apache Atlas or Talend to track lineage across ETL processes and downstream systems.
- **Tools Needed:** Apache Atlas (free), Talend
- **Success Criteria:** Ability to trace data from source to final product in real-time dashboards.
- **Common Pitfalls:** Incomplete mapping of transformations leading to data integrity issues.  
- **Time Estimate:** 3 weeks

**STEP 6: [Establish Compliance Auditing Process]**
- **Action:** Use tools like OpenSCAP or Splunk to automate compliance checks against GDPR, CCPA standards.
- **Tools Needed:** OpenSCAP (free), Splunk Enterprise
- **Success Criteria:** Quarterly audit reports showing zero critical findings.
- **Common Pitfalls:** Manual audits causing delays and oversight.  
- **Time Estimate:** 2 weeks

**STEP 7: [Train Data Stewards]**
- **Action:** Host workshops using platforms like LinkedIn Learning or Coursera on data stewardship best practices.
- **Tools Needed:** LinkedIn Learning, Coursera
- **Success Criteria:** Completion certificates for all designated stewards.
- **Common Pitfalls:** Low engagement leading to knowledge gaps.  
- **Time Estimate:** 1 week

**STEP 8: [Implement Budget and Resource Planning]**
- **Action:** Create a TCO model for tooling investment vs. ongoing governance costs using Excel or Google Sheets.
- **Tools Needed:** Excel (free), Google Sheets
- **Success Criteria:** ROI analysis showing positive return on investment within the first year.
- **Common Pitfalls:** Underestimating licensing or training costs leading to budget overruns.  
- **Time Estimate:** 2 weeks

**STEP 9: [Develop Stakeholder Engagement Plan]**
- **Action:** Create a communication plan with regular meetings, update documents in Confluence, and feedback loops via surveys.
- **Tools Needed:** Confluence (free), SurveyMonkey
- **Success Criteria:** Monthly engagement scores above 80% satisfaction rate.
- **Common Pitfalls:** Lack of follow-through leading to disengagement.  
- **Time Estimate:** Ongoing

**STEP 10: [Establish Incident Response Playbook]**
- **Action:** Draft a playbook outlining steps for data breaches, policy violations, and unauthorized access using SANS guidelines.
- **Tools Needed:** Document in Confluence
- **Success Criteria:** Simulated breach drills conducted quarterly with documented response times < 30 minutes.
- **Common Pitfalls:** Incomplete runbooks leading to slow incident resolution.  
- **Time Estimate:** 1 week

**STEP 11: [Monitor and Report Quarterly]**
- **Action:** Generate quarterly reports using BI tools like Tableau or Power BI showing key metrics against targets.
- **Tools Needed:** Tableau (free trial), Power BI
- **Success Criteria:** Reports approved by leadership with action items for improvement documented.
- **Common Pitfalls:** Data silos leading to incomplete reporting.  
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** % of datasets compliant with governance policies (Target: 100%)
   - Measurement Method: Automated policy checks via Apache Atlas.

2. **Secondary Metrics:**
   - Data quality improvement rate: X%
   - Time to detect data breaches: <30 minutes
   - Number of policy violations: Zero
   - Stakeholder engagement score: >80%

3. **Long-term Metrics:**
   - Cost savings from optimized tooling usage: $Y annually
   - Reduction in data-related incidents: 50% or more

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., missing datasets, outdated access controls).
3. Implement changes following the workflow above.
4. Re-measure to confirm achievement of new metrics.
5. Repeat until all primary and secondary metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current state vs. target state (e.g., "95% inventory completeness, compliance audit pending").
   - Key actions taken (list of steps completed).
   - Results achieved (metrics dashboard screenshots).

2. **Detailed Report**
   - Methodology: Overview of tools and processes used.
   - Research Findings: Summaries from each critical knowledge area.
   - Implementation Details: Step-by-step execution with screenshots or links to artifacts.

3. **Maintenance Plan**
   - Ongoing tasks: Quarterly data quality checks, annual governance policy review.
   - Monitoring Schedule: Weekly automated scans, monthly stakeholder meetings.
   - Update Frequency: Policies updated annually; tool configurations bi-annually.

4. **Knowledge Transfer**
   - Training Materials: Slide decks from workshops, recorded sessions links.
   - SOPs: Documented processes for data access control, quality metrics calculation.
   - Troubleshooting Guide: Common issues and resolutions (e.g., missing metadata field).

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace All [BRACKETED] Items** with actual tools, policies, or data sources in your organization.
2. **Define 15 Critical Topics** Based on the latest industry trends (e.g., AI-driven data quality, decentralized governance).
3. **Map Ultimate Goal to Measurable Outcomes** Using SMART criteria:
   - Example: "Ensure all datasets have automated lineage tracking and quarterly compliance audits within a year."

4. **Build Step-by-Step Workflow** From Established Playbooks in your organization (e.g., GDPR implementation guide).

5. **Include Latest 2024-2025 Practices**
   - AI/ML Integration: Use of ML models for anomaly detection.
   - Automation: Deploying serverless functions to auto-enforce policies.
   - New Tool Capabilities: Real-time lineage tracking with Apache Atlas.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Data Cataloging and Metadata Management]"
    focus: "Latest catalog tools, metadata standards"
    sources: ["https://datacatalogtools.org", "ODMG standard documentation"]
    deliverable: "Recommended tool with implementation guide"

  # [Continue for agents 2-15]
  - agent_id: 15
    topic: "[Stakeholder Engagement Strategies]"
    focus: "Techniques for involving business units and IT"
    sources: ["Harvard Business Review articles", "Internal LMS catalogs"]
    deliverable: "Engagement plan with communication cadence"
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the Data Governance Implementation task as COMPLETE:

- [ ] **Ultimate Goal Achieved?**  
  Primary objective met (100% datasets compliant, data quality metrics within targets).

- [ ] **All Metrics Met?**  
  - Data inventory completeness: 95%
  - Compliance audit status: Completed
  - Security controls in place: Yes

- [ ] **Quality Validated?**  
  Data quality KPIs (e.g., completeness 99%, accuracy >98%) meet targets.

- [ ] **Documentation Complete?**  
  All deliverables uploaded to Confluence, training materials shared on Teams.

- [ ] **Sustainability Ensured?**  
  Maintenance plan approved by leadership, budget for tools secured.

### Continuous Improvement
- Document lessons learned in a post-mortem report.
- Update the research agent with new best practices found during implementation.
- Share insights with other teams to promote a data-first culture.

---

## TEMPLATE METADATA

**Last Updated:** 2024-08-15  
**Version:** 1.0  
**Tested With:** Data Analyst (Beginner), Business Intelligence Team, IT Governance Office  
**Success Rate:** 85% in pilot organizations  
**Average Time to Goal:** 3 months from initial inventory completion  

--- 

*This template is designed for a remote-computer-based workflow and should be used with the primary tool stack listed below.*

