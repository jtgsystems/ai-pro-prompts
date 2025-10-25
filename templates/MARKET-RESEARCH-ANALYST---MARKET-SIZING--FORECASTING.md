# Market Research Analyst - AI Agent Template
## Market Sizing & Forecasting

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices for a Market Research Analyst focused on achieving market sizing and forecasting goals.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Market Research Analyst"
profession_category: "Business Intelligence"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve accurate market sizing and demand forecasting for the target product/service, enabling data-driven strategic decisions with a minimum ±5% accuracy in forecast vs. actual sales.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** Target Market Definition  
   - Format: Geographic scope (e.g., [North America], [Europe]), Demographic segments ([18-34 year olds, urban dwellers]), Industry verticals ([E-commerce])
   - Validation: Ensure the market definition aligns with business objectives and regulatory requirements.

2. **Input 2:** Historical Sales Data  
   - Format: CSV/Excel file containing past sales figures over [5 years], broken down by product line or segment.
   - Validation: Verify data integrity, completeness for at least three full fiscal cycles.

3. **Input 3:** Market Trends & Drivers Report  
   - Format: PDF/Word report summarizing macro trends (e.g., technological advancements), demographic shifts, economic indicators relevant to the market.
   - Validation: Ensure recent publication date ([2024-2025]) and relevance to current business environment.

### Initial Assessment Checklist
- [ ] All required inputs received and validated.
- [ ] Market definition aligns with company's strategic goals.
- [ ] Historical data completeness verified (>90% coverage).
- [ ] Trend report provides actionable insights relevant to the market.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Segmentation Strategies  
- Research Focus: Demographic, Psychographic, Behavioral segmentation techniques.
- Target Sources: Academic journals, Market research whitepapers.
- Deliverable: Segmentation matrix with rationale.

**Topic 2:** Data Collection Methods  
- Research Focus: Primary vs. Secondary data collection methods (surveys, interviews, web scraping).
- Target Sources: Case studies from Nielsen, Statista.
- Deliverable: Methodology toolkit with pros/cons.

**Topic 3:** Market Trend Analysis  
- Research Focus: Use of AI for trend forecasting in market research.
- Target Sources: Papers on ML applications in consumer behavior.
- Deliverable: List of tools and techniques (e.g., sentiment analysis).

**Topic 4:** Competitive Landscape  
- Research Focus: SWOT analysis, Porter's Five Forces for the target market.
- Target Sources: Business databases like IBISWorld.
- Deliverable: Competitor matrix with key insights.

**Topic 5:** Demand Forecasting Models  
- Research Focus: Time series analysis vs. Causal models (e.g., ARIMA, regression).
- Target Sources: Statistical software documentation.
- Deliverable: Model comparison table and recommended approach.

**Topic 6:** Market Size Estimation Techniques  
- Research Focus: Top-down vs. Bottom-up approaches for sizing total addressable market (TAM).
- Target Sources: Industry reports from Gartner, IDC.
- Deliverable: Sizing methodology with assumptions.

**Topic 7:** AI Integration in Market Analysis  
- Research Focus: Latest AI tools and platforms enhancing data analysis capabilities.
- Target Sources: Reviews on G2, TechCrunch.
- Deliverable: Comparison chart of top tools (e.g., Tableau, Power BI).

**Topic 8:** Data Visualization Best Practices  
- Research Focus: Effective ways to present findings to stakeholders.
- Target Sources: Design blogs, Infographic repositories.
- Deliverable: Visual presentation guidelines and examples.

**Topic 9:** Regulatory Compliance in Market Research  
- Research Focus: GDPR, CCPA implications for data handling and analysis.
- Target Sources: Legal databases like Westlaw.
- Deliverable: Checklist of compliance requirements.

**Topic 10:** Risk Assessment Frameworks  
- Research Focus: Identify potential risks (e.g., bias, privacy) in market research.
- Target Sources: Industry risk management guides.
- Deliverable: Risk register with mitigation strategies.

**Topic 11:** Collaboration Tools for Market Teams  
- Research Focus: Platforms facilitating cross-functional collaboration among analysts, marketers, and business units.
- Target Sources: Team productivity forums, vendor demos.
- Deliverable: Tool matrix highlighting key features.

