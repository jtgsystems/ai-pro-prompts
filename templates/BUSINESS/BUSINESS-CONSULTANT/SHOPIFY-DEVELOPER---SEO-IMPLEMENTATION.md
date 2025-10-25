# Shopify Developer - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Shopify Developer"
profession_category: "Technology / E-commerce Development"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Successfully implement SEO best practices that will elevate the Shopify store's search engine ranking for targeted keywords, leading to a minimum 30% increase in organic traffic within three months of implementation.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** [Primary Target Keywords] - List of top 10-15 target keywords with search volume and difficulty scores (Format: Text/URL)
2. **Input 2:** [Existing SEO Setup] - Current SEO status including meta tags, alt texts, structured data (Format: JSON/XML snippets)
3. **Input 3:** [Performance Metrics] - Current organic traffic numbers, bounce rate, conversion rate from search results (Format: Google Analytics reports)

### Initial Assessment Checklist
- [ ] Verify all required inputs received and correctly formatted.
- [ ] Validate input quality and completeness through keyword research tools.
- [ ] Identify immediate red flags such as missing meta descriptions or structured data errors.
- [ ] Establish baseline metrics for current SEO performance.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Shopify SEO Fundamentals
- Research Focus: Core SEO principles specific to Shopify themes and app ecosystem.
- Target Sources: Shopify official documentation, E-commerce SEO blogs (2024 editions).

**Topic 2:** Keyword Optimization Strategies
- Research Focus: How to leverage long-tail keywords effectively in product pages and categories.
- Target Sources: Google Keyword Planner, SEMrush (free tier), Shopify blog posts.

**Topic 3:** Technical SEO for Shopify Stores
- Research Focus: Best practices for site speed optimization, mobile-friendliness, SSL certificates, and canonical tags on Shopify.
- Target Sources: GTmetrix, Lighthouse, Shopify theme guides.

**Topic 4:** Meta Tags & Schema Markup
- Research Focus: Detailed schema implementation including Product, Article, FAQ schemas.
- Target Sources: JSON-LD reference docs, Google Search Console recommendations.

**Topic 5:** Image SEO
- Research Focus: Alt text optimization and image compression techniques unique to Shopify stores.
- Target Sources: Adobe Photoshop tutorials for web, TinyPNG (free).

**Topic 6:** Content Strategy for SEO
- Research Focus: How to create SEO-friendly content that appeals to both search engines and customers.
- Target Sources: Case studies from top Shopify brands.

**Topic 7:** Link Building Strategies
- Research Focus: How to acquire high-quality backlinks specific to the e-commerce niche on Shopify.
- Target Sources: Outreach templates, broken link building tools (e.g., BuzzSumo free tier).

**Topic 8:** E-commerce SEO Analytics Tools
- Research Focus: The latest analytics platforms for tracking keyword performance and site health.
- Target Sources: Google Search Console API (free), Ahrefs (limited free trial), SEMrush.

**Topic 9:** Local SEO Implementation on Shopify
- Research Focus: How to optimize for local search queries, especially if the store has physical locations or services.
- Target Sources: Yelp integration guides, Google My Business updates.

**Topic 10:** Mobile-First Indexing Considerations
- Research Focus: Ensuring Shopify sites are optimized for mobile-first indexing by search engines.
- Target Sources: Mobile-Friendly Test tool (Google), responsive design guidelines in Shopify themes.

**Topic 11:** Performance Optimization Techniques
- Research Focus: CDN integration, image optimization plugins, and other performance tweaks specific to Shopify stores.
- Target Sources: Cloudflare free tier docs, ImageOptim for Mac (free).

**Topic 12:** Emerging SEO Trends in E-commerce (2024-2025)
- Research Focus: AI-driven SEO tools, voice search optimization, and other new trends impacting e-commerce sites.
- Target Sources: Moz Blog, Search Engine Journal articles on AI SEO.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy prioritizing actions by impact and ease of implementation.
2. Identify conflicts in best practices (e.g., different opinions on schema usage) and resolve them based on the latest industry standards.
3. Create master action plan with timelines for execution.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Foundation Setup]**
- **Action:** Conduct a comprehensive site audit using tools like Screaming Frog, Google Search Console, and GTmetrix to identify technical SEO issues.
- **Tools Needed:** Screaming Frog (free trial), GTmetrix, Google Search Console, Lighthouse.
- **Success Criteria:** Completion of the site audit report with all critical errors fixed.
- **Common Pitfalls:** Ignoring crawl errors or failing to fix SSL certificate warnings.
- **Time Estimate:** 2 weeks.

