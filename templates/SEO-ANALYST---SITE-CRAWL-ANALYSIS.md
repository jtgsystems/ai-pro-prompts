# SEO Analyst - AI Agent Template
## Site Crawl Analysis

### Success Definition (Measurable)
**Primary Objective:** Achieve a site crawl analysis score of 95%+ completeness for all URLs on the target website within 48 hours using only free tools.

**Success Criteria:**
- **Completeness Score:** ≥95% of total indexed pages successfully crawled
- **Error Rate:** ≤5% of crawled URLs result in errors (404, timeout)
- **Duplicate Content Detection:** All duplicate content identified and consolidated into single canonical URL
- **Technical Issues Identified:** Any critical technical issues resolved or documented

### Critical Knowledge Areas for SEO Analyst

1. **Core Technical SEO**
   - Understanding indexability signals
   - Robots.txt best practices
   - XML sitemap generation
   - Canonicalization strategies

2. **Site Structure & Navigation Analysis**
   - Identifying silos and logical groupings
   - Analyzing internal linking structure
   - Assessing URL hierarchy (1-3 levels deep)

3. **On-Page SEO Factors**
   - Keyword mapping for crawled pages
   - Content relevance analysis
   - Meta tag optimization
   - Image alt text compliance

4. **Technical Performance Metrics**
   - Page load speed impact on crawlability
   - Server response time thresholds
   - SSL/TLS security status

5. **Redirect Management**
   - Identifying and analyzing all redirect chains
   - Canonical URLs for post-redirect pages

6. **Mobile Friendliness & Responsive Design**
   - Checking if mobile site is fully crawled
   - Mobile vs desktop crawlability comparison

7. **Structured Data Implementation**
   - Validating JSON-LD implementation
   - Identifying schema errors affecting crawlers

8. **Security Implications for Crawling**
   - Identifying potential security issues impacting crawling (e.g., malware)
   - Implementing security measures to enhance crawl experience

9. **International SEO Considerations**
   - URL structure for international domains/subfolders
   - hreflang tag implementation and accuracy

10. **Crawl Budget Optimization**
    - Analyzing server logs for bot traffic patterns
    - Prioritizing critical pages for crawling depth

11. **Broken Link Identification**
    - Detecting 404 errors in sitemap vs crawled URLs
    - Creating a plan to fix broken links

12. **Competitor Crawl Analysis Benchmarking**
    - Comparing crawl scores against industry peers
    - Identifying best practices from competitors' crawls

### Detailed Execution Steps with Specific Actions

**STEP 1: [Foundation Setup] (2 hours)**
- **Action:** Define target website URL, set up Google Search Console property for the site
- **Tools Needed:** Browser (e.g., Chrome), Notepad++, Trello or Asana
- **Success Criteria:** Website URL confirmed and Google Search Console verified
- **Common Pitfalls:** Incorrect URL format, missing protocol (http vs https)
- **Time Estimate:** 1 hour

**STEP 2: [Generate Site Map] (3 hours)**
- **Action:** Create an XML sitemap using Screaming Frog or Sitebulb free version
- **Tools Needed:** Screaming Frog SEO Spider (free), Sitebulb (free, optional)
- **Success Criteria:** Sitemap file generated with all critical pages and correct URL structure
- **Common Pitfalls:** Missing `robots.txt` rules blocking some URLs
- **Time Estimate:** 2 hours

**STEP 3: [Initial Crawl] (4 hours)**
- **Action:** Run initial crawl using Screaming Frog or Sitebulb, focusing on main pages first
- **Tools Needed:** Screaming Frog SEO Spider, Sitebulb
- **Success Criteria:** >95% of URLs crawled with status codes <500
- **Common Pitfalls:** Timeout errors due to server speed issues
- **Time Estimate:** 3 hours

**STEP 4: [Error Analysis] (2 hours)**
- **Action:** Identify all error pages (404, timeout), prioritize fixes based on traffic impact
- **Tools Needed:** Exported crawl data from Screaming Frog or Sitebulb
- **Success Criteria:** All critical error pages identified and prioritized for action
- **Common Pitfalls:** Ignoring 404 errors leading to duplicate content issues
- **Time Estimate:** 1 hour

**STEP 5: [Duplicate Content Check] (2 hours)**
- **Action:** Identify duplicate URLs, consolidate into canonical version using Screaming Frog or Sitebulb
- **Tools Needed:** Screaming Frog SEO Spider, Sitebulb
- **Success Criteria:** All duplicates resolved and canonical tags correctly implemented
- **Common Pitfalls:** Overlooking dynamic URL parameters causing duplication
- **Time Estimate:** 1 hour

**STEP 6: [Technical Performance Review] (2 hours)**
- **Action:** Analyze page load speed, server response time for top 100 URLs using Google PageSpeed Insights
- **Tools Needed:** Google PageSpeed Insights
- **Success Criteria:** >80% of pages achieve performance score ≥80
- **Common Pitfalls:** Ignoring mobile performance issues affecting crawlability
- **Time Estimate:** 2 hours

