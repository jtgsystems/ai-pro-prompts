# SEO Analyst - AI Agent Template
## Complete Technical SEO Audit

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a complete technical SEO audit for websites.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "SEO Analyst"
profession_category: "Marketing"
experience_level: "[Beginner/Intermediate]"
```

#### Ultimate Goal
**Primary Objective:** Conduct a thorough and comprehensive technical SEO audit of the target website, achieving 100% compliance with Google's core web vitals, mobile-friendliness, HTTPS encryption, structured data markup, crawl budget optimization, XML sitemap validity, server performance (LCP & TTFB), canonicalization, pagination, and other technical SEO best practices.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Target website URL  
   - Format: URL string  
   - Validation: Must be a valid domain name with reachable HTTP/HTTPS pages.
2. **Input 2:** Primary target keywords for ranking analysis  
   - Format: List of keyword strings  
   - Validation: At least 10-15 relevant, high-volume keywords (global search volume >100).
3. **Input 3:** Technical SEO constraints or requirements from stakeholders  
   - Format: Text description  
   - Validation: Clear and specific technical preferences.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags (e.g., HTTP vs HTTPS, mobile-friendliness issues).
- [ ] Establish baseline metrics (current state of SEO health).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (10-20 Topics)

**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices.

**Topic 1:** Core Web Vitals  
- Research Focus: Definition, impact on rankings, and optimization strategies.
- Target Sources: Google's Search Central documentation, recent SEO blogs (2024).
- Deliverable: Key insights and best practice checklist for LCP, FID, CLS improvements.

**Topic 2:** Mobile-Friendliness & Responsiveness  
- Research Focus: Importance of mobile-first indexing, responsive design techniques.
- Target Sources: Google's Mobile-Friendly Test results, responsive UI frameworks (Bootstrap).
- Deliverable: Checklist of mobile-friendly design elements and code changes needed.

**Topic 3:** HTTPS Encryption  
- Research Focus: Security benefits, SEO implications, and migration strategies.
- Target Sources: OWASP SSL/TLS Recommendations, Chrome security reports.
- Deliverable: Step-by-step guide to secure site with Let's Encrypt and HTTP/2.

**Topic 4:** Structured Data Markup  
- Research Focus: Schema.org implementations for rich snippets, Breadcrumbs, FAQ schema.
- Target Sources: Schema.org documentation, Google Search Console Help articles.
- Deliverable: JSON-LD code samples and implementation guide.

**Topic 5:** Crawl Budget Optimization  
- Research Focus: Indexing speed, canonicalization issues, sitemap size best practices.
- Target Sources: Screaming Frog SEO crawler guides, Moz blog on crawl budget.
- Deliverable: List of technical changes to improve crawl budget without throttling bots.

**Topic 6:** XML Sitemap Validity & Optimization  
- Research Focus: Sitemap structure, change frequency updates, URL inclusion rules.
- Target Sources: Yoast SEO plugin documentation, Screaming Frog analysis tools.
- Deliverable: Updated sitemap.xml file and validation report from Google Search Console.

**Topic 7:** Server Performance (LCP & TTFB)  
- Research Focus: Core metrics, server response time optimization techniques.
- Target Sources: WebPageTest reports, GTmetrix tutorials, Cloudflare performance guides.
- Deliverable: Optimization plan with CDN implementation and asset compression strategies.

**Topic 8:** Canonicalization & Pagination Issues  
- Research Focus: Handling duplicate content from paginated or filtered pages.
- Target Sources: Moz blog on canonical tags, Google Search Central guidelines.
- Deliverable: Implementation of rel=canonical links and proper pagination markup.

**Topic 9:** XML Robots.txt Best Practices  
- Research Focus: Proper syntax rules, disallowing non-indexed directories.
- Target Sources: Official robots.txt specification, Screaming Frog configuration guides.
- Deliverable: Updated robots.txt file with best practice recommendations.

**Topic 10:** Server Security (HTTPS & SSL)  
- Research Focus: HSTS implementation, OWASP security headers, CSRF protection.
- Target Sources: Nginx/ Apache security configurations, Google's HTTP Security Headers report.
- Deliverable: Secure server configuration checklist with recommended header settings.

**Topics 11-20 (Advanced):**
- **Topic 11:** International SEO (hreflang tags)
- **Topic 12:** AMP implementation for mobile speed
- **Topic 13:** Lazy loading of images & videos
- **Topic 14:** Redirect chains and loops analysis
- **Topic 15:** Site schema for product listings
- **Topic 16:** Mobile usability enhancements
- **Topic 17:** SSL certificate management (Let's Encrypt)
- **Topic 18:** Performance budgeting with Lighthouse CI
- **Topic 19:** Automated SEO testing tools integration (Screaming Frog, WebPageTest API)
- **Topic 20:** AI-powered SEO analysis using GPT models for content optimization

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Conduct a full website crawl using Screaming Frog or similar tool to generate an XML sitemap.
- **Tools Needed:** Screaming Frog, Google Search Console API (free), JSON-LD validator.
- **Success Criteria:** Complete crawl report with URLs indexed/not indexed and core issues flagged.
- **Common Pitfalls:** Missing HTTPS pages, incorrect pagination parameters.
- **Time Estimate:** 1 hour for initial crawl setup.

**STEP 2: [Initial Implementation]**
- **Action:** Fix all identified technical SEO issues from the crawl report (e.g., add missing meta descriptions, fix broken links).
- **Tools Needed:** CMS editor, HTML validator, Google Search Console.
- **Success Criteria:** All critical issues resolved; website shows no crawl errors in Screaming Frog.
- **Common Pitfalls:** Incorrect canonical tags leading to duplicate content warnings.
- **Time Estimate:** 4-6 hours for initial fixes.

**STEP 3: [Core Work]**
- **Action:** Implement HTTPS on all pages, set up structured data using JSON-LD script in the footer.
- **Tools Needed:** Let's Encrypt, JSON-LD validator, Yoast SEO plugin (if available).
- **Success Criteria:** All pages loaded over HTTPS; Structured Data validated by Google Search Console.
- **Common Pitfalls:** Mixed content warnings due to outdated scripts not removed.

**STEP 4: [Optimize Crawl Budget]**
- **Action:** Optimize site indexability by ensuring only important URLs are crawled (robots.txt, XML sitemap).
- **Tools Needed:** Robots.txt generator, Screaming Frog SEO crawler.
- **Success Criteria:** Crawlers accessing correct URLs without being blocked; Indexing speed improved in Search Console.
- **Common Pitfalls:** Overly restrictive robots.txt causing entire site to be excluded.

**STEP 5: [Sitemap & Redirect Management]**
- **Action:** Update and submit the XML sitemap through Google Search Console, fix any redirect chains.
- **Tools Needed:** Google Search Console API (free), Redirect checker tool.
- **Success Criteria:** Sitemap accepted by Google; No redirect loops detected.
- **Common Pitfalls:** Missing redirects for canonical URLs causing crawl budget issues.

**STEP 6: [Performance Optimization]**
- **Action:** Optimize site speed using CDN, image compression tools, and minify CSS/JS files.
- **Tools Needed:** Cloudflare (free tier), ImageOptim/GIMP for images, Google PageSpeed Insights.
- **Success Criteria:** LCP < 2.5 seconds on mobile; TTFB < 0.8 seconds on desktop.
- **Common Pitfalls:** Overly aggressive compression causing broken assets.

**STEP 7: [Security Hardening]**
- **Action:** Implement HSTS, security headers (Content-Security-Policy), and CSP for critical resources.
- **Tools Needed:** Cloudflare, SSL Labs test.
- **Success Criteria:** Security Headers validated as passing in the Browser Security Check tool.
- **Common Pitfalls:** Incorrect header values causing browser warnings.

**STEP 8: [Final QA & Testing]**
- **Action:** Run a final crawl with Lighthouse CI to validate all critical metrics are within acceptable ranges.
- **Tools Needed:** Lighthouse CI, Screaming Frog.
- **Success Criteria:** All audits passing; No red flags in performance or accessibility sections.

**STEP 9: [Monitoring Setup]**
- **Action:** Configure Google Search Console alerts for indexing issues and core errors.
- **Tools Needed:** Google Search Console.
- **Success Criteria:** Real-time notifications set up for critical crawl errors.
- **Common Pitfalls:** Alerts not configured correctly leading to delayed issue detection.

**STEP 10: [Reporting & Documentation]**
- **Action:** Generate a comprehensive SEO audit report with before/after metrics, actionable items, and maintenance plan.
- **Tools Needed:** Google Docs, Excel for data visualization.
- **Success Criteria:** Final report submitted to stakeholders within agreed timeframe; All action items tracked.

#### Quality Checkpoints
Insert checkpoints between major steps:

**Checkpoint 1 (After Step 2):** Verify that all initial crawl issues are resolved and no new errors introduced.  
**Checkpoint 2 (After Step 4):** Validate that crawl budget is optimized without de-indexing important pages.  
**Checkpoint 3 (After Step 8):** Confirm that security headers pass Chrome's HTTP Security Check.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Core Web Vitals score >= 89 (LCP, FID, CLS).
2. **Secondary Metrics:**
   - Mobile-Friendliness: 100% passing on Google's Mobile-Friendly Test.
   - HTTPS Encryption: No mixed content warnings in Chrome DevTools.
   - Structured Data Validation: All structured data correctly indexed by Google Search Console.
3. **Long-term Metrics:**
   - Crawl Budget Efficiency: Index coverage at >95% for important pages.
   - Server Performance: Average LCP < 2.5s on mobile, TTFB < 0.8s on desktop.

#### Iterative Improvement Loop
1. Measure current performance against targets using Google PageSpeed Insights and Core Web Vitals dashboard.
2. Identify top 3 improvement opportunities based on audit report.
3. Implement changes (e.g., CDN configuration, image optimization).
4. Re-measure to confirm metrics improved.
5. Repeat until all primary and secondary metrics meet targets.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables

**1. Executive Summary**
- Current state vs. target state.
- Key actions taken (e.g., SSL implementation, structured data addition).
- Results achieved (e.g., Core Web Vitals score).

**2. Detailed Report**
- Complete methodology used for audit.
- All research findings and source citations.
- Implementation details with screenshots or logs.
- Before/after performance comparisons.

**3. Maintenance Plan**
- Ongoing tasks to maintain SEO health (e.g., weekly sitemap updates).
- Monitoring schedule (Google Search Console alerts, periodic crawls).
- Update frequency for audit documentation.
- Contingency procedures for critical failures.

**4. Knowledge Transfer**
- Training materials for team members on technical SEO best practices.
- Standard operating procedures for implementing HTTPS and structured data.
- Best practices documentation for future audits.
- Troubleshooting guide for common crawl errors and performance issues.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Core Web Vitals]"
    focus: "Latest optimization strategies for LCP, FID, CLS"
    sources: ["Google Search Central", "WebVitals.org"]
    deliverable: "Checklist with recommended techniques and tools"

  - agent_id: 2
    topic: "[Mobile-Friendliness]"
    focus: "Responsive design guidelines and performance best practices"
    sources: ["Chrome DevTools", "Bootstrap Documentation"]
    deliverable: "Design patterns checklist for mobile-first sites"

  # [Continue for agents 3-10]
```

---

### SUCCESS VALIDATION

Before marking this task as COMPLETE:

- [ ] **Primary Goal Achieved?** The website is fully compliant with Google's Core Web Vitals and other technical SEO requirements.
- [ ] **Metrics Met?** All defined success criteria (e.g., Core Web Vitals score, mobile-friendliness) are met or exceeded.
- [ ] **Quality Validated?** Technical fixes do not degrade user experience; site loads under target performance thresholds.
- [ ] **Documentation Complete?** All deliverables include comprehensive reports and maintenance plans.
- [ ] **Stakeholder Satisfied?** Final report accepted by the client/stakeholders with no further objections.

### Continuous Improvement
Document lessons learned, update the template with new best practices discovered during execution, share insights within the SEO community, and schedule regular reviews to ensure ongoing alignment with evolving search engine algorithms and user experience standards.

