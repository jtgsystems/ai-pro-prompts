# Technical Writer - AI Agent Template
## Content Audit

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve a technical writing content audit.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Technical Writer"
profession_category: "Technology/Engineering"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Conduct a comprehensive Content Audit that identifies all existing documentation for [COMPANY'S PRODUCTS/SERVICES] and assesses each document's relevance, accuracy, clarity, accessibility, compliance with standards (e.g., WCAG 2.1), and SEO optimization.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Input 1:** List of all product/service documentation locations (websites, wikis, repositories)
   - Format: URLs or file paths
   - Validation: All URLs resolve, files exist in listed paths

2. **Input 2:** Target audience for each document
   - Format: Audience categories (e.g., Developers, End-users, Support Teams)
   - Validation: Clear and distinct audience definitions

3. **Input 3:** Scope of audit (e.g., All documents vs. New releases only)
   - Format: Scope statement
   - Validation: No ambiguity in what is included/excluded

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Documentation Standards and Best Practices  
- Research Focus: Industry standards for technical documentation, best practices for clarity, usability, accessibility, and SEO.
- Target Sources: IEEE Software Engineering Standards, WCAG guidelines, SEO blogs.

**Topic 2:** Latest Technical Writing Tools  
- Research Focus: Top tools for writing, editing, version control, collaboration, and content management.
- Target Sources: Reviews on Capterra, G2, vendor documentation.

**Topic 3:** Accessibility Guidelines (WCAG 2.1)  
- Research Focus: How to make technical documents accessible to users with disabilities.
- Target Sources: W3C WCAG guidelines, accessibility testing tools.

**Topic 4:** SEO Optimization for Technical Docs  
- Research Focus: Keyword research, content structuring, metadata optimization techniques specific to tech docs.
- Target Sources: SEO blogs (e.g., Moz, Search Engine Journal), keyword tools like SEMrush.

**Topic 5:** Version Control and Collaboration Platforms  
- Research Focus: Tools that facilitate version control, peer review, and collaborative editing.
- Target Sources: GitHub, GitLab, Confluence documentation platforms.

**Topic 6:** Content Management Systems (CMS)  
- Research Focus: How to integrate technical documents into CMS for improved discoverability and maintenance.
- Target Sources: WordPress plugins, Drupal modules, specialized tech doc platforms like Docusaurus.

**Topic 7:** Localization Best Practices  
- Research Focus: Guidelines for translating technical documentation across languages while maintaining accuracy and usability.
- Target Sources: Localization blogs, standards set by ISO/IEC.

**Topic 8:** Compliance with Industry Standards  
- Research Focus: Ensuring documents comply with regulatory requirements (e.g., FDA, HIPAA) relevant to the products/services.
- Target Sources: Regulatory compliance guides, legal consults.

**Topic 9:** User Experience (UX) Principles in Docs  
- Research Focus: How to structure content for better user experience and readability.
- Target Sources: UX design blogs, Nielsen Norman Group research.

**Topic 10:** Metadata and Structured Data Optimization  
- Research Focus: Best practices for using metadata to improve search engine visibility of technical documents.
- Target Sources: SEO tools documentation, schema.org resources.

**Topic 11:** Technical Writing Education and Resources  
- Research Focus: Latest online courses, webinars, and community forums focused on improving writing skills in technical contexts.
- Target Sources: Coursera, LinkedIn Learning, specialized tech writing forums.

**Topic 12:** Emerging Trends in Technical Documentation  
- Research Focus: New trends such as interactive docs, AI-assisted documentation, augmented reality (AR) for manuals, etc.
- Target Sources: Industry conferences, webinars on emerging tech writing tools and practices.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Discovery & Inventory]**
- **Action:** Catalog all existing documentation locations, formats (e.g., Word docs, Markdown files), versions.
- **Tools Needed:** List of URLs or file paths, a spreadsheet for inventory tracking, Git repositories for version control access.
- **Success Criteria:** All documents are listed with their latest versions and owners.
- **Common Pitfalls:** Missing hidden documentation in shared drives or internal wikis.
- **Time Estimate:** 3 days

