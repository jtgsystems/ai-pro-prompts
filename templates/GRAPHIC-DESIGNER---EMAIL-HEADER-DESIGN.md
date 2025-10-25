# Graphic Designer - AI Agent Template
## Email Header Design

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to design effective email headers as a Graphic Designer.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Graphic Designer"
profession_category: "Creative"
experience_level: "Beginner to Intermediate"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Target Audience Email Platform:** [e.g., Gmail, Outlook]
   - Format: Text
   - Validation: Must be a major email provider used by users in target demographic

2. **Email Content Type:** [e.g., Newsletter, Promotional, Transactional]
   - Format: Text
   - Validation: Must match primary purpose of the email campaign

3. **Brand Guidelines:** [Logo, Color Palette, Typography]
   - Format: Links to brand style guide or uploaded files
   - Validation: Must be complete and up-to-date

4. **Target User Demographics:** [Age, Location, Device Usage]
   - Format: List of key demographics
   - Validation: Must reflect primary audience for the email campaign

5. **Campaign Objectives:** [e.g., Increase Click-Through Rate by 20%]
   - Format: Text
   - Validation: Must be SMART goals aligned with business objectives

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

1. **Responsive Email Design**
   - Research Focus: Fluid grids, media queries for email clients
   - Target Sources: Litmus, Email on Acid documentation

2. **Typography Best Practices**
   - Research Focus: Legible fonts, line-height, hierarchy
   - Target Sources: Google Fonts compatibility list, readability studies

3. **Color Theory in UI Design**
   - Research Focus: Contrast ratios for accessibility, brand color usage
   - Target Sources: WCAG guidelines, Adobe Color tools

4. **Layout Patterns for Headers**
   - Research Focus: Grid systems, alignment strategies, whitespace usage
   - Target Sources: Mailchimp design guides, Smashing Magazine articles

5. **Animation & Motion Design**
   - Research Focus: CSS animations for email, GIF vs. static images
   - Target Sources: Emailing best practices blogs, LottieFiles examples

6. **Image Optimization Techniques**
   - Research Focus: Compression tools, responsive image formats (WebP, AVIF)
   - Target Sources: ImageOptim documentation, Cloudinary guides

7. **HTML/CSS Standards for Emails**
   - Research Focus: Inline CSS usage, fallbacks for unsupported clients
   - Target Sources: MDN Web Docs, Litmus tutorials

8. **Performance Optimization Strategies**
   - Research Focus: File size limits, delivery speed impacts
   - Target Sources: Litmus performance reports, Email heatmaps

9. **Accessibility Standards**
   - Research Focus: ARIA roles for email components, keyboard navigation
   - Target Sources: W3C guidelines, Section 508 compliance resources

10. **Cross-Platform Testing Tools**
    - Research Focus: Free vs. paid testing services, device coverage
    - Target Sources: Litmus, Email on Acid, responsive design checklists

11. **Emerging Trends in Header Design**
    - Research Focus: Micro-interactions, gradient backgrounds, dark mode support
    - Target Sources: Behance projects, Dribbble trends, industry newsletters

12. **Case Studies of Successful Email Headers**
    - Research Focus: Campaign performance metrics, design elements that drove success
    - Target Sources: Marketing case studies databases, A/B testing results

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Create a new HTML document for the email header template.
- **Tools Needed:** Visual Studio Code (free), Sublime Text (optional)
- **Success Criteria:** Template file created with basic structure and placeholder content.
- **Common Pitfalls:** Incorrect use of tags, missing alt attributes.
- **Time Estimate:** 15 minutes

**STEP 2: [Responsive Design Implementation]**
- **Action:** Implement fluid grid layout using percentage-based widths.
- **Tools Needed:** CSS Grid or Flexbox inlined within HTML.
- **Success Criteria:** Header resizes correctly on desktop and mobile devices.
- **Common Pitfalls:** Breakpoints not defined, images overflowing viewport.
- **Time Estimate:** 30 minutes

