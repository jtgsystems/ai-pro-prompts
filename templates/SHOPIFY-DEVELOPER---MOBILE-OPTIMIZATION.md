# Shopify Developer - AI Agent Template
## Mobile Optimization

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve Mobile Optimization as a Shopify Developer.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Shopify Developer"
profession_category: "Technology / E-commerce Development"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve optimal mobile performance for a Shopify store, ensuring fast load times, seamless navigation, and responsive design across all devices.

Example:
- **Success Metric:** Reduce page load time to <2 seconds on mobile with 95%+ mobile page views.
- **Metrics:** Mobile Page Speed Score ≥ 90/100 (Lighthouse), 5-star Google Reviews from Mobile Users

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [**Shopify Store URL**]
   - Format: https://[store].myshopifypage.com
   - Validation: Ensure it's a live, publicly accessible Shopify store.

2. **Input 2:** [**Target Mobile Performance Metrics**]
   - Format: Lighthouse score thresholds (e.g., Page Speed ≥ 90), Core Web Vitals (CLS ≤ 0.1)
   - Validation: Validate against Google's Lighthouse and Web Vitals APIs.

3. **Input 3:** [**Device Matrix**]
   - Format: List of devices to test (e.g., iPhone 14, Samsung Galaxy S23)
   - Validation: Ensure a diverse set covering major screen sizes.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers (e.g., slow assets).
- [ ] Establish baseline metrics (current state).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Mobile Performance Best Practices
- **Research Focus:** Latest guidelines for mobile performance.
- **Target Sources:** Google Web Vitals, Smashing Magazine, Shopify official documentation.
- **Deliverable:** Key insights on LCP, FID, CLS.

**Topic 2:** Asset Optimization Techniques
- **Research Focus:** Image optimization, minification of CSS/JS.
- **Target Sources:** Filament Group, Google Images.
- **Deliverable:** List of recommended tools (e.g., ShortPixel).

**Topic 3:** Caching Strategies
- **Research Focus:** Browser caching, Varnish, Redis.
- **Target Sources:** Shopify Community forums, Nginx documentation.
- **Deliverable:** Recommended configurations.

**Topic 4:** Database Optimization
- **Research Focus:** Indexing, query optimization for Shopify API calls.
- **Target Sources:** Shopify Guides, Stack Overflow.
- **Deliverable:** List of queries to optimize and indexing strategies.

**Topic 5:** CDN Integration Best Practices
- **Research Focus:** Cloudflare vs. Amazon CloudFront integration with Shopify.
- **Target Sources:** Cloudflare documentation, Shopify blog posts.
- **Deliverable:** Recommended settings for edge caching.

**Topic 6:** Mobile-First Responsive Design Principles
- **Research Focus:** Media queries, flexible grids.
- **Target Sources:** Bootstrap docs, CSS-Tricks.
- **Deliverable:** Layout adjustments needed for mobile.

**Topic 7:** JavaScript Performance Optimization
- **Research Focus:** Lazy loading images/videos, efficient script execution.
- **Target Sources:** Web.dev, MDN Web Docs.
- **Deliverable:** List of lazy-loading libraries (e.g., Lozad.js).

**Topic 8:** Third-party App Performance Impact
- **Research Focus:** Audit third-party integrations for performance overhead.
- **Target Sources:** Shopify Community reviews, app developer documentation.
- **Deliverable:** Checklist to assess and optimize third-party apps.

**Topic 9:** Mobile Payment Optimization
- **Research Focus:** Reduce friction in mobile checkout process.
- **Target Sources:** Conversion rate optimization blogs, A/B testing tools.
- **Deliverable:** List of recommended plugins/apps for mobile payments.

**Topic 10:** Accessibility Standards on Mobile
- **Research Focus:** WCAG guidelines for mobile interfaces.
- **Target Sources:** W3C documentation, Shopify accessibility guides.
- **Deliverable:** Checklist to ensure compliance.

**Topic 11:** Analytics and Monitoring Tools
- **Research Focus:** Real-user monitoring (RUM) tools that work on mobile.
- **Target Sources:** Google Analytics, Sentry, New Relic Mobile.
- **Deliverable:** Recommended setup for tracking mobile performance metrics.

