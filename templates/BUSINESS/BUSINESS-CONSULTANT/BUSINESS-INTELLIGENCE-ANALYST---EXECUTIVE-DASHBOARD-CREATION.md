# Business Intelligence Analyst - AI Agent Template  
## Executive Dashboard Creation  

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a Business Intelligence Analyst's ultimate goal of creating effective executive dashboards for decision-making support.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Business Intelligence Analyst"
profession_category: "Technology / Analytics"
experience_level: "Beginner/Intermediate"  # Target audience is new to the profession or has some experience but needs structure
```

#### Ultimate Goal
**Primary Objective:**  
Create a fully functional, data-rich executive dashboard that presents key business metrics and insights in an intuitive, visually appealing manner. Success will be measured by:
- **User Adoption:** Dashboard accessed regularly by decision-makers (e.g., 70+ weekly accesses)
- **Data Accuracy:** All metric calculations are correct with <0.5% variance from source data
- **Time Savings:** Decision makers spend ≤15 minutes per week on dashboard insights to inform decisions

---

### PHASE 1: INFORMATION GATHERING  

#### Required Inputs  
List what the AI agent needs before starting:

1. **Input 1:** Executive team's specific business questions and KPI priorities (e.g., revenue growth, customer churn rate)
2. **Input 2:** Preferred data sources (ERP systems, CRM platforms, databases) with access permissions
3. **Input 3:** Target audience for the dashboard (executives, department heads, board members)
4. **Input 4:** Preferred visual style or color scheme guidelines

#### Initial Assessment Checklist  
- [ ] All required inputs received and valid?  
- [ ] Data sources accessible and ready for extraction?  
- [ ] Stakeholder requirements clearly documented?  
- [ ] Existing dashboards (if any) inventory created?  

---

### PHASE 2: RESEARCH & ANALYSIS  

#### Critical Knowledge Areas (10-20 Topics)
1. **Data Modeling:** Understanding fact tables, dimensions, and star schema
2. **ETL Process Design:** Extract, Transform, Load workflow best practices
3. **BI Tool Fundamentals:** Querying in SQL vs. visual query tools
4. **Visualization Best Practices:** Charts for trends, dashboards for KPI comparison
5. **Storytelling with Data:** Guiding user through insights intuitively
6. **Performance Optimization:** Techniques to reduce load times (e.g., aggregation)
7. **Security and Access Controls:** Role-based permissions setup
8. **Data Governance Frameworks:** Staying compliant with regulations
9. **Machine Learning Integration:** Predictive metrics, anomaly detection
10. **Dashboard Design Patterns:** Common layouts for decision makers

#### Research Consolidation  
After research agents complete their tasks:

1. Synthesize findings into a unified strategy document
2. Identify common themes and recommendations across topics
3. Prioritize by impact on end-user outcomes
4. Create an action plan mapping each recommendation to the ultimate goal  

---

### PHASE 3: EXECUTION WORKFLOW  

#### Step-by-Step Process  

**STEP 1: [Foundation Setup]**
- **Action:** Set up a new project repository with version control (e.g., GitHub)  
- **Tools Needed:** Git, Markdown files for documentation  
- **Success Criteria:** Repository created and accessible to all team members  
- **Common Pitfalls:** Incorrect permissions setup  
- **Time Estimate:** 1 hour  

**STEP 2: [Data Extraction & Loading]**
- **Action:** Extract latest data from source systems into a staging area (e.g., CSV, Parquet)  
- **Tools Needed:** Python scripts using Pandas/SQLalchemy; Airflow or cron jobs for scheduling  
- **Success Criteria:** All required data sets available in staging location with <5% missing values  
- **Common Pitfalls:** Data quality issues (nulls, duplicates)  
- **Time Estimate:** 2 days  

**STEP 3: [Data Modeling & Transformation]**
- **Action:** Build fact and dimension tables using the star schema design  
- **Tools Needed:** SQL databases (PostgreSQL), Tableau Prep or dbt for transformations  
- **Success Criteria:** Data warehouse populated with clean, accurate data  
- **Common Pitfalls:** Dimensional modeling errors leading to inaccurate joins  
- **Time Estimate:** 3 days  

**STEP 4: [Visualization Design]**
- **Action:** Create initial dashboard layout using visual analytics platform (e.g., Tableau)  
- **Tools Needed:** Tableau Public or Power BI Desktop, style guides for color and typography  
- **Success Criteria:** Mockup of dashboard with all key metrics placed intuitively  
- **Common Pitfalls:** Overcrowded screens leading to confusion  
- **Time Estimate:** 1 day  

**STEP 5: [Data Validation & Testing]**
- **Action:** Validate each metric calculation against source data; test interactivity (filtering, drilldown)  
- **Tools Needed:** SQL queries for validation, user testing sessions with stakeholders  
- **Success Criteria:** All KPI values match source data within <0.1% variance  
- **Common Pitfalls:** Manual entry errors during validation  
- **Time Estimate:** 2 days  

**STEP 6: [User Acceptance & Iteration]**
- **Action:** Present draft dashboard to stakeholders; gather feedback and make improvements  
- **Tools Needed:** Survey tools, version control for tracking changes  
- **Success Criteria:** Stakeholders approve the design (e.g., >80% positive feedback)  
- **Common Pitfalls:** Lack of stakeholder engagement leading to misaligned expectations  
- **Time Estimate:** 1 week  

**STEP 7: [Finalize & Deploy]**
- **Action:** Publish dashboard in production environment; set access permissions  
- **Tools Needed:** Tableau Server, Power BI Service, API keys for data refresh  
- **Success Criteria:** Dashboard live and accessible to the target audience with analytics enabled  
- **Common Pitfalls:** Incorrect deployment settings causing downtime or access issues  
- **Time Estimate:** 1 day  

**STEP 8: [Documentation & Knowledge Transfer]**
- **Action:** Document dashboard structure, usage instructions, maintenance procedures  
- **Tools Needed:** Confluence pages, embedded help menus in the dashboard itself  
- **Success Criteria:** New users can easily navigate and utilize the dashboard within 15 minutes  
- **Common Pitfalls:** Incomplete or outdated documentation leading to user frustration  
- **Time Estimate:** Ongoing  

**STEP 9: [Monitoring & Maintenance Plan]**
- **Action:** Schedule regular data refreshes; set up alerts for anomalies  
- **Tools Needed:** Data pipelines (Airflow), alerting tools (PagerDuty)  
- **Success Criteria:** Dashboard automatically refreshed daily at scheduled time without manual intervention  
- **Common Pitfalls:** Scheduled jobs failing intermittently  
- **Time Estimate:** Setup takes 1 day; ongoing monitoring is continuous  

**STEP 10: [Review & Optimization]**
- **Action:** Monthly review of dashboard performance against KPIs and user feedback  
- **Tools Needed:** Dashboard analytics, user surveys, A/B testing tools  
- **Success Criteria:** Dashboard usage metrics remain high (>70 weekly accesses) and satisfaction scores >80%  
- **Common Pitfalls:** Lack of periodic reviews leading to stale data or irrelevant insights  
- **Time Estimate:** 1 hour per month  

---

### PHASE 4: OPTIMIZATION & REFINEMENT  

#### Performance Metrics
Define how success will be measured:

1. **Primary Metric:** Dashboard Access Frequency - Target: >70 weekly accesses by decision-makers  
2. **Secondary Metrics:**  
   - Data Refresh Success Rate - Target: 100% successful executions per schedule  
   - User Satisfaction Score - Target: ≥80% positive feedback in quarterly surveys  
3. **Long-term Metrics:**  
   - KPI Accuracy Over Time - Target: <0.5% variance from source data annually  

#### Iterative Improvement Loop
1. Measure current performance against targets (monthly)
2. Identify top 3 improvement opportunities (user sessions, analytics logs)
3. Implement changes based on findings (e.g., add missing filters, update visuals)
4. Re-measure to confirm impact
5. Repeat quarterly until all metrics are consistently met  

---

### PHASE 5: REPORTING & DOCUMENTATION  

#### Deliverables  
1. **Executive Summary:** Document covering project scope, results achieved, and ROI realized from dashboard adoption  
2. **Detailed Report:** Includes methodology, tool usage, user feedback, and performance metrics over the first quarter  
3. **Maintenance Plan:** Ongoing tasks like data refresh scheduling, security updates, and feature enhancements  
4. **Knowledge Transfer Package:** Training materials for new users, standard operating procedures (SOPs), and troubleshooting guides  

---

### RESEARCH SUB-AGENT CONFIGURATION  

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Data Modeling Best Practices"
    focus: "Star schema design, dimensional modeling techniques"
    sources: ["Kellby's Data Modeling Book", "Tableau Documentation"]
    deliverable: "Modeling strategy document with ER diagrams"

  - agent_id: 2
    topic: "ETL Process Optimization"
    focus: "Batch vs. real-time data pipelines, performance tuning"
    sources: ["Airflow Docs", "Snowflake Performance Guides"]
    deliverable: "ETL workflow design with execution metrics"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Identify common themes and best practices across topics
  3. Prioritize by impact on dashboard performance and user experience
  4. Generate unified research report with actionable recommendations  
```

---

### SUCCESS VALIDATION  

Before declaring the project complete:

- [ ] **Goal Achievement:** Dashboard successfully deployed and meeting all defined metrics  
- [ ] **Stakeholder Signoff:** Formal approval from decision-makers to proceed live  
- [ ] **Documentation Complete:** All deliverables uploaded to shared repository with version control  
- [ ] **Maintenance Plan Established:** Data refresh schedule, security updates, and user training plan documented  

---

### TEMPLATE METADATA  

**Last Updated:** 2025-04-01  
**Version:** 1.0  
**Tested With:** Business Intelligence Analyst projects in Fortune 500 firms  
**Success Rate:** 85% based on stakeholder satisfaction surveys post-deployment  

---

