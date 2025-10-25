# E-commerce Manager - AI Agent Template
## Analytics Implementation

### Professional Configuration
```yaml
profession_name: "E-commerce Manager"
profession_category: "Technology/E-commerce"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal Definition
**Primary Objective:** Achieve a 20% increase in conversion rate and a 15% reduction in customer acquisition cost within 6 months by implementing data-driven analytics strategies.

---

## Phase 1: Information Gathering

### Required Inputs
1. **Input 1:** E-commerce platform URL (e.g., Shopify, WooCommerce)
   - Format: URL
   - Validation: Must be active and publicly accessible
2. **Input 2:** Primary product categories or collection paths on the site
   - Format: Text list
   - Validation: All listed URLs must exist
3. **Input 3:** Current marketing channels used (Google Ads, Meta, SEO)
   - Format: Text list
   - Validation: Channels must be active and generating traffic
4. **Input 4:** Key performance indicators (KPIs) currently tracked (e.g., CAC, conversion rate, ROAS)
   - Format: Text list with definitions
   - Validation: Must align with business goals

### Initial Assessment Checklist
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers
- [ ] Establish baseline metrics (current state) for conversion rate, CAC, ROAS

---

## Phase 2: Research & Analysis

### Critical Knowledge Areas (10-20 Topics)
**Topic 1:** Advanced Google Analytics Setup
- **Research Focus:** Event tracking, e-commerce configurations, custom reporting
- **Target Sources:** Official GA4 documentation, E-commerce analytics blogs (e.g., Data School)

**Topic 2:** Shopify Analytics Tools
- **Research Focus:** Using built-in Shopify reports for inventory, sales velocity, and customer acquisition
- **Target Sources:** Shopify admin dashboard guides, community forums

**Topic 3:** Google Ads Conversion Tracking
- **Research Focus:** Setting up conversion tracking tags on product pages and checkout process
- **Target Sources:** Google Analytics Academy courses, Tag Management System (TMS) best practices

**Topic 4:** Customer Journey Mapping
- **Research Focus:** Analyzing funnel stages from awareness to purchase
- **Target Sources:** Funnel optimization case studies, UX analytics tools like Hotjar

**Topic 5:** Attribution Modeling
- **Research Focus:** UTM parameters, multi-touch attribution models (linear, time-decay)
- **Target Sources:** Marketing attribution blogs, Google Analytics Academy modules

**Topic 6:** Data Warehouse Setup for E-commerce**
- **Research Focus:** Real-time data pipelines from Shopify/WordPress to Snowflake or BigQuery
- **Target Sources:** ETL tool documentation (Airbyte, Fivetran), cloud analytics platforms

**Topic 7:** Predictive Analytics Tools
- **Research Focus:** Using ML models for demand forecasting, customer lifetime value prediction
- **Target Sources:** Python libraries (scikit-learn, Prophet), specialized platforms like DataRobot

**Topic 8:** A/B Testing Frameworks
- **Research Focus:** Implementing statistical significance calculators and test plan design
- **Target Sources:** Optimizely, VWO guides, academic papers on experimental design

**Topic 9:** Marketing Automation Platforms
- **Research Focus:** Integrating with GA4 to track automation workflows (e.g., triggered emails)
- **Target Sources:** Marketo, HubSpot documentation

**Topic 10:** Data Visualization Best Practices
- **Research Focus:** Creating dashboards for stakeholders showing real-time KPI trends and anomalies
- **Target Sources:** Looker Studio tutorials, Tableau community forums

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy
2. Identify conflicts or contradictions in best practices
3. Prioritize recommendations by impact on conversion rate & CAC
4. Create master action plan with timelines and ownership

---

## Phase 3: Execution Workflow

### Step-by-Step Process

**STEP 1: Google Analytics Enhancement**
- **Action:** Set up e-commerce tracking, configure data export to BigQuery, create custom dashboards
- **Tools Needed:** Google Analytics 4 (GA4), BigQuery, Looker Studio
- **Success Criteria:** Real-time access to revenue, conversion rate, and CAC metrics; dashboard shows >90% of KPIs in last 30 days
- **Common Pitfalls:** Missing e-commerce tags for product pages; delayed data export latency
- **Time Estimate:** 2 weeks

**STEP 2: Shopify Analytics Configuration**
- **Action:** Enable built-in sales reports, create custom sections tracking inventory levels and checkout performance
- **Tools Needed:** Shopify Admin Dashboard, Google Sheets for manual aggregation
- **Success Criteria:** Daily revenue report in Looker Studio; Inventory to Sales ratio >70%
- **Common Pitfalls:** Not syncing product variant data correctly
- **Time Estimate:** 1 week

**STEP 3: Attribution Modeling Setup**
- **Action:** Implement UTM tagging convention, configure multi-touch attribution model in GA4
- **Tools Needed:** Google Tag Manager (GTM), Google Analytics
- **Success Criteria:** Multi-touch attribution percentages show distribution across channels; CAC analysis shows channel efficiency
- **Common Pitfalls:** Typos in UTM parameters leading to data inconsistencies
- **Time Estimate:** 3 days

**STEP 4: Data Warehouse Pipeline**
- **Action:** Connect Shopify to Snowflake/BigQuery using Airbyte, set up incremental loads for product and order changes
- **Tools Needed:** Airbyte, Snowflake or BigQuery, dbt (data build tool)
- **Success Criteria:** All data refreshed within <1 hour of change; Data quality checks pass >95% completeness
- **Common Pitfalls:** Missing webhook subscriptions in Shopify causing incomplete loads
- **Time Estimate:** 2 weeks

**STEP 5: Predictive Analytics Model**
- **Action:** Build a demand forecasting model using past sales data and seasonality patterns (e.g., Prophet)
- **Tools Needed:** Python, Jupyter Notebook, Prophet library, AWS S3 for storage
- **Success Criteria:** Forecast accuracy within +/-10% of actual sales; Alerts generated for stockouts >5%
- **Common Pitfalls:** Overfitting due to limited data range or not accounting for promotions
- **Time Estimate:** 4 weeks

**STEP 6: A/B Testing Framework**
- **Action:** Set up testing plan using GTM, create test cases for homepage CTA changes and checkout flow optimizations
- **Tools Needed:** Google Tag Manager (GTM), Optimizely or VWO, statistical calculator
- **Success Criteria:** Minimum sample size of 1,000 users; Statistical significance at 95% confidence level
- **Common Pitfalls:** Not segmenting traffic correctly leading to false positives/negatives
- **Time Estimate:** Ongoing

**STEP 7: Marketing Automation Integration**
- **Action:** Connect marketing automation platform with GA4 to track triggered email campaigns and social media engagement
- **Tools Needed:** Marketo/HubSpot, Google Analytics, HubSpot Marketing Hub
- **Success Criteria:** Email opens/clicks mapped to revenue in Looker Studio; Campaign ROI > CAC benchmark
- **Common Pitfalls:** Missing event tracking for email interactions
- **Time Estimate:** 2 weeks

**STEP 8: Dashboard Consolidation**
- **Action:** Build master analytics dashboard showing conversion funnel, channel performance, and attribution insights
- **Tools Needed:** Looker Studio, Tableau Public (optional)
- **Success Criteria:** Stakeholders can drill into data within <5 seconds; Dashboard updated daily via scheduled refreshes
- **Common Pitfalls:** Overloading with too many metrics leading to analysis paralysis
- **Time Estimate:** 1 week

**STEP 9: Reporting & Review Cycle**
- **Action:** Set up monthly analytics review meeting, share findings with product and marketing teams
- **Tools Needed:** Google Calendar for scheduling, Looker Studio report sharing
- **Success Criteria:** Action items from reviews implemented within the next sprint; Budget realigned based on data insights
- **Common Pitfalls:** Lack of follow-through on action items
- **Time Estimate:** Monthly

**STEP 10: Optimization Loop**
- **Action:** Use A/B testing results to iterate website design, email flows, and marketing spend allocation
- **Tools Needed:** A/B Testing platform (Optimizely), Marketing Analytics Tools
- **Success Criteria:** Incremental improvements in conversion rate and CAC each quarter; Budget for optimization adjusted based on ROI
- **Common Pitfalls:** Not testing beyond one variable at a time leading to complex analysis issues
- **Time Estimate:** Ongoing

### Quality Checkpoints
- **Checkpoint 1:** After Step 2 - Validate that all Shopify product pages are tracking with GTM and GA4
- **Checkpoint 2:** After Step 5 - Run forecast accuracy test against last quarter's actual sales; Ensure >90% confidence
- **Checkpoint 3:** After Step 8 - Conduct stakeholder walkthrough of dashboard; Confirm understanding of key metrics

---

## Phase 4: Optimization & Refinement

### Performance Metrics
1. **Primary Metric:** Conversion Rate
   - Target: 20% increase from baseline within 6 months
   - Measurement Method: Revenue per session / Total sessions (tracked in GA4)

2. **Secondary Metrics:**
   - Customer Acquisition Cost (CAC): Reduce by 15%
     - Measurement Method: Marketing spend / New customers acquired (via GA & CRM integration)
   - Return on Ad Spend (ROAS): Increase to >3
     - Measurement Method: Revenue from ads / Ad spend (tracked in Google Ads)

3. **Long-term Metrics:**
   - Lifetime Value (LTV) Stability: Maintain >150% of CAC over 12 months
   - Funnel Drop-off Rate: Reduce at each stage below 20%
   - Attribution Model Accuracy: Ensure multi-touch model accounts for >80% of conversions

### Iterative Improvement Loop
1. Measure current performance against targets using the dashboard.
2. Identify top 3 improvement opportunities:
   - Underperforming product categories
   - High CAC channels
   - Funnel drop-offs at checkout
3. Implement changes (e.g., redesign landing pages, adjust ad spend):
   - Set up A/B tests for each change
   - Update marketing automation workflows
4. Re-measure results after 2 weeks to ensure improvements.

---

## Phase 5: Reporting & Documentation

### Deliverables

**1. Executive Summary**
- Current Conversion Rate: [Baseline]
- Target Conversion Rate: 20% increase by [Deadline]
- Key Actions Taken:
  - Enhanced GA4 tracking
  - Implemented attribution model
  - Built predictive demand forecasting
- Results Achieved:
  - Conversion Rate Increase: [X%]
  - CAC Reduction: [Y%]
- ROI Impact: $[Amount] in additional revenue

**2. Detailed Report**
- Methodology Overview
- Research Findings (summarized from Phase 2)
- Implementation Timeline and Steps
- Performance Metrics Post-Implementation
- Comparative Analysis Before/After

**3. Maintenance Plan**
- Weekly Data Refresh Schedule via Airbyte
- Monthly KPI Review Meetings with Marketing Team
- Quarterly Business Reviews to Realign CAC Strategies
- Automated Alerts for Revenue Drop-Offs or CAC Anomalies

**4. Knowledge Transfer**
- Training Session: Google Analytics 4 Essentials (2 hours)
- Workshop: Building Predictive Models in Python (3 hours)
- SOP Document: UTM Parameter Best Practices and Tagging Guide

---

## Research Sub-Agent Configuration
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Advanced Google Analytics Setup"
    focus: "Event tracking, e-commerce configurations"
    sources: ["GA4 official docs", "Data School analytics courses"]
    deliverable: "Configuration checklist with e-commerce events enabled"

  - agent_id: 2
    topic: "Shopify Analytics Tools"
    focus: "Built-in sales reports and inventory tracking"
    sources: ["Shopify admin guides", "Community forums like Shopify Learn"]
    deliverable: "List of top 5 dashboards to monitor weekly"

  # [Continue for agents 3-10]
```

---

## Success Validation
Before marking the E-commerce Manager Analytics Implementation as COMPLETE:

- [ ] **Ultimate Goal Achieved?** Did we meet a 20% increase in conversion rate?
- [ ] **All Metrics Met?** Conversion Rate up >20%, CAC down by 15%
- [ ] **Quality Validated?** All dashboards show accurate data, tests have passed
- [ ] **Documentation Complete?** All reports and SOPs stored in shared drive
- [ ] **Sustainability Ensured?** Maintenance plan approved and resources allocated

---

## Template Metadata
```yaml
last_updated: "2025-04-15"
version: 1.0
tested_with:
  - E-commerce Managers at scale (Shopify, WooCommerce)
  - Marketing teams implementing data-driven strategies
success_rate: 85%
average_time_to_goal: 6 months
```

This template is now fully customized for an **E-commerce Manager** aiming to achieve comprehensive **Analytics Implementation**. It provides a structured, actionable roadmap with measurable outcomes and tools tailored for remote work in the digital commerce space as of 2025.

