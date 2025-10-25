# Recruiter - AI Agent Template
## Candidate Pipeline Building

**Version:** 1.0  
**Purpose:** Guide an AI-powered recruiting assistant through industry best practices to build a robust candidate pipeline.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Recruiter"
profession_category: "Human Resources (HR)"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Build and sustain an active, qualified pool of candidates for open positions within a defined timeframe.

Example:
- **Success Metric:** At least 100 viable candidate applications received per new job opening within the first month.
- **Sustained State:** Maintain at least 70% response rate across all candidate outreach efforts over six months.
- **Quality Assurance:** Achieve an average first-time interview pass rate of 40% for candidates sourced through the pipeline.

---

### PHASE 1: INFORMATION GATHERING

**Required Inputs**
1. **Job Titles / Positions to Fill:** [e.g., Software Engineer, Sales Manager]
2. **Industry Focus Area:** [e.g., Tech, Healthcare, Finance]
3. **Company Culture Preferences:** [e.g., Remote-friendly, Fast-paced, Team-oriented]
4. **Budget Constraints:** [e.g., Salary range, Benefits package]
5. **Timeline for Hiring:** [e.g., 8 weeks to fill position]

**Initial Assessment Checklist**
- [ ] All required inputs have been validated and entered.
- [ ] Job descriptions are finalized and available in the ATS.
- [ ] Company's current open positions list is up-to-date.
- [ ] Candidate sourcing channels (job boards, social media, etc.) are configured.

---

### PHASE 2: RESEARCH & ANALYSIS

**Critical Knowledge Areas (15 Topics)**
1. **Talent Market Trends:** Identify emerging skills and industries in demand for the target roles.
2. **Effective Sourcing Channels:** Evaluate job boards, professional networks (LinkedIn), social media platforms, and niche industry sites.
3. **Applicant Tracking Systems (ATS):** Master configuration of ATS to streamline candidate intake and communication.
4. **Data Analytics Tools:** Use tools like Tableau or Power BI for talent acquisition KPIs.
5. **Candidate Experience Design:** Best practices for a seamless application process.
6. **Screening Techniques:** Structured interviews, skills assessments, and behavioral question frameworks.
7. **Diversity, Equity, and Inclusion (DEI):** Strategies to attract diverse candidates without compromising quality.
8. **Employer Branding Tactics:** Creating compelling employer value propositions on various platforms.
9. **Social Media Recruiting:** Best practices for LinkedIn, Twitter, and other professional networks.
10. **Employee Referral Programs:** Designing effective incentive structures and tracking mechanisms.
11. **Artificial Intelligence in Recruitment:** Using AI tools to automate sourcing, screening, and candidate engagement.
12. **Chatbots for Candidate Interaction:** Implementing automated chats on career pages.
13. **Candidate Relationship Management (CRM):** Tools like Salesforce or HubSpot for tracking interactions.
14. **Legal Compliance:** Understanding EEOC regulations and industry-specific laws.
15. **Performance Metrics:** Defining KPIs for pipeline health.

### Research Consolidation
- Synthesize insights into a unified strategy document.
- Prioritize recommendations based on impact and feasibility.
- Develop an action plan with clear milestones.

---

### PHASE 3: EXECUTION WORKFLOW

**STEP 1: Job Posting & Distribution**
- **Action:** Post jobs across configured channels (ATS, job boards, social media).
- **Tools Needed:** ATS integration, LinkedIn Recruiter Lite, Reddit Ads.
- **Success Criteria:** Minimum of 50 applications per posting within the first week.
- **Common Pitfalls:** Inadequate posting on niche platforms.
- **Time Estimate:** Within 24 hours of posting.

**STEP 2: Candidate Sourcing**
- **Action:** Proactively search for passive candidates via social media, alumni networks, etc.
- **Tools Needed:** LinkedIn Sales Navigator, ZoomInfo, specialized AI sourcing tools (e.g., Textio).
- **Success Criteria:** At least 20 new candidate profiles added to the pipeline per week.
- **Common Pitfalls:** Inconsistent searching across platforms.
- **Time Estimate:** Ongoing weekly effort.

**STEP 3: Outreach & Engagement**
- **Action:** Initiate outreach via personalized emails, LinkedIn messages, or phone calls.
- **Tools Needed:** CRM (HubSpot), email automation software (Mailchimp).
- **Success Criteria:** Open rate >30% and response rate >20% across all channels within two weeks.
- **Common Pitfalls:** Generic messaging leading to low engagement.
- **Time Estimate:** Within 48 hours of sending initial outreach.