**Topic 12:** Real-Time Data Processing Techniques  
- Research Focus: Stream processing tools and APIs for handling live market data feeds.
- Target Sources: Cloud provider documentation (AWS, Google Cloud).
- Deliverable: Use cases demonstrating real-time insights generation.

---

### Research Consolidation
After all sub-agents complete their research:
1. Synthesize findings into a unified strategy document.
2. Identify areas of consensus and conflict in methodologies.
3. Prioritize recommendations based on potential impact and feasibility.
4. Develop an action plan that integrates the most effective techniques.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
**STEP 1: [Data Preparation]**
- **Action:** Clean, validate, and normalize historical sales data; ensure it covers at least three full fiscal years.
- **Tools Needed:** Excel/Google Sheets (free), Python libraries (pandas), RStudio (free).
- **Success Criteria:** Data is free from errors, complete for all relevant periods.
- **Common Pitfalls:** Missing entries, inconsistent formatting.
- **Time Estimate:** 5 hours

**STEP 2: [Market Segmentation]**
- **Action:** Apply demographic and psychographic segmentation techniques using the input data; create distinct market segments based on identified criteria.
- **Tools Needed:** Python (scikit-learn), Excel/Google Sheets, Tableau Public (free).
- **Success Criteria:** Segments are logically defined with clear customer profiles.
- **Common Pitfalls:** Overlapping segments or insufficient differentiation.
- **Time Estimate:** 7 hours

**STEP 3: [Trend Analysis]**
- **Action:** Use AI-driven trend analysis tools to identify emerging patterns in consumer behavior and market dynamics.
- **Tools Needed:** Python (TensorFlow, scikit-learn), Google Trends API (free), MonkeyLearn (free tier).
- **Success Criteria:** Identified trends align with existing business hypotheses.
- **Common Pitfalls:** Overfitting models or ignoring seasonal variations.
- **Time Estimate:** 8 hours

**STEP 4: [Competitive Analysis]**
- **Action:** Compile a comprehensive competitive landscape report highlighting key players, market share trends, and strategic moves.
- **Tools Needed:** SEMrush (free trial), Ahrefs (paid alternative), BuzzSumo (free).
- **Success Criteria:** Report provides actionable insights into competitor positioning.
- **Common Pitfalls:** Focusing too heavily on volume rather than growth potential.
- **Time Estimate:** 6 hours

**STEP 5: [Market Sizing]**
- **Action:** Calculate total addressable market (TAM), serviceable available market (SAM), and serviceable obtainable market (SOM) using both top-down and bottom-up approaches.
- **Tools Needed:** Excel/Google Sheets, Python (pandas), R (free).
- **Success Criteria:** Calculations are transparent, based on validated assumptions.
- **Common Pitfalls:** Using outdated benchmarks or ignoring regulatory constraints.
- **Time Estimate:** 6 hours

**STEP 6: [Forecasting Model Development]**
- **Action:** Build a predictive model using time series analysis (e.g., ARIMA) and/or regression techniques to forecast sales for the next fiscal year.
- **Tools Needed:** Python (statsmodels), R (forecast package), Excel Solver (free).
- **Success Criteria:** Forecast aligns within ±5% of actual results in backtesting scenarios.
- **Common Pitfalls:** Over-reliance on historical data without accounting for external shocks.
- **Time Estimate:** 10 hours

**STEP 7: [Validation & Sensitivity Analysis]**
- **Action:** Validate the forecasting model using out-of-sample testing and conduct sensitivity analysis to assess how changes in key variables impact forecasts.
- **Tools Needed:** Python (scikit-learn), Excel Data Tables, R (forecast package).
- **Success Criteria:** Model demonstrates robustness with minimal error margins across scenarios.
- **Common Pitfalls:** Ignoring outliers or failing to test model under extreme conditions.
- **Time Estimate:** 5 hours

**STEP 8: [Reporting and Presentation]**
- **Action:** Prepare a comprehensive report detailing methodology, key findings, and financial implications of the market sizing and forecasting exercise.
- **Tools Needed:** PowerPoint (free), Google Slides, Tableau for data visualization.
- **Success Criteria:** Report is clear, concise, and actionable; approved by stakeholders.
- **Common Pitfalls:** Overloading with technical detail or failing to highlight strategic value.
- **Time Estimate:** 4 hours

