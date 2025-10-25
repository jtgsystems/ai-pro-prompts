# Customer Success Manager - AI Agent Template

## Customer Feedback Program

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to establish a robust Customer Feedback Program for Customer Success Managers.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Customer Success Manager"
profession_category: "Customer Experience Management"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Establish and maintain an effective Customer Feedback Program that consistently gathers, analyzes, and acts on customer feedback within 30 days of collection, achieving a minimum 90% response rate from target customers.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Customer demographics and usage patterns (e.g., [email list, customer profiles]).
   - Format: JSON/CSV files with customer data.
   - Validation: Ensure at least 90% of customers have valid contact information.

2. **Input 2:** Current feedback collection channels (e.g., [surveys, social media, support tickets]).
   - Format: List of URLs or ticket IDs.
   - Validation: Verify all links are active and accessible.

3. **Input 3:** Key performance indicators for customer success (e.g., [CSAT scores, NPS, churn rate]).
   - Format: Dashboard metrics.
   - Validation: Ensure data is from the last 90 days.

### Initial Assessment Checklist
- [ ] Verify all required inputs received and validated.
- [ ] Validate input quality by checking for completeness and accuracy.
- [ ] Identify immediate red flags or blockers in feedback collection.
- [ ] Establish baseline metrics (current CSAT/NPS, churn rate).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Customer Journey Mapping
- Research Focus: Understand customer touchpoints and pain points.
- Target Sources: Customer feedback data, support tickets, user interviews.

**Topic 2:** Feedback Collection Best Practices
- Research Focus: Optimal methods for gathering structured feedback.
- Target Sources: Industry blogs (e.g., Gartner), case studies from Fortune 500 companies.

**Topic 3:** Sentiment Analysis Tools
- Research Focus: Identify tools that can automatically analyze sentiment in customer feedback.
- Target Sources: Reviews of AI-powered analytics platforms like MonkeyLearn or IBM Watson.

**Topic 4:** Data Integration and Centralization
- Research Focus: Best practices for integrating feedback data from various sources into a single platform.
- Target Sources: Documentation on tools like Zapier, Make.com, or custom ETL pipelines using Python (Pandas).

**Topic 5:** Real-Time Feedback Systems
- Research Focus: Technologies enabling immediate feedback collection and response.
- Target Sources: Forums discussing real-time analytics platforms.

**Topic 6:** Customer Segmentation Techniques
- Research Focus: Methods to segment customers based on feedback data for targeted actions.
- Target Sources: Data science literature, customer success blogs.

**Topic 7:** AI-Powered Insights for Feedback Analysis
- Research Focus: How AI can be used to predict churn or identify emerging issues from feedback.
- Target Sources: Whitepapers on AI applications in CXM.

**Topic 8:** Legal and Ethical Considerations for Data Collection
- Research Focus: Compliance with GDPR, CCPA, etc., when handling customer data.
- Target Sources: Legal databases like Westlaw, regulatory updates.

**Topic 9:** Feedback Loop Implementation
- Research Focus: Steps to create an effective feedback loop from collection to action.
- Target Sources: Industry frameworks and best practice articles.

**Topic 10:** Automation of Feedback Processes
- Research Focus: Tools that automate repetitive feedback tasks (e.g., routing tickets, sending follow-ups).
- Target Sources: Reviews of automation platforms like Workato or custom scripts using Node.js/Python.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy document.
2. Identify common themes and actionable insights across topics.
3. Prioritize recommendations based on feasibility and impact.
4. Create an action plan outlining the next steps for implementation.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Setup Feedback Collection Infrastructure]**
- **Action:** Integrate feedback collection tools (surveys, social listening) into a central database.
- **Tools Needed:** Zapier, Make.com for integration; Python scripts for ETL processes.
- **Success Criteria:** All feedback data is stored in the central database within 24 hours of collection.
- **Common Pitfalls:** Misconfigured integrations leading to data loss.
- **Time Estimate:** 5 days

**STEP 2: [Analyze Initial Feedback Data]**
- **Action:** Run sentiment analysis and categorize feedback based on themes (e.g., product, pricing, support).
- **Tools Needed:** MonkeyLearn for sentiment analysis; Python libraries like NLTK or spaCy.
- **Success Criteria:** Comprehensive report identifying top issues with customer satisfaction scores mapped to specific segments.
- **Common Pitfalls:** Lack of clear tagging leading to mixed results in analysis.
- **Time Estimate:** 3 days

**STEP 3: [Prioritize and Segment Customers]**
- **Action:** Use the analyzed data to segment customers based on feedback severity, frequency, and satisfaction scores.
- **Tools Needed:** Customer data platform (CDP) like Segment or custom Python scripts for segmentation logic.
- **Success Criteria:** Segmented customer list with clear priority levels indicating which segments need immediate attention.
- **Common Pitfalls:** Overlapping segments leading to confusion in targeting efforts.
- **Time Estimate:** 2 days

