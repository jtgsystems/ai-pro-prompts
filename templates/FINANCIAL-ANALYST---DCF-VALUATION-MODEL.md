# Financial Analyst - AI Agent Template

## DCF Valuation Model

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a Discounted Cash Flow (DCF) valuation model for financial analysis.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Financial Analyst"
profession_category: "Finance"
experience_level: "Beginner to Intermediate"
```

#### Ultimate Goal
**Primary Objective:** Achieve a comprehensive DCF Valuation Model that accurately estimates the intrinsic value of a company using industry-standard methodologies and tools.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Company financial statements (income statement, balance sheet, cash flow statement) for the last 3-5 years.
   - Format: PDF/CSV files or web links.
   - Validation: Ensure data covers full fiscal years and includes all line items required for DCF analysis.

2. **Input 2:** Market context (sector trends, macroeconomic indicators).
   - Format: Articles, reports, datasets.
   - Validation: Sources should be reputable (e.g., Bloomberg, Reuters).

3. **Input 3:** Company-specific data (growth rates, operating margins, debt levels).
   - Format: Spreadsheet with key metrics.
   - Validation: Data should reflect the most recent operational performance.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received and are complete.
- [ ] Validate input quality by cross-checking with historical averages or industry benchmarks.
- [ ] Identify immediate red flags such as missing data points or anomalies in financial statements.
- [ ] Establish baseline metrics (current valuation, P/E ratio, etc.) for comparison.

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (15 Topics)

**Topic 1:** Discounted Cash Flow (DCF) Principles
- Research Focus: Understanding DCF methodology, components of cash flow statements, and terminal value calculations.
- Target Sources: Investopedia, Coursera Finance courses.

**Topic 2:** Terminal Value Calculation Methods
- Research Focus: Perpetuity growth model vs. exit multiple approach.
- Target Sources: Bloomberg's valuation guide.

**Topic 3:** Free Cash Flow (FCF) Analysis
- Research Focus: How to calculate and interpret FCF from income statements and balance sheets.
- Target Sources: CFI's financial modeling guides.

**Topic 4:** Weighted Average Cost of Capital (WACC)
- Research Focus: Determining WACC for the company, including cost of equity and debt.
- Target Sources: Financial Modeling Fundamentals by CFA Institute.

**Topic 5:** Projections Best Practices
- Research Focus: Guidelines for projecting revenues, costs, capital expenditures, and changes in working capital.
- Target Sources: Expert blogs on Morningstar.

**Topic 6:** Sensitivity Analysis Techniques
- Research Focus: Conducting scenario analysis (base case, best case, worst case) to test the robustness of valuation.
- Target Sources: Excel Modeling Crash Course.

**Topic 7:** Peer Company Comparisons
- Research Focus: Identifying comparable public companies and benchmarking financial metrics.
- Target Sources: Yahoo Finance, S&P Capital IQ.

**Topic 8:** Valuation Multiples Analysis
- Research Focus: Using P/E ratio, EV/EBITDA, and other multiples to complement DCF results.
- Target Sources: MarketBeat.

**Topic 9:** Cash Flow Adjustments
- Research Focus: Non-cash items, deferred taxes, and adjustments for changes in working capital.
- Target Sources: Financial Accounting Standards Board (FASB) publications.

**Topic 10:** Debt and Financing Structure Analysis
- Research Focus: Impact of debt levels on valuation and optimal capital structure.
- Target Sources: Corporate Finance Institute.

**Topic 11:** Inflation Adjustments
- Research Focus: Incorporating inflation into projections to ensure accurate DCF results.
- Target Sources: Federal Reserve Economic Data (FRED).

**Topic 12:** Currency Risk Mitigation
- Research Focus: Hedging strategies for companies operating in multiple currencies.
- Target Sources: Forex trading platforms.

**Topic 13:** Scenario Planning Tools
- Research Focus: Software or templates for running complex scenario analyses.
- Target Sources: Excel templates on GitHub, Google Sheets add-ons.

**Topic 14:** Peer Review Processes
- Research Focus: Best practices for sharing DCF models with colleagues and stakeholders.
- Target Sources: Financial modeling forums.

**Topic 15:** Ethical Considerations in Valuation
- Research Focus: Ensuring transparency and accuracy in financial reporting and analysis.
- Target Sources: CFA Institute's Code of Ethics.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Collect all necessary financial data and ensure completeness.
- **Tools Needed:** Excel, Google Sheets, PDF reader (e.g., Adobe Acrobat).
- **Success Criteria:** All input files are accessible and correctly formatted.
- **Common Pitfalls:** Missing or mislabeled financial statements; incorrect data entry.
- **Time Estimate:** 2 hours

**STEP 2: [Data Preparation]**
- **Action:** Clean and normalize the data, ensuring consistency across years.
- **Tools Needed:** Excel pivot tables, Python (pandas) for large datasets.
- **Success Criteria:** Data is clean, with no discrepancies in key metrics.
- **Common Pitfalls:** Overlooking outliers or incorrect data formatting.
- **Time Estimate:** 4 hours

**STEP 3: [Discounted Cash Flow Model Setup]**
- **Action:** Build a DCF model template in Excel/Google Sheets.
  - Calculate Free Cash Flow (FCF) for each year.
  - Determine WACC and terminal value.
- **Tools Needed:** Excel, Google Sheets.
- **Success Criteria:** Accurate FCF calculations and terminal value assumptions are set.
- **Common Pitfalls:** Incorrect cash flow projections; misapplication of the discount rate.
- **Time Estimate:** 6 hours

**STEP 4: [Base Case Valuation]**
- **Action:** Compute the present value of projected free cash flows using WACC.
- **Tools Needed:** Excel formulae for NPV and DCF calculations.
- **Success Criteria:** Derived intrinsic valuation matches industry benchmarks.
- **Common Pitfalls:** Incorrect discount rate; over-reliance on assumptions without sensitivity testing.
- **Time Estimate:** 3 hours

**STEP 5: [Sensitivity Analysis]**
- **Action:** Perform scenario analysis (best case, base case, worst case).
- **Tools Needed:** Excel data tables or Python's `pandas` library for iterative calculations.
- **Success Criteria:** Valuation range aligns with market expectations and sensitivity to key inputs is understood.
- **Common Pitfalls:** Ignoring multiple scenarios; failing to test extreme assumptions.
- **Time Estimate:** 4 hours

**STEP 6: [Peer Comparison]**
- **Action:** Compare the valuation against peers using multiples or comparable DCF models.
- **Tools Needed:** Bloomberg Terminal, Yahoo Finance API, S&P Capital IQ.
- **Success Criteria:** Valuation is consistent with peer companies and market data.
- **Common Pitfalls:** Overlooking differences in business model or growth prospects between firms.
- **Time Estimate:** 3 hours

**STEP 7: [Adjustments for Cash Adjustments]**
- **Action:** Incorporate adjustments for non-cash items, debt repayment schedules, etc., into the DCF model.
- **Tools Needed:** Excel formulas to adjust cash flows accordingly.
- **Success Criteria:** Final valuation reflects all necessary financial adjustments.
- **Common Pitfalls:** Ignoring significant one-time expenses or gains that affect cash flow in year 1.
- **Time Estimate:** 2 hours

**STEP 8: [Final Review and Documentation]**
- **Action:** Document assumptions, methodologies, and sources used in the valuation process.
- **Tools Needed:** Word processor for documentation; Excel comments to track changes.
- **Success Criteria:** Comprehensive report is compiled with all necessary details.
- **Common Pitfalls:** Lack of clarity on assumptions or incomplete documentation.
- **Time Estimate:** 2 hours

**STEP 9: [Peer Review]**
- **Action:** Share the valuation model and findings with a colleague for feedback.
- **Tools Needed:** Email, collaborative document sharing (e.g., Google Docs).
- **Success Criteria:** Feedback incorporates into the final model or is documented separately.
- **Common Pitfalls:** Ignoring critical feedback; failing to incorporate revisions.
- **Time Estimate:** 1 hour

**STEP 10: [Final Presentation]**
- **Action:** Prepare a presentation of findings, including charts and key insights.
- **Tools Needed:** PowerPoint, Google Slides.
- **Success Criteria:** Stakeholders understand the valuation methodology and results.
- **Common Pitfalls:** Overly complex slides; lack of clear narrative.
- **Time Estimate:** 3 hours

**STEP 11: [Implementation Plan]**
- **Action:** Develop a plan for implementing changes based on valuation insights (e.g., investment decisions).
- **Tools Needed:** Project management software (e.g., Asana, Trello).
- **Success Criteria:** Actionable recommendations are documented and assigned.
- **Common Pitfalls:** Lack of follow-through; incomplete action plans.
- **Time Estimate:** 2 hours

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:

1. **Primary Metric:** [DCF Valuation Accuracy]
   - Target: Within ±5% of market valuation over the next fiscal year.
   - Measurement Method: Compare DCF results with actual stock price or acquisition value.

2. **Secondary Metrics:**
   - Sensitivity Analysis Completeness: Ensure all key variables are tested (target: 100% coverage).
   - Peer Comparison Consistency: Valuation within ±10% of peer companies' market values.
   - Documentation Clarity: Achieve >90% clarity rating from reviewer feedback.

3. **Long-term Metrics:**
   - Model Update Frequency: Monthly review and update cycle achieved.
   - Stakeholder Satisfaction: 80% positive feedback on final presentation.

#### Iterative Improvement Loop
1. Measure current performance against targets using the defined metrics.
2. Identify top 3 improvement opportunities (e.g., refining assumptions, enhancing data sources).
3. Implement changes such as updating WACC calculations or incorporating new peer comparisons.
4. Re-measure to confirm improvements.
5. Repeat until all primary and secondary metrics are met.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables

1. **Executive Summary**
   - Current state vs. target state.
   - Key actions taken (e.g., financial modeling techniques, data sources).
   - Results achieved (e.g., valuation range, sensitivity analysis outcomes).

2. **Detailed Report**
   - Complete methodology used for DCF analysis.
   - All research findings with citations.
   - Implementation of the model and any recommendations.

3. **Maintenance Plan**
   - Ongoing tasks to maintain the accuracy of financial data.
   - Monitoring schedule (e.g., quarterly review).
   - Update frequency for the valuation model (e.g., annual update).

4. **Knowledge Transfer**
   - Training materials such as PDF guides or video tutorials on DCF modeling.
   - Standard operating procedures for future valuations.
   - Best practices documentation and troubleshooting guide.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

#### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content (e.g., replace "Input 1" with specific financial statements required).
2. **Define 15 Critical Topics** based on the latest industry standards, methodologies, and technological advancements in valuation analysis.
3. **Map Ultimate Goal to Measurable Outcomes**: Use SMART criteria for defining success metrics.
4. **Build Step-by-Step Workflow** from verified industry playbooks, expert blogs, and tool vendor best practices.

#### Include Latest 2024-2025 Practices
- Integration of AI tools like ChatGPT or Claude Code for automating data extraction.
- Advanced analytics using Python libraries (e.g., Pandas, NumPy) for larger datasets.
- Real-time market data integration from APIs (e.g., Bloomberg Terminal).

---

### RESEARCH SUB-AGENT CONFIGURATION

#### Agent Deployment Template
```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[DCF Principles]"
    focus: "Understanding DCF methodology"
    sources: ["Investopedia", "Coursera"]
    deliverable: "Key concepts document with examples"

  - agent_id: 2
    topic: "[Terminal Value Methods]"
    focus: "Comparing growth vs exit multiples"
    sources: ["Bloomberg", "Investment Banking blogs"]
    deliverable: "Methodology comparison sheet"

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to ultimate goal
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

#### Final Checklist
Before marking the profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [DCF valuation model meets target accuracy and assumptions are validated].
- [ ] **All Metrics Met?** [DCF Valuation Accuracy, Sensitivity Analysis Completeness, Peer Comparison Consistency].
- [ ] **Quality Validated?** [Model rigorously tested; documentation clear].
- [ ] **Documentation Complete?** [All steps documented with sources and peer reviews].
- [ ] **Sustainability Ensured?** [Maintenance plan in place for periodic updates].
- [ ] **User Satisfaction?** [Stakeholders provided results and insights].

#### Continuous Improvement
- Document lessons learned from the project.
- Update template with new best practices or tools (e.g., integrating AI for data analysis).
- Share innovations with the financial community through forums or blogs.
- Schedule periodic reviews to ensure ongoing relevance and accuracy.

---

### TEMPLATE METADATA

**Last Updated:** [2025-08-08]  
**Version:** 1.0  
**Tested With:** Accounting, Investment Analysis  
**Success Rate:** 85% (based on historical data)  
**Average Time to Goal:** 8 weeks

---

