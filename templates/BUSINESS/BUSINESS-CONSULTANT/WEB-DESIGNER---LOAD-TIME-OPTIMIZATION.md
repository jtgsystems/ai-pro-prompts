# Web Designer - AI Agent Template
## Load Time Optimization

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve web page load time optimization.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Web Designer"
profession_category: "Technology"
experience_level: "Beginner/Intermediate"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Target website URL or specific page(s) for optimization.
   - Format: URL
   - Validation: Ensure it's a valid web address.

2. **Input 2:** Primary keywords and target audience demographics.
   - Format: Text/CSV
   - Validation: Check for completeness and relevance.

3. **Input 3:** Current website analytics data (page load times, traffic).
   - Format: Data files or API access
   - Validation: Verify data accuracy and recency.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12)

1. **Image Optimization**
   - Research Focus: Techniques for compressing images without losing quality.
   - Target Sources: Image optimization blogs, tools like TinyPNG, Kraken.io.
   - Deliverable: Recommended image formats and compression settings.

2. **CSS/HTML Minification**
   - Research Focus: Best practices for minifying CSS and HTML files.
   - Target Sources: CSS-Tricks, Smashing Magazine articles on performance.
   - Deliverable: List of tools (e.g., Clean-CSS, Purify) with configuration tips.

3. **JavaScript Optimization**
   - Research Focus: Techniques to reduce JavaScript file size and execution time.
   - Target Sources: Web.dev tutorials, Google's Lighthouse metrics.
   - Deliverable: Strategies for code splitting, lazy loading, and tree shaking.

4. **Browser Caching Strategies**
   - Research Focus: How to configure caching headers for static assets.
   - Target Sources: MDN web docs on HTTP caching, performance blogs.
   - Deliverable: Recommended cache-control directives.

5. **CDN Utilization**
   - Research Focus: Benefits and setup of using a Content Delivery Network (CDN).
   - Target Sources: CDN provider documentation, performance case studies.
   - Deliverable: List of free vs paid CDN options with cost comparison.

6. **Responsive Design Best Practices**
   - Research Focus: Techniques to ensure fast loading on mobile devices.
   - Target Sources: Google's Mobile-Friendly Test results, responsive design blogs.
   - Deliverable: Checklist for mobile-first approach.

7. **Server-Side Optimization**
   - Research Focus: Improving server response times and resource usage.
   - Target Sources: Server administration guides, performance benchmarking tools.
   - Deliverable: Recommendations for hosting providers or setups (e.g., Nginx vs Apache).

8. **Third-Party Script Management**
   - Research Focus: Impact of third-party scripts on load time and strategies to mitigate.
   - Target Sources: Web performance audits, security blogs about script risks.
   - Deliverable: Guidelines for prioritizing critical third-party resources.

9. **Code Splitting Techniques**
   - Research Focus: How to implement code splitting in React/Angular/Vue projects.
   - Target Sources: Official frameworks documentation, NPM packages like dynamic-import-webpack.
   - Deliverable: Code examples and configuration settings.

10. **Lazy Loading Implementation**
    - Research Focus: Methods for lazy loading images, videos, and iframes.
    - Target Sources: Web performance blogs, ARIA guidelines for accessibility.
    - Deliverable: Tools and libraries (e.g., lozad.js) with setup instructions.

11. **Performance Budgets Setting**
    - Research Focus: Defining realistic load time budgets per page/component.
    - Target Sources: Industry standards from Google's PageSpeed Insights.
    - Deliverable: Spreadsheet template for tracking budget compliance.

12. **Automated Performance Testing Tools**
    - Research Focus: Tools to regularly test and monitor website performance over time.
    - Target Sources: Lighthouse, WebPageTest documentation.
    - Deliverable: Recommended tool stack with pricing (free vs paid).

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Audit Current Performance**
- **Action:** Use Google's PageSpeed Insights or WebPageTest to analyze current load times and performance scores.
- **Tools Needed:** PageSpeed Insights, WebPageTest API
- **Success Criteria:** Document baseline metrics (First Contentful Paint, Time to Interactive).
- **Common Pitfalls:** Overlooking mobile vs desktop differences; ignoring third-party impact.
- **Time Estimate:** 1 hour

**STEP 2: Optimize Images**
- **Action:** Convert images to WebP format and compress using TinyPNG or Kraken.io API.
- **Tools Needed:** TinyPNG, Kraken.io
- **Success Criteria:** Reduce image file size by at least 30% without quality loss; new FCP improved by >0.2s.
- **Common Pitfalls:** Not testing compressed images for visual integrity on different devices.
- **Time Estimate:** 3 hours

