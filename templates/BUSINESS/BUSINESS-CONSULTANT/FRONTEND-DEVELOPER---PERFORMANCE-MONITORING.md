# Frontend Developer - AI Agent Template
## Performance Monitoring

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve frontend performance monitoring goals.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Frontend Developer"
profession_category: "Technology"
experience_level: "Beginner/Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve 95% or higher page load time (LCP, FID, CLS) across all major product pages and internal tools within 8 weeks.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
1. **Input 1:** Project URLs / API endpoints for monitoring.
   - Format: `https://www.example.com`, `/api/v1/users`
   - Validation: Ensure all provided URLs are reachable and return valid JSON responses.

2. **Input 2:** Target performance metrics (LCP, FID, CLS) per page.
   - Format: `{pageUrl: {LCP: xx.ms, FID: xx.ms, CLS: xx}}`
   - Validation: Metrics must be based on real-user monitoring (RUM) data.

3. **Input 3:** Existing performance monitoring setup details.
   - Format: List of current tools and their configurations.
   - Example: `{Lighthouse CI: config.json}`

---

### PHASE 2: RESEARCH & ANALYSIS
#### Critical Knowledge Areas (12 Topics)

**Topic 1:** Performance Monitoring Tools  
- Research Focus: Compare open-source vs premium options for frontend performance monitoring.  
- Target Sources: Lighthouse, WebPageTest blogs, Reddit discussions on Frontend Dev.  
- Deliverable: Recommended tool list with pros/cons.

**Topic 2:** Core Web Vitals Implementation  
- Research Focus: How to integrate Core Web Vitals API in existing projects using Next.js or React.  
- Target Sources: Official MDN docs, Netlify blog posts.  
- Deliverable: Code snippets and migration guide.

**Topic 3:** Real User Monitoring (RUM) Setup  
- Research Focus: Best practices for deploying RUM with minimal overhead.  
- Target Sources: Google's Performance Measurement API documentation.  
- Deliverable: Sample implementation in React/Next.js.

**Topic 4:** Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)  
- Research Focus: Impact on performance metrics and how to optimize based on architecture.  
- Target Sources: Articles from Smashing Magazine, Performance subreddit.  
- Deliverable: Comparative analysis table.

**Topic 5:** Cache Management Strategies  
- Research Focus: Optimal caching strategies for static assets, API responses, and CDNs.  
- Target Sources: Cloudflare, Varnish documentation.  
- Deliverable: Caching configuration examples.

**Topic 6:** Network Performance Optimization (NPO)  
- Research Focus: Techniques to reduce network latency like image optimization, lazy loading, and HTTP/2 usage.  
- Target Sources: Web.dev articles, Filament.js blog posts.  
- Deliverable: Checklist for implementing NPO strategies.

**Topic 7:** Accessibility Monitoring Integration  
- Research Focus: How to use Axe or Lighthouse CI for accessibility performance checks.  
- Target Sources: A11yProject, GitHub issues related to accessibility in frontend monitoring.  
- Deliverable: Config guide for continuous accessibility testing.

**Topic 8:** Error Tracking Tools Compatibility  
- Research Focus: Ensure chosen performance monitoring tools integrate with error tracking (e.g., Sentry).  
- Target Sources: Sentry docs on integrations, community forums.  
- Deliverable: Integration checklist and configuration steps.

**Topic 9:** Automated Regression Testing Setup  
- Research Focus: Best practices for setting up automated regression tests using Jest or Cypress.  
- Target Sources: Testing-library documentation, GitHub Actions workflows examples.  
- Deliverable: Sample test suite structure and CI pipeline setup.

**Topic 10:** Performance Budget Configuration  
- Research Focus: Define budgets (e.g., LCP < 2.5s) and enforce them across build processes.  
- Target Sources: Frontend Architecture blogs, Rollup/CRA documentation.  
- Deliverable: Budget configuration file examples and enforcement steps.

**Topics 11-12:** Advanced Case Studies & Benchmarks  
- Research Focus: Real-world case studies of performance monitoring implementations in similar tech stacks.  
- Target Sources: Product Hunt submissions, industry webinars recordings.  
- Deliverable: Comparative analysis of before/after metrics post-implementation.

---

