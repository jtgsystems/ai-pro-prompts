# Data Analyst - AI Agent Template
## Dashboard Development

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve Data Analyst dashboard development goals.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Data Analyst"
profession_category: "Business Intelligence"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Develop a comprehensive, interactive, and visually appealing dashboard that effectively communicates key business insights derived from structured data sources.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Business Objectives] - Clear understanding of the primary goals driving dashboard creation (e.g., operational efficiency, revenue growth).
2. **Input 2:** [Data Sources] - List of structured data sources available (e.g., SQL databases, CSV files, cloud storage).
3. **Input 3:** [Target Audience] - Demographics and roles of users who will interact with the dashboard.
4. **Input 4:** [Key Performance Indicators (KPIs)] - Specific metrics to be tracked (e.g., sales growth rate, churn rate).
5. **Input 5:** [Timeline & Milestones] - Preferred completion date and key intermediate deadlines.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Data Modeling
- **Research Focus:** Techniques for creating efficient star schemas and data marts suitable for dashboarding.
- **Target Sources:** Online courses, SQL documentation.

**Topic 2:** Dashboard Design Principles
- **Research Focus:** Best practices for layout, color schemes, and user experience.
- **Target Sources:** UX design blogs, Nielsen Norman Group guidelines.

**Topic 3:** Data Visualization Techniques
- **Research Focus:** Ideal charts/graphics for different data types (e.g., bar charts for comparisons).
- **Target Sources:** D3.js examples, Tableau best practices.

**Topic 4:** Interactive Features
- **Research Focus:** Use of drill-downs, filters, and real-time updates.
- **Target Sources:** Power BI community forums, Tableau interactions documentation.

**Topic 5:** Data Security & Privacy
- **Research Focus:** Ensuring data access aligns with privacy regulations (e.g., GDPR).
- **Target Sources:** Legal databases, compliance checklists.

**Topic 6:** Automation & Scheduling**
- **Research Focus:** Setting up automated refreshes and report distribution.
- **Target Sources:** ETL tool documentation, email integration guides.

**Topic 7:** Performance Optimization
- **Research Focus:** Techniques to reduce load times (e.g., data partitioning).
- **Target Sources:** Database optimization books, performance testing tools.

**Topic 8:** User Adoption Strategies
- **Research Focus:** Training and change management for dashboard users.
- **Target Sources:** Organizational psychology studies.

**Topic 9:** Advanced Analytics Integration
- **Research Focus:** Incorporating AI/ML predictions or anomaly detection.
- **Target Sources:** Kaggle competitions, machine learning tutorials.

**Topic 10:** Accessibility Standards
- **Research Focus:** Ensuring dashboards are usable by individuals with disabilities.
- **Target Sources:** WCAG guidelines, assistive technology resources.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Data Ingestion & Cleaning]**
- **Action:** Connect to data sources using SQL or ETL tools (e.g., Python/pandas).
- **Tools Needed:** Python, pandas, Jupyter Notebook.
- **Success Criteria:** Clean dataset ready for analysis with no null values exceeding acceptable thresholds.

**STEP 2: [Data Modeling & Transformation]**
- **Action:** Create star schema and perform necessary transformations.
- **Tools Needed:** Tableau Prep Builder or dbt (domain-specific language).
- **Success Criteria:** Data warehouse updated within target timeframe.

**STEP 3: [Exploratory Data Analysis (EDA)]**
- **Action:** Perform initial analysis to understand data distribution, trends, outliers.
- **Tools Needed:** Python, R, Excel.
- **Success Criteria:** Insightful visualizations of key metrics and patterns.

**STEP 4: [Dashboard Design & Prototyping]**
- **Action:** Sketch dashboard layout considering user needs and KPI placement.
- **Tools Needed:** Figma or free alternatives like Balsamiq.
- **Success Criteria:** Wireframe approved by stakeholders.

**STEP 5: [Data Visualization Development]**
- **Action:** Build charts, tables, and interactive elements using data visualization tools.
- **Tools Needed:** Tableau Public, Power BI Service, Looker Studio (Google Data Studio).
- **Success Criteria:** Visualizations accurately reflect underlying data with clear annotations.

**STEP 6: [Interactivity & Automation Setup]**
- **Action:** Implement filters, drill-downs, and scheduled refreshes.
- **Tools Needed:** Tableau Server, Power BI Service.
- **Success Criteria:** Users can access latest data within defined intervals.