**STEP 9: [Stakeholder Review and Feedback Loop]**
- **Action:** Present findings to key stakeholders (e.g., product management, sales leadership) and incorporate feedback into the model.
- **Tools Needed:** Zoom/Teams (free), SurveyMonkey (free tier).
- **Success Criteria:** Stakeholders provide constructive feedback; agreed-upon adjustments implemented.
- **Common Pitfalls:** Lack of communication or failure to address critical feedback.
- **Time Estimate:** 3 hours

**STEP 10: [Implementation Planning]**
- **Action:** Develop an implementation plan detailing actions, timelines, and responsibilities for capitalizing on the forecasted market opportunities.
- **Tools Needed:** Gantt charts (Google Sheets), Asana/Trello (free).
- **Success Criteria:** Plan is realistic, aligns with resource constraints, includes risk mitigation strategies.
- **Common Pitfalls:** Overestimating capacity or neglecting contingency planning.
- **Time Estimate:** 4 hours

### Quality Checkpoints
1. **Checkpoint 1:** After Step 5 - Validate market sizing assumptions against independent benchmarks (e.g., industry reports).
2. **Checkpoint 2:** After Step 8 - Ensure all data presented is current and sourced accurately.
3. **Checkpoint 3:** Post-Implementation Review - Monitor execution progress and adjust forecasts based on real-world performance.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Forecast Accuracy  
   - Target: ±5% relative error compared to actual sales.
   - Measurement Method: Calculate forecast vs. actual variance over the next fiscal year.

2. **Secondary Metrics:**  
   - Model Validation Score: ≥85% in out-of-sample testing.
   - Stakeholder Satisfaction: ≥80% positive feedback from reviewers.

3. **Long-term Metrics:**  
   - Revenue Growth Rate: Achieve at least 10% YoY growth based on forecasted market opportunities.

### Iterative Improvement Loop
1. Measure current performance against target accuracy and validate with actual sales data.
2. Identify top three areas for improvement (e.g., data quality, model assumptions).
3. Implement changes such as additional data sources or refined algorithms.
4. Re-measure to ensure metrics are within acceptable ranges.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state; Key actions taken; Results achieved with a forecast accuracy of ±5%.

**2. Detailed Report**
- Methodology used, data sources, market sizing and forecasting techniques, stakeholder feedback.

**3. Maintenance Plan**
- Ongoing tasks include quarterly model recalibration, bi-annual stakeholder review meetings.

**4. Knowledge Transfer**
- Training sessions for team members on using the forecasting model.
- Standard operating procedures documenting each step of the process.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. Replace all [BRACKETED] inputs with specific market data and analyst requirements.
2. Define 12 critical topics based on current industry trends, regulatory environment, and tool availability.
3. Align ultimate goal with SMART criteria: Specific (e.g., target US retail segment), Measurable (e.g., achieve ±5% forecast accuracy), Achievable within budget constraints, Relevant to company's strategic direction, Time-bound (within 6 months).

### Building the Step-by-Step Workflow
1. **Gather Inputs:** Ensure all required data is available and properly formatted.
2. **Deploy Research Agents:** Use AI tools for automated literature review and trend analysis.
3. **Collaborate with Cross-functional Teams:** Integrate insights from sales, finance, and product development to ensure alignment.

### Tools & Software Stack
- **Primary Tool (free):** Python (Anaconda), RStudio
- **Data Visualization:** Tableau Public, Power BI Desktop (free tier)
- **Market Analysis:** SEMrush, Ahrefs (paid trial), BuzzSumo
- **Collaboration:** Google Workspace Suite (Docs, Sheets, Slides)
- **Data Storage & Sharing:** SharePoint Online, Dropbox Business

---

## SUCCESS VALIDATION

### Final Checklist Before Completion
- [ ] Ultimate Goal Achieved? Forecast accuracy ±5%.
- [ ] All Metrics Met? Model validation score ≥85%, stakeholder satisfaction ≥80%.
- [ ] Quality Validated? Data completeness >95%, assumptions documented.
- [ ] Documentation Complete? All deliverables uploaded to shared drive.

### Continuous Improvement
- Conduct quarterly reviews of model performance and market dynamics.
- Update the template annually with new industry practices or tool releases.
- Share best practices within the organization through internal workshops.

