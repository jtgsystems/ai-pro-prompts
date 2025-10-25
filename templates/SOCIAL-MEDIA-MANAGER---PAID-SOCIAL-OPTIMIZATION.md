# Social Media Manager - AI Agent Template

## Paid Social Optimization

### PROFESSION CONFIGURATION

**Profession Name:** Social Media Manager  
**Profession Category:** Marketing/Advertising  
**Experience Level:** Beginner to Intermediate (someone new to the role)

### Ultimate Goal Definition

**Primary Objective:** Achieve measurable growth and optimization in paid social media campaigns, driving a minimum 20% increase in Return on Ad Spend (ROAS) within 3 months of implementation.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Target Platform(s):** [Facebook Ads Manager, Instagram Insights, LinkedIn Campaign Manager]
2. **Campaign Objectives:** [Lead Generation, Brand Awareness, App Install, Website Traffic]
3. **Budget Allocation:** [$ per platform/monthly]
4. **Audience Demographics:** [Age, Gender, Location, Interests]
5. **Creative Assets:** [Images/Videos/Ad Copy Templates]

### Initial Assessment Checklist
- [ ] Verify all required inputs received and correctly formatted.
- [ ] Validate input quality (e.g., budget is realistic for platform).
- [ ] Identify immediate red flags (e.g., budget too low, unclear objectives).
- [ ] Establish baseline metrics (current ROAS, CPC, CTR).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Audience Segmentation  
**Research Focus:** Best practices for segmenting audiences based on behavior and demographics.
**Target Sources:** Facebook Business Help Center, LinkedIn Marketing Solutions.

**Topic 2:** Ad Creative Framework  
**Research Focus:** Latest design trends, color psychology, and format effectiveness.
**Target Sources:** Dribbble, Canva Pro (premium), Google Trends.

**Topic 3:** Algorithm Updates  
**Research Focus:** How algorithm changes impact ad performance on each platform.
**Target Sources:** Platform blogs, Social Media Examiner.

**Topic 4:** Targeting Options  
**Research Focus:** Expanded targeting options available in 2025.
**Target Sources:** Facebook Ads Help Center, Twitter Ads Guide.

**Topic 5:** Budget Allocation Strategies  
**Research Focus:** Advanced budget pacing and bidding strategies for optimal spend.
**Target Sources:** HubSpot Academy, Google Analytics Academy.

**Topic 6:** Measurement Framework  
**Research Focus:** Defining KPIs beyond ROAS (e.g., engagement rates, brand lift).
**Target Sources:** Nielsen Social Media Index, Brandwatch.

**Topic 7:** Cross-Platform Campaign Strategies  
**Research Focus:** Best practices for multi-channel ad campaigns.
**Target Sources:** HubSpot Blog, Sprout Social Benchmark Reports.

**Topic 8:** Ad Copy Optimization Techniques  
**Research Focus:** A/B testing frameworks and copywriting trends.
**Target Sources:** CXL Institute, Conversion Science.

**Topic 9:** Automation Tools  
**Research Focus:** Latest automation features in ad management platforms.
**Target Sources:** Buffer Blog, Hootsuite Insights.

**Topic 10:** Data-Driven Decision Making  
**Research Focus:** Leveraging analytics for campaign optimization.
**Target Sources:** Tableau Public, Google Data Studio.

**Topic 11:** Emerging Platforms and Trends  
**Research Focus:** New social media platforms or trends impacting strategy (e.g., Threads).
**Target Sources:** Social Media Today, Platform Announcements.

**Topic 12:** Case Studies on Paid Social Optimization  
**Research Focus:** Successful case studies highlighting ROI improvements.
**Target Sources:** LinkedIn Learning Library, Industry Whitepapers.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Account Setup and Configuration**
- **Action:** Create ad accounts for each platform, set currency and time zone.
- **Tools Needed:** Facebook Ads Manager, Google Analytics (optional), Hootsuite or Buffer (free).
- **Success Criteria:** Accounts live with correct settings; dashboards updated.

**STEP 2: Audience Research & Segmentation**
- **Action:** Analyze existing audience data; create new segments based on behavior.
- **Tools Needed:** Facebook Insights, Looker Studio (free), Google Analytics.
- **Success Criteria:** At least three distinct audience segments defined with clear demographics.

**STEP 3: Creative Development Workflow**
- **Action:** Design ad copy and visuals using Canva Pro for templates; iterate on designs based on research.
- **Tools Needed:** Canva Pro, Adobe Photoshop (free trial), Figma (optional).
- **Success Criteria:** Minimum of five ad variations ready for testing.

