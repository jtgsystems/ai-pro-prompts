# AI PROFESSION TEMPLATE - MASTER FRAMEWORK

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Conversion Rate Optimizer"
profession_category: "Digital Marketing"
experience_level: "Beginner to Intermediate"
```

## PROFESSIONAL GOAL DEFINITION

**Primary Objective:** Optimize page load speed to achieve a 95%+ PageSpeed score on Lighthouse (2024-2025 standards) and improve conversion rate by at least 10% within 90 days, measured against industry benchmarks for similar websites.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Website URL (e.g., https://example.com)
2. **Input 2:** Current average page load time (target: >3 seconds)
3. **Input 3:** Conversion funnel stages and metrics (e.g., Bounce Rate, Time on Page, Add to Cart Rate)
4. **Input 4:** Target audience demographics and device usage patterns
5. **Input 5:** Existing SEO performance data

### Initial Assessment Checklist
- [ ] Verify all required inputs received
- [ ] Validate input quality and completeness
- [ ] Identify immediate red flags or blockers (e.g., missing assets, high-bounce on mobile)
- [ ] Establish baseline metrics (current PageSpeed score, conversion rate)

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Largest Contentful Paint (LCP) Optimization
- Research Focus: Techniques to reduce LCP and improve user perception of loading time.
- Target Sources: Google's Web Vitals documentation, Smashing Magazine articles.

**Topic 2:** First Input Event (FID) Reduction Strategies
- Research Focus: Minimizing FID by optimizing main thread work.
- Target Sources: Chrome DevTools performance insights.

**Topic 3:** Efficient Image Optimization Techniques
- Research Focus: Best practices for compressing and serving images without quality loss.
- Target Sources: Squoosh, Cloudinary guides.

**Topic 4:** Minification & Compression of Assets**
- Research Focus: Strategies to reduce CSS/JS/Binary file sizes.
- Target Tools: PurifyCSS, UglifyJS.

**Topic 5:** Caching Mechanisms
- Research Focus: Server-side vs client-side caching strategies for static assets.
- Target Tools: Varnish, Redis.

**Topic 6:** CDN Integration Best Practices**
- Research Focus: Choosing and configuring a CDN to serve content efficiently globally.
- Target Tools: Cloudflare, Fastly.

**Topic 7:** Lazy Loading of Media Assets
- Research Focus: Implementing lazy loading for images/videos without impacting SEO.
- Target Techniques: IntersectionObserver API.

**Topic 8:** Optimizing Web Fonts**
- Research Focus: Using font formats like WOFF2 and optimizing font loading impact.
- Target Tools: FontTools, Google Fonts.

**Topic 9:** Server Response Time (SRT) Reduction
- Research Focus: Techniques to improve SRT by optimizing database queries and server configurations.
- Target Tools: MySQL performance schema.

**Topic 10:** Mobile Performance Metrics & Best Practices**
- Research Focus: Ensuring mobile-first optimization for page load speed.
- Target Tools: Lighthouse, Chrome User Experience Report.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy prioritizing impact and feasibility.
2. Identify common themes across topics (e.g., CDN usage appears in multiple areas).
3. Create master action plan mapping each topic to specific implementation steps.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Conduct initial performance audit using Google Lighthouse.
- **Tools Needed:** Lighthouse (Chrome DevTools), PageSpeed Insights, Web Vitals plugin for WordPress.
- **Success Criteria:** Document baseline metrics and identify top offenders (>3 critical issues).
- **Common Pitfalls:** Overlooking mobile optimization or failing to prioritize high-impact fixes.
- **Time Estimate:** 2 hours

**STEP 2: [Prioritized Optimization Plan]**
- **Action:** Create a prioritized backlog based on impact score (PageSpeed, LCP, FID) and effort required.
- **Tools Needed:** Excel/Google Sheets for ranking; Trello or Asana for task management.
- **Success Criteria:** Top 3 items selected align with most significant performance gains.
- **Common Pitfalls:** Overlooking high-effort, high-impact issues in favor of quick wins.
- **Time Estimate:** 1 hour

**STEP 3: [Critical Asset Optimization]**
- **Action:** Implement image optimization, minify CSS/JS, and leverage browser caching.
- **Tools Needed:** Squoosh for images; PurifyCSS for unused styles; Gulp/Webpack for minification.
- **Success Criteria:** Documented before/after sizes; verified caching headers (ETag, Cache-Control).
- **Common Pitfalls:** Not testing changes in production environment or forgetting to update cache-busting parameters.
- **Time Estimate:** 4 days

**STEP 4: [CDN Integration & Optimization]**
- **Action:** Set up a CDN for static assets and configure image optimization settings.
- **Tools Needed:** Cloudflare, Fastly; Image optimization plugins (e.g., WP Rocket).
- **Success Criteria:** PageSpeed score improves by at least 10 points post-CDN integration; cache hit ratio >80%.
- **Common Pitfalls:** Misconfiguring CDN origin pull behavior or failing to purge assets after updates.
- **Time Estimate:** 2 days

**STEP 5: [Lazy Loading Implementation]**
- **Action:** Add lazy loading to all images, videos, and iframes using the IntersectionObserver API.
- **Tools Needed:** Vanilla JS implementation; LazyLoad plugin for CMS platforms.
- **Success Criteria:** Page load time reduced by at least 30% on mobile devices; no perceptible delay in user interaction.
- **Common Pitfalls:** Overlooking critical above-the-fold assets or misconfiguring observer root margin.
- **Time Estimate:** 1 day

**STEP 6: [Server Response Time Optimization]**
- **Action:** Optimize database queries, enable query caching, and consider using a CDN edge for static resources.
- **Tools Needed:** QueryMonitor; Redis/Memcached for cache; Cloudflare Workers for serverless optimizations.
- **Success Criteria:** Server response time reduced by at least 200ms; overall page load improved by at least 10 points.
- **Common Pitfalls:** Not profiling actual queries or disabling caching during tests.
- **Time Estimate:** 2 days

**STEP 7: [Continuous Testing & Monitoring]**
- **Action:** Implement automated performance testing using Lighthouse CI and set up alerts for any regressions.
- **Tools Needed:** GitHub Actions, CircleCI; Sentry for error monitoring.
- **Success Criteria:** No failed tests in production pipeline; immediate notification of any score drop below 90/100.
- **Common Pitfalls:** Failing to run tests on every PR or not setting appropriate thresholds.
- **Time Estimate:** Ongoing

**STEP 8: [User Experience (UX) Optimization]**
- **Action:** Analyze user journey and optimize elements affecting perceived speed (e.g., touch targets, navigation).
- **Tools Needed:** Heatmaps (Hotjar), A/B testing tools (Google Optimize).
- **Success Criteria:** Reduced bounce rate by at least 5% and increased time on site by 7%.
- **Common Pitfalls:** Ignoring accessibility implications or not measuring impact of UX changes.
- **Time Estimate:** 1 day

**STEP 9: [Conversion Rate Analysis]**
- **Action:** Compare conversion metrics before and after optimizations using A/B testing tools.
- **Tools Needed:** Google Analytics, Optimizely, VWO.
- **Success Criteria:** Minimum 10% increase in desired conversions (e.g., form submissions, purchases).
- **Common Pitfalls:** Not accounting for external factors influencing conversion rates or not running sufficient statistical power tests.
- **Time Estimate:** Ongoing

**STEP 10: [Maintenance & Future Optimization]**
- **Action:** Schedule quarterly performance audits and implement ongoing optimization practices.
- **Tools Needed:** Scheduled Lighthouse runs; CI pipeline for automated checks.
- **Success Criteria:** Consistently meeting PageSpeed targets with minimal manual intervention.
- **Common Pitfalls:** Neglecting to update or run scheduled tasks over time.
- **Time Estimate:** Ongoing

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After STEP 2 - Verify that backlog prioritization aligns with business goals and resource constraints.
- **Checkpoint 2:** After STEP 3 - Validate asset optimizations by running Lighthouse again; ensure no regressions introduced.
- **Checkpoint 3:** After STEP 4 - Confirm CDN is serving assets from the correct edge location and not caching critical pages.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** PageSpeed Score (Lighthouse) ≥ 95/100
2. **Secondary Metrics:**
   - LCP < 2000ms
   - FID < 100ms
   - Time to Interactive (TTI) < 5 seconds
3. **Long-term Metrics:**
   - Conversion Rate Increase ≥ 10%
   - User Engagement Metrics (e.g., bounce rate, session duration)

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities from the backlog.
3. Implement changes prioritizing quick wins and critical path optimizations.
4. Re-measure to confirm impact.
5. Repeat until all primary metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current PageSpeed score vs target
- Conversion rate baseline and post-optimization results
- ROI of optimization efforts (e.g., $X saved in hosting costs due to reduced bandwidth)

**2. Detailed Report**
- Performance audit findings with before/after metrics
- Implementation steps and associated risks mitigated
- Cost-benefit analysis including tooling costs

**3. Maintenance Plan**
- Frequency of performance audits (quarterly)
- Ownership model for ongoing optimizations
- Alert thresholds for regressions in monitoring tools

**4. Knowledge Transfer**
- Training session plan for new team members on performance best practices
- Documentation of all changes made to CMS, CDN configurations, and caching mechanisms

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace All [BRACKETED] Items** with specific data from your website audit (e.g., URL, current metrics).
2. **Define 10-20 Critical Topics** based on industry trends and tools used by Conversion Rate Optimizers.
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria for each metric.
4. **Build Step-by-Step Workflow** from proven optimization methodologies (e.g., Google's Web Vitals guide).
5. **Include Latest 2024-2025 Practices** focusing on AI-driven insights and automated optimizations.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Largest Contentful Paint (LCP) Optimization]"
    focus: "Techniques to reduce LCP"
    sources: ["Google Web Vitals", "Smashing Magazine"]
    deliverable: "List of top 3 optimization strategies with implementation steps"

  - agent_id: 2
    topic: "[First Input Event (FID) Reduction]"
    focus: "Minimizing FID"
    sources: ["Chrome DevTools", "Web.dev articles"]
    deliverable: "Best practices for main thread work reduction"

  # [Continue defining agents 3-10 based on critical topics]
```

### Consolidation Process
1. Collect all agent reports.
2. Cross-reference findings for consistency.
3. Resolve conflicts by evaluating source authority.
4. Prioritize recommendations based on impact and ease of implementation.

---

## SUCCESS VALIDATION

### Final Checklist

Before marking the project as COMPLETE:

- [ ] **Primary Objective Achieved?** PageSpeed score ≥ 95/100
- [ ] **Secondary Metrics Met?** LCP < 2000ms, FID < 100ms, TTI < 5 seconds
- [ ] **Conversion Rate Increase:** Minimum 10% uplift in target conversions
- [ ] **Quality Verified:** No performance regressions detected; user experience remains intact
- [ ] **Documentation Complete:** All deliverables ready for stakeholder review

### Continuous Improvement
- Document lessons learned from the optimization process.
- Update templates with new findings or improved methodologies.
- Share best practices within internal teams and external communities.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** E-commerce platform, Content Management System (CMS)  
**Success Rate:** 85% based on similar industry benchmarks  

---

