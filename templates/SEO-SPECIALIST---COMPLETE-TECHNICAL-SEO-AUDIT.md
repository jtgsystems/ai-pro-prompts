# SEO Specialist - AI Agent Template
## Complete Technical SEO Audit

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a complete technical SEO audit for an SEO specialist.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "SEO Specialist"
profession_category: "Marketing"
experience_level: "[Beginner/Intermediate]"
```

#### Ultimate Goal
**Primary Objective:**  
Complete a comprehensive technical SEO audit of the target website to achieve optimal search engine ranking performance, with measurable improvements in organic traffic and keyword rankings.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Target Website URL]  
   - Format: URL  
   - Validation: Ensure it's a valid web address that resolves to an active website.
2. **Input 2:** [Primary Target Keywords (5-10)]  
   - Format: List of keywords  
   - Validation: Confirm relevance and search volume.
3. **Input 3:** [Website Structure Overview]  
   - Format: Brief description or sitemap outline  
   - Validation: Ensure it reflects the actual site architecture.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received.  
- [ ] Validate input quality and completeness (e.g., correct URL format, relevant keywords).  
- [ ] Identify immediate red flags or blockers (e.g., server errors, blocked pages).  
- [ ] Establish baseline metrics (current keyword rankings, organic traffic, crawlability scores).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (15 Topics)

1. **Core Web Vitals** - How to improve LCP, FID, CLS using Google's Core Web Vitals.
2. **Site Speed Optimization** - Techniques for reducing page load time and improving performance scores.
3. **Mobile-First Design** - Best practices for mobile optimization including responsive design and touch targets.
4. **Crawlability & Indexing** - Ensuring search engines can crawl the site effectively, identifying 404 errors and noindex tags.
5. **Structured Data Implementation** - Implementing schema markup to enhance rich snippets in search results.
6. **SSL / HTTPS Security** - Best practices for secure website deployment and maintaining SSL certificates.
7. **Canonicalization & Duplicate Content** - Strategies to prevent duplicate content issues and ensure proper canonical tags are used.
8. **Redirect Management** - Proper use of 301 redirects for moved pages or URL changes.
9. **XML Sitemap Generation** - Creating, updating, and validating XML sitemaps to aid search engine crawling.
10. **Robots.txt Best Practices** - Crafting an effective robots.txt file that balances security with crawlability needs.
11. **Internal Linking Structure** - Optimizing internal links for SEO impact while maintaining user experience.
12. **Image Optimization** - Using alt attributes, compressing images to improve page load speed and accessibility.
13. **Server Configuration (e.g., Apache/Nginx)** - Configuring servers for optimal performance, security, and SEO compliance.
14. **Security Best Practices** - Implementing HTTPS, managing SSL certificates, and securing the site against vulnerabilities.
15. **User Experience (UX) Optimization** - Redesigning page layouts to enhance dwell time and reduce bounce rates.

#### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into a unified strategy prioritizing actions by impact.
2. Identify conflicts or contradictions in best practices across sources.
3. Create a master action plan with clear milestones and responsible parties.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Pre-Audit Preparation]**
- **Action:** Run initial crawl of the website to identify any obvious technical issues such as broken links or missing robots.txt.  
- **Tools Needed:** Screaming Frog SEO Spider (free), Google Search Console, Xenu Link Checker.  
- **Success Criteria:** Identify at least 3 critical issues needing immediate attention.  
- **Common Pitfalls:** Skipping preliminary crawl or ignoring low-priority errors.  
- **Time Estimate:** 2 hours.

**STEP 2: [Performance Analysis]**
- **Action:** Use Google PageSpeed Insights to analyze Core Web Vitals and generate a performance report.  
- **Tools Needed:** Google PageSpeed Insights, Lighthouse (Chrome DevTools).  
- **Success Criteria:** Achieve an overall score of 80+ on the Performance metric.  
- **Common Pitfalls:** Overlooking mobile optimization despite its critical importance for rankings.  
- **Time Estimate:** 1 hour.

**STEP 3: [Site Structure & Navigation Audit]**
- **Action:** Review sitemap.xml and robots.txt, verify all URLs are accessible from both crawler and user perspectives.  
- **Tools Needed:** Screaming Frog, Google Search Console.  
- **Success Criteria:** No broken links; all important pages crawlable by search engines.  
- **Common Pitfalls:** Incorrectly configured redirects or disallowing crucial content accidentally.  
- **Time Estimate:** 3 hours.

**STEP 4: [Structured Data & Schema Markup]**
- **Action:** Identify key information to markup (e.g., product reviews, events) and implement schema.org structured data using tools like Google's Structured Data Testing Tool.  
- **Tools Needed:** Google's Structured Data Testing Tool, Screaming Frog.  
- **Success Criteria:** Structured data validated without errors in the Rich Results Test.  
- **Common Pitfalls:** Incorrectly implemented JSON-LD markup causing validation errors.  
- **Time Estimate:** 2 hours.

**STEP 5: [HTTPS / SSL Implementation]**
- **Action:** Secure all pages with HTTPS, update internal links, and monitor for mixed content warnings.  
- **Tools Needed:** Let's Encrypt (free), Chrome DevTools, Redirect Checker.  
- **Success Criteria:** All pages served over HTTPS without mixed-content errors.  
- **Common Pitfalls:** Forgetting to redirect HTTP versions or leaving old redirects in place.  
- **Time Estimate:** 1 hour.

**STEP 6: [Canonical Tags & Duplicate Content]**
- **Action:** Ensure canonical tags are correctly set on duplicate content pages and that all internal links point to the canonical version.  
- **Tools Needed:** Screaming Frog, Google Search Console.  
- **Success Criteria:** No duplicate content warnings in search console reports.  
- **Common Pitfalls:** Missing canonical tags causing indexing issues or incorrect rel="next" relationships for pagination.  
- **Time Estimate:** 1 hour.

**STEP 7: [XML Sitemap Creation & Submission]**
- **Action:** Generate an updated XML sitemap and submit it to Google Search Console.  
- **Tools Needed:** Screaming Frog, Yoast SEO (free) or similar plugin.  
- **Success Criteria:** Sitemap validated by Google Search Console without errors.  
- **Common Pitfalls:** Missing entire sections of the site in the generated sitemap causing incomplete indexing.  
- **Time Estimate:** 1 hour.

**STEP 8: [Robots.txt File Review]**
- **Action:** Ensure robots.txt file blocks only non-essential content and allows search engines to crawl all important pages.  
- **Tools Needed:** Screaming Frog, Google Search Console.  
- **Success Criteria:** Robots exclusion policy aligns with SEO goals without unintentionally blocking essential content.  
- **Common Pitfalls:** Overly restrictive rules causing crawl budget issues or missed indexing opportunities.  
- **Time Estimate:** 1 hour.

**STEP 9: [Redirect Management]**
- **Action:** Review all redirects (301, 302) for moved pages and ensure they're correctly implemented to avoid loops or stale content.  
- **Tools Needed:** Screaming Frog, Redirect Checker.  
- **Success Criteria:** All necessary URLs have valid 301 redirects; no redirect loops detected.  
- **Common Pitfalls:** Mixing up 301 and 302 redirects causing crawl errors or indexing issues.  
- **Time Estimate:** 1 hour.

**STEP 10: [Image Optimization]**
- **Action:** Optimize all images by compressing files, adding descriptive alt text, and verifying they load correctly on mobile devices.  
- **Tools Needed:** TinyPNG (free), Screaming Frog, Google PageSpeed Insights.  
- **Success Criteria:** All critical images optimized with proper dimensions and alt tags; no broken image references detected.  
- **Common Pitfalls:** Ignoring large file sizes causing slow page loads or missing alt attributes reducing accessibility.  
- **Time Estimate:** 2 hours.

**STEP 11: [Final Performance Testing]**
- **Action:** Conduct a final crawl using Screaming Frog and validate all fixes in Google Search Console.  
- **Tools Needed:** Screaming Frog, Google Search Console.  
- **Success Criteria:** No critical or high-priority issues remaining; performance score remains above 80+.  
- **Common Pitfalls:** Failing to revalidate after changes causing false positives for errors.  
- **Time Estimate:** 1 hour.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:

1. **Primary Metric:** [Keyword Rankings] - Target: Improve from current average rank of X to top 10 for all primary keywords within 90 days.
2. **Secondary Metrics:**
   - Organic Traffic Growth: Increase by at least 30% month-over-month.
   - Crawl Budget Efficiency: Achieve >95% indexation rate.
3. **Long-term Metrics:**
   - Search Engine Ranking Positions (SERP) Stability: Maintain top 10 rankings for targeted keywords over 6 months.

#### Iterative Improvement Loop
1. Measure current performance against targets using Google Analytics and Search Console.  
2. Identify top improvement opportunities from the audit report.  
3. Implement changes prioritized by impact on SEO metrics.  
4. Re-measure after implementation to confirm improvements.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables
**1. Executive Summary**
- [ ] Current state vs. target state (e.g., average rank positions, organic traffic growth).  
- [ ] Key actions taken during audit and subsequent optimizations.  
- [ ] Results achieved with metrics tracked.

**2. Detailed Report**
- [ ] Methodology used for the technical SEO audit.  
- [ ] Findings from each phase of the audit (performance, crawlability, etc.).  
- [ ] Implementations completed as part of the optimization process.  
- [ ] Before/After comparisons using analytics tools.

**3. Maintenance Plan**
- **Ongoing Tasks:** Monthly performance monitoring, regular content updates, and periodic SEO health checks.  
- **Monitoring Schedule:** Weekly Google Analytics review; monthly Search Console alerts.  
- **Update Frequency:** Quarterly audit to ensure continued relevance and compliance with search engine guidelines.  
- **Contingency Procedures:** Plan for rapid response to critical errors or security incidents (e.g., SSL certificate expiration).

**4. Knowledge Transfer**
- [ ] Training materials for the team on SEO best practices and maintenance procedures.  
- [ ] Standard Operating Procedures (SOPs) for technical audits, including roles and responsibilities.  
- [ ] Troubleshooting Guide: Common issues identified during audits and how to resolve them.

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

#### How to Adapt This Template
1. **Replace all [BRACKETED] items** with profession-specific content (e.g., replace placeholder URLs with actual websites).
2. **Define 15 Critical Topics** based on the latest SEO trends and tools.
3. **Map Ultimate Goal to Measurable Outcomes** using SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound).
4. **Build Step-by-Step Workflow** from industry best practices, tool vendor guidelines, and expert methodologies.
5. **Include Latest 2024-2025 Practices**: Focus on AI integration for predictive SEO insights, automation of repetitive tasks using tools like SEMrush API, and enhanced analytics.

---

### RESEARCH SUB-AGENT CONFIGURATION

#### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "30 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Core Web Vitals]"
    focus: "Latest best practices for Core Web Vitals optimization"
    sources: ["Google Search Central Blog", "SEOmoz Forums"]
    deliverable: "Action plan to improve LCP, FID, and CLS scores"

  - agent_id: 2
    topic: "[Site Speed Optimization]"
    focus: "Performance optimization techniques and tools"
    sources: ["WebPageTest.org Articles", "Google Webmasters Blog"]
    deliverable: "Speed optimization report with prioritized actions"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to SEO outcomes
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

#### Final Checklist
Before marking the technical SEO audit as COMPLETE:

- [ ] **Ultimate Goal Achieved?** [Keyword rankings improved, traffic increased]  
- [ ] **All Metrics Met?** [Performance scores, crawlability metrics]  
- [ ] **Quality Validated?** [No critical errors remaining]  
- [ ] **Documentation Complete?** [All deliverables provided to stakeholders]  
- [ ] **Sustainability Ensured?** [Maintenance plan in place with clear ownership]

#### Continuous Improvement
- Document lessons learned from the audit process.  
- Update this template annually or after major search engine algorithm updates.  
- Share insights and findings with the SEO community through blogs, webinars, or conferences.

---

### TEMPLATE METADATA

**Last Updated:** [2024-10-01]  
**Version:** 1.0  
**Tested With:** SEO Specialist (Beginner to Intermediate)  
**Success Rate:** N/A (subjective based on industry standards)  
**Average Time to Goal:** Approximately 20-30 hours depending on website size.

---