**STEP 4: Campaign Launch**
- **Action:** Create campaigns in each platform with budget allocation and targeting settings.
- **Tools Needed:** Facebook Ads Manager, LinkedIn Campaign Manager.
- **Success Criteria:** All campaigns launched within target budget; A/B testing set up.

**STEP 5: Real-Time Monitoring & Optimization**
- **Action:** Monitor daily performance metrics (CTR, ROAS); pause underperforming ads.
- **Tools Needed:** Facebook Ads Manager Dashboard, Google Data Studio for integration.
- **Success Criteria:** Daily KPI review process established; optimization actions taken within 24 hours.

**STEP 6: Budget Pacing & Optimization**
- **Action:** Adjust budget pacing based on performance trends; shift spend to top-performing segments.
- **Tools Needed:** Facebook Ads Manager, Hootsuite Insights (optional).
- **Success Criteria:** Budget utilized efficiently with high ROAS across all campaigns.

**STEPS 7-10+:** [Ongoing Optimization]
- Implement machine learning models for predictive budget allocation.
- Use AI-driven insights to tweak audience targeting and ad creatives.

### Quality Checkpoints
- **Checkpoint 1:** Verify account settings and data integration after STEP 1.
- **Checkpoint 2:** Validate audience segments against platform analytics post STEP 3.
- **Checkpoint 3:** Confirm campaign setup accuracy post STEP 4.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:
1. **Primary Metric:** ROAS (Revenue per Ad Spend)
   - Target: Minimum 20% increase over baseline.
   - Measurement Method: Compare against pre-optimization ROI.

2. **Secondary Metrics:**
   - CTR (Click-Through Rate): Aim for >3% improvement.
   - CPC (Cost Per Click): Maintain < $1.50 average spend.
   - Engagement Rate: Target >5% increase in likes/shares/comments.

### Iterative Improvement Loop
1. Measure current performance against targets each week.
2. Identify top 3 areas for improvement (e.g., underperforming ad sets).
3. Implement changes (budget shift, creative update).
4. Re-measure impact after 72 hours.
5. Repeat until primary metric goal achieved.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current vs. Target State
   - Key Actions Taken
   - Results Achieved (e.g., ROAS, CTR)

2. **Detailed Report**
   - Methodology Overview
   - Research Findings
   - Implementation Steps
   - Before/After Performance Metrics

3. **Maintenance Plan**
   - Ongoing Tasks: Weekly budget review, monthly creative refresh.
   - Monitoring Schedule: Daily for KPI tracking, Monthly for strategy updates.

4. **Knowledge Transfer**
   - Training Materials: Best practices guide for team members.
   - SOPs: Documented workflows for ad setup and optimization.
   - Troubleshooting Guide: Common issues (e.g., budget caps) with solutions.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Audience Segmentation"
    focus: "Latest segmentation techniques and tools"
    sources: ["Facebook Help Center", "Nielsen Social Media Index"]
    deliverable: "Segmentation framework with examples"

  - agent_id: 2
    topic: "Ad Creative Framework"
    focus: "Design trends and A/B testing methodologies"
    sources: ["Canva Pro", "Dribbble", "CXL Institute"]
    deliverable: "Creative brief template and test plan"

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Prioritize by impact to primary goal
  4. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the campaign as COMPLETE:

- [ ] **Primary Goal Achieved?** Is ROAS at least 20% higher than baseline?
- [ ] **All Metrics Met?** Are secondary KPIs (CTR, CPC) within target ranges?
- [ ] **Quality Validated?** Have all creative assets passed quality checks?
- [ ] **Documentation Complete?** All reports and SOPs delivered to team.
- [ ] **Sustainability Ensured?** Maintenance plan in place for ongoing optimization.

### Continuous Improvement
- Document lessons learned from the campaign.
- Update research templates with new findings.
- Share best practices within the marketing team.
- Schedule quarterly reviews of performance metrics.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Social Media Manager, Paid Ads Specialist  
**Success Rate:** N/A (to be measured post-completion)  
**Average Time to Goal:** Approximately 3 months for 20% ROAS increase

---

This template is now fully customized for a **Social Media Manager** aiming for **Paid Social Optimization**. It provides a detailed roadmap from initial setup through execution and optimization, complete with tools, metrics, and best practices specific to the role in 2024-2025.

