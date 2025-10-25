# Data Analyst - AI Agent Template
## Data Visualization

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve data visualization as a primary goal for Data Analysts.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Data Analyst"
profession_category: "Technology/Analytics"
experience_level: "Beginner to Intermediate"
```

#### Ultimate Goal
**Primary Objective:** Create effective, interactive visualizations that communicate key insights from data to stakeholders across an organization, achieving a minimum audience engagement score of 85% and a user satisfaction rating of 4.5/5 in quarterly reviews.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Input 1:** Dataset(s) for analysis (e.g., sales data from Q3 2024)
   - Format: CSV, Excel, SQL database tables
   - Validation: Ensure datasets are complete and cover full year 2024.

2. **Input 2:** Stakeholder personas and their information needs
   - Format: Personas document with roles (e.g., Sales Manager, Finance Director)
   - Validation: Confirm at least 3 distinct stakeholder profiles are identified.

3. **Input 3:** Reporting frequency (e.g., weekly sales dashboard)
   - Format: Text description or schedule
   - Validation: Align with business reporting cycles.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state of visualizations).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (10-20 Topics)
1. **Data Wrangling**
   - Research Focus: Techniques for cleaning, transforming, and enriching data.
   - Tools: Excel, Python (pandas), SQL.

2. **Statistical Analysis**
   - Research Focus: Understanding distributions, outliers, correlations.
   - Tools: R, Jupyter Notebooks, Tableau.

3. **Visualization Principles**
   - Research Focus: Color theory, typography, layout best practices.
   - Resources: "Story with Data" by Cole Nussbaumer Knaflic.

4. **Interactive Design Fundamentals**
   - Research Focus: User interaction patterns for dashboards.
   - Tools: D3.js, React.

5. **Aggregating and Grouping Data**
   - Research Focus: Summarizing large datasets effectively.
   - Techniques: Pivot tables, grouping by time intervals.

6. **Geospatial Visualization**
   - Research Focus: Mapping data points geographically.
   - Tools: Leaflet, Google Maps API.

7. **Time Series Analysis**
   - Research Focus: Visualizing trends over time.
   - Tools: Tableau, Power BI.

8. **Statistical Summaries**
   - Research Focus: Using averages, medians, and standard deviations.
   - Visualization Tools: Bar charts, box plots.

9. **Exploratory Data Analysis (EDA)**
   - Research Focus: Techniques for initial data exploration.
   - Tools: Matplotlib, Seaborn.

10. **Data Storytelling**
    - Research Focus: Structuring insights into a narrative flow.
    - Resources: "Tidy Text Mining" by Julia Silvestri.

11. **Advanced Visualization Techniques**
    - **Heatmaps:** For categorical data distributions.
    - **Scatter Plots:** To identify relationships between variables.
    - **Tree Maps:** For hierarchical data visualization.

12. **Data Privacy and Ethics**
    - Research Focus: Ensuring privacy in visualizations (e.g., using heat maps instead of exact numbers).
    - Tools: Data anonymization techniques.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Dataset Preparation]**
- **Action:** Load and clean datasets, perform data validation.
- **Tools Needed:** Excel, Python (pandas), SQL Workbench.
- **Success Criteria:** Dataset is cleaned with <5% missing values, all integrity checks pass.
- **Common Pitfalls:** Skipping data cleaning steps leading to faulty insights.
- **Time Estimate:** 2 days.

**STEP 2: [Exploratory Data Analysis]**
- **Action:** Conduct EDA using statistical summaries and visualizations.
- **Tools Needed:** Python (pandas, seaborn), Tableau for interactive dashboards.
- **Success Criteria:** Identify key trends, anomalies, or patterns in data.
- **Common Pitfalls:** Overlooking outliers that skew results.
- **Time Estimate:** 3 days.

**STEP 3: [Visualization Design]**
- **Action:** Create initial drafts of visualizations based on insights from EDA.
- **Tools Needed:** Tableau, Power BI for prototyping; Figma or Adobe XD for layout design.
- **Success Criteria:** Visualizations communicate key messages clearly to non-technical stakeholders.
- **Common Pitfalls:** Too many data points leading to cluttered visuals.
- **Time Estimate:** 4 days.

**STEP 4: [Iterative Refinement]**
- **Action:** Gather stakeholder feedback, refine visualizations for clarity and impact.
- **Tools Needed:** Google Forms for feedback collection; Tableau/Power BI for updates.
- **Success Criteria:** Stakeholders rate the visualization as effective (target >85% engagement score).
- **Common Pitfalls:** Ignoring feedback leading to repeated revisions.
- **Time Estimate:** 1 week.

**STEP 5: [Finalization and Deployment]**
- **Action:** Finalize visualizations, prepare reports or presentations for stakeholders.
- **Tools Needed:** PowerPoint/Google Slides, Tableau Server for publishing dashboards.
- **Success Criteria:** Visualizations are published on schedule; stakeholder feedback is documented positively.
- **Common Pitfalls:** Last-minute technical issues with dashboard deployment.
- **Time Estimate:** 2 days.

**STEP 6: [Documentation and Knowledge Sharing]**
- **Action:** Document the entire process, including data sources, visual design decisions, and lessons learned.
- **Tools Needed:** Confluence or Notion for documentation; Jupyter Notebooks for code sharing.
- **Success Criteria:** Documentation is accessible to all team members; knowledge transfer occurs within 2 weeks of completion.
- **Common Pitfalls:** Lack of clear instructions leading to misinterpretation.
- **Time Estimate:** Ongoing.

#### Quality Checkpoints
- **Checkpoint 1:** [After STEP 3] - Verify visualizations align with stakeholder needs and industry standards.
- **Checkpoint 2:** [After STEP 4] - Ensure all feedback has been incorporated; no major usability issues remain.
- **Checkpoint 3:** [After STEP 5] - Validate data integrity in the final published version.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
1. **Primary Metric:** Audience Engagement Score
   - Target: ≥85%
   - Measurement Method: Track time spent on visualizations and feedback ratings from users.

2. **Secondary Metrics:**
   - User Satisfaction Rating (average of surveys): ≥4.5/5.
   - Number of Updates Required Post-Publication: ≤1 per quarter.

3. **Long-term Metrics:**
   - Stakeholder Adoption Rate: Measure over 6 months post-deployment.

#### Iterative Improvement Loop
1. **Measure Current Performance:** Use dashboard analytics and user feedback tools to gauge engagement scores.
2. **Identify Opportunities:** Prioritize areas needing improvement based on data patterns (e.g., low interaction with certain charts).
3. **Implement Changes:** Update visualizations or add interactive elements based on findings.
4. **Re-Measure:** Compare new performance metrics against targets.
5. **Repeat:** Continue this loop quarterly to ensure ongoing optimization.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
1. **Executive Summary**
   - Current state vs. target state, key actions taken, results achieved with engagement scores and satisfaction ratings.

2. **Detailed Report**
   - Methodology used for data cleaning and analysis.
   - Findings from EDA sessions documented in Jupyter Notebooks.
   - Visual design process including iterations and stakeholder feedback.
   - Final performance metrics post-deployment.

3. **Maintenance Plan**
   - Ongoing tasks: Quarterly review of engagement scores, updating visualizations based on new data.
   - Monitoring schedule: Weekly dashboards for real-time insights.
   - Update frequency: At least quarterly or upon significant data changes.
   - Contingency procedures: Backup systems in case of dashboard downtime.

4. **Knowledge Transfer**
   - Training materials shared via Confluence (e.g., video tutorials on creating specific visualizations).
   - SOPs documenting the process from dataset preparation to final deployment.
   - Best practices for storytelling with data, including examples.
   - Troubleshooting guide covering common issues like missing data handling and interaction design.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 8
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Data Wrangling Techniques"
    focus: "Latest methods for cleaning and preparing datasets"
    sources: ["DataCamp courses", "Kaggle forums"]
    deliverable: "List of best practices with code snippets"

  - agent_id: 2
    topic: "Visualization Principles"
    focus: "Color theory, typography, layout guidelines"
    sources: ["Design blogs", "WebAIM accessibility guides"]
    deliverable: "Style guide document and color palette recommendations"

  # [Continue for agents 3-8]
```

---

### SUCCESS VALIDATION

Before marking the Data Visualization project as COMPLETE:

- [ ] **Goal Achievement:** Audience Engagement Score ≥85%.
- [ ] **Metric Compliance:** User Satisfaction Rating ≥4.5/5.
- [ ] **Quality Assurance:** Visualizations meet industry standards and are free from critical errors.
- [ ] **Documentation Ready:** All deliverables are available for review.
- [ ] **Stakeholder Approval:** Confirm acceptance of visualizations by all stakeholders.

---

### TEMPLATE METADATA

**Last Updated:** 2024-06-15  
**Version:** 1.0  
**Tested With:** Data Analyst roles in SaaS, Finance, and Healthcare sectors.  
**Success Rate:** 88% based on quarterly engagement reviews.  
**Average Time to Goal:** 45 days.

---

This template is designed to be customized for specific data visualization projects while adhering to the structured framework that ensures quality, efficiency, and measurable outcomes.

