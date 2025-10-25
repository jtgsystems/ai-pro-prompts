# Email Marketing Specialist - AI Agent Template
## Deliverability Mastery

### PROFESSION CONFIGURATION
```yaml
profession_name: "Email Marketing Specialist"
profession_category: "Marketing Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve 99.5% or higher email deliverability rate for all campaigns with sustained performance across all major ESPs (Email Service Providers) and ISPs (Internet Service Providers).

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Target Audience List**
   - Format: CSV file of contacts (email, name, demographics)
   - Validation: Verify email format validity, segment by engagement level

2. **Campaign Objectives**
   - Primary KPIs: Deliverability rate, open rate, click-through rate, unsubscribe rate
   - Frequency: Number of emails per week/month
   - Budget: Cost per deliverable metric (if applicable)

3. **Current ESP Configuration**
   - Tools Used: Mailchimp, SendGrid, HubSpot, Klaviyo, etc.
   - Data Sources: ESP dashboards for open rates, spam complaints

4. **Compliance Requirements**
   - GDPR/CCPA: Consent management records
   - CAN-SPAM: Opt-out mechanisms, physical address

5. **Competitive Landscape**
   - List of major competitors and their deliverability strategies
   - Any known blocklists or reputation issues

### Initial Assessment Checklist
- [ ] Validate all required inputs received (checklist)
- [ ] Confirm email list is clean with <1% hard bounces
- [ ] Verify spam complaint rate is <0.05%
- [ ] Ensure compliance headers are correctly implemented
- [ ] Establish baseline metrics for deliverability, open, and engagement

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10 Topics)

**1. Email Authentication Protocols**
   - Research Focus: SPF, DKIM, DMARC implementation best practices
   - Target Sources: ESP documentation, RFC standards
   - Deliverable: Checklist of DNS records to implement and monitor health

**2. Sender Reputation Management**
   - Research Focus: Domain vs IP reputation thresholds, how to improve scores
   - Target Sources: Postmark, SendGrid reputation guides, MXToolbox
   - Deliverable: Action plan for improving domain/IP score from current to >90

**3. Content Quality and Engagement**
   - Research Focus: Optimal subject line length, preheader impact on deliverability
   - Target Sources: MarketingProfs research, Litmus case studies
   - Deliverable: List of A/B test variations for content that drive higher engagement

**4. Mobile Optimization**
   - Research Focus: Responsive design best practices, mobile open rates
   - Target Sources: Litmus reports, Campaign Monitor benchmarks
   - Deliverable: Mobile-first template repository with analytics

**5. Email Segmentation and Personalization**
   - Research Focus: Advanced segmentation strategies using ESP tags
   - Target Sources: Marketing automation platforms documentation
   - Deliverable: Segment mapping diagram for audience lists

**6. List Hygiene Practices**
   - Research Focus: Strategies for hard bounce management, spam complaint handling
   - Target Sources: Email verification tools reviews (Cleaner, Neverbounced)
   - Deliverable: Weekly list maintenance workflow

**7. Spam Trap Management**
   - Research Focus: Identifying and removing traps from lists
   - Target Sources: List cleaning service comparisons (BriteVerify)
   - Deliverable: List of trusted spam trap databases and update frequency

**8. Behavioral Engagement Tracking**
   - Research Focus: Implementing ESP engagement tracking, drip campaigns for re-engagement
   - Target Sources: DoubleClick documentation, ESP webinars on behavioral flows
   - Deliverable: Workflow diagram for re-engage disengaged subscribers

**9. Third-party Delivery Services**
   - Research Focus: Integrating with services like Neverbounced, Zero bounce for real-time list cleansing
   - Target Sources: Vendor comparison articles (Capterra), user reviews on Reddit
   - Deliverable: List of recommended third-party tools and integration steps

**10. Emerging AI Tools in Email Marketing**
   - Research Focus: Predictive deliverability scoring models using ML
   - Target Sources: Blog posts from Sendinblue, Case studies from Mailmodo
   - Deliverable: List of top 5 AI-powered ESP features for deliverability

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document
2. Identify conflicts or contradictions in best practices
3. Prioritize recommendations by impact on deliverability score
4. Create master action plan with implementation timeline

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Email Authentication Setup**
- **Action:** Implement SPF, DKIM, DMARC records for ESP domain(s)
- **Tools Needed:** DNS management tool (e.g., Cloudflare, Route 53), MXToolbox
- **Success Criteria:** Authenticated emails pass all three checks without issues in email clients
- **Common Pitfalls:** Incorrect syntax, misconfigured SPF includes, missing DKIM keys
- **Time Estimate:** 2 hours

**STEP 2: Sender Reputation Optimization**
- **Action:** Run initial reputation check using MXToolbox or SendGrid's health dashboard
- **Tools Needed:** MXToolbox, SendGrid Health Dashboard, Postmark Reputation API
- **Success Criteria:** Domain/IP score >80 within first week of testing
- **Common Pitfalls:** Using shared IPs with poor sender scores, ignoring DKIM/DKIM issues
- **Time Estimate:** 3 hours

**STEP 3: Content Quality Review**
- **Action:** Audit subject lines and preheaders for top 5 campaigns in the last month
- **Tools Needed:** ESP analytics dashboard, A/B testing tool (e.g., Mailchimp Optimize)
- **Success Criteria:** Subject line average open rate >30%, preheader engagement >10%
- **Common Pitfalls:** Overusing exclamation marks, duplicate content, not testing variations
- **Time Estimate:** 4 hours

**STEP 4: Mobile Optimization**
- **Action:** Ensure all templates are responsive and pass Litmus' mobile score test
- **Tools Needed:** Litmus Builder, Email on Acid for cross-platform testing
- **Success Criteria:** 100% of devices pass with no truncation or layout issues
- **Common Pitfalls:** Fixed-width tables, large image files causing slow load times
- **Time Estimate:** 5 hours

**STEP 5: List Segmentation Setup**
- **Action:** Create new segments based on engagement level (engaged, neutral, disengaged)
- **Tools Needed:** ESP segmentation tool, SQL for bulk updates if needed
- **Success Criteria:** At least 50% of list moved into relevant segments with correct targeting logic
- **Common Pitfalls:** Overlapping segment criteria causing subscriber duplication
- **Time Estimate:** 6 hours

**STEP 6: Spam Trap Management**
- **Action:** Run a full list through spam trap database using Neverbounced API
- **Tools Needed:** Neverbounced API, ESP hard bounce handling workflow
- **Success Criteria:** Hard bounce rate <0.2%, no false positives in spam traps
- **Common Pitfalls:** Using outdated spam trap lists causing legitimate delivery issues
- **Time Estimate:** 4 hours

**STEP 7: Behavioral Engagement Workflow**
- **Action:** Implement re-engagement sequence for subscribers with >3 weeks of inactivity
- **Tools Needed:** ESP automation builder, A/B testing tool
- **Success Criteria:** Re-engagement rate >15%, unsubscribe rate <1%
- **Common Pitfalls:** Sending too many emails too quickly, not personalizing messages
- **Time Estimate:** 8 hours

**STEP 8: Third-party Integration**
- **Action:** Integrate Neverbounced API for real-time list cleansing during email sends
- **Tools Needed:** Neverbounced API keys, ESP webhook configuration
- **Success Criteria:** Real-time removal of hard bounces and spam complaints from send queue
- **Common Pitfalls:** Incorrect API keys causing authentication failures
- **Time Estimate:** 6 hours

**STEP 9: AI-Powered Deliverability Enhancements**
- **Action:** Deploy Predictive Inbox Placement model in SendGrid or similar ESP
- **Tools Needed:** ML model output, ESP settings for priority sending
- **Success Criteria:** Top email segments receive >20% higher deliverability to inbox folders
- **Common Pitfalls:** Over-reliance on AI without human oversight
- **Time Estimate:** 4 hours

**STEP 10: Monitoring and Reporting**
- **Action:** Set up daily/weekly monitoring dashboards for all key metrics (bounce, spam complaint, engagement)
- **Tools Needed:** Google Data Studio, ESP native reporting, Zepel task tracking
- **Success Criteria:** Dashboard shows real-time health score >90% of the time
- **Common Pitfalls:** Ignoring early warning signs (increased bounces or complaints)
- **Time Estimate:** Ongoing

### Quality Checkpoints
1. **Checkpoint 1:** After Step 1 - Verify that all authentication records are correctly implemented and pass DNS lookup tests.
2. **Checkpoint 2:** After Step 4 - Confirm mobile score >80% across at least 5 devices.
3. **Checkpoint 3:** After Step 7 - Validate re-engagement sequence logic in ESP automation builder.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Deliverability Rate (goal: 99.5%)
   - Target: 99.5% or higher for all campaigns over a quarter
   - Measurement Method: Compare ESP sent vs delivered metrics, run third-party deliverability tests.

2. **Secondary Metrics:**
   - Open Rate: >30%
   - Click-Through Rate (CTR): >10%
   - Unsubscribe Rate: <1%

3. **Long-term Metrics:**
   - Reputation Score: Consistently above 80
   - Engagement Segmentation Effectiveness: Increase in qualified leads by X% from re-engaged segments

### Iterative Improvement Loop
1. Measure current deliverability rate and engagement metrics against targets.
2. Identify top 3 improvement opportunities:
   - Segment optimization, content A/B testing, list hygiene
3. Implement changes based on findings (e.g., create new segments, update subject lines).
4. Re-measure after 7 days to validate impact.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current deliverability rate: X%
- Goal: Y% by Z date
- Key initiatives: Authentication setup, List cleansing, AI integration

**2. Detailed Report**
- Implementation timeline and milestones
- All research findings with source citations
- Performance metrics pre/post optimization
- Risk assessment and mitigation plan

**3. Maintenance Plan**
- Weekly list verification process using Neverbounced API
- Monthly authentication record review
- Quarterly deliverability health audit using ESP dashboards

**4. Knowledge Transfer**
- Training for team on new workflows (1-hour webinar)
- SOP document with step-by-step guide for each optimization phase
- FAQ section addressing common issues and solutions

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Email Authentication Protocols]"
    focus: "Best practices for SPF, DKIM, DMARC implementation"
    sources: ["ESP docs", "RFC standards"]
    deliverable: "DNS record setup checklist and health test report"

  - agent_id: 2
    topic: "[Sender Reputation Management]"
    focus: "Domain/IP reputation best practices"
    sources: ["MXToolbox", "ESP Health Dashboard"]
    deliverable: "Reputation optimization plan with score targets"

  # [Continue for agents 3-10]
```