**STEP 2: [Initial Implementation]**
- **Action:** Update all product pages and category listings with optimized meta descriptions, titles, alt tags for images, and structured data using JSON-LD schema.
- **Tools Needed:** Shopify theme editor or custom code (e.g., CodePen), Yoast SEO plugin (free).
- **Success Criteria:** 90% of product pages have valid structured data; all pages pass Google’s Rich Results Test.
- **Common Pitfalls:** Typos in alt text, missing schema on important pages.
- **Time Estimate:** 1 week.

**STEP 3: [Core Work]**
- **Action:** Optimize site speed by compressing images, enabling lazy loading, and ensuring SSL is correctly implemented. Also, configure GSC for better crawling signals.
- **Tools Needed:** TinyPNG (free), ImageOptim (Mac free), Shopify’s built-in image optimization features, Cloudflare (free tier).
- **Success Criteria:** Site speed score > 80 on Lighthouse; all pages properly indexed in Google Search Console.
- **Common Pitfalls:** Overlooking lazy loading settings or misconfiguring SSL.
- **Time Estimate:** 1 week.

**STEP 4: [Keyword Implementation]**
- **Action:** Implement targeted keyword optimization across product descriptions, blog posts, and category pages based on the list of top keywords.
- **Tools Needed:** Shopify CMS editor, SEO plugins like All in One SEO (free tier), Google Keyword Planner (free).
- **Success Criteria:** Target keywords appear in the first 100 words of content; improved search rankings for at least 5 target keywords.
- **Common Pitfalls:** Stuffing keywords unnaturally or neglecting competitor analysis.
- **Time Estimate:** Ongoing, but initial focus should be on top 10 keywords.

**STEP 5: [Structured Data Setup]**
- **Action:** Add structured data to the site schema using JSON-LD. Focus on Product and Article types for better visibility in search results.
- **Tools Needed:** JSON-LD snippets provided by Schema Markup Generator, Shopify theme’s HTML tags area.
- **Success Criteria:** All major product pages show rich snippets in Google Search Console; no validation errors from Schema Markup Validator.
- **Common Pitfalls:** Incorrectly specifying URLs or fields in the schema markup.
- **Time Estimate:** 2 days.

**STEP 6: [Image SEO]**
- **Action:** Optimize all images for web using TinyPNG or ImageOptim. Add alt tags that include primary keywords and are descriptive.
- **Tools Needed:** TinyPNG, ImageOptim, Shopify theme editor.
- **Success Criteria:** All images have reduced file sizes by at least 30% without loss of quality; alt text includes target keywords.
- **Common Pitfalls:** Forgetting to optimize product upload images or using generic alt texts.
- **Time Estimate:** Ongoing but should be completed within first month.

**STEP 7: [Content Strategy Execution]**
- **Action:** Publish high-quality, SEO-friendly blog posts that target long-tail keywords and include internal linking to product pages.
- **Tools Needed:** Shopify CMS, keyword research tools like Ahrefs free tier, Google Trends for identifying trending topics.
- **Success Criteria:** At least 5 new blog posts published monthly; each post ranks for at least one primary keyword.
- **Common Pitfalls:** Lack of a content calendar or publishing low-quality content.
- **Time Estimate:** Monthly.

**STEP 8: [Link Building Strategy]**
- **Action:** Develop a link building plan focusing on quality backlinks from relevant blogs, directories, and e-commerce sites.
- **Tools Needed:** Ahrefs (free tier), BuzzSumo free trial, Google Alerts for brand mentions.
- **Success Criteria:** At least 10 high-quality backlinks acquired in the first month; improved domain authority score.
- **Common Pitfalls:** Buying links or using spammy tactics.
- **Time Estimate:** Ongoing effort.

**STEP 9: [Local SEO Optimization]**
- **Action:** Optimize Google My Business listing, local citations, and Google Maps integration for Shopify store locations.
- **Tools Needed:** Google My Business dashboard (free), Yext (free tier).
- **Success Criteria:** Correct business hours, accurate contact info; improved visibility in local search results.
- **Common Pitfalls:** Incorrect address data or missed GMB listing completion tasks.
- **Time Estimate:** 1 week.

