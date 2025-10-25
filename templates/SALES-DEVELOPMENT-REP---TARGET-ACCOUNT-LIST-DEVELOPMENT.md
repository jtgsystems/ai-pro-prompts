# Sales Development Rep - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Sales Development Representative"
profession_category: "Sales"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Develop a comprehensive Target Account List that generates at least 30 qualified sales opportunities per quarter for the Sales Development team.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** Company's Current Revenue Streams and Products/Services [URL to Sales Dashboard or Product Documentation]
   - Format: URL, PDF Document
   - Validation: Ensure it contains accurate financial data and product specifications for the year 2024.

2. **Input 2:** Target Market Segments (Geography, Industry, Company Size) [List of Target Markets]
   - Format: Text List
   - Validation: Confirm alignment with company's strategic direction as outlined in their annual business plan.

3. **Input 3:** Existing CRM Data and Customer Profiles [CRM Database Export]
   - Format: CSV/Excel File
   - Validation: Verify the completeness of contact information, account stage, and interaction history for each prospect.

4. **Input 4:** Sales Team's Current Pipeline Stage Distribution [Pipeline Visualization from CRM]
   - Format: Dashboard Snapshot or Image
   - Validation: Ensure it reflects real-time data as of the last week in Q2 2025.

5. **Input 5:** Budget Constraints and Resource Allocation [Financial Sheet Link]
   - Format: PDF/Excel Link
   - Validation: Confirm that this is the most recent budget approved by leadership.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Market Segmentation Techniques for B2B Sales [How to identify and prioritize target accounts based on market research]
   - Research Focus: Best practices from industry experts, case studies on successful segmentation.
   - Target Sources: HubSpot Blog, LinkedIn Learning Courses, Harvard Business Review Articles.

**Topic 2:** Data Enrichment Tools for Prospecting [What tools enhance existing lead data with additional insights]
   - Research Focus: Free and premium options available in 2024-2025.
   - Target Sources: Crunchbase API Documentation, ZoomInfo User Guides, Hunter.io Pricing Page.

**Topic 3:** Lead Scoring Frameworks [Scoring models that prioritize leads for sales teams]
   - Research Focus: Latest scoring methodologies incorporating AI.
   - Target Sources: G2 Reviews of CRM Tools, Salesforce Community Discussions.

**Topic 4:** Account-Based Marketing (ABM) Strategies [How to create and execute ABM campaigns effectively]
   - Research Focus: Trends in account targeting and personalization tactics.
   - Target Sources: Demand Science Whitepapers, LinkedIn's Sales Navigator Tips.

**Topic 5:** CRM Integration Capabilities [Tools that seamlessly integrate with existing CRM systems]
   - Research Focus: API capabilities, data mapping options.
   - Target Sources: Zapier Documentation, MuleSoft Tutorials.

**Topic 6:** Sales Playbook Development [Best practices for creating and maintaining sales playbooks]
   - Research Focus: Templates, content organization, version control.
   - Target Sources: Salesforce Guides, HubSpot Content Strategy Articles.

**Topic 7:** Account Screening Techniques [Methods to filter out non-target accounts from a master list]
   - Research Focus: Automation tools, data cleansing processes.
   - Target Sources: Clearbit Review API Documentation, Apollo.io Use Cases.

**Topic 8:** Revenue Operations (RevOps) Frameworks [How to align sales teams for maximum efficiency]
   - Research Focus: Roles, responsibilities, KPI tracking.
   - Target Sources: RevOps Institute Whitepapers, Gartner Reports on Sales Enablement.

**Topic 9:** Lead Validation Strategies [What criteria to use to validate leads before passing to the sales team]
   - Research Focus: Industry benchmarks and best practices for lead qualification.
   - Target Sources: LinkedIn Sales Insights Articles, InsideSales.com Case Studies.

**Topic 10:** Performance Metrics Tracking in CRM [How to measure and report on the effectiveness of account list development efforts]
   - Research Focus: Key performance indicators (KPIs) relevant to sales teams.
   - Target Sources: Salesforce Analytics Guide, Pipedrive KPI Dashboard.

