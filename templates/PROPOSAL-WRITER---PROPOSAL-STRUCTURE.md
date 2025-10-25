# Proposal Writer - AI Agent Template
## Proposal Structure

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a well-structured proposal as a professional Proposal Writer.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Proposal Writer"
profession_category: "Professional Services/Consulting"
experience_level: "[Beginner/Intermediate]"
```

#### Ultimate Goal
**Primary Objective:** Create a professionally structured, compelling, and client-ready proposal that meets the specific needs of the target audience within 2 weeks.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Input 1:** Target Client Profile (industry, company size, decision-makers)
   - Format: [Text description]
   - Validation: Ensure detailed client persona is available.
2. **Input 2:** Proposal Objectives and Key Deliverables
   - Format: List of objectives with measurable outcomes.
   - Validation: Confirm alignment with client needs.
3. **Input 3:** Stakeholder Requirements (specific information, concerns)
   - Format: [Text list]
   - Validation: Ensure all relevant stakeholders are represented.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received and validated.
- [ ] Validate the completeness of client requirements.
- [ ] Identify potential gaps or ambiguities in objectives.
- [ ] Establish baseline metrics (current state of proposal).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (15 Topics)

**Topic 1:** Proposal Framework and Structure
- **Research Focus:** Latest frameworks for effective proposals.
- **Target Sources:** Industry blogs, professional development courses.

**Topic 2:** Formatting Standards
- **Research Focus:** Preferred layouts in client sectors.
- **Target Sources:** Case studies from [Client Type].

**Topic 3:** Legal and Compliance Requirements
- **Research Focus:** Any legal clauses required for the industry.
- **Target Sources:** [Legal Guidelines], [Industry Regulations].

**Topic 4:** Data Visualization Techniques
- **Research Focus:** Best practices for presenting data.
- **Target Sources:** Visual Design blogs, infographics resources.

**Topic 5:** Project Management Methodologies
- **Research Focus:** How to structure project deliverables in proposals.
- **Target Sources:** PMI publications, industry-specific templates.

**Topic 6:** Stakeholder Engagement Strategies
- **Research Focus:** Techniques for engaging different stakeholders.
- **Target Sources:** Stakeholder engagement studies.

**Topic 7:** Competitive Proposal Analysis
- **Research Focus:** Benchmarking against competitors.
- **Target Sources:** [Competitor Proposals], industry reports.

**Topic 8:** Client Communication Styles
- **Research Focus:** Tailoring language to client preferences.
- **Target Sources:** Cultural and communication research.

**Topic 9:** Budget Presentation Techniques
- **Research Focus:** How to present costs effectively.
- **Target Sources:** Financial modeling experts, budgeting courses.

**Topic 10:** Risk Assessment Frameworks
- **Research Focus:** Identifying risks in client projects.
- **Target Sources:** [Risk Management Tools], industry case studies.

**Topic 11:** Proposal Technology Stack
- **Research Focus:** Best tools for proposal creation and collaboration.
- **Primary Tool (free):** Google Docs or ProtonMail  
- **Alternative (paid, optional):** Adobe InDesign

**Topic 12:** Version Control and Collaboration Tools
- **Research Focus:** Platforms to manage multiple stakeholders.
- **Primary Tool (free):** Google Drive or Dropbox  
- **Alternative (paid, optional):** Confluence, Asana.

**Topic 13:** Proposal Templates and Themes
- **Research Focus:** Popular templates that have proven successful.
- **Primary Tool (free):** Canva or LibreOffice Impress  
- **Alternative (paid, optional):** Zoho Show.

**Topic 14:** Data Analysis Tools for Proposals
- **Research Focus:** Software to create compelling data visuals.
- **Primary Tool (free):** Excel or Google Sheets  
- **Alternative (paid, optional):** Tableau Public.

**Topic 15:** Legal Drafting and Review Platforms
- **Research Focus:** Tools for drafting legal clauses securely.
- **Primary Tool (free):** OpenOffice Writer or LibreOffice Calc  
- **Alternative (paid, optional):** Adobe FrameMaker.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Outline Creation]**
- **Action:** Develop a detailed outline based on research.
- **Tools Needed:** Google Docs or ProtonMail
- **Success Criteria:** Comprehensive outline covering all sections.
- **Common Pitfalls:** Skipping critical sections like budget.
- **Time Estimate:** 3 days.

**STEP 2: [Drafting]**
- **Action:** Write each section using the finalized template.
- **Tools Needed:** Google Docs or LibreOffice
- **Success Criteria:** First draft completed with all required elements.
- **Common Pitfalls:** Overlooking formatting requirements.
- **Time Estimate:** 5 days.

**STEP 3: [Stakeholder Review]**
- **Action:** Share the draft with stakeholders for feedback.
- **Tools Needed:** Google Docs comments or ProtonMail
- **Success Criteria:** All critical feedback incorporated.
- **Common Pitfalls:** Ignoring negative feedback.
- **Time Estimate:** 2 days.

**STEP 4: [Legal Review]**
- **Action:** Have the draft reviewed by legal for compliance.
- **Tools Needed:** Google Docs or Adobe InDesign
- **Success Criteria:** All legal issues resolved.
- **Common Pitfalls:** Missing minor clauses.
- **Time Estimate:** 1 day.

**STEP 5: [Final Formatting and Proofreading]**
- **Action:** Apply final formatting, proofread for errors.
- **Tools Needed:** Grammarly or ProWritingAid
- **Success Criteria:** Clean, error-free proposal document.
- **Common Pitfalls:** Skipping thorough review.
- **Time Estimate:** 1 day.

**STEP 6: [Client Presentation Preparation]**
- **Action:** Prepare presentation materials if required.
- **Tools Needed:** PowerPoint or Google Slides
- **Success Criteria:** All presentation components ready and aligned.
- **Common Pitfalls:** Lack of visual aids.
- **Time Estimate:** 2 days.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
1. **Primary Metric:** Proposal Approval Rate
   - Target: [X%] within 7 days of submission.
   - Measurement Method: Track client responses via CRM.

2. **Secondary Metrics:**
   - Review Cycle Time: Aim for < 3 days.
   - Feedback Incorporation Rate: Ensure > 95% feedback addressed.
   - Compliance Check: Zero legal issues flagged during review.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
1. **Executive Summary:** Executive summary of proposal goals and outcomes.
2. **Detailed Proposal Document:** Complete, formatted proposal ready for submission.
3. **Presentation Slides:** Visual aids used in client presentations.
4. **Maintenance Plan:** Ongoing updates to the proposal template based on feedback.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

1. Replace all [BRACKETED] placeholders with specific client details and objectives.
2. Define 15 critical topics relevant to Proposal Writing.
3. Map the ultimate goal to measurable outcomes using SMART criteria.
4. Build a step-by-step workflow from industry best practices and tool capabilities.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "5 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Proposal Framework]"
    focus: "Latest frameworks for effective proposals"
    sources: ["industry blogs", "professional development courses"]
    deliverable: "3-5 actionable insights with sources"

  - agent_id: 2
    topic: "[Formatting Standards]"
    focus: "Preferred layouts in client sectors"
    sources: ["case studies from [Client Type]"]
    deliverable: "Recommended layout guidelines"

  # Continue for agents 3-10...

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact to ultimate goal
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

#### Final Checklist
- [ ] **Primary Objective Met:** Proposal approved or client engaged.
- [ ] **Metrics Achieved:** All defined success metrics met.
- [ ] **Quality Confirmed:** No critical errors found during final review.
- [ ] **Documentation Complete:** All deliverables prepared and shared.
- [ ] **Client Satisfaction:** Client provides positive feedback.

---

### TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Proposal Writing for [Service Industry], Project Management Consulting  
**Success Rate:** [Track completion rate]  
**Average Time to Goal:** [Measure time taken historically]

--- 

This template provides a detailed, actionable roadmap for a beginner to intermediate Proposal Writer aiming to achieve a well-structured proposal. It is tailored specifically to the profession with industry-relevant tools and best practices.