**STEP 10: [Monitoring & Reporting]**
- **Action:** Set up Google Analytics and Search Console to monitor organic traffic, rankings, and user engagement metrics.
- **Tools Needed:** Google Analytics, Google Search Console, SEMrush (free tier), GTmetrix.
- **Success Criteria:** At least a 30% increase in organic search traffic within three months; improved bounce rate and conversion rates from search results.
- **Common Pitfalls:** Ignoring negative SEO signals or failing to adjust strategies based on performance data.
- **Time Estimate:** Continuous monitoring.

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After Step X] - Verify that all meta tags are correctly implemented and no crawl errors exist in Screaming Frog reports.
- **Checkpoint 2:** [After Step Y] - Validate structured data using Google’s Rich Results Test; ensure no validation errors.
- **Checkpoint 3:** [After Step Z] - Confirm keyword rankings for top target keywords have improved at least 10% compared to baseline.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Organic Traffic Increase
   - Target: Minimum 30% increase in organic search traffic within three months.
   - Measurement Method: Google Analytics tracking of session data from organic search.

2. **Secondary Metrics:**
   - Keyword Rankings: Target a top-10 ranking for at least 5 primary keywords.
   - Bounce Rate: Reduce bounce rate from search results by 15%.
   - Conversion Rate: Increase conversion rate from search traffic by 5%.

3. **Long-term Metrics:**
   - Domain Authority Growth: Aim for a 25% increase in domain authority within six months.
   - Mobile Usability Score: Maintain above 80 on Google’s Mobile-Friendly Test.

### Iterative Improvement Loop
1. Measure current performance against targets using the defined metrics.
2. Identify top improvement opportunities through data analysis (e.g., underperforming keywords, high bounce rates).
3. Implement changes based on insights (e.g., refine content strategy, add missing structured data).
4. Re-measure to confirm improvements and adjust strategies as needed.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current SEO Status: [Baseline metrics from Google Analytics and Search Console]
- Target Metrics: [30% traffic increase, top-10 rankings for key terms]
- Key Actions Taken: [Brief overview of implemented changes]

**2. Detailed Report**
- Methodology Used: [Keyword research, technical audits, content strategy]
- Research Findings: [Summarized insights from each critical topic]
- Implementation Details: [Step-by-step execution process with screenshots and logs]
- Performance Metrics: [Before/after comparison tables for traffic, rankings, etc.]

**3. Maintenance Plan**
- Ongoing Tasks: Monthly SEO audit, content updates, link building monitoring.
- Monitoring Schedule: Weekly checks on Google Search Console; monthly review of analytics reports.
- Update Frequency: Adjustments every 4 weeks based on performance data.

**4. Knowledge Transfer**
- Training Materials: Checklist for ongoing SEO tasks; keyword research guide.
- SOPs: Step-by-step processes for updating meta tags and structured data.
- Troubleshooting Guide: Common SEO issues in Shopify and how to resolve them.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Shopify SEO Fundamentals]"
    focus: "Latest best practices for Shopify-specific SEO"
    sources: ["Shopify official docs", "Industry blogs"]
    deliverable: "Actionable insights with examples"

  - agent_id: 2
    topic: "[Keyword Optimization Strategies]"
    focus: "How to use keywords effectively in product pages and categories"
    sources: ["Google Keyword Planner", "SEMrush free tier"]
    deliverable: "List of target keywords with difficulty scores"

  # [Continue for agents 3-12]
```

### Consolidation Process
1. Collect all agent reports.
2. Synthesize findings into unified strategy.
3. Prioritize by impact and feasibility.
4. Generate master action plan.

---

## SUCCESS VALIDATION

### Final Checklist

Before marking this task as COMPLETE:

- [ ] **Primary Objective Achieved?** SEO metrics met the 30% traffic increase target.
- [ ] **All Metrics Met?** Key performance indicators improved as expected.
- [ ] **Quality Validated?** All implemented changes meet industry standards and best practices.
- [ ] **Documentation Complete?** All deliverables are documented, reviewed, and signed off by stakeholders.
- [ ] **Sustainability Ensured?** Ongoing maintenance tasks and a monitoring plan are in place.

### Continuous Improvement
- Document lessons learned from the SEO implementation process.
- Schedule quarterly reviews to adjust strategies based on performance data.
- Share insights with the team through workshops or internal blogs.
- Update the template annually to reflect new trends and tools.

---

## TEMPLATE METADATA

**Last Updated:** [Current Date]
**Version:** 1.0
**Tested With:** Shopify Developer (Beginner/Intermediate)
**Success Rate:** [Track completion based on defined metrics]
**Average Time to Goal:** [Based on typical project timelines]

---