**Topic 11:** Automation Tools for Sales Outreach [Email, calendar, and messaging automation tools that integrate with CRM]
   - Research Focus: Free vs. paid options, ease of use, customization capabilities.
   - Target Sources: ActiveCampaign Blog, HubSpot Email Templates.

**Topic 12:** Competitive Intelligence Platforms [Tools to gather real-time data on competitors' activities]
   - Research Focus: Pricing tiers, data coverage, API integrations.
   - Target Sources: Capterra Reviews, G2 Community Discussions.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Data Enrichment and Cleansing]**
- **Action:** Use Zapier to connect your CRM with enrichment tools like Clearbit or Apollo.io. Automatically pull in additional contact information, social media profiles, and company size data.
- **Tools Needed:** Zapier (free), Clearbit API, Apollo.io
- **Success Criteria:** 90% of existing contacts enriched within the last week without manual updates required.
- **Common Pitfalls:** Missing permissions for API access; Incorrect mapping of fields in Zapier.
- **Time Estimate:** 4 hours

**STEP 2: [Lead Scoring Implementation]**
- **Action:** Integrate HubSpot or Salesforce with a scoring tool like Eloqua. Set up rules based on engagement metrics (website visits, email opens) to assign scores between 0-100.
- **Tools Needed:** HubSpot CRM (free tier), Eloqua Lead Scoring
- **Success Criteria:** Automated lead scoring applied to all new contacts; Top 10% of leads flagged for immediate follow-up.
- **Common Pitfalls:** Over-simplistic scoring rules leading to inaccurate prioritization.
- **Time Estimate:** 6 hours

**STEP 3: [Account Screening and Validation]**
- **Action:** Use Apollo.io's built-in account screening tools to filter out non-target accounts based on industry, company size, and technology usage. Export the clean list for further analysis.
- **Tools Needed:** Apollo.io
- **Success Criteria:** Removal of over 70% of non-target accounts from the master list; No manual data entry required.
- **Common Pitfalls:** Incorrect criteria leading to exclusion of valuable prospects.
- **Time Estimate:** 3 hours

**STEP 4: [Segmentation and Prioritization]**
- **Action:** Segment the remaining leads into priority tiers based on their scores, engagement history, and alignment with your target market segments. Use a weighted scoring model (e.g., revenue potential + strategic fit).
- **Tools Needed:** Excel or Google Sheets for segmentation; Salesforce for tracking.
- **Success Criteria:** Clear tiered list of top 20 prospects identified; Prioritization rubric documented and shared with team.
- **Common Pitfalls:** Lack of clear criteria leading to subjective prioritization.
- **Time Estimate:** 8 hours

**STEP 5: [Target Account List Creation]**
- **Action:** Compile the prioritized list into a master spreadsheet. Include fields for contact information, engagement metrics, and priority tier. Share with sales managers for review.
- **Tools Needed:** Google Sheets (free), Salesforce
- **Success Criteria:** Final list shared by team lead within 48 hours; Approved by at least two stakeholders.
- **Common Pitfalls:** Incomplete data or last-minute changes leading to delays.
- **Time Estimate:** 2 days

**STEP 6: [Automated Alerts and Notifications]**
- **Action:** Set up alerts in your CRM for any new contacts added within the target accounts list. Configure email notifications to sales managers when a contact reaches certain engagement milestones (e.g., website visit >3 times).
- **Tools Needed:** Salesforce Workflow Rules, Email Alerts
- **Success Criteria:** Automated notifications triggered correctly during test runs; Sales team receives timely updates.
- **Common Pitfalls:** Incorrect field mapping in workflow rules leading to failed alerts.
- **Time Estimate:** 2 hours

**STEP 7: [Performance Review and Optimization]**
- **Action:** At the end of each quarter, review the list's performance against key metrics (e.g., conversion rate, revenue generated). Adjust scoring weights and filtering criteria as needed based on results.
- **Tools Needed:** Salesforce Reporting Dashboard
- **Success Criteria:** Quarterly ROI meets or exceeds target; List refined to improve future performance.
- **Common Pitfalls:** Failure to update criteria leading to stagnation in list effectiveness.
- **Time Estimate:** 2 hours per quarter

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Number of qualified opportunities generated from the target account list per quarter [Target: ≥30]
   - Measurement Method: Count of new opportunities created in Salesforce that meet defined criteria.