**STEP 2: [Technical Audit]**
- **Action:** Review each document's technical accuracy, completeness of sections (e.g., installation, troubleshooting), compliance with standards, and SEO content.
- **Tools Needed:** Version control system (GitHub/GitLab), link analysis tools (Ahrefs), accessibility checker (axe).
- **Success Criteria:** 90%+ documents pass basic quality checks (accuracy, completeness, accessibility).
- **Common Pitfalls:** Overlooking archived or outdated documentation.
- **Time Estimate:** 5 days

**STEP 3: [User Experience Review]**
- **Action:** Assess each document's clarity, organization, and searchability for target audience types.
- **Tools Needed:** User testing tools (Hotjar), heatmaps (Crazy Egg), accessibility checkers.
- **Success Criteria:** All documents are rated with a UX score of 4/5 or higher.
- **Common Pitfalls:** Poorly organized sections, missing TOCs in long docs.
- **Time Estimate:** 3 days

**STEP 4: [SEO Audit]**
- **Action:** Evaluate each document's SEO elements (metadata, headings, keyword usage) and ensure they are properly indexed by search engines.
- **Tools Needed:** Google Search Console, Screaming Frog SEO Spider for crawl errors.
- **Success Criteria:** All documents pass basic SEO checks with no critical crawl errors or missing metadata.
- **Common Pitfalls:** Overuse of keywords (keyword stuffing), broken links.
- **Time Estimate:** 2 days

**STEP 5: [Accessibility Review]**
- **Action:** Use accessibility tools to scan each document for WCAG compliance and identify necessary improvements.
- **Tools Needed:** axe, Lighthouse in Chrome DevTools.
- **Success Criteria:** All documents meet AA level accessibility standards with minor exceptions noted.
- **Common Pitfalls:** Missing alt text for images or tables without headers.
- **Time Estimate:** 2 days

**STEP 6: [Content Gap Analysis]**
- **Action:** Identify any missing documentation needed based on user feedback, product changes, regulatory requirements.
- **Tools Needed:** Survey tools (Typeform), CRM data, regulatory compliance databases.
- **Success Criteria:** A prioritized list of new or updated documents with estimated effort and deadlines.
- **Common Pitfalls:** Ignoring low-priority but critical updates due to resource constraints.
- **Time Estimate:** 2 days

**STEP 7: [Prioritization & Planning]**
- **Action:** Prioritize all issues based on impact, effort, and urgency. Create a roadmap for remediation tasks.
- **Tools Needed:** JIRA or Asana for task management, Gantt chart tool (TeamGantt).
- **Success Criteria:** A detailed action plan with timelines and responsible owners for each issue.
- **Common Pitfalls:** Overloading the team's capacity without considering existing workload.
- **Time Estimate:** 1 day

**STEP 8: [Implementation of Fixes]**
- **Action:** Begin implementing fixes based on prioritized list, update metadata, improve structure, rewrite sections as needed.
- **Tools Needed:** Git for version control during implementation, document authoring tool (e.g., Confluence, Docusaurus).
- **Success Criteria:** All high-priority issues are resolved with updated documents in production.
- **Common Pitfalls:** Failing to push changes to the live environment or documentation platform.
- **Time Estimate:** 5 days

**STEP 9: [Review & Approval Process]**
- **Action:** Conduct a final review of all updated documents, including QA by technical SMEs and end-users if possible.
- **Tools Needed:** Review templates (Google Docs), version control for final approval.
- **Success Criteria:** All finalized documents receive sign-off from stakeholders and are published.
- **Common Pitfalls:** Missing approvals leading to incomplete or unapproved documentation.
- **Time Estimate:** 2 days