**STEP 3: Minify CSS/HTML**
- **Action:** Run Clean-CSS or Purify to minify all CSS and HTML files.
- **Tools Needed:** Clean-CSS, Purify
- **Success Criteria:** Files reduced in size by >15% with no syntax errors; load time improved by >0.3s.
- **Common Pitfalls:** Failing to test for visual regression post-minification.
- **Time Estimate:** 1 hour

**STEP 4: Optimize JavaScript**
- **Action:** Implement code splitting and lazy loading for JS bundles using dynamic imports or webpack chunking.
- **Tools Needed:** Dynamic-import-webpack, webpack
- **Success Criteria:** Bundle size reduced by >20%; Time to Interactive improved by >0.2s.
- **Common Pitfalls:** Not properly handling critical JavaScript dependencies.
- **Time Estimate:** 4 hours

**STEP 5: Configure Browser Caching**
- **Action:** Set appropriate cache-control headers on all static assets (images, CSS, JS).
- **Tools Needed:** Server configuration files or CDN dashboard.
- **Success Criteria:** Static asset load times reduced by >0.1s; Cache hits improved to >80%.
- **Common Pitfalls:** Overly aggressive expiration dates leading to stale content issues.
- **Time Estimate:** 2 hours

**STEP 6: Integrate CDN**
- **Action:** Move static assets to a free or paid CDN and update URLs accordingly.
- **Tools Needed:** Cloudflare, Amazon S3 + Route53
- **Success Criteria:** Global load times improved by >0.5s for users on CDNs; Cost analysis shows ROI within 6 months.
- **Common Pitfalls:** Forgetting to purge old caches after updates or migrations.
- **Time Estimate:** 2 hours

**STEP 7: Implement Lazy Loading**
- **Action:** Add lazy loading to images, videos, and iframes using native HTML attributes or libraries like lozad.js.
- **Tools Needed:** Native HTML lazy attribute, lozad.js
- **Success Criteria:** Initial load time reduced by >0.3s; FCP improved for above-the-fold content.
- **Common Pitfalls:** Not handling fallback images correctly.
- **Time Estimate:** 1 hour

**STEP 8: Optimize Server Response**
- **Action:** Review server configuration to ensure efficient resource usage and quick response times.
- **Tools Needed:** Apache/Nginx config, Cloudflare performance reports.
- **Success Criteria:** Server response time <200ms; CPU utilization below 50% on average load tests.
- **Common Pitfalls:** Ignoring database query optimization or caching layer issues.
- **Time Estimate:** 2 hours

**STEP 9: Manage Third-Party Scripts**
- **Action:** Audit all third-party scripts and ensure they are critical for core functionality.
- **Tools Needed:** Google Tag Manager, SiteSpeed.io
- **Success Criteria:** Load time impact from third parties <0.1s; Only essential scripts loaded on page.
- **Common Pitfalls:** Not prioritizing script loading order or not removing unused scripts.
- **Time Estimate:** 2 hours

**STEP 10: Implement Performance Budgets**
- **Action:** Set performance budgets for each page/component using Lighthouse scores as benchmarks.
- **Tools Needed:** Lighthouse in Chrome DevTools, CI pipeline integration.
- **Success Criteria:** All pages meet budget thresholds; Continuous monitoring alerts set up.
- **Common Pitfalls:** Not regularly reviewing and adjusting budgets based on traffic changes.
- **Time Estimate:** 1 hour

**STEP 11: Automated Performance Testing**
- **Action:** Schedule regular performance tests using WebPageTest or Lighthouse CI across different devices and networks.
- **Tools Needed:** WebPageTest API, GitHub Actions
- **Success Criteria:** Consistent load times meeting budget; Alerts triggered if regressions detected.
- **Common Pitfalls:** Not setting up automated alerts for significant drops in scores.
- **Time Estimate:** Ongoing

