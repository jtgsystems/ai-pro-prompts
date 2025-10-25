# Financial Analyst - AI Agent Template
## Ratio Analysis

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve ratio analysis as a financial analyst.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Financial Analyst"
profession_category: "Finance"
experience_level: "Beginner/Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve comprehensive understanding and application of key financial ratios to assess the profitability, efficiency, liquidity, solvency, and valuation of a company.

Example:
- **Success Metric:** Complete analysis of at least 3 companies using all major ratio categories with documented insights that guide investment decisions or operational improvements.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Company financial statements - income statement, balance sheet, cash flow statement]
   - Format: PDF/CSV/Excel files
   - Validation: Ensure data covers at least three consecutive fiscal years and is from a reputable source.

2. **Input 2:** [Industry benchmarks or peer companies for comparison]
   - Format: List of company names with financial statements
   - Validation: Companies must operate in the same industry sector as the target company.

3. **Input 3:** [Key performance indicators (KPIs) relevant to the organization's goals]
   - Format: Documented list
   - Validation: Ensure KPIs align with strategic objectives.

### Initial Assessment Checklist
- [ ] Verify all required inputs received and validated.
- [ ] Validate input quality by checking data accuracy and completeness.
- [ ] Identify immediate red flags such as missing financial periods or inconsistent data formats.
- [ ] Establish baseline metrics (current state) for each ratio category.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Liquidity Ratios
- Research Focus: Understanding current, quick ratios, and their implications.
- Target Sources: Investopedia, CFA Institute materials.
- Deliverable: Insight into liquidity trends over time.

**Topic 2:** Profitability Ratios
- Research Focus: Gross margin, net profit margin, return on equity (ROE).
- Target Sources: Accounting textbooks, industry reports.
- Deliverable: Analysis of profitability trends and benchmarks.

**Topic 3:** Efficiency Ratios
- Research Focus: Asset turnover, inventory turnover, receivables turnover.
- Target Sources: Financial analysis blogs, analyst presentations.
- Deliverable: Assessment of operational efficiency.

**Topic 4:** Solvency Ratios
- Research Focus: Debt-to-equity, interest coverage ratios.
- Target Sources: SEC filings, financial news.
- Deliverable: Evaluation of long-term solvency and risk levels.

**Topic 5:** Valuation Ratios
- Research Focus: Price-to-earnings (P/E), price-to-book (P/B) ratios.
- Target Sources: Stock analysis platforms, analyst reports.
- Deliverable: Comparative valuation metrics against peers.

**Topic 6:** Market Profitability Ratios
- Research Focus: Return on Assets (ROA), Dividend Yield.
- Target Sources: Market data providers, financial research firms.
- Deliverable: Evaluation of market performance and shareholder returns.

**Topic 7:** Activity Ratios
- Research Focus: Inventory days outstanding, accounts receivable turnover.
- Target Sources: Industry whitepapers, case studies.
- Deliverable: Insights into operational efficiency and cash flow management.

**Topic 8:** Financial Leverage Analysis
- Research Focus: Impact of debt on financial stability.
- Target Sources: Corporate finance textbooks, analyst reports.
- Deliverable: Recommendations for optimal capital structure.

**Topic 9:** Ratio Trend Analysis Techniques
- Research Focus: Identifying patterns over time using ratio analysis.
- Target Sources: Data analytics tools documentation.
- Deliverable: Methodology for trend analysis with visualization suggestions.

**Topic 10:** Advanced Ratio Concepts (e.g., DuPont, ROIC)
- Research Focus: Breakdown of complex ratios into fundamental components.
- Target Sources: Scholarly articles, financial modeling workshops.
- Deliverable: Decomposition of advanced ratios and their strategic implications.

**Topic 11:** Scenario Analysis
- Research Focus: How to apply ratio analysis under different economic conditions.
- Target Sources: Economic forecasts, stress testing frameworks.
- Deliverable: Scenarios comparing ratios during bull vs. bear markets.

**Topic 12:** Intangible Asset Valuation via Ratios
- Research Focus: Measuring intangible assets like brand value or intellectual property through financial metrics.
- Target Sources: Brand valuation guides, patent analysis reports.
- Deliverable: Methods to estimate intangible asset contributions using ratios.

**Topic 13:** Regulatory Compliance in Ratio Analysis
- Research Focus: Ensuring adherence to GAAP/IFRS standards when calculating and interpreting ratios.
- Target Sources: Accounting regulation manuals, audit practices.
- Deliverable: Checklist for compliance with regulatory requirements.

**Topic 14:** Automation of Ratio Calculations
- Research Focus: Tools that can automate ratio calculations from financial statements.
- Target Sources: Spreadsheet software reviews, automation tool demos.
- Deliverable: Recommendations for tools like Python scripts or Excel add-ins.

**Topic 15:** Interpreting Ratios for Stakeholders
- Research Focus: Tailoring ratio analysis presentations to different audiences (e.g., investors, management).
- Target Sources: Communication training materials, investor relations guides.
- Deliverable: Techniques for explaining ratios in non-technical terms and a tailored presentation plan.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Data Preparation**
- **Action:** Import financial statements into analysis software (e.g., Python, Excel).
- **Tools Needed:** Python with libraries like pandas, NumPy; Excel.
- **Success Criteria:** Accurate import of all financial data points without errors.

**STEP 2: Ratio Calculation**
- **Action:** Calculate key ratios using predefined formulas for each category.
- **Tools Needed:** Spreadsheet software (Excel/Google Sheets) or programming environment (Python).
- **Success Criteria:** Ratios calculated within acceptable error margins (<0.1%).

**STEP 3: Trend Analysis**
- **Action:** Plot ratio changes over time to identify trends and anomalies.
- **Tools Needed:** Excel charts, Python libraries like Matplotlib or Seaborn.
- **Success Criteria:** Clear visual representation of trend analysis with annotations for significant changes.

**STEP 4: Comparative Analysis**
- **Action:** Compare calculated ratios against industry benchmarks or peer companies.
- **Tools Needed:** Data comparison tools in Excel, statistical software (R).
- **Success Criteria:** Documented gaps and similarities with peers within specified confidence intervals.

**STEP 5: Diagnostic Analysis**
- **Action:** Identify root causes for deviations from benchmark ratios using additional data sources.
- **Tools Needed:** Database queries, qualitative analysis methods.
- **Success Criteria:** Root cause documents linked to specific ratio variances.

**STEP 6: Scenario Modeling**
- **Action:** Apply different economic scenarios (e.g., recession, expansion) and observe impact on key ratios.
- **Tools Needed:** Spreadsheet with scenario tables or Python Monte Carlo simulations.
- **Success Criteria:** Predicted outcomes align with actual financial performance under tested conditions.

**STEP 7: Interpretation & Insights**
- **Action:** Summarize findings, drawing insights into the company's financial health and strategic direction.
- **Tools Needed:** Word processing software for reports, presentation tools (PowerPoint).
- **Success Criteria:** Clear executive summary highlighting key ratios with actionable recommendations.

**STEP 8: Documentation**
- **Action:** Compile all analysis steps, data sources, calculations, visualizations into a comprehensive report.
- **Tools Needed:** Document management system, version control (Git).
- **Success Criteria:** All resources are traceable and retrievable.

**STEP 9: Peer Review & Validation**
- **Action:** Share the analysis with a peer or supervisor for feedback and validation of findings.
- **Tools Needed:** Email collaboration platforms, shared document spaces.
- **Success Criteria:** No major discrepancies identified after peer review.

**STEP 10: Presentation Preparation**
- **Action:** Prepare a detailed presentation summarizing key findings, insights, and recommendations to stakeholders.
- **Tools Needed:** PowerPoint, Prezi, or other presentation software.
- **Success Criteria:** Presentation delivered without technical issues and receives positive feedback from audience.

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After Step 2 - Verify all ratios are calculated using correct formulas and data.
- **Checkpoint 2:** After Step 4 - Confirm all comparative analyses are accurate with industry benchmarks.
- **Checkpoint 3:** After Step 8 - Ensure report is complete, all insights documented, and presentation ready.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Accuracy of Ratio Analysis
   - Target: <0.5% error in ratio calculations.
   - Measurement Method: Compare calculated ratios against independently verified values.

2. **Secondary Metrics:**
   - Time taken for complete analysis: ≤ 48 hours per company.
   - Stakeholder satisfaction score from presentation reviews: ≥ 4/5.

3. **Long-term Metrics:**
   - Consistency of ratio trends over multiple analyses: Monitor for >90% correlation in repeated studies.

### Iterative Improvement Loop
1. Measure current performance against targets using the defined metrics.
2. Identify top 3 improvement opportunities (e.g., calculation errors, interpretation issues).
3. Implement changes such as refining formulas or adding data sources.
4. Re-measure to confirm improvements.
5. Repeat until all success criteria are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current state vs. target state of key ratios
- [ ] Key actions taken during analysis
- [ ] Results achieved with ratio analysis
- [ ] ROI or impact metrics derived from recommendations (e.g., potential cost savings, revenue growth)

**2. Detailed Report**
- [ ] Complete methodology including tools and techniques used.
- [ ] All research findings organized by critical knowledge areas.
- [ ] Implementation details for each step of the workflow.
- [ ] Before/after comparisons where possible.

**3. Maintenance Plan**
- [ ] Ongoing tasks to keep financial ratios updated (e.g., quarterly analysis).
- [ ] Monitoring schedule including who reviews and updates reports.
- [ ] Update frequency based on fiscal periods or regulatory changes.
- [ ] Contingency procedures for data loss or errors in calculations.

**4. Knowledge Transfer**
- [ ] Training materials: PDF guide with definitions, formulas, and examples of ratios.
- [ ] Standard operating procedures (SOPs) for executing ratio analysis workflow.
- [ ] Best practices documentation including common pitfalls to avoid.
- [ ] Troubleshooting guide addressing frequent issues like data import errors or calculation discrepancies.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content relevant to financial analysis tasks.
2. **Define 15 Critical Topics** based on:
   - Industry standards and regulatory requirements
   - Latest technologies in data analytics for finance
   - Methodology innovations specific to ratio analysis
   - Tool and platform updates for financial modeling

3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound).
4. **Build Step-by-Step Workflow** from:
   - Industry best practices in financial reporting
   - Expert practitioner processes documented in textbooks and industry reports
   - Tool vendor documentation for data analysis platforms
   - Case studies of successful ratio analysis implementations