**STEP 10: [Publish & Communicate]**
- **Action:** Publish all updated documents in the live environment, notify relevant teams of changes, update internal search indexes.
- **Tools Needed:** Deployment scripts (GitHub Actions), communication tools (Slack, Teams).
- **Success Criteria:** All changes are reflected across documentation platforms and accessible to users.
- **Common Pitfalls:** Failing to update linked references or forgotten to remove draft versions from the repo.
- **Time Estimate:** 1 day

**STEP 11: [Post-Audit Review]**
- **Action:** Conduct a final review after all documents have been published, assess impact on key metrics (e.g., time-to-support tickets).
- **Tools Needed:** Analytics dashboards (Mixpanel), support ticket analysis.
- **Success Criteria:** Demonstrated improvements in user satisfaction scores and reduction in support incidents.
- **Common Pitfalls:** Not tracking the ROI of documentation updates or assuming immediate benefits without measurement.
- **Time Estimate:** 1 day

### Quality Checkpoints
- **Checkpoint 1:** After Step 2 - Verify all documents pass basic accuracy, completeness, and accessibility checks.
- **Checkpoint 2:** After Step 4 - Confirm all SEO elements are present and correctly formatted.
- **Checkpoint 3:** After Step 7 - Ensure prioritization list is approved by leadership.
- **Checkpoint 4:** After Step 10 - Validate successful deployment with no broken links or errors.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** % of Documents Meeting Quality Standards  
   - Target: 95%+ accuracy, completeness, accessibility.
   - Measurement Method: Automated tools and manual QA scores.

2. **Secondary Metrics:**
   - **Metric 1:** Reduction in Support Ticket Volume  
     - Target: Decrease by at least 10% within the first quarter post-audit.
     - Measurement Method: Track support tickets related to documentation usage.

   - **Metric 2:** Increase in Document Usage Analytics  
     - Target: Average page views per user increase by 15%.
     - Measurement Method: Use Google Analytics or built-in analytics tools.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary**
   - Current state vs. target state metrics.
   - Key actions taken and resources invested.

2. **Detailed Audit Report**
   - Methodology used for the audit.
   - Findings categorized by document type (e.g., user guides, API docs).
   - Recommendations for ongoing maintenance.

3. **Maintenance Plan**
   - Ongoing QA processes for new documents.
   - Frequency of full audits (e.g., every 6 months).
   - Training schedule for documentation updates.

4. **Knowledge Transfer & Best Practices Documentation**
   - Updated style guides and templates.
   - Guidelines on using the latest tools effectively.
   - Tips for maintaining high-quality documentation.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Documentation Standards and Best Practices]"
    focus: "Latest industry standards, best practices for technical writing"
    sources: ["IEEE", "WCAG guidelines"]
    deliverable: "Best practice guide with examples"

  - agent_id: 2
    topic: "[Latest Technical Writing Tools]"
    focus: "Reviews and comparisons of new tools in the market"
    sources: ["Capterra", "G2"]
    deliverable: "Tool comparison matrix with pricing models"

  # [Continue for agents 3-12]
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact to the content audit process
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

Before marking this task COMPLETE:

- [ ] **Primary Goal Achieved?** All documents meet industry standards for accuracy, accessibility, and SEO.
- [ ] **Quality Metrics Met?** At least 90% of documents pass all quality checks (accuracy, completeness, accessibility).
- [ ] **Performance Improvements Observed?** Support tickets related to documentation usage reduced by at least 10% within the first quarter post-audit.

---

## TEMPLATE METADATA

**Last Updated:** [2025-04-05]  
**Version:** 1.0  
**Tested With:** Technical Writer roles in software companies, SaaS platforms  
**Success Rate:** Based on industry benchmarks for technical documentation audits (average 85%+ completion rate)  
**Average Time to Goal:** 2 weeks (including discovery and implementation phases)

---

*This template is designed to be customized for each specific content set a Technical Writer is responsible for. The structure remains consistent, but the details will vary based on industry standards, tools used, and company-specific requirements.*

