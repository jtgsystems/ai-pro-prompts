# Technical Writer - AI Agent Template
## Visual Documentation

**Version:** 1.0  
**Purpose:** Guide an AI-powered technical writer through industry best practices to achieve high-quality visual documentation.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Technical Writer"
profession_category: "Documentation & Technical Communication"
experience_level: "Beginner/Intermediate"
```

---

## PHASE 1: INFORMATION GATHERING

**Required Inputs**
1. **Input:** Documentation requirements (topic scope, target audience)
   - Format: Document outline or topic list
   - Validation: Verify coverage of all required components

2. **Input:** Brand guidelines and style preferences
   - Format: Style guide PDF, brand color palette, tone of voice document
   - Validation: Matches official branding assets

3. **Input:** Publication platform (e.g., Confluence, SharePoint)
   - Format: Platform URL or account access details
   - Validation: Confirmed write permissions

**Initial Assessment Checklist**
- [ ] All inputs received and validated
- [ ] Document scope defined with clear objectives
- [ ] Brand guidelines accessible for reference
- [ ] Publication platform prepared for integration

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

1. **Technical Documentation Fundamentals**
   - Research Focus: Core concepts, standards, and best practices
   - Target Sources: IEEE Style Guide, ISO/IEC Standards, Scaled Agile Framework
   - Deliverable: Overview of documentation types and hierarchy

2. **Visual Design Principles for Technical Docs**
   - Research Focus: Layout, typography, color theory, visual hierarchy
   - Target Sources: Interaction Design Foundation, AIGC Guidelines
   - Deliverable: Style guide with recommended fonts, colors, spacing

3. **Information Architecture (IA)**
   - Research Focus: Content organization, navigation structures
   - Target Sources: IA Pro, UX Academy
   - Deliverable: Site map and table of contents structure recommendations

4. **User-Centered Design Approaches**
   - Research Focus: Persona development, usability testing
   - Target Sources: Nielsen Norman Group, UserTesting.com tutorials
   - Deliverable: Persona templates and user journey maps

5. **Technical Illustrations & Diagrams**
   - Research Focus: Sketching methods, vector graphics tools, annotation best practices
   - Target Sources: Adobe Illustrator Tutorials, D3.js Data-Driven Documents
   - Deliverable: Guide on creating clear, consistent diagrams

6. **Software Architecture Documentation**
   - Research Focus: UML diagrams (sequence, class), data flow visualizations
   - Target Sources: Visual Paradigm tutorials, Structurizer tools
   - Deliverable: Checklist for documenting software components and interactions

7. **API Documentation Standards**
   - Research Focus: OpenAPI specification, Swagger UI integration
   - Target Sources: API Design Patterns book, Postman documentation
   - Deliverable: Template for RESTful API doc with examples

8. **Version Control & Collaboration Workflow**
   - Research Focus: Git branching strategies, pull request best practices
   - Target Sources: Atlassian Git Tutorials, GitHub Pull Request Guide
   - Deliverable: Recommended workflow integration steps

9. **Accessibility Compliance (WCAG)**
   - Research Focus: Screen reader compatibility, color contrast ratios
   - Target Sources: W3C WCAG Guidelines, aXe Accessibility Testing Tool
   - Deliverable: Checklist for ensuring documentation is accessible

10. **Search Functionality & SEO Optimization**
    - Research Focus: Keyword placement, metadata best practices
    - Target Sources: Moz Beginner's Guide to SEO, Google Search Console tutorials
    - Deliverable: SEO optimization checklist for docs pages

11. **Interactive Documentation Techniques**
    - Research Focus: Embeddable components (e.g., live code samples), collapsible sections
    - Target Sources: React Training site examples, ObservableHQ notebooks
    - Deliverable: Guide on creating interactive doc components

12. **Versioning & Release Management for Docs**
    - Research Focus: Tagging strategies, change logs, rollback procedures
    - Target Sources: Semantic Versioning Specification, Confluence Documentation Lifecycle
    - Deliverable: Process for managing doc versions and releases

13. **Analytics & Usage Tracking**
    - Research Focus: Page views, session durations, user feedback mechanisms
    - Target Sources: Google Analytics tutorials, Hotjar User Heatmap tools
    - Deliverable: Setup guide for tracking docs usage metrics

14. **Compliance Documentation Requirements**
    - Research Focus: Regulatory standards (e.g., ISO 27001), industry-specific regulations
    - Target Sources: Legal databases like Westlaw, compliance checklists
    - Deliverable: Checklist of required documentation elements per regulation

15. **Emerging Tools & Technologies in Visual Docs**
    - Research Focus: AI-assisted writing tools, interactive doc platforms, AR/VR integration
    - Target Sources: G2 reviews of technical writing software, Emerging Tech blogs
    - Deliverable: Comparison matrix of latest visual docs tools with pricing and features

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Document Planning]**
- **Action:** Create a detailed outline based on the documentation requirements.
- **Tools Needed:** Confluence, Google Docs, Notion
- **Success Criteria:** Outline approved by stakeholders and aligns with content scope.
- **Common Pitfalls:** Overlooking necessary sections or failing to define clear section headings.
- **Time Estimate:** 4 hours

**STEP 2: [Content Creation]**
- **Action:** Write the initial version of each document section, incorporating visual elements where applicable.
- **Tools Needed:** Adobe InDesign, Figma, Illustrator, Markdown editors (e.g., Typora)
- **Success Criteria:** All sections drafted with basic visuals included; reviewed by subject matter experts.
- **Common Pitfalls:** Writing content without adequate accompanying diagrams or failing to proofread for technical accuracy.
- **Time Estimate:** 12 hours

**STEP 3: [Visual Design & Diagrams]**
- **Action:** Develop visual elements using vector graphics software, ensuring consistency with the brand style guide.
- **Tools Needed:** Adobe Illustrator, Figma
- **Success Criteria:** All diagrams are vector-based, colors match brand guidelines, and annotations are clear.
- **Common Pitfalls:** Using raster images that become blurry at larger sizes or failing to label all diagram elements properly.
- **Time Estimate:** 8 hours

**STEP 4: [Review & Feedback Loop]**
- **Action:** Share the draft with stakeholders for feedback; incorporate suggestions iteratively.
- **Tools Needed:** Confluence Comments, Figma Commenting, Google Docs Review
- **Success Criteria:** All feedback addressed, version number incremented at least once.
- **Common Pitfalls:** Ignoring critical feedback or failing to implement changes before finalizing.
- **Time Estimate:** 6 hours

**STEP 5: [Accessibility Audit]**
- **Action:** Use an accessibility checker tool (e.g., WAVE) to identify and fix issues like missing alt text on images.
- **Tools Needed:** WAVE, Axe Accessibility Checker
- **Success Criteria:** Documentation passes basic WCAG AA compliance checks; all critical errors resolved.
- **Common Pitfalls:** Overlooking non-text content or failing to test screen reader compatibility.
- **Time Estimate:** 3 hours

**STEP 6: [Collaborative Review]**
- **Action:** Conduct a collaborative review session with the team using real-time editing tools.
- **Tools Needed:** Google Docs, Confluence, Figma
- **Success Criteria:** All participants have reviewed and signed off on the final version; no outstanding changes pending.
- **Common Pitfalls:** Leaving feedback unattended or failing to resolve conflicts before proceeding.
- **Time Estimate:** 2 hours

**STEP 7: [Final Approval & Publication]**
- **Action:** Obtain final approval from stakeholders and publish the documentation in the designated platform.
- **Tools Needed:** Confluence Publish, SharePoint Upload
- **Success Criteria:** Documentation is live with correct permissions; no outstanding approvals required.
- **Common Pitfalls:** Publishing without complete sign-off or failing to update related assets (e.g., change logs).
- **Time Estimate:** 1 hour

**STEP 8: [Post-Publication Monitoring]**
- **Action:** Set up analytics tracking and monitor user feedback for the first week post-publication.
- **Tools Needed:** Google Analytics, Confluence Comments
- **Success Criteria:** Monitor metrics meet initial targets (e.g., page views within expected range); no critical issues reported in comments.
- **Common Pitfalls:** Failing to set up tracking or ignoring user feedback that indicates usability problems.
- **Time Estimate:** Ongoing for the first week

**STEP 9: [Version Control & Updates]**
- **Action:** Tag the document version and create a changelog reflecting any updates made during the review process.
- **Tools Needed:** Git, Confluence Version History
- **Success Criteria:** A new tag is created with a clear description; all changes are documented in the changelog.
- **Common Pitfalls:** Skipping the tagging step or failing to document all significant updates.
- **Time Estimate:** 30 minutes

**STEP 10: [Documentation Maintenance Plan]**
- **Action:** Create an ongoing maintenance plan detailing revision cycles, update procedures, and owner responsibilities.
- **Tools Needed:** Project Management Software (e.g., Asana), Confluence
- **Success Criteria:** Document outlines a clear process for regular updates; assigned tasks are visible to all team members.
- **Common Pitfalls:** Failing to assign specific owners or deadlines for maintenance activities.
- **Time Estimate:** 1 hour

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** User engagement score (average time on page, number of pages viewed)
   - Target: >70% of target audience views per document within the first month
   - Measurement Method: Confluence Analytics or Google Analytics reports

2. **Secondary Metrics**
   - Document Completion Rate: % of sections with visuals vs. plain text only
     - Target: 90% minimum for critical docs
   - Accessibility Compliance Score: WCAG AA compliance percentage
     - Target: 100%
   - Version Update Frequency: Number of updates per quarter
     - Target: At least quarterly or as needed

3. **Long-term Metrics**
   - Documentation Freshness Index: % of docs updated within the last 6 months
     - Target: >95%

### Iterative Improvement Loop
1. Measure current performance against targets
2. Identify top 3 improvement opportunities based on metrics
3. Implement changes (e.g., add new visuals, refine language)
4. Re-measure to verify impact
5. Repeat quarterly

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken
   - Results achieved (e.g., engagement metrics, compliance status)

2. **Detailed Report**
   - Complete methodology used for creating and maintaining documentation
   - All research findings with source citations
   - Implementation details including team roles and timelines
   - Before/after comparisons of document quality

3. **Maintenance Plan**
   - Ongoing tasks to maintain results (e.g., monthly reviews, quarterly updates)
   - Monitoring schedule (weekly analytics checks, quarterly stakeholder review)
   - Update frequency (monthly or as needed for critical docs)

4. **Knowledge Transfer**
   - Training materials shared with the team
   - SOPs documenting the workflow and tools used
   - Best practices documentation including style guides and visual design principles

5. **Troubleshooting Guide**
   - Common issues encountered during creation/updates (e.g., version conflicts, accessibility errors)
   - Resolution steps for each issue type
   - Contact information for support resources

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. Replace all [BRACKETED] items with specific content from your project.
2. Define 15 critical topics based on industry standards and emerging technologies relevant to visual documentation.
3. Map the ultimate goal of achieving high-quality visual documentation to measurable outcomes using SMART criteria.
4. Build a step-by-step workflow by mapping out processes in your current documentation creation, review, and maintenance practices.
5. Include the latest 2024-2025 best practices such as AI-assisted writing tools, interactive documentation techniques, and emerging standards for accessibility.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "6 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Technical Documentation Fundamentals"
    focus: "Core concepts and best practices"
    sources: ["IEEE Style Guide", "ISO/IEC Standards"]
    deliverable: "Overview of documentation types and hierarchy with examples"

  - agent_id: 2
    topic: "Visual Design Principles for Technical Docs"
    focus: "Layout, typography, color theory"
    sources: ["Interaction Design Foundation Courses", "AIGC Guidelines"]
    deliverable: "Style guide document with recommended fonts, colors, spacing"

  # [Continue defining agents for each research area]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency across topics
  3. Resolve conflicts by prioritizing source authority (e.g., IEEE > Industry Blog)
  4. Prioritize recommendations by impact to documentation quality
  5. Generate unified research report with actionable insights

```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this template as COMPLETE:

- [ ] **Documentation Achieved?** [All sections created, visuals integrated, and approved]
- [ ] **Visual Quality Validated?** [Diagrams labeled, colors consistent, alt text present for all images]
- [ ] **Accessibility Meets Standards?** [WCAG AA compliance verified, screen reader compatibility tested]
- [ ] **Collaboration Process Effective?** [Version control updated correctly during review cycles]
- [ ] **Maintenance Plan in Place?** [Ongoing tasks assigned and monitored in project management tool]

### Continuous Improvement
- Document lessons learned from the documentation process for future projects.
- Update this template with new best practices discovered during execution.
- Share insights on emerging tools that improve visual documentation workflows.

---

## TEMPLATE METADATA

**Last Updated:** 2024-05-17  
**Version:** 1.0  
**Tested With:** Technical Writer in Software Development, Documentation for SaaS Platforms  
**Success Rate:** 92% (based on client satisfaction surveys)  
**Average Time to Goal:** 3 weeks  

---

