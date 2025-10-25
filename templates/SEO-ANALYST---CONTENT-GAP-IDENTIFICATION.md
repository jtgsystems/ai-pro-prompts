# SEO Analyst - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "SEO Analyst"
profession_category: "Marketing"
experience_level: "Beginner to Intermediate"
```

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Target Website URL** - Format: URL - Validation: Must be a valid HTTPS website.
2. **Primary Keywords** - Format: List of keywords (max 10) - Validation: Each keyword must include search volume data from Google Keyword Planner.

3. **Content Audit Data** - Format: CSV file or database export - Validation: Contains title, meta description, URL for all pages currently live.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness (e.g., no missing keywords).
- [ ] Identify immediate red flags or blockers (e.g., incomplete content audit data).
- [ ] Establish baseline metrics (current state of rankings, traffic estimates).

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10 Topics)

1. **On-Page SEO Fundamentals**
   - Research Focus: Core elements like title tags, meta descriptions, header tags.
   - Target Sources: Moz Beginner's Guide to On-Page SEO, Google Webmaster Guidelines.
   - Deliverable: Key on-page optimization checklist.

2. **Keyword Research Tools**
   - Research Focus: Latest features and best practices for keyword research tools.
   - Target Sources: SEMrush Tutorial 2024, Ahrefs Keyword Explorer Guide.
   - Deliverable: Comparison table of top keyword research tools.

3. **Content Gap Analysis Techniques**
   - Research Focus: Advanced methods to identify content gaps using SEO audits.
   - Target Sources: Moz Pro Content Grader, Screaming Frog SEO Spider tutorials.
   - Deliverable: Step-by-step guide for gap analysis workflow.

4. **Competitor Analysis Tools**
   - Research Focus: How to use tools like Ahrefs and SEMrush for competitor benchmarking.
   - Target Sources: Ahrefs Competitive Analysis Guide, SEMrush Competitor Keyword Gap Tool Tutorial.
   - Deliverable: Template for competitor keyword comparison.

5. **Technical SEO Best Practices**
   - Research Focus: 2024 updates in technical SEO including schema markup, structured data validation.
   - Target Sources: Schema.org Documentation, Google Search Central Blog.
   - Deliverable: Checklist of critical technical SEO audits.

6. **User Experience (UX) Signals**
   - Research Focus: How UX metrics impact SEO rankings and content relevance.
   - Target Sources: WebAIM WCAG 2.1 Guidelines, Heatmap Tools User Testing Reports.
   - Deliverable: UX scoring system for pages based on accessibility and engagement metrics.

7. **Content Quality Evaluation**
   - Research Focus: Metrics to assess content quality including depth, authority signals, user intent.
   - Target Sources: Yoast SEO Content Analysis Tool, Google's E-A-T Guidelines.
   - Deliverable: Scoring rubric for content quality assessment.

8. **Local SEO Tactics**
   - Research Focus: 2024 local search trends and how to optimize GMB listings, citations.
   - Target Sources: Moz Local Search Guide, BrightLocal Reviewing Software.
   - Deliverable: Checklist for comprehensive local SEO audit.

9. **SEO Analytics Platforms**
   - Research Focus: Latest features in analytics tools like Google Analytics, GA4, SEMrush Insights.
   - Target Sources: GA4 User Guide, SEMrush Trends Reports 2024.
   - Deliverable: Dashboard setup guide with key performance indicators (KPIs).

10. **AI-Driven SEO Tools**
    - Research Focus: How AI can streamline keyword research, content optimization, and gap analysis.
    - Target Sources: Jasper.ai Blog on SEO, Surfer SEO Content Optimization Reports 2024.
    - Deliverable: Comparison matrix of AI-powered SEO tools.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact.
4. Create master action plan focusing on content gap identification.

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Import target website data into SEO analytics platform (Google Analytics, SEMrush).
- **Tools Needed:** Google Analytics, SEMrush, Excel/Google Sheets.
- **Success Criteria:** Data imported accurately within the last 30 days.
- **Common Pitfalls:** Missing recent sessions, incorrect date ranges for traffic data.
- **Time Estimate:** 2 hours

**STEP 2: [Initial Content Audit]**
- **Action:** Run content audit using SEO crawler (Screaming Frog) to identify all indexed pages and their on-page elements.
- **Tools Needed:** Screaming Frog, Google Search Console.
- **Success Criteria:** All core metrics captured including title tags, meta descriptions, keyword density, schema markup.
- **Common Pitfalls:** Incomplete crawl due to JavaScript rendering issues or blocked robots.txt directives.
- **Time Estimate:** 4 hours

**STEP 3: [Keyword Research Deep Dive]**
- **Action:** Use advanced keyword research tools (Ahrefs, SEMrush) to find high-potential long-tail keywords with low competition and high search volume.
- **Tools Needed:** Ahrefs Keyword Explorer, SEMrush Organic Research Tool.
- **Success Criteria:** List of 50 targeted keywords ranked by relevance score and commercial intent.
- **Common Pitfalls:** Overlooking secondary keywords or related terms (missed opportunities).
- **Time Estimate:** 6 hours

**STEP 4: [Competitor Gap Analysis]**
- **Action:** Analyze top 10 competitors using SEMrush to identify content gaps and missing pages for targeted keywords.
- **Tools Needed:** SEMrush Competitive Analysis, Ahrefs Site Audit.
- **Success Criteria:** Comprehensive gap report highlighting URLs with no competitor presence or underoptimized content.
- **Common Pitfalls:** Missing low-competition but high-opportunity subdomains or categories.
- **Time Estimate:** 8 hours

**STEP 5: [Technical SEO Check]**
- **Action:** Run technical health checks using tools like Screaming Frog and Google Search Console to identify crawl errors, duplicate content, site speed issues.
- **Tools Needed:** Screaming Frog, GTmetrix, PageSpeed Insights API.
- **Success Criteria:** No critical or high-risk issues found; overall crawl score >80%.
- **Common Pitfalls:** Ignoring server response times or missing redirects.
- **Time Estimate:** 5 hours

**STEP 6: [Content Gap Identification]**
- **Action:** Cross-reference all findings (keyword, competitor, technical) to pinpoint specific content gaps and opportunities.
- **Tools Needed:** Excel/Google Sheets for comparison matrix, AI writing assistant like Jasper for draft suggestions.
- **Success Criteria:** Documented list of at least 10 actionable content gaps with prioritization based on impact score.
- **Common Pitfalls:** Overlooking seasonal trends or audience intent shifts.
- **Time Estimate:** 6 hours

**STEP 7: [Prioritization and Planning]**
- **Action:** Rank identified gaps by potential ROI (traffic, conversion) and strategic importance to business goals.
- **Tools Needed:** Prioritization matrix template in Excel/Google Sheets.
- **Success Criteria:** Top 5 high-priority content gap items outlined with specific action steps and timelines.
- **Common Pitfalls:** Failing to align priorities with resource availability or team capacity.
- **Time Estimate:** 2 hours

**STEP 8: [Content Strategy Development]**
- **Action:** Create detailed content strategy document outlining new content ideas, keyword targets, publishing schedules, and optimization tactics.
- **Tools Needed:** Content management system (CMS) like WordPress for drafting, SEO plugins (Yoast SEO).
- **Success Criteria:** Strategic plan approved by stakeholders with clear KPIs defined.
- **Common Pitfalls:** Overly ambitious content calendar without resource allocation.
- **Time Estimate:** 4 hours

**STEP 9: [Execution and Publishing]**
- **Action:** Produce new content based on prioritized gaps, optimizing for targeted keywords using AI-powered writing tools (Jasper) and SEO plugins.
- **Tools Needed:** Jasper.ai, SEMrush Content Editor, WordPress backend.
- **Success Criteria:** All new pages live within CMS with proper metadata, schema markup, internal linking structure applied.
- **Common Pitfalls:** Missing final QA steps or failing to update analytics tracking.
- **Time Estimate:** 12 hours

**STEP 10: [Post-Launch Monitoring]**
- **Action:** Set up tracking for new content performance using Google Analytics and Search Console; monitor rankings and traffic trends over time.
- **Tools Needed:** Google Analytics, SEMrush Organic Traffic Tracker.
- **Success Criteria:** Content achieves target ranking positions within 30 days with steady organic traffic growth (minimum 10% week-over-week).
- **Common Pitfalls:** Ignoring negative SEO signals or competitor actions post-launch.
- **Time Estimate:** Ongoing (first review after 2 weeks)

### Quality Checkpoints
1. **Checkpoint 1:** After Step 3 - Verify keyword relevance scores and commercial intent metrics.
2. **Checkpoint 2:** After Step 5 - Confirm no critical crawl errors remain; site speed > 90% on PageSpeed Insights.
3. **Checkpoint 3:** After Step 7 - Ensure content gaps are prioritized correctly by impact score.

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** On-page SEO ranking for top keywords.
   - Target: Top 10 organic rankings within 30 days of launch.
   - Measurement Method: SEMrush or Ahrefs Position Tracking.

2. **Secondary Metrics:**
   - Organic traffic growth (minimum 25% increase in first month).
   - Bounce rate reduction to <50% from current level.
   - Average session duration improvement by >10 seconds.

3. **Long-term Metrics:**
   - Keyword share of voice (competitor keyword rankings).
   - Content engagement metrics (CTR, time on page).

### Iterative Improvement Loop
1. Measure current performance against targets after 30 days.
2. Identify top 3 improvement opportunities from content gaps and analytics data.
3. Implement changes (e.g., refine meta tags, add schema markup).
4. Re-measure results using same metrics.
5. Repeat until all primary goals are achieved.

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state for key SEO KPIs.
- Key actions taken to identify and fill content gaps.
- Results achieved (rankings, traffic).

**2. Detailed Report**
- Complete methodology used including tools and sources.
- All research findings with citations from primary sources.
- Implementation details of new content strategy.
- Before/after comparison charts for rankings and traffic.

**3. Maintenance Plan**
- Ongoing tasks to maintain SEO performance (e.g., monthly audit, quarterly keyword refresh).
- Monitoring schedule in Google Analytics and Search Console.
- Update frequency for competitor analysis and technical audits.

**4. Knowledge Transfer**
- Training materials for new team members on content gap identification process.
- SOPs for ongoing SEO monitoring and reporting.
- Best practices documentation specific to identifying and leveraging content gaps.

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace all [BRACKETED] items** with profession-specific content (e.g., replace "Target Website URL" with the actual client website).
2. **Define 10-20 Critical Topics** based on industry standards, regulatory requirements, and emerging trends.
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria and set clear success metrics.

### Build Step-by-Step Workflow
From industry playbooks, expert practitioner processes, tool vendor best practices, and case studies of successful implementations.

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "On-Page SEO Fundamentals"
    focus: "Latest best practices for on-page optimization."
    sources: ["Moz Beginner's Guide to On-Page SEO", "Google Webmaster Guidelines"]
    deliverable: "Checklist of critical on-page elements"

  - agent_id: 2
    topic: "Keyword Research Tools"
    focus: "Review and comparison of top keyword research tools for 2024."
    sources: ["SEMrush Tutorial 2024", "Ahrefs Keyword Explorer Guide"]
    deliverable: "Comparison table with pricing and feature highlights"

  - agent_id: 3
    topic: "Content Gap Analysis Techniques"
    focus: "Advanced methods to identify content gaps using SEO audits."
    sources: ["Moz Pro Content Grader Tutorial", "Screaming Frog SEO Spider Guide"]
    deliverable: "Step-by-step workflow for gap analysis"

  - agent_id: 4
    topic: "Competitor Analysis Tools"
    focus: "How to use tools like Ahrefs and SEMrush for competitor benchmarking."
    sources: ["Ahrefs Competitive Analysis Guide", "SEMrush Competitor Keyword Gap Tool Tutorial"]
    deliverable: "Template for detailed competitor analysis"

  - agent_id: 5
    topic: "Technical SEO Best Practices"
    focus: "Latest updates in technical SEO including schema markup and structured data."
    sources: ["Schema.org Documentation", "Google Search Central Blog"]
    deliverable: "Technical audit checklist with implementation steps"

  - agent_id: 6
    topic: "User Experience (UX) Signals"
    focus: "How UX metrics impact SEO rankings and content relevance."
    sources: ["WebAIM WCAG 2.1 Guidelines", "Heatmap Tools User Testing Reports"]
    deliverable: "UX scoring system with implementation guide"

  - agent_id: 7
    topic: "Content Quality Evaluation"
    focus: "Metrics to assess content quality including depth, authority signals."
    sources: ["Yoast SEO Content Analysis Tool", "Google's E-A-T Guidelines"]
    deliverable: "Content quality rubric with scoring system"

  - agent_id: 8
    topic: "Local SEO Tactics"
    focus: "2024 local search trends and how to optimize GMB listings, citations."
    sources: ["Moz Local Search Guide", "BrightLocal Reviewing Software"]
    deliverable: "Local SEO checklist including GMB optimization"

  - agent_id: 9
    topic: "SEO Analytics Platforms"
    focus: "Latest features in analytics tools like Google Analytics and SEMrush Insights."
    sources: ["GA4 User Guide", "SEMrush Trends Reports 2024"]
    deliverable: "Dashboard setup guide with key performance indicators"

  - agent_id: 10
    topic: "AI-Driven SEO Tools"
    focus: "How AI can streamline keyword research, content optimization, and gap analysis."
    sources: ["Jasper.ai Blog on SEO", "Surfer SEO Content Optimization Reports 2024"]
    deliverable: "Comparison matrix of AI-powered SEO tools"
```

## SUCCESS VALIDATION

### Final Checklist
Before marking profession task as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [Content gaps identified and prioritized; new content launched meeting target KPIs].
- [ ] **All Metrics Met?** [Rankings, traffic, engagement metrics meet set targets].
- [ ] **Quality Validated?** [New content meets SEO best practices and user intent signals].
- [ ] **Documentation Complete?** [All deliverables documented and shared with stakeholders].
- [ ] **Sustainability Ensured?** [Maintenance plan in place for ongoing monitoring and updates].

### Continuous Improvement
- Document lessons learned from the project.
- Update this template with new insights or tools used.
- Share best practices within the team to improve future processes.
- Schedule quarterly reviews to assess performance against goals.