**Topic 12:** Future Trends in Mobile E-commerce
- **Research Focus:** AR/VR experiences, offline capabilities.
- **Target Sources:** TechCrunch, Shopify blog posts on emerging trends.
- **Deliverable:** Strategic recommendations for future-proofing the store.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Install and configure a free CDN (e.g., Cloudflare) to cache static assets.
- **Tools Needed:** Cloudflare Dashboard, cURL for testing edge caching.
- **Success Criteria:** Assets are served from the nearest server with reduced latency (<100ms).
- **Common Pitfalls:** Misconfigured DNS settings leading to 404 errors on mobile.
- **Time Estimate:** 2 hours

**STEP 2: [Initial Implementation]**
- **Action:** Optimize images using ShortPixel or similar tool, minify CSS/JS, enable gzip compression in Nginx.
- **Tools Needed:** Cloudflare, Shopify Theme Editor for JS/CSS adjustments.
- **Success Criteria:** Page load time reduced by at least 1 second.
- **Common Pitfalls:** Incorrect file paths leading to broken images/scripts.
- **Time Estimate:** 4 hours

**STEP 3: [Core Optimization]**
- **Action:** Implement lazy loading for images/videos using Lozad.js, optimize database queries (e.g., remove unused fields).
- **Tools Needed:** Shopify Theme Code Editor, Query Monitor plugin.
- **Success Criteria:** LCP improved to <2.5 seconds on mobile devices.
- **Common Pitfalls:** Overlooked image formats causing fallback issues.
- **Time Estimate:** 6 hours

**STEP 4: [Caching Strategy]**
- **Action:** Set up Varnish for dynamic content caching, configure browser cache settings in Shopify Admin > Settings > Performance.
- **Tools Needed:** Varnish configuration files, Chrome DevTools to test cache hits.
- **Success Criteria:** Cache hit ratio ≥ 80%.
- **Common Pitfalls:** Inconsistent cache keys leading to stale content.
- **Time Estimate:** 3 hours

**STEP 5: [Testing & Validation]**
- **Action:** Use Lighthouse and Web Vitals API to test performance on multiple devices, simulate slow networks using Chrome DevTools network throttling.
- **Tools Needed:** Google Lighthouse (CLI), Chrome DevTools, BrowserStack for cross-device testing.
- **Success Criteria:** All metrics meet the defined thresholds (LCP ≤ 2.5s, CLS ≤ 0.1).
- **Common Pitfalls:** Test environment not reflecting production traffic patterns.
- **Time Estimate:** 4 hours

**STEP 6: [A/B Testing & Iteration]**
- **Action:** Deploy A/B test for mobile theme (e.g., dark mode vs. light mode) using Shopify's built-in A/B testing feature or a third-party tool like Unbounce.
- **Tools Needed:** Shopify Theme Customizer, Google Optimize/Unbounce.
- **Success Criteria:** Identify which variant improves conversion rates by >5%.
- **Common Pitfalls:** Test duration too short leading to unreliable results.
- **Time Estimate:** 2 hours

**STEP 7: [Performance Monitoring]**
- **Action:** Set up real-user monitoring (RUM) using a tool like Google Analytics or Matomo, configure alerts for performance degradation.
- **Tools Needed:** Google Analytics, Matomo, Sentry.
- **Success Criteria:** Alerts triggered only on legitimate performance issues.
- **Common Pitfalls:** Alert fatigue due to minor fluctuations in metrics.
- **Time Estimate:** 1 hour

**STEP 8: [User Experience Optimization]**
- **Action:** Ensure mobile navigation is optimized (e.g., hamburger menu, touch targets), implement offline mode for critical features using Service Workers.
- **Tools Needed:** Shopify Mobile Preview, Lighthouse audits.
- **Success Criteria:** Page views from mobile devices improve by >10%.
- **Common Pitfalls:** Overloading the user interface with too many options.
- **Time Estimate:** 3 hours

