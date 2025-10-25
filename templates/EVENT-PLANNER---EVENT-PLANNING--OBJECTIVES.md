# Event Planner - AI Agent Template
## Event Planning & Objectives

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve event planning and objectives with measurable success criteria.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Event Planner"
profession_category: "Hospitality/Events Management"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Successfully plan, execute, and deliver a professional event that meets the specified objectives with measurable success criteria.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information is needed to start:

1. **Input 1:** Event type (wedding, corporate conference, charity gala)  
   - Format: String  
   - Validation: Must be a recognized event category.

2. **Input 2:** Target audience demographics  
   - Format: JSON object with age, location, interests  
   - Validation: Ensure demographic data is realistic and relevant.

3. **Input 3:** Event objectives (e.g., networking opportunities, fundraising goals)  
   - Format: List of strings or bullet points  
   - Validation: Objectives should be SMART criteria aligned to the event type.

4. **Input 4:** Budget constraints  
   - Format: Numeric value with currency symbol  
   - Validation: Must stay within allocated funds.

5. **Input 5:** Date and venue details  
   - Format: Specific date (YYYY-MM-DD) and location name or coordinates  
   - Validation: Confirm availability and suitability for the event type.

6. **Input 6:** Key stakeholders (client, sponsors)  
   - Format: List of names with contact information  
   - Validation: Ensure all parties are informed and aligned.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices.

1. **Event Scheduling & Logistics**  
   - Research Focus: Best practices for timing, venue layout, and vendor coordination.
   - Target Sources: Event planning blogs, case studies, industry forums.
   - Deliverable: 5 key insights on optimal event flow and logistical tips.

2. **Budget Management**  
   - Research Focus: Cost breakdowns, cost-saving strategies, budget tracking tools.
   - Target Sources: Financial management books, spreadsheets software reviews.
   - Deliverable: Budget template with categories and allocation guidelines.

3. **Vendor Selection & Contracting**  
   - Research Focus: Vendor evaluation criteria, contract negotiation tips, payment processing.
   - Target Sources: Vendor comparison sites, legal templates for contracts.
   - Deliverable: Checklist of required vendor information and red flags.

4. **Marketing & Promotion Strategies**  
   - Research Focus: Digital marketing channels, social media campaigns, email outreach tactics.
   - Target Sources: Marketing blogs, analytics tools, past campaign results.
   - Deliverable: Integrated marketing plan with timelines and KPIs.

5. **Registration & Ticketing Management**  
   - Research Focus: Platforms for ticket sales, attendee management systems, payment processing.
   - Target Sources: E-commerce platforms reviews, registration system tutorials.
   - Deliverable: Recommended tools and setup guidelines.

6. **Technology Integration**  
   - Research Focus: Event apps, live streaming solutions, AV equipment rental.
   - Target Sources: Technology blogs, vendor demos, user feedback.
   - Deliverable: Tech stack recommendation with cost comparison.

7. **Risk Management & Contingency Planning**  
   - Research Focus: Potential risks (weather, security), mitigation strategies, insurance options.
   - Target Sources: Risk management literature, industry forums.
   - Deliverable: Comprehensive risk register and contingency plan outline.

8. **Legal Compliance**  
   - Research Focus: Venue permits, liability waivers, ADA compliance, data privacy regulations.
   - Target Sources: Legal databases, government websites, case law summaries.
   - Deliverable: Checklist of legal requirements specific to the event type.

9. **Social Media & Community Engagement**  
   - Research Focus: Hashtag strategies, influencer partnerships, attendee interaction tactics.
   - Target Sources: Social media analytics tools, influencer marketing platforms.
   - Deliverable: Social media calendar and engagement plan.

10. **Post-Event Evaluation & Reporting**  
    - Research Focus: Metrics for success (attendance, satisfaction, ROI), reporting templates.
    - Target Sources: Event evaluation frameworks, feedback collection tools.
    - Deliverable: Final report template with lessons learned and recommendations.

11. **Sustainability Practices**  
    - Research Focus: Eco-friendly event options, waste reduction strategies, carbon footprint measurement.
    - Target Sources: Sustainability blogs, green certification programs.
    - Deliverable: Sustainable event checklist and vendor recommendations.

12. **Health & Safety Protocols**  
    - Research Focus: COVID-19 guidelines, emergency response plans, first aid requirements.
    - Target Sources: CDC guidelines, safety management software reviews.
    - Deliverable: Health and safety compliance plan with protocols.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy document outlining the event's direction.
