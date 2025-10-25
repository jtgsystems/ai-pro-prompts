# Recruiter - AI Agent Template
## Offer Negotiation

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to successfully negotiate job offers in a recruiting role.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Recruiter"
profession_category: "Human Resources"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Successfully negotiate and secure the best possible offer for candidates while meeting employer expectations within a specified timeline.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Candidate profile details (e.g., [LinkedIn URL], skills, experience level)
   - Format: URL/Text
   - Validation: Ensure link is active and contains relevant data.

2. **Input 2:** Job requirements and employer expectations (e.g., required vs. preferred qualifications)
   - Format: Text description
   - Validation: Matches job posting or offer letter.

3. **Input 3:** Candidate's current offers, if any
   - Format: List of offers with details
   - Validation: Includes role, compensation, benefits, and start date.

4. **Input 4:** Company-specific negotiation policies (e.g., salary ranges, benefits packages)
   - Format: Text or policy document link
   - Validation: Accessible and up-to-date.

---

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state of negotiations).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Compensation Benchmarking  
- **Research Focus:** Latest salary ranges for the role, industry standards.  
- **Target Sources:** Glassdoor, Payscale, LinkedIn Salary Insights.  
- **Deliverable:** Recommended compensation range with justification.

**Topic 2:** Benefits Package Analysis  
- **Research Focus:** What benefits are most valued by candidates in your market?  
- **Target Sources:** Offer letter templates, industry surveys.  
- **Deliverable:** List of top desired benefits and their perceived value.

**Topic 3:** Negotiation Tactics & Strategies  
- **Research Focus:** Effective techniques for negotiation (e.g., BATNA analysis).  
- **Target Sources:** Books like "Never Hire Without This," blogs by top recruiters.  
- **Deliverable:** Strategy guide with key tactics.

**Topic 4:** Legal Compliance in Hiring  
- **Research Focus:** Laws affecting compensation, benefits, and workplace conditions.  
- **Target Sources:** EEOC guidelines, state labor laws.  
- **Deliverable:** Checklist of legal requirements met.

**Topic 5:** Candidate Experience Optimization  
- **Research Focus:** Best practices for maintaining candidate experience during negotiations.  
- **Target Sources:** Case studies from top recruiting firms.  
- **Deliverable:** Action plan to improve communication and transparency.

**Topic 6:** Technology Stack in Recruiting  
- **Research Focus:** Latest tools enhancing negotiation (e.g., ATS with offer tracking).  
- **Target Sources:** Vendor websites, user reviews.  
- **Deliverable:** Recommended tech stack list.

**Topic 7:** Industry Trends Impacting Offers  
- **Research Focus:** How current trends affect compensation and benefits.  
- **Target Sources:** News articles, industry reports.  
- **Deliverable:** Trend analysis report.

**Topic 8:** Cultural Fit Assessment Methods  
- **Research Focus:** Techniques for evaluating cultural alignment during offers.  
- **Target Sources:** Interviews, assessments.  
- **Deliverable:** Cultural fit checklist.

**Topic 9:** Alternative Compensation Models  
- **Research Focus:** Non-salary incentives (e.g., stock options, bonuses).  
- **Target Sources:** Offer letters, industry surveys.  
- **Deliverable:** Comparison of alternative compensation models.

**Topic 10:** Negotiation Communication Best Practices  
- **Research Focus:** How to communicate effectively during offers (tone, channels).  
- **Target Sources:** Etiquette guides, communication research.  
- **Deliverable:** Communication style guide.

**Topics 11-20: Advanced Topics**
- [ ] Data-driven negotiation with AI tools.
- [ ] Negotiating for remote work flexibility.
- [ ] Leveraging network effects during offers.
- [ ] Preparing candidates for difficult questions.
- [ ] Using performance metrics to justify offer terms.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified negotiation strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on candidate satisfaction and employer retention.
4. Create a master action plan with timelines.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Initial Draft Offer Creation]**
- **Action:** Compile all gathered data into an initial draft offer letter.  
- **Tools Needed:** Word processor (e.g., LibreOffice, Google Docs), ATS system integration tool (e.g., Zapier).  
- **Success Criteria:** Draft includes compensation, benefits, start date, and other standard terms.  
- **Common Pitfalls:** Missing required fields, incorrect formatting for legal review.  
- **Time Estimate:** 2 hours.

**STEP 2: [Candidate Review & Feedback]**
- **Action:** Share draft with candidate via preferred communication channel (e.g., email).  
- **Tools Needed:** Email client (e.g., Gmail), version control system (e.g., GitHub for tracking changes).  
- **Success Criteria:** Candidate provides written feedback within 24 hours.  
- **Common Pitfalls:** Lack of response, vague feedback.  
- **Time Estimate:** 1 day.

**STEP 3: [Initial Negotiation Cycle]**
- **Action:** Based on candidate feedback, revise offer and send back for final approval.  
- **Tools Needed:** Same as Step 1.  
- **Success Criteria:** Candidate signs off or provides specific counter-offer points.  
- **Common Pitfalls:** Multiple rounds without resolution.  
- **Time Estimate:** 3 days.

**STEP 4: [Legal Review & Compliance Check]**
- **Action:** Send offer to legal/compliance team for review against company policies and state laws.  
- **Tools Needed:** Legal document management system (e.g., DocuSign).  
- **Success Criteria:** No legal red flags, compliance checklist completed.  
- **Common Pitfalls:** Non-compliant terms, missing signatures.  
- **Time Estimate:** 1 week.