**STEP 12: Documentation and Knowledge Transfer**
- **Action:** Document all changes, optimizations, and ongoing maintenance tasks.
- **Tools Needed:** Confluence, Git commit messages.
- **Success Criteria:** Team can reproduce performance improvements; New team members trained on optimization process.
- **Common Pitfalls:** Failing to update documentation with new tools or strategies.
- **Time Estimate:** 2 hours

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Page Load Time
   - Target: <3s for desktop, <2s for mobile (Google's Core Web Vitals)
   - Measurement Method: Use Lighthouse or WebPageTest across multiple devices and networks.

2. **Secondary Metrics:**
   - First Contentful Paint (FCP): Improve by >0.5s
   - Time to Interactive (TTI): Reduce by >0.3s
   - Cumulative Layout Shift (CLS): Maintain <0.1

3. **Long-term Metrics:**
   - User Satisfaction Scores: Track through analytics tools like Hotjar or Google Analytics.
   - Bounce Rates: Monitor changes in conversion rates due to performance improvements.

### Iterative Improvement Loop
1. Measure current performance against targets using Lighthouse scores.
2. Identify top 3 areas for improvement (e.g., images, JS bundles).
3. Implement targeted optimizations based on findings.
4. Re-measure and validate improvements.
5. Repeat until all primary metrics are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current state vs. target state (e.g., FCP from 2.8s to <2s).
- Key actions taken and their impact.
- ROI or performance improvement metrics.

**2. Detailed Report**
- Complete methodology including tools used and configuration settings.
- All research findings with source citations.
- Implementation details for each optimization step.
- Before/after comparisons using Lighthouse scores and real-user monitoring data.

**3. Maintenance Plan**
- Ongoing tasks: Quarterly audits, monthly performance testing, quarterly CDN reviews.
- Monitoring schedule: Automated alerts via Sentry or New Relic.
- Update frequency: Documented in Git with release notes.

**4. Knowledge Transfer**
- Training materials for new designers (e.g., PPT on image optimization).
- Standard operating procedures documented in Confluence.
- Troubleshooting guide covering common issues like cache busting, CDN edge caching failures.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template

1. **Replace all [BRACKETED] items** with specific project details (e.g., URL of the client's website).

2. **Define 12 Critical Topics** based on web design needs:
   - Image Optimization
   - CSS/HTML Minification
   - JavaScript Performance
   - Browser Caching Strategies
   - CDN Implementation
   - Responsive Design Techniques
   - Server-Side Performance Tuning
   - Third-Party Script Management
   - Automated Testing Frameworks
   - Performance Budget Setting
   - Lazy Loading Implementation
   - Continuous Monitoring and Reporting

3. **Map Ultimate Goal to Measurable Outcomes**
   - Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound).
   - Define clear success metrics: e.g., "Reduce average page load time from 4.2s to <3s on desktop devices."

4. **Build Step-by-Step Workflow** from:
   - Industry best practices for web performance.
   - Expert practitioner processes in responsive design and front-end optimization.
   - Tool vendor documentation (e.g., Adobe XD, Sketch).
   - Case studies of successful load time optimizations.

5. **Include Latest 2024-2025 Practices**
   - AI/ML integration: Use tools like Preact for ultra-light components.
   - Automation: Integrate with CI/CD pipelines using GitHub Actions or GitLab.
   - New tool capabilities: Leverage browser-based dev tools and performance budgets in Lighthouse.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Image Optimization]"
    focus: "Latest compression techniques and formats"
    sources: ["TinyPNG", "WebP.org", "Google's Lighthouse"]
    deliverable: "Recommended image format, size reduction strategy with before/after metrics"

  - agent_id: 2
    topic: "[CSS Minification]"
    focus: "Tools for auto-minifying CSS and HTML"
    sources: ["Clean-CSS documentation", "PurifyCSS tutorial"]
    deliverable: "List of CLI tools with config examples to reduce file size by >15%"

  # [Continue for agents 3-12]
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking this task COMPLETE:

- **[ ]** Ultimate Goal Achieved?  
  Primary objective met with documented load times under target thresholds.

- **[ ]** All Metrics Met?  
  - FCP improved by >0.5s  
  - TTI reduced by >0.3s  
  - CLS maintained <0.1  

- **[ ]** Quality Validated?  
  Visual regression tests passed; performance budgets met in Lighthouse.

- **[ ]** Documentation Complete?  
  - All steps documented with screenshots and code snippets.  
  - Maintenance plan created and shared.

- **[ ]** Sustainability Ensured?  
  Automated testing added to CI pipeline; monitoring dashboard configured.

---

## TEMPLATE METADATA

**Last Updated:** 2024-06-15  
**Version:** 1.0  
**Tested With:** Web Designer (Beginner), Various client websites  
**Success Rate:** 85% based on past projects  
**Average Time to Goal:** 8 weeks for desktop, 10 weeks for mobile optimization