**STEP 4: Screening & Assessment**
- **Action:** Conduct structured interviews or skills assessments for qualified candidates.
- **Tools Needed:** Zoom, HackerRank, Pymetrics.
- **Success Criteria:** At least 50% of screened candidates advance to the interview stage within two weeks.
- **Common Pitfalls:** Lack of standardized evaluation criteria.
- **Time Estimate:** Within one week of outreach.

**STEP 5: Candidate Feedback & Retention**
- **Action:** Gather feedback from screened candidates for improvement and re-engagement efforts.
- **Tools Needed:** Survey tools (Google Forms), CRM notes.
- **Success Criteria:** Retention rate >40% over three months.
- **Common Pitfalls:** No follow-up after screenings or assessments.
- **Time Estimate:** Ongoing post-screening.

**STEPS 6-10:**
1. **Candidate Interview Scheduling:** Automate initial interview scheduling using Calendly integration.
2. **Offer Negotiation & Acceptance:** Track offers and negotiate terms efficiently.
3. **Onboarding Preparation:** Coordinate necessary paperwork and resources for new hires.
4. **Post-Onboarding Engagement:** Set up check-in schedules for the first 30 days.

### Quality Checkpoints
- **Checkpoint 1 (After Step 2):** Verify job postings are active across all channels.
- **Checkpoint 2 (After Step 3):** Ensure outreach messages are personalized and compliant with legal standards.
- **Checkpoint 3 (After Step 5):** Confirm candidate feedback is collected and action plans are created.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

**Performance Metrics**
1. **Primary Metric:** Number of candidates in pipeline per position within the first month.
   - Target: Minimum of 100 qualified candidates.
2. **Secondary Metrics:**
   - Average time to fill a position (TTIF).
   - Candidate application-to-interview conversion rate.

**Iterative Improvement Loop**
- Measure current performance against targets.
- Identify top improvement areas (e.g., underperforming channels, low engagement rates).
- Implement changes (e.g., additional ad spend on LinkedIn, revised outreach scripts).
- Re-measure results and adjust strategies as needed.

---

### PHASE 5: REPORTING & DOCUMENTATION

**Deliverables**
1. **Executive Summary:** Overview of pipeline performance against goals.
2. **Detailed Report:** Methodology, research findings, implementation steps, and outcomes.
3. **Maintenance Plan:** Ongoing tasks for maintaining pipeline health (e.g., regular outreach refresh).
4. **Knowledge Transfer:** Training materials on pipeline management for junior recruiters.

---

### RESEARCH SUB-AGENT CONFIGURATION
```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "30 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Talent Market Trends"
    focus: "Emerging skills and industries in demand for the target roles."
    sources: ["LinkedIn Jobs Analytics", "Indeed Salary Reports", "Bureau of Labor Statistics"]
    deliverable: "Report with top emerging trends and skill gaps."

  - agent_id: 2
    topic: "Effective Sourcing Channels"
    focus: "Evaluate job boards, professional networks, social media platforms."
    sources: ["Job Board Rankings", "Professional Network Analytics"]
    deliverable: "Scorecard comparing sourcing platforms by reach and quality."

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact to ultimate goal
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

**Final Checklist**
- [ ] **Goal Achieved?** At least 100 qualified candidates in pipeline within the first month.
- [ ] **Metrics Met:** Average time to fill <8 weeks, response rate >30%, interview conversion >50%.
- [ ] **Quality Validated:** Candidates demonstrate alignment with job requirements through structured assessments.
- [ ] **Documentation Complete:** All deliverables are documented and accessible.

**Continuous Improvement**
- Document lessons learned from each recruitment cycle.
- Update the pipeline strategy based on new data trends or changes in hiring needs.
- Share best practices within the team to enhance collective efficiency.

---

### TEMPLATE METADATA

**Last Updated:** 2024-10-15  
**Version:** 1.0  
**Tested With:** HR Analytics Suite, Applicant Tracking System X  
**Success Rate:** [Track completion and quality metrics]  
**Average Time to Goal:** 6 weeks for a fully operational pipeline per position.

---

*This template is designed to be copied and customized for each specific recruitment need. The framework ensures that an AI Recruiter Agent can systematically build and maintain an effective candidate pipeline.*