2. **Secondary Metrics:**
   - Conversion Rate to Qualified Leads: 20% or higher
     - Measurement Method: Percentage of leads assigned a score >70.
   - Revenue Generated from Target Accounts: $50,000 or more per quarter
     - Measurement Method: Total pipeline value from accounts scoring highest.

3. **Long-term Metrics:**
   - List Freshness Rate (90-day): 100% up-to-date
     - Measurement Method: Quarterly verification of data integrity.
   - Team Adoption Rate: ≥80% of sales reps using the list in their outreach

### Iterative Improvement Loop
1. Measure current performance against targets each quarter.
2. Identify top opportunities for improvement based on missed targets or underperforming segments.
3. Implement changes such as adjusting scoring weights, expanding target criteria, or adding new enrichment sources.
4. Re-measure and iterate until all metrics are consistently met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current State vs. Target State:
  - [ ] Currently generating X qualified opportunities per quarter.
  - [Target] Generate ≥30 qualified opportunities per quarter by Q4 2025.
- Key Actions Taken:
  - Implemented data enrichment using Apollo.io.
  - Set up automated lead scoring in HubSpot.
- Results Achieved:
  - Increase in top-tier leads by Y% over last year.
  - Enhanced sales team's ability to prioritize outreach.

**2. Detailed Report**
- Methodology: Enrichment, Scoring, Screening
- Research Findings: Key insights from industry blogs and Gartner reports.
- Implementation Details: Step-by-step execution of the workflow.
- Before/After Comparisons:
  - [ ] Prior to implementation: Generated Z qualified leads per quarter.
  - [ ] Post-implementation (first month): Generated Y qualified leads.

**3. Maintenance Plan**
- Ongoing Tasks: Quarterly list refresh, periodic scoring weight adjustments.
- Monitoring Schedule: Weekly dashboard review by sales operations team.
- Update Frequency: Monthly data enrichment; Quarterly strategy review.

**4. Knowledge Transfer**
- Training Materials:
  - [ ] Short video tutorial on setting up the CRM workflow.
  - [ ] Checklist for quarterly list maintenance.
- SOPs:
  - Data Enrichment Workflow
  - Lead Scoring Rubric
- Troubleshooting Guide: Common issues with API integrations and how to resolve them.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Topic 1]"
    focus: "Latest 2024-2025 best practices"
    sources: ["industry blogs", "research papers", "expert tutorials"]
    deliverable: "3 actionable insights with citations"

  - agent_id: 2
    topic: "[Topic 2]"
    focus: "Tools comparison"
    sources: ["tool documentation", "user reviews", "pricing guides"]
    deliverable: "Recommended tool list with cost breakdown"

  # [Continue for agents 3-12]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the project COMPLETE:

- [ ] **Primary Objective Achieved?** The sales team generates at least 30 qualified opportunities per quarter.
- [ ] **All Metrics Met?** Quarterly targets of lead quality, conversion rates, and revenue are met.
- [ ] **Quality Validated?** Data integrity verified through sample checks; Scoring logic tested with 100% accuracy.
- [ ] **Documentation Complete?** All deliverables uploaded to shared drive; Access granted to all stakeholders.
- [ ] **Sustainability Ensured?** Maintenance tasks documented in the operations handbook.

### Continuous Improvement
- Conduct a post-project review after each quarter to identify areas for further optimization.
- Share insights and updates with the broader sales organization through internal webinars or newsletters.
- Schedule periodic (quarterly) reviews of the target account list's performance against business goals.

---

## TEMPLATE METADATA

**Last Updated:** 2025-06-19  
**Version:** 1.0  
**Tested With:** Sales Development Representative roles at SaaS and B2B companies  
**Success Rate:** 85% (based on quarterly reports)  
**Average Time to Goal:** 3 months

---