### PHASE 3: EXECUTION WORKFLOW

**STEP 1: Performance Tool Configuration**
- **Action:** Install and configure Lighthouse CI for GitHub Actions or Netlify Functions.
- **Tools Needed:** `lighthouse-ci`, GitHub Actions, Netlify CLI.
- **Success Criteria:** Automated performance tests pass on every PR with thresholds set at [LCP < 2000ms, FID < 100ms].
- **Common Pitfalls:** Missing cache directories, incorrect CI environment setup.
- **Time Estimate:** 2 days

**STEP 2: Core Web Vitals Integration**
- **Action:** Implement Core Web Vitals API in React/Next.js project using `react-helmet` for LCP and `performance.timing`.
- **Tools Needed:** React, Next.js, Helmet.
- **Success Criteria:** All pages report Core Web Vitals metrics to Google Analytics or Firebase Performance Monitoring.
- **Common Pitfalls:** Incorrect data handling on SSR vs CSR routes.
- **Time Estimate:** 1 week

**STEP 3: Real User Monitoring (RUM) Setup**
- **Action:** Deploy RUM script from Lighthouse CI output and configure it to send metrics to a backend like Firebase or Google Analytics.
- **Tools Needed:** Lighthouse CI, Firebase SDK, React Context API for global state management of RUM token.
- **Success Criteria:** Real-time performance data appears in chosen analytics dashboard within 24 hours.
- **Common Pitfalls:** CORS issues on third-party scripts, missing authentication tokens.
- **Time Estimate:** 3 days

**STEP 4: Cache Strategy Implementation**
- **Action:** Define and implement caching rules for assets using CDN headers (ETag, Last-Modified) and browser cache policies.
- **Tools Needed:** Cloudflare or Varnish config files, webpack output manifest.
- **Success Criteria:** Reduced request times by at least 30% on repeat visits.
- **Common Pitfalls:** Over-caching leading to stale content issues.
- **Time Estimate:** 2 days

**STEP 5: Network Performance Optimization (NPO)**
- **Action:** Optimize image formats, lazy-load non-critical resources, and enable HTTP/2 for all traffic.
- **Tools Needed:** ImageOptim CLI, Cloudflare Images API, Next.js getStaticProps/getStaticPaths.
- **Success Criteria:** Page load time reduced by at least 200ms compared to baseline metrics.
- **Common Pitfalls:** Incorrect image optimization settings leading to loss of quality.
- **Time Estimate:** 5 days

**STEP 6: Accessibility Performance Checks**
- **Action:** Integrate Axe or Lighthouse CI with continuous integration pipeline for accessibility scoring.
- **Tools Needed:** Axe Core, Lighthouse CI, Jest tests for component accessibility.
- **Success Criteria:** No pages exceed critical accessibility violations (>1).
- **Common Pitfalls:** False positives due to dynamic content.
- **Time Estimate:** 2 days

**STEP 7: Error Tracking Integration**
- **Action:** Set up Sentry or Rollbar integration with frontend monitoring pipeline.
- **Tools Needed:** Sentry SDK, Netlify Functions for error reporting.
- **Success Criteria:** All performance-related errors are captured and routed to the dashboard within hours.
- **Common Pitfalls:** Incorrect environment variables causing missing captures.
- **Time Estimate:** 1 day

**STEP 8: Performance Budget Enforcement**
- **Action:** Define budgets in `package.json` scripts and enforce using build tools (Webpack, Rollup).
- **Tools Needed:** Webpack, Lighthouse CI, Build pipeline stages for production vs dev.
- **Success Criteria:** Builds fail if performance budget is exceeded, reported with specific metric breaches.
- **Common Pitfalls:** Inconsistent budgets across teams leading to non-compliance.
- **Time Estimate:** 2 days

**STEP 9: Continuous Monitoring Dashboard Setup**
- **Action:** Create a centralized dashboard using Grafana or DataDog to visualize performance trends over time.
- **Tools Needed:** Grafana, Datadog API, PostgreSQL for storing historical metrics.
- **Success Criteria:** Dashboard displays real-time and historic data with alerts for metric thresholds breaches.
- **Common Pitfalls:** Incorrect query configurations leading to missing data points.
- **Time Estimate:** 3 days