2. Identify conflicts or contradictions in best practices across different research areas.
3. Prioritize recommendations by impact on achieving the defined objectives.
4. Create master action plans for each phase of the event planning process.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
**STEP 1: [Foundation Setup]**
- **Action:** Conduct initial site visit to assess venue capabilities and constraints.
- **Tools Needed:** Google Earth, Venue capacity calculators, Basic layout software (e.g., PowerPoint).
- **Success Criteria:** Detailed venue assessment report with identified strengths and limitations.
- **Common Pitfalls:** Overlooking accessibility requirements or failing to verify real-time availability.
- **Time Estimate:** 2 days

**STEP 2: [Initial Implementation]**
- **Action:** Develop preliminary event budget using the financial management research insights.
- **Tools Needed:** Excel, Google Sheets (free), Budgeting templates from industry forums.
- **Success Criteria:** Approved draft budget with categories allocated to each expense type.
- **Common Pitfalls:** Omitted costs or inflated estimates for specific vendors.
- **Time Estimate:** 1 week

**STEP 3: [Core Work]**
- **Action:** Select key vendors and negotiate contracts based on vendor selection research.
- **Tools Needed:** Vendor comparison platforms, Contract templates (e.g., LawDepot), Email management tools (Gmail).
- **Success Criteria:** Signed contracts with all essential terms documented and communicated to stakeholders.
- **Common Pitfalls:** Ambiguous contract language or missed deadlines for contract signing.
- **Time Estimate:** 2 weeks

**STEP 4: [Marketing & Registration Setup]**
- **Action:** Design event landing page, set up ticketing system, and create social media content calendar.
- **Tools Needed:** Wix/Ticketize (free tier), Eventbrite (for ticketing), Buffer/Hootsuite (social media scheduling).
- **Success Criteria:** Live website with payment processing enabled, scheduled posts on all platforms for the event week.
- **Common Pitfalls:** Technical issues preventing registration or website downtime.
- **Time Estimate:** 3 weeks

**STEP 5: [Technology & Logistics Coordination]**
- **Action:** Integrate event app, AV equipment rental, and live streaming setup according to technology integration research.
- **Tools Needed:** Hopin/StreamYard (live streaming), Zoom/VirtualEventPro (AV tools), API integrations for ticketing and registration platforms.
- **Success Criteria:** Seamless tech demo with all components functioning as planned in a pre-event rehearsal.
- **Common Pitfalls:** Compatibility issues between software or hardware failures during the event.
- **Time Estimate:** 2 days

**STEP 6: [Risk & Compliance Management]**
- **Action:** Develop risk register, finalize insurance policies, and ensure legal compliance with venue permits.
- **Tools Needed:** Risk management software (e.g., Qualys), Legal consulting platforms (e.g., Avvo), Permit request forms.
- **Success Criteria:** Completed risk register approved by stakeholders, all necessary permits secured.
- **Common Pitfalls:** Underestimating insurance costs or overlooking permit requirements.
- **Time Estimate:** 1 week

**STEP 7: [Marketing Launch & Engagement]**
- **Action:** Execute the marketing campaign across digital platforms and begin attendee engagement activities.
- **Tools Needed:** Email marketing tools (Mailchimp), Social media management platforms, Event-specific chat platforms (e.g., Slack).
- **Success Criteria:** Achieve targeted reach metrics (opens, clicks) and high attendee interaction levels on social media.
- **Common Pitfalls:** Low email open rates or engagement failure due to poor content strategy.
- **Time Estimate:** 2 weeks

**STEP 8: [Final Preparations]**
- **Action:** Conduct a final walkthrough of the venue with all vendors, finalize logistics details, and prepare for event day contingencies.
- **Tools Needed:** Google Maps, Checklists (e.g., Trello), Communication platforms (Slack/Teams).
- **Success Criteria:** All logistical elements are confirmed and documented in a master checklist.
- **Common Pitfalls:** Last-minute changes to vendor availability or venue access issues.
- **Time Estimate:** 1 week