**STEP 4: [Develop Follow-Up Action Plans]**
- **Action:** Create tailored action plans for each customer segment based on their feedback.
- **Tools Needed:** Project management software (e.g., Asana, Trello) for tracking actions; CRM integration for personalized communication.
- **Success Criteria:** Action items assigned with clear owners and deadlines.
- **Common Pitfalls:** Missed deadlines due to lack of follow-through mechanisms.
- **Time Estimate:** 3 days

**STEP 5: [Implement Feedback Loop]**
- **Action:** Set up automated notifications or reminders for teams when action plans are overdue.
- **Tools Needed:** Workflow automation tools like Zapier, custom Slack bots using Python.
- **Success Criteria:** Notifications trigger on time without manual intervention.
- **Common Pitfalls:** Incorrect time settings leading to missed alerts.
- **Time Estimate:** 1 day

**STEP 6: [Regular Review and Reporting]**
- **Action:** Schedule weekly reviews of feedback trends, action plan progress, and customer satisfaction scores.
- **Tools Needed:** Dashboards in Looker Studio or Power BI for visual reporting; Email templates for updates to stakeholders.
- **Success Criteria:** Weekly reports are generated automatically and reviewed by leadership within 2 days of the review date.
- **Common Pitfalls:** Reports not delivered due to broken automation links.
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After Step 1 - Verify data integrity and completeness in the central database.
- **Checkpoint 2:** After Step 2 - Validate sentiment analysis results by a peer with no access to raw data.
- **Checkpoint 3:** After Step 4 - Confirm action plans are realistic and have clear ownership assigned.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Customer Satisfaction Score (CSAT) improvement of at least 15% within the first quarter.
   - Target: +15% in CSAT score from baseline.
   - Measurement Method: Quarterly surveys using Typeform or SurveyMonkey.

2. **Secondary Metrics:**
   - Feedback Collection Rate: Maintain >90% response rate.
     - Measurement Method: Track submission rates of feedback forms.
   - Resolution Time for Follow-Up Issues: <48 hours.
     - Measurement Method: Monitor ticket resolution times in the CRM system.

3. **Long-term Metrics:**
   - Churn Reduction: Achieve a 10% reduction in customer churn rate over two years.
     - Measurement Method: Track churn metrics monthly.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., low response rates, high churn).
3. Implement changes (e.g., more personalized follow-ups, additional support resources).
4. Re-measure after implementation period.
5. Repeat until all metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current CSAT score vs. target.
- Feedback collection rate and trends.
- Top issues identified from customer feedback.
- Action plan status overview.

**2. Detailed Report**
- Methodology used for data collection and analysis.
- All research findings organized by topic area.
- Implementation details of the feedback program.
- Pre/post implementation performance metrics.

**3. Maintenance Plan**
- Ongoing tasks (e.g., quarterly CSAT surveys, monthly review meetings).
- Monitoring schedule (how often dashboards are updated).
- Update frequency for tools and processes.
- Contingency procedures in case of data loss or system downtime.

**4. Knowledge Transfer**
- Training sessions for the team on using new feedback tools.
- SOPs detailing how to handle different types of feedback.
- Best practices documentation covering all steps taken during implementation.
- Troubleshooting guide addressing common issues (e.g., integration errors, low response rates).

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "5 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Customer Journey Mapping"
    focus: "Identify key touchpoints and pain points."
    sources: ["customer surveys", "support tickets", "interview transcripts"]
    deliverable: "Journey map with identified issues"

  - agent_id: 2
    topic: "Feedback Collection Best Practices"
    focus: "Research optimal methods for structured feedback collection."
    sources: ["industry blogs", "case studies", "whitepapers"]
    deliverable: "Best practices document with examples"

  # [Continue defining agents 3-10 based on topics above]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to CSAT improvement
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking this template as COMPLETE:

- [ ] **Ultimate Goal Achieved?** A measurable improvement in CSAT and sustained feedback rate.
- [ ] **All Metrics Met?** All defined KPIs are met within the agreed timeframe.
- [ ] **Quality Validated?** Feedback is accurately analyzed with high sentiment accuracy.
- [ ] **Documentation Complete?** All deliverables, including reports and SOPs, are stored in the shared drive.
- [ ] **Sustainability Ensured?** Ongoing processes documented for future teams to maintain.

### Continuous Improvement
- Document lessons learned from each phase.
- Update the template with new best practices or tools.
- Share insights gained through customer feedback programs.
- Schedule quarterly reviews to ensure continued alignment with business goals.