**STEP 7: [Redirect & Canonical Analysis] (1.5 hours)**
- **Action:** Verify all redirects (302, 301), ensure canonical URLs correctly set for post-redirect pages
- **Tools Needed:** Screaming Frog SEO Spider
- **Success Criteria:** All redirects properly implemented with correct targets
- **Common Pitfalls:** Redirect loops causing crawl delays
- **Time Estimate:** 1.5 hours

**STEP 8: [Security & Crawl Accessibility Check] (1 hour)**
- **Action:** Verify no security blocks preventing crawling, check for malware on site
- **Tools Needed:** VirusTotal API integration, Burp Suite community edition (free)
- **Success Criteria:** Site accessible to crawlers with no security blockages
- **Common Pitfalls:** Ignoring 403/404 errors due to misconfigured `.htaccess`
- **Time Estimate:** 1 hour

**STEP 9: [Competitor Crawl Comparison] (2 hours)**
- **Action:** Compare crawl results with top competitors using similar tools, identify gaps and opportunities
- **Tools Needed:** Screaming Frog SEO Spider, Sitebulb
- **Success Criteria:** Identified at least 3 actionable improvements based on competitor analysis
- **Common Pitfalls:** Overlooking differences in site architecture between domains
- **Time Estimate:** 2 hours

**STEP 10: [Final Validation & Reporting] (1 hour)**
- **Action:** Run final crawl, validate all previous steps, compile comprehensive report
- **Tools Needed:** Screaming Frog SEO Spider, Trello or Asana for tracking
- **Success Criteria:** Report completed with complete audit findings and action plan
- **Common Pitfalls:** Skipping validation step leading to incomplete analysis
- **Time Estimate:** 1 hour

### Tools & Software Stack (2024-2025)

**Primary Tools (Free):**
1. **Screaming Frog SEO Spider** - Crawls, analyzes HTML source, checks for technical issues
2. **Sitebulb Browser-based Crawler** - Real-time crawling with extensive reporting
3. **Google Search Console** - Tracks indexing status and uncrawled URLs
4. **GTmetrix** - Performance insights from multiple locations globally

**Alternative / Premium Tools (Paid):**
1. **Ahrefs Site Audit** (paid subscription)
2. **SEMrush Crawl Diagnostic** (pro features)
3. **MOZ Pro's Link Explorer** - For technical link analysis
4. **Wappalyzer** - Detects technologies used on the site

### Troubleshooting Common Issues

**Issue 1: Indexation Errors**
- **Cause:** `robots.txt` disallowing critical pages, server errors (500)
- **Solution:** Verify robots.txt is correctly structured, check server logs for errors
- **Prevention:** Regularly audit robots.txt and set up alerts for new blocks in Search Console

**Issue 2: Timeout Errors**
- **Cause:** High latency on certain URLs or IP rate limiting by web host
- **Solution:** Use proxies to bypass local timeout issues, optimize site performance
- **Prevention:** Conduct load testing before critical releases

**Issue 3: Duplicate Content Issues**
- **Cause:** Canonicalization problems, different URL parameters serving same content
- **Solution:** Ensure canonical tags are correct, use URL parameter handling in Screaming Frog/ Sitebulb
- **Prevention:** Implement consistent URL structure and schema markup

**Issue 4: Security Blocks**
- **Cause:** Malware protection software blocking crawls, IP bans
- **Solution:** Configure crawler to bypass security scans, check .htaccess/.nginx rules
- **Prevention:** Regularly scan site for malware using VirusTotal API integration

### Realistic Timeline to Achieve Site Crawl Analysis (2024-2025)

**Week 1: Foundation & Initial Setup**
- Define project scope and success criteria
- Verify target website URL and set up Search Console
- Generate XML sitemap using Screaming Frog or Sitebulb

**Week 2: First Full Crawl & Error Identification**
- Run initial crawl focusing on main pages
- Identify all error URLs (404, timeout) and prioritize fixes
- Analyze duplicate content and canonicalization issues

**Week 3: Technical Performance Review & Redirects**
- Evaluate page load speed for top critical pages using GTmetrix/Pulseway
- Verify correct implementation of redirects and canonical tags
- Check for security blocks preventing crawling

**Week 4: Competitor Benchmarking, Validation & Reporting**
- Compare findings with competitors' sites using similar tools
- Run final crawl to validate all issues resolved
- Compile comprehensive report documenting all metrics, actions taken, and recommendations

### Final Checklist Before Project Completion

- [ ] All critical URLs (≥95% of total) successfully crawled
- [ ] Error rate ≤5% across all crawls
- [ ] Duplicate content fully consolidated with correct canonical tags
- [ ] Technical performance scores ≥80 for top pages in both mobile and desktop views
- [ ] All security blocks properly addressed, site accessible to crawlers
- [ ] Final crawl report generated and shared with stakeholders
- [ ] Action plan documented for any remaining issues or improvements

**Remember:** This template is a living document. Update it regularly based on new tools, methodologies, and best practices in the SEO field as they emerge in 2024-2025.