**STEP 9: [Event Execution]**
- **Action:** Implement all marketing strategies, manage registration flow, oversee logistics during the event, and coordinate with vendors for on-site operations.
- **Tools Needed:** Live monitoring software (e.g., Google Analytics), On-site coordination apps (e.g., Slack), Real-time issue resolution tools (e.g., JIRA).
- **Success Criteria:** Event runs smoothly without technical or logistical disruptions; attendee satisfaction is high post-event.
- **Common Pitfalls:** Overwhelmed staff during peak times, miscommunication between vendors and staff.
- **Time Estimate:** Day of event

**STEP 10: [Post-Event Wrap-Up]**
- **Action:** Collect feedback, analyze data, prepare final report, and document lessons learned for future events.
- **Tools Needed:** Survey tools (Google Forms), Data analysis software (Excel), Documentation platforms (Notion).
- **Success Criteria:** Comprehensive post-event report with actionable insights delivered within 2 weeks of the event.
- **Common Pitfalls:** Delayed feedback collection or incomplete data analysis.
- **Time Estimate:** 2 weeks

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify all venue logistics are documented and accessible to all stakeholders.
- **Checkpoint 2:** [After Step Y] - Validate that the marketing campaign is live on all channels and scheduled correctly.
- **Checkpoint 3:** [After Step Z] - Confirm budget allocations have been approved by key stakeholders.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Event attendance vs. target number of attendees  
   - Target: Achieve or exceed the projected number based on marketing reach.
   - Measurement Method: Final event registration data and post-event surveys.

2. **Secondary Metrics:**  
   - Budget adherence (variance from approved budget)  
     - Target: Stay within +/- 5% variance.
     - Measurement Method: Detailed expense tracking throughout execution phases.

   - Attendee satisfaction score (via surveys)  
     - Target: Achieve an average rating of 4.5/5 or higher.
     - Measurement Method: Sentiment analysis from survey responses.

3. **Long-term Metrics:**  
   - ROI on marketing spend  
     - Target: At least a 2:1 return on the total marketing budget.
     - Measurement Method: Compare revenue generated to marketing costs.

   - Repeat attendee rate for future events  
     - Target: Increase repeat attendance by 10% compared to previous year.
     - Measurement Method: Track registered attendees across multiple events.

### Iterative Improvement Loop
1. Measure current performance against targets using collected data and feedback.
2. Identify top 3 improvement opportunities (e.g., marketing inefficiencies, vendor delays).
3. Implement changes based on identified issues (e.g., adjust budget allocation, enhance communication tools).
4. Re-measure to ensure improvements have the desired impact.
5. Repeat until all metrics meet or exceed targets.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state  
- Key actions taken  
- Results achieved (attendance, budget adherence, satisfaction scores)  

**2. Detailed Report**
- Complete methodology used for planning and execution  
- All research findings compiled in one document  
- Implementation details with timelines and responsibilities  
- Before/after comparisons of key metrics  

**3. Maintenance Plan**
- Ongoing tasks to maintain results post-event (e.g., updating contact lists, reviewing feedback)  
- Monitoring schedule (weekly/monthly reports)  
- Update frequency for documentation (quarterly)  
- Contingency procedures in case of unforeseen issues

**4. Knowledge Transfer**
- Training materials for staff on best practices learned during the event  
- Standard operating procedures documented for future use  
- Best practices shared with team members and stakeholders  

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Event Scheduling & Logistics]"
    focus: "Latest best practices for timing, venue layout, and vendor coordination."
    sources: ["Event planning blogs", "Industry case studies"]
    deliverable: "5 key insights on optimal event flow with examples."

  - agent_id: 2
    topic: "[Budget Management]"
    focus: "Cost breakdowns, cost-saving strategies, budget tracking tools."
    sources: ["Financial management books", "Spreadsheet software reviews"]
    deliverable: "Budget template with categories and allocation guidelines."

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to event planning objectives
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the profession task as COMPLETE:

- [ ] **Event Planning Success:** Event executed successfully meeting all primary and secondary metrics.
- [ ] **Objective Achievement:** All set goals (attendance, budget adherence, satisfaction) met or exceeded.
- [ ] **Quality Assurance:** Work completed with high quality standards and documented thoroughly.
- [ ] **Sustainability & Compliance:** Meets sustainability practices and legal requirements without penalties.
- [ ] **Stakeholder Satisfaction:** Client and stakeholders are fully satisfied with the event outcome.

### Continuous Improvement
- Document lessons learned from the event.
- Update the research and execution template with new best practices.
- Share insights gained with the broader community through blogs or webinars.
- Schedule regular reviews to ensure future events build on this success model.