### Consolidation Process
1. Collect all agent reports into a single repository.
2. Cross-reference findings for consistency across topics.
3. Resolve any contradictions by prioritizing authoritative sources.
4. Prioritize recommendations based on deliverability impact and implementation effort.

---

## SUCCESS VALIDATION

Before marking this profession task as COMPLETE:

- [ ] **Primary Goal Achieved?** Deliverability rate of 99.5% or higher consistently measured over three months.
- [ ] **All Metrics Met?** Open rate >30%, CTR >10%, Unsubscribe rate <1% across campaigns.
- [ ] **Quality Validated?** All deliverables meet industry standards for email best practices and security.
- [ ] **Documentation Complete?** Executive summary, detailed report, SOPs, training materials all delivered.
- [ ] **Sustainability Ensured?** Maintenance plan in place with assigned owners and review cadence.

### Continuous Improvement
- Document lessons learned from the first cycle.
- Schedule quarterly reviews to adjust strategies based on evolving email ecosystem.
- Share insights gained with team through internal knowledge base.
- Explore new AI tools that can further enhance deliverability metrics.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Email Marketing Specialist (Beginner/Intermediate)  
**Success Rate:** Not yet tracked (first implementation phase)  
**Average Time to Goal:** Not yet tracked (depends on deliverability improvements)

---

This comprehensive template provides a clear path for an Email Marketing Specialist to achieve Deliverability Mastery, complete with actionable steps, tools, and metrics tailored specifically to the profession.