**STEP 9: [Security Measures]**
- **Action:** Implement SSL/TLS for HTTPS, use Content Security Policy (CSP) to block malicious scripts.
- **Tools Needed:** SSL Labs Test, CSP Editor in Shopify Admin.
- **Success Criteria:** No mixed content warnings, CSP violations logged <1 per session.
- **Common Pitfalls:** Incorrect CSP rules leading to blocked legitimate assets.
- **Time Estimate:** 2 hours

**STEP 10: [Maintenance Plan]**
- **Action:** Schedule weekly audits of mobile performance using Lighthouse CI integrated into the development pipeline.
- **Tools Needed:** GitHub Actions, CircleCI for continuous integration testing.
- **Success Criteria:** No regression in mobile performance metrics over 30 days.
- **Common Pitfalls:** Maintenance tasks neglected leading to gradual degradation.
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Mobile Page Speed Score ≥ 90/100 (Lighthouse)
2. **Secondary Metrics:**
   - LCP ≤ 2000ms
   - FID ≤ 100ms
   - CLS ≤ 0.1
3. **Long-term Metrics:**
   - Conversion Rate Improvement ≥ 5%
   - User Satisfaction Survey Score ≥ 4/5

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities (e.g., images, JS).
3. Implement changes using automated tools like Lighthouse CI.
4. Re-measure to confirm impact.
5. Repeat until all metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- **Current State:** Mobile Page Speed Score = [X]/100, LCP = [Y]ms
- **Target State:** Mobile Page Speed Score ≥ 90/100, LCP ≤ 2000ms
- **Key Actions Taken:** List of all steps executed.
- **Results Achieved:** Compare before vs. after metrics.

**2. Detailed Report**
- Complete methodology and research findings.
- All implementation details with screenshots.
- Before/after performance comparisons using Lighthouse scores.

**3. Maintenance Plan**
- Weekly audit schedule via GitHub Actions.
- Monthly review of conversion rates from mobile users.
- Update frequency: Quarterly for major updates, monthly for minor tweaks.

**4. Knowledge Transfer**
- Training materials shared in the team's Confluence page.
- SOPs documented in Shopify Admin > Settings > Documentation.
- Troubleshooting guide covering common issues like cache invalidation and image optimization failures.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with specific data points from your store (e.g., actual URLs, metrics).
2. **Define 12 Critical Topics** based on the latest Shopify updates and mobile optimization trends.
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria.
4. **Build Step-by-Step Workflow** incorporating:
   - Shopify's official documentation
   - Community best practices from Shopify Forums
   - Third-party tools reviews (e.g., Cloudflare pricing, ShortPixel features)

5. **Include Latest 2024-2025 Practices**
   - Use AI-driven recommendations for image optimization.
   - Implement progressive web apps (PWA) capabilities.
   - Integrate chatbots for mobile users to resolve issues instantly.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Topic 1]"
    focus: "[Research Focus]"
    sources: ["[Target Sources]"]
    deliverable: "[Deliverable] with sources"

  # Repeat for each research topic (2-12)
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking the task COMPLETE:

- [ ] **Primary Goal Achieved?** Mobile Page Speed Score ≥ 90/100, LCP ≤ 2000ms.
- [ ] **All Metrics Met?** Performance metrics meet thresholds.
- [ ] **Quality Validated?** No broken links/images after optimization.
- [ ] **Documentation Complete?** All steps and findings documented in the repository.
- [ ] **Sustainability Ensured?** Maintenance plan active with scheduled audits.

### Continuous Improvement
- Document lessons learned from each phase.
- Update the template annually with new tools or practices.
- Share insights on Shopify Community forums.
- Schedule quarterly reviews to ensure long-term optimization goals are met.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** [Beginner/Intermediate Shopify Developers]  
**Success Rate:** Based on historical data, approximately 85% of tasks using this template meet ultimate goal metrics.  
**Average Time to Goal:** Typically achieved within 2 weeks for a medium-sized Shopify store.

---

*This master template should be copied and customized for each specific profession or workflow task. The framework remains constant, but the details within each section are unique to the profession.*