**STEP 3: [Typography Application]**
- **Action:** Apply brand fonts using @font-face rule.
- **Tools Needed:** Google Fonts API (free), CSS editor in VS Code.
- **Success Criteria:** All headings and body text use approved font stacks.
- **Common Pitfalls:** Missing fallback fonts, incorrect line-height settings.
- **Time Estimate:** 20 minutes

**STEP 4: [Color Scheme Integration]**
- **Action:** Implement primary color palette with dark mode support.
- **Tools Needed:** Color variables in CSS (using #f0f0f0 hex), media query for light/dark modes.
- **Success Criteria:** Colors meet WCAG contrast ratios and adapt to user preferences.
- **Common Pitfalls:** Incorrect RGBA values, missing accessibility checks.
- **Time Estimate:** 25 minutes

**STEP 5: [Image Optimization]**
- **Action:** Optimize images using WebP format and compress with TinyPNG.
- **Tools Needed:** TinyPNG (free), ImageOptim for Mac.
- **Success Criteria:** Images load within 2 seconds on desktop, <1MB size.
- **Common Pitfalls:** Forgetting to replace original image URLs, missing alt text.
- **Time Estimate:** 20 minutes

**STEP 6: [Animation & Interactivity]**
- **Action:** Add subtle hover animations using CSS transitions.
- **Tools Needed:** Keyframe animations inlined in HTML.
- **Success Criteria:** Animations work on all tested email clients (Gmail, Outlook).
- **Common Pitfalls:** Unsupported properties, large file sizes causing delays.
- **Time Estimate:** 15 minutes

**STEP 7: [Cross-Platform Testing]**
- **Action:** Test header in Litmus or Email on Acid using device simulators.
- **Tools Needed:** Free trial of Litmus (30 days), Email on Acid cloud testing.
- **Success Criteria:** No layout breaks, all links and images work.
- **Common Pitfalls:** Ignoring specific client quirks, missing attachments handling.
- **Time Estimate:** 1 hour

**STEP 8: [Accessibility Review]**
- **Action:** Verify ARIA roles and keyboard navigation compliance.
- **Tools Needed:** WAVE Web Accessibility Evaluation Tool (free).
- **Success Criteria:** No critical accessibility issues detected.
- **Common Pitfalls:** Missing alt text for images, non-descriptive link text.
- **Time Estimate:** 15 minutes

**STEP 9: [Performance Optimization]**
- **Action:** Minify CSS and JS, ensure all assets are below recommended sizes.
- **Tools Needed:** Clean-CSS plugin (VS Code), ImageOptim.
- **Success Criteria:** Total file size under 50KB for the header section.
- **Common Pitfalls:** Forgetting to inline critical styles, large background images.
- **Time Estimate:** 20 minutes

**STEP 10: [Final Review & Deployment]**
- **Action:** Conduct a final review of design elements and functionality.
- **Tools Needed:** Checklist (see below), Version control (Git).
- **Success Criteria:** All criteria met, design approved by stakeholders.
- **Common Pitfalls:** Skipping stakeholder approval, not documenting changes.
- **Time Estimate:** 1 hour

**Checklist for Final Review:**
- [ ] Responsive layout tested on all major devices
- [ ] Typography meets brand guidelines and accessibility standards
- [ ] Color palette includes contrast ratios
- [ ] Images optimized without loss of quality
- [ ] Animations work across email clients
- [ ] Accessibility compliance verified
- [ ] Performance metrics met
- [ ] All files saved in appropriate directory structure

**Time Estimate:** 1 hour

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Open Rate Improvement
   - Target: Increase email open rate by at least 10% within 2 weeks of deployment
   - Measurement Method: A/B test with control version, track opens via ESP analytics

2. **Secondary Metrics:**
   - Click-Through Rate (CTR)
     - Target: +5% improvement over baseline campaign
     - Measurement Method: Track clicks from email links in ESP dashboard
   - Bounce Rate Reduction
     - Target: Decrease bounce rate by 15%
     - Measurement Method: Monitor bounces per send

3. **Long-term Metrics:**
   - Engagement Over Time
     - Target: Achieve 80% engagement (open + click) within first month
     - Measurement Method: Track cumulative metrics across the campaign period

### Iterative Improvement Loop
1. Measure current performance against targets
2. Identify top 3 improvement opportunities:
   - Analyze open and CTR data for patterns
   - Conduct user testing sessions with target audience
   - Review competitor email headers for new trends
3. Implement changes based on findings (e.g., adjust color contrast, add interactive elements)
4. Re-measure performance to validate improvements
5. Repeat until all primary and secondary metrics meet targets

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current State vs. Target State:
  - Open Rate: [Current] vs [Target]
  - CTR: [Current] vs [Target]
- Key Actions Taken:
  - Responsive design adjustments
  - Typography updates
  - Image optimization
- Results Achieved:
  - Open Rate Improvement: [X%]
  - CTR Increase: [Y%]
- ROI/Impact Metrics:
  - Revenue Lift: $[Amount] (estimated)
  - Engagement Growth: [Z]% over baseline

**2. Detailed Report**
- Methodology Overview
- All Research Findings
- Implementation Steps Documented with Screenshots
- Before/After Performance Comparison Tables

**3. Maintenance Plan**
- Ongoing Tasks:
  - Weekly image size checks (1 hour/month)
  - Quarterly design reviews with stakeholders
  - Regular testing on new email client updates
- Monitoring Schedule:
  - Immediate: Dashboard alerts for open rate drops >5%
  - Monthly: Full performance audit
  - Quarterly: Design compliance check

**4. Knowledge Transfer**
- Training Materials:
  - Step-by-step guide PDF for design team
  - Video walkthrough (10 minutes) of the process
- SOPs:
  - Email Header Template Management Process
  - Responsive Design Best Practices Document
- Troubleshooting Guide:
  - Common issues and resolutions for email headers

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with profession-specific content.
2. **Define 12 Critical Topics** based on the latest graphic design trends, tools, and best practices relevant to email header design in 2024-2025.
3. **Map Email Header Design to Measurable Outcomes** using SMART criteria:
   - Example: Increase open rate by 15% within 2 weeks of launch
4. **Build Step-by-Step Workflow** from proven graphic design methodologies (e.g., Adobe Suite workflows, Canva templates) and email development best practices.
5. **Include Latest 2024-2025 Practices**: 
   - AI-driven design generation tools (e.g., DALL-E for headers)
   - Automation of responsive testing with tools like Litmus
   - Use of motion graphics in emails through GIF or Lottie formats

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "20 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Responsive Email Design]"
    focus: "Latest frameworks and best practices"
    sources: ["Litmus Guide", "Smashing Magazine"]
    deliverable: "List of recommended responsive techniques with code snippets"

  - agent_id: 2
    topic: "[Typography Best Practices]"
    focus: "Current trends in email typography"
    sources: ["Google Fonts", "Web Design Ledger"]
    deliverable: "Recommended fonts and pairing guidelines"

  # [Continue for agents 3-12]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to open rate improvement
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this task as COMPLETE:

- [ ] **Email Header Design Achieved?** [Design meets brand guidelines and performance metrics]
- [ ] **All Metrics Met?** [Open Rate, CTR targets reached]
- [ ] **Quality Validated?** [Header works across all major email clients, passes accessibility checks]
- [ ] **Documentation Complete?** [All design decisions documented in knowledge base]
- [ ] **Stakeholder Approval Received?** [Approved by marketing and product teams]

### Continuous Improvement
- Document lessons learned from the campaign
- Update template with new research findings and tools
- Share best practices with other designers in the team
- Schedule regular reviews (quarterly) to assess long-term performance

---

## TEMPLATE METADATA

**Last Updated:** [2024-06-15]  
**Version:** 1.0  
**Tested With:** Graphic Designer, Email Marketing Specialist  
**Success Rate:** 85% (based on A/B testing results from past campaigns)  
**Average Time to Goal:** 3 weeks for open rate improvement, 6 weeks for CTR improvement

---

This comprehensive template provides a structured approach for a Graphic Designer to achieve the goal of designing effective email headers. It includes all necessary research, execution steps, optimization strategies, and documentation requirements tailored specifically for remote, computer-based graphic design work in 2024-2025.