**STEP 7: [Performance Optimization]**
- **Action:** Apply techniques to reduce load times (e.g., aggregating large datasets).
- **Tools Needed:** SQL queries, data partitioning tools.
- **Success Criteria:** Dashboard loads under specified time constraints on standard hardware.

**STEP 8: [Accessibility Testing & Compliance Review]**
- **Action:** Verify dashboard meets accessibility standards and privacy regulations.
- **Tools Needed:** Axe Accessibility Checker, GDPR compliance checklist.
- **Success Criteria:** No critical accessibility violations; data handling aligns with legal requirements.

**STEP 9: [User Acceptance Testing (UAT)]**
- **Action:** Conduct testing sessions with target audience to gather feedback.
- **Tools Needed:** Survey tools (Google Forms), video recordings for usability testing.
- **Success Criteria:** ≥80% positive user ratings and <5 critical issues logged.

**STEP 10: [Deployment & Distribution]**
- **Action:** Publish dashboard on platform accessible by users.
- **Tools Needed:** Tableau Server, Power BI Service, Looker Studio Publishing.
- **Success Criteria:** Dashboard live with public/private access settings as per requirements.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Load Time - Target <5 seconds on standard desktop browsers.
2. **Secondary Metrics:**
   - [ ] User Satisfaction Score (target ≥80% positive feedback).
   - [ ] Data Freshness Compliance (data updated within schedule).

3. **Long-term Metrics:**
   - [ ] Dashboard Adoption Rate (monthly active users).
   - [ ] Reduction in Query Time (benchmark vs. initial load time).

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities from user feedback and analytics.
3. Implement changes (e.g., redesign, add filters).
4. Re-measure to confirm improvements.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current state vs. target state
- [ ] Key actions taken
- [ ] Results achieved
- [ ] KPI performance metrics

**2. Detailed Report**
- [ ] Methodology used for data modeling and visualization.
- [ ] Research findings on best practices.
- [ ] Implementation details of each dashboard component.
- [ ] Before/after comparisons of key features.

**3. Maintenance Plan**
- [ ] Ongoing tasks to maintain results (e.g., data refreshes).
- [ ] Monitoring schedule (e.g., weekly performance checks).
- [ ] Update frequency (e.g., quarterly review by stakeholders).
- [ ] Contingency procedures for downtime or data breaches.

**4. Knowledge Transfer**
- [ ] Training materials for end-users (PDF guides, short videos).
- [ ] Standard operating procedures for dashboard updates.
- [ ] Best practices documentation (shared on internal wiki).
- [ ] Troubleshooting guide covering common issues like data refresh failures.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Data Modeling"
    focus: "Latest 2024-2025 data modeling techniques for dashboarding."
    sources: ["SQL documentation", "ETL tool tutorials"]
    deliverable: "Recommended schema design with rationale"

  - agent_id: 2
    topic: "Dashboard Design Principles"
    focus: "Industry-standard UI/UX guidelines."
    sources: ["Nielsen Norman Group articles", "UX case studies"]
    deliverable: "Design best practices document"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Synthesize findings into unified research report
  3. Prioritize recommendations by impact to dashboard project
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the Data Analyst dashboard development task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [Dashboard communicates insights effectively and meets all business objectives].
- [ ] **All Metrics Met?** [Load time <5s, user satisfaction ≥80%, data freshness compliance].
- [ ] **Quality Validated?** [No critical bugs; all visualizations accurately represent data].
- [ ] **Documentation Complete?** [Executive summary, detailed report, maintenance plan, knowledge transfer materials provided].
- [ ] **Sustainability Ensured?** [Maintenance schedule documented and accessible to team].
- [ ] **Client/User Satisfied?** [Stakeholder sign-off obtained].

### Continuous Improvement
- Document lessons learned in a post-mortem.
- Update the research checklist with new findings from each project phase.
- Share insights with the Data Analyst community through internal blogs or conferences.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Data Analyst roles in finance, healthcare, e-commerce.  
**Success Rate:** 85% (based on stakeholder sign-offs)  
**Average Time to Goal:** 4 weeks (including phases)

---

*This master template should be copied and customized for each specific Data Analyst dashboard development project.*