**STEP 5: [Finalize Offer & Sign-off]**
- **Action:** Incorporate feedback and finalize offer with candidate signature.  
- **Tools Needed:** E-signature tool (e.g., DocuSign), ATS system for final entry.  
- **Success Criteria:** Signed offer uploaded to ATS, all fields populated.  
- **Common Pitfalls:** Missing signatures or incomplete data.  
- **Time Estimate:** 2 days.

**STEP 6: [Communicate Offer Internally]**
- **Action:** Share finalized offer with hiring manager and internal stakeholders for approval.  
- **Tools Needed:** Internal messaging platform (e.g., Slack), ATS system.  
- **Success Criteria:** Approval from all required parties, documented in ATS.  
- **Common Pitfalls:** Lack of approval leading to delays.  
- **Time Estimate:** 1 day.

**STEP 7: [Candidate Acceptance Notification]**
- **Action:** Notify candidate and internal team of acceptance status.  
- **Tools Needed:** Email client.  
- **Success Criteria:** Candidate informed, all parties updated in ATS.  
- **Common Pitfalls:** Outdated contact information leading to missed notifications.  
- **Time Estimate:** 1 day.

**STEP 8: [Onboarding Preparation]**  
- **Action:** Initiate onboarding process for the new hire.  
- **Tools Needed:** Onboarding software (e.g., BambooHR), communication tools (e.g., Slack).  
- **Success Criteria:** Candidate's welcome email sent, necessary documents prepared.  
- **Common Pitfalls:** Delayed access to systems or missing paperwork.  
- **Time Estimate:** 1 week.

**STEP 9: [Post-Onboarding Feedback Collection]**  
- **Action:** Collect feedback from new hire and manager about the onboarding experience.  
- **Tools Needed:** Survey tool (e.g., Typeform), CRM system for tracking responses.  
- **Success Criteria:** Completed surveys submitted, actionable insights generated.  
- **Common Pitfalls:** Low response rates due to poor incentives or unclear instructions.  
- **Time Estimate:** Ongoing.

---

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify candidate's understanding of terms.
- **Checkpoint 2:** [After Step Y] - Validate legal compliance with company and state laws.
- **Checkpoint 3:** [After Step Z] - Confirm all stakeholders have approved the offer.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Candidate Acceptance Rate  
   - Target: 90%+ acceptance rate within specified timeline.
   - Measurement Method: Track acceptance status in ATS.

2. **Secondary Metrics:**  
   - Average Time to Offer Finalization (TTOF): Aim for ≤10 days.  
   - Legal Review Completion Time: ≤1 week.

3. **Long-term Metrics:**  
   - Employee Retention Rate within 6 months post-onboarding.
   - Candidate Experience Score (surveys).

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top improvement opportunities (e.g., bottlenecks in communication).
3. Implement changes (e.g., additional training for recruiters on offer negotiation).
4. Re-measure results after implementation.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- [ ] Current state vs. target state.
- [ ] Key actions taken during negotiations.
- [ ] Results achieved (e.g., acceptance rate, time to finalize).

**2. Detailed Report**
- [ ] Full methodology used for offer negotiation.
- [ ] All research findings and analysis.
- [ ] Implementation timeline with screenshots of ATS entries.
- [ ] Comparative analysis of final offer vs. initial draft.

**3. Maintenance Plan**
- [ ] Ongoing tasks: Regular review of candidate feedback, compliance updates.
- [ ] Monitoring schedule: Weekly check-ins during negotiation phase.
- [ ] Update frequency: Quarterly for policy reviews.
- [ ] Contingency procedures: Alternative offers if primary offer falls through.

**4. Knowledge Transfer**
- [ ] Training materials for new recruiters on best practices.
- [ ] SOPs documenting the negotiation process.
- [ ] Troubleshooting guide (e.g., handling last-minute candidate objections).
- [ ] Case studies of successful negotiations from previous years.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Compensation Benchmarking]"
    focus: "Latest salary ranges for the role"
    sources: ["Glassdoor", "Payscale"]
    deliverable: "Recommended compensation range with justification"

  - agent_id: 2
    topic: "[Benefits Package Analysis]"
    focus: "Desired benefits by candidates"
    sources: ["Offer letter templates"]
    deliverable: "List of top desired benefits and perceived value"

  # [Continue for agents 3-10]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the task COMPLETE:

- [ ] **Ultimate Goal Achieved?** Offer successfully negotiated, accepted by candidate.
- [ ] **All Metrics Met?** Acceptance rate, TTOF, compliance checks within targets.
- [ ] **Quality Validated?** All terms clear, legally compliant, culturally appropriate.
- [ ] **Documentation Complete?** All reports and documentation prepared.
- [ ] **Sustainability Ensured?** Maintenance plan in place for post-onboarding support.

### Continuous Improvement
- Document lessons learned from the negotiation process.
- Update template with new insights or technologies used.
- Share best practices within the recruiting team.
- Schedule a quarterly review of this process to ensure ongoing effectiveness.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** HR Analytics Platform, ATS systems (e.g., Greenhouse), Offer Management Tools (e.g., BambooHR)  
**Success Rate:** [To be determined post-implementation]  
**Average Time to Goal:** [To be determined post-implementation]

---

*This master template should be copied and customized for each specific profession. The framework remains constant, but the details within each section are profession-specific.*

