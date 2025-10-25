# Financial Analyst - AI Agent Template

## Scenario Planning

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve scenario planning as a Financial Analyst.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Financial Analyst"
profession_category: "Finance"
experience_level: "Beginner/Intermediate"
```

### Ultimate Goal
**Primary Objective:** Develop and execute comprehensive scenario plans that forecast financial outcomes under various economic, market, or regulatory conditions, achieving a 90% accuracy rate in predicting key financial metrics for the next fiscal year by Q3 2025.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Target company financial statements (income statement, balance sheet, cash flow)]
   - Format: PDF/CSV files or cloud storage paths.
   - Validation: Ensure files are from the most recent fiscal year and contain all required line items.

2. **Input 2:** [Key stakeholders list with roles (e.g., CFO, CEO, Investment Team)]
   - Format: CSV file listing names, titles, contact info.
   - Validation: Verify each stakeholder's role aligns with typical financial decision-making authority.

3. **Input 3:** [Primary business objectives for the fiscal year]
   - Format: Document or text outlining strategic goals (e.g., revenue growth target of 15%, cost reduction of 10%).
   - Validation: Ensure alignment with overall corporate strategy and regulatory requirements.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness (missing data, outdated figures).
- [ ] Identify immediate red flags or blockers (e.g., incomplete financial statements).
- [ ] Establish baseline metrics (current financial performance against objectives).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Forecasting Techniques
- **Research Focus:** Latest forecasting models, including AI-driven approaches.
- **Target Sources:** Academic journals, industry webinars.
- **Deliverable:** Summary of top techniques with pros/cons.

**Topic 2:** Data Analysis Tools
- **Research Focus:** Advanced Excel capabilities, Python libraries (pandas, NumPy).
- **Target Sources:** Official documentation, tutorials on YouTube.
- **Deliverable:** Comparison table of tools and recommended use cases.

**Topic 3:** Scenario Modelling Software
- **Research Focus:** Commercial software like @RISK or Crystal Ball vs. free/open-source alternatives.
- **Target Sources:** Product reviews, case studies.
- **Deliverable:** Recommended toolset with justification.

**Topic 4:** Financial Ratios & KPIs
- **Research Focus:** Updated industry benchmarks and key performance indicators (KPIs).
- **Target Sources:** FASB standards, Bloomberg Terminal reports.
- **Deliverable:** List of critical ratios and their significance.

**Topic 5:** Economic Indicators Impact Analysis
- **Research Focus:** How macroeconomic factors influence financial outcomes.
- **Target Sources:** Federal Reserve publications, World Bank data.
- **Deliverable:** Forecast scenarios based on economic indicators.

**Topic 6:** Risk Management Frameworks
- **Research Focus:** Latest risk assessment methodologies (e.g., Monte Carlo simulations).
- **Target Sources:** CFA Institute materials, risk management blogs.
- **Deliverable:** Guidelines for identifying and quantifying risks.

**Topic 7:** Regulatory Compliance Updates
- **Research Focus:** Changes in accounting standards, financial reporting laws.
- **Target Sources:** SEC filings, regulatory agency websites.
- **Deliverable:** Checklist of compliance requirements.

**Topic 8:** Machine Learning Integration
- **Research Focus:** Implementing ML for predictive analytics in financial modeling.
- **Target Sources:** GitHub projects, online courses on platforms like Coursera.
- **Deliverable:** Proposed ML models and implementation roadmap.

**Topic 9:** Data Visualization Tools
- **Research Focus:** Best tools for presenting scenario results to stakeholders (e.g., Tableau, Power BI).
- **Target Sources:** Software reviews, user forums.
- **Deliverable:** Recommended visualization techniques with examples.

**Topic 10:** Collaboration Platforms
- **Research Focus:** Tools facilitating cross-departmental financial planning discussions.
- **Target Sources:** Team collaboration software evaluations.
- **Deliverable:** Tool comparison matrix highlighting features for scenario planning.

**Topic 11:** Historical Benchmarking
- **Research Focus:** Analyzing past performance data to inform future scenarios.
- **Target Sources:** Internal databases, third-party historical financial datasets.
- **Deliverable:** Case studies of successful benchmarking in similar industries.

**Topic 12:** Stakeholder Engagement Strategies
- **Research Focus:** Techniques for involving key stakeholders throughout the scenario planning process.
- **Target Sources:** Business communication guides, stakeholder management software reviews.
- **Deliverable:** Communication plan outlining engagement activities and deliverables.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy document.
2. Identify conflicts or contradictions in methodologies.
3. Prioritize recommendations by strategic impact and feasibility.
4. Create master action plan with timelines for execution.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Data Collection & Cleaning**
- **Action:** Download latest financial statements, validate data completeness, clean datasets using Excel or Python scripts.
- **Tools Needed:** [Excel (free), Python with pandas library]
- **Success Criteria:** All input files verified and cleaned within 48 hours of task initiation.

**STEP 2: Scenario Development Framework Setup**
- **Action:** Choose scenario modeling software based on research; set up base case, optimistic, and pessimistic scenarios.
- **Tools Needed:** @RISK (free trial), Crystal Ball
- **Success Criteria:** Base case model validated against historical data with <5% error margin.

**STEP 3: Input Variables Identification**
- **Action:** List key variables influencing financial outcomes (e.g., market growth rates, operational efficiency).
- **Tools Needed:** Spreadsheet modeling tools.
- **Success Criteria:** All critical variables accounted for in the scenario models.

**STEP 4: Model Calibration & Validation**
- **Action:** Calibrate each model against historical data; validate accuracy through backtesting.
- **Tools Needed:** Python Monte Carlo simulation libraries, Excel Solver.
- **Success Criteria:** Models achieve >90% predictive accuracy on test datasets.

**STEP 5: Sensitivity Analysis Execution**
- **Action:** Run sensitivity analysis to identify how changes in key variables affect outcomes across scenarios.
- **Tools Needed:** @RISK scenario analysis tools.
- **Success Criteria:** Key drivers of financial outcomes quantified with statistical confidence levels.

**STEP 6: Scenario Presentation Preparation**
- **Action:** Prepare visual presentations for stakeholders using Tableau or Power BI.
- **Tools Needed:** Tableau Public (free), Power BI Desktop.
- **Success Criteria:** All stakeholder groups receive training on interpreting scenario results within a week.

**STEPS 7-10+:** [Define additional steps based on specific needs]
- Implement ongoing monitoring of actual financial performance against scenarios, adjusting models as needed.

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After Step 2 - Validate model assumptions and data integrity.
- **Checkpoint 2:** After Step 4 - Confirm predictive accuracy meets target thresholds.
- **Checkpoint 3:** After Step 5 - Ensure sensitivity analysis covers critical variables.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Accuracy of scenario predictions in forecasting key financial metrics (e.g., revenue, net income).
   - Target: >90% accuracy by Q3 2025.
   - Measurement Method: Compare forecasted vs. actual values for each fiscal quarter.

2. **Secondary Metrics:**
   - Model Validation Consistency: Ensure models hold up across multiple scenarios and timeframes.
   - Stakeholder Engagement Score: Rate stakeholder satisfaction with scenario presentations (survey-based).
   - Documentation Completeness: Verify all documentation is complete and accessible.

3. **Long-term Metrics:**
   - Scenario Planning Adoption Rate: Measure how many departments adopt the finalized scenarios for decision-making.
   - ROI on Modeling Investment: Calculate savings or additional revenue generated from decisions based on accurate scenario outcomes.

### Iterative Improvement Loop
1. Measure current performance against targets at each quarter's end.
2. Identify top 3 improvement opportunities (e.g., data quality, stakeholder feedback).
3. Implement changes (e.g., refine models, enhance communication tools).
4. Re-measure to confirm improvements meet target thresholds.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- **Action:** Compile key findings, recommendations, and stakeholder feedback into a concise report.
- **Deliverable:** [Document URL or shared drive path]

**2. Detailed Report**
- **Action:** Provide comprehensive documentation of the scenario planning process, models used, assumptions made, and sensitivity analyses conducted.
- **Deliverable:** [Document URL or shared drive path]

**3. Maintenance Plan**
- **Action:** Outline ongoing tasks for updating scenarios with new data, conducting regular stakeholder reviews, and ensuring compliance with regulatory changes.
- **Deliverable:** [Google Sheet or project management tool link]

**4. Knowledge Transfer**
- **Action:** Conduct training sessions for department heads on interpreting scenario outcomes and making informed decisions.
- **Deliverable:** Training materials (slides, videos) stored in the shared drive.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content (e.g., industry benchmarks).
2. **Define 12 Critical Topics** based on:
   - Latest advancements in financial technology.
   - Regulatory changes impacting the sector.
   - Tool and platform updates.
   - Methodology innovations.

3. **Map Ultimate Goal to Measurable Outcomes:**
   - Use SMART criteria for each metric (e.g., forecast revenue growth to be within ±5% of actual by 2024).
   - Define clear success metrics (e.g., variance between forecasted and actual results).

4. **Build Step-by-Step Workflow** from:
   - Industry playbooks.
   - Expert practitioner processes.
   - Tool vendor best practices.

5. **Include Latest 2024-2025 Practices:**
   - AI/ML integration for predictive analytics.
   - Automation of data collection and model calibration.
   - New tool capabilities (e.g., real-time scenario updates via APIs).

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Forecasting Techniques"
    focus: "Latest forecasting models including AI-driven approaches."
    sources: ["academic journals", "industry webinars"]
    deliverable: "Summary of top techniques with pros/cons"

  - agent_id: 2
    topic: "Data Analysis Tools"
    focus: "Advanced Excel capabilities and Python libraries."
    sources: ["official documentation", "YouTube tutorials"]
    deliverable: "Comparison table of tools and recommended use cases"

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

### Final Checklist

Before marking this task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Forecast accuracy meets the >90% target.
- [ ] **All Metrics Met?** All quantitative and qualitative performance targets are met or exceeded.
- [ ] **Quality Validated?** Data integrity verified, models validated against historical data.
- [ ] **Documentation Complete?** All deliverables stored in shared drive with proper naming conventions.
- [ ] **Sustainability Ensured?** Ongoing maintenance plan documented and approved by stakeholders.

### Continuous Improvement
- Document lessons learned from the scenario planning process.
- Update this template annually based on new best practices.
- Share insights gained with colleagues across departments.
- Schedule a quarterly review to assess ongoing relevance and effectiveness.