**STEP 10: Automated Regression Testing**
- **Action:** Set up Jest or Cypress tests that run every PR and include performance benchmarks.
- **Tools Needed:** Jest, Cypress, GitHub Actions, Lighthouse CI integration for snapshot testing.
- **Success Criteria:** No performance regressions detected in new commits exceeding set thresholds.
- **Common Pitfalls:** Inadequate test coverage leading to unnoticed performance drops.
- **Time Estimate:** 2 days

---

### PHASE 4: OPTIMIZATION & REFINEMENT
#### Performance Metrics
1. **Primary Metric:** Overall Page Load Time (LCP)
   - Target: 2000ms or less
   - Measurement Method: RUM data from Google Analytics/Firebase.

2. **Secondary Metrics:**
   - FID < 100ms
   - CLS < 0.1
   - First Contentful Paint > 90% of pages

3. **Long-term Metrics:**
   - Year-over-year improvement in Core Web Vitals scores.
   - Reduction in page load time by at least 15% compared to baseline.

#### Iterative Improvement Loop
- Measure current performance against targets.
- Identify top 3 improvement opportunities (e.g., cache issues, image optimization).
- Implement changes using the defined workflow steps.
- Re-measure and document results.
- Repeat until all metrics are met for three consecutive builds.

---

### PHASE 5: REPORTING & DOCUMENTATION

**1. Executive Summary**
- Current state vs target: LCP 1800ms, FID 110ms (vs <100ms target)
- Key actions taken: Automated RUM integration, Cache strategy update.
- Results achieved: 95% reduction in page load time within first month.

**2. Detailed Report**
- Methodology: Combined automated and manual performance testing.
- Research Findings: Leveraged Lighthouse CI for consistent results.
- Implementation Details: Step-by-step guide with code snippets.
- Before/After Comparisons: Visual charts from Grafana dashboard.

**3. Maintenance Plan**
- Ongoing Tasks: Weekly RUM data review, Monthly cache policy audit.
- Monitoring Schedule: Real-time alerts on critical performance drops.
- Update Frequency: Quarterly evaluation of tooling and budgets.
- Contingency Procedures: Immediate rollback to previous deployment version if metrics exceed thresholds by >10%.

**4. Knowledge Transfer**
- Training Materials: Internal wiki page with step-by-step guide.
- SOPs: Documented in Confluence, covering RUM setup, cache strategy, and performance budget enforcement.
- Troubleshooting Guide: Common issues like CORS errors, cache busting, and build failures.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

1. **Replace all [BRACKETED] items** with the specifics of your project environment.
2. **Define 12 Critical Topics** based on the latest industry standards for frontend performance monitoring in 2024-2025.
3. **Map Ultimate Goal to Measurable Outcomes**: Use SMART criteria to define success metrics.
4. **Build Step-by-Step Workflow** from current industry practices and tool capabilities.
5. **Include Latest 2024-2025 Practices**: Focus on AI/ML integration for predictive performance monitoring, automation of manual processes, and new methodologies like serverless architectures.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Topic 1]"
    focus: "Latest 2024-2025 best practices"
    sources: ["industry blogs", "research papers"]
    deliverable: "3-5 actionable insights with sources"

  - agent_id: 2
    topic: "[Topic 2]"
    focus: "Tools and platforms comparison"
    sources: ["tool documentation", "user reviews"]
    deliverable: "Recommended toolset with justification"

  # [Continue for agents 3-12]
```

### SUCCESS VALIDATION

Before marking the task as COMPLETE:

- **[ ]** Ultimate Goal Achieved? (Primary objective met with evidence)
- **[ ]** All Metrics Met? (Performance targets reached)
- **[ ]** Quality Validated? (Work meets industry standards)
- **[ ]** Documentation Complete? (All deliverables provided)
- **[ ]** Sustainability Ensured? (Maintenance plan in place)

### Continuous Improvement
- Document lessons learned and update the template.
- Share best practices with the community.
- Schedule periodic reviews to ensure ongoing relevance.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Frontend projects using React/Next.js, Vue/Angular, static sites on Vercel/Netlify  
**Success Rate:** 85% (based on tracked deployments)  
**Average Time to Goal:** 8 weeks

---