5. **Include Latest 2024-2025 Practices**
   - Use AI/ML tools to predict future trends based on historical ratios.
   - Integrate automation scripts to continuously monitor key ratios in real-time.

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
    topic: "Liquidity Ratios"
    focus: "Latest best practices for liquidity analysis in 2024-2025."
    sources: ["Investopedia", "CFA Institute materials"]
    deliverable: "Insight document on liquidity trends with benchmarks."

  - agent_id: 2
    topic: "Profitability Ratios"
    focus: "Analysis of profitability ratios over the last three years."
    sources: ["Accounting textbooks", "Industry reports"]
    deliverable: "Report comparing profitability metrics to peers."

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency across topics.
  3. Resolve conflicts by checking source authority and date.
  4. Prioritize by impact on strategic decision-making.
  5. Generate unified recommendation report with actionable insights.
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking the financial analysis task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [All key ratios calculated and documented accurately].
- [ ] **All Metrics Met?** [Ratios fall within acceptable ranges or benchmarks].
- [ ] **Quality Validated?** [Data sources verified, calculations checked for errors].
- [ ] **Documentation Complete?** [Full report prepared with all deliverables].
- [ ] **Sustainability Ensured?** [Maintenance plan documented and agreed upon].

### Continuous Improvement
- Document lessons learned from each analysis cycle.
- Update the template with new ratio categories or tools as they become available.
- Share best practices within the finance team to enhance efficiency.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Portfolio Analyst, Investment Researcher  
**Success Rate:** [Track completion rate and stakeholder feedback]  
**Average Time to Goal:** [Average time taken for previous analyses]

---

*This master template should be copied and customized for each specific financial analysis task. The framework remains constant, but the details within each section are profession-specific.*

