# Amazon FBA Specialist - AI Agent Template

## Keyword Research

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve keyword research as a core function for Amazon FBA Specialists.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Amazon FBA Specialist"
profession_category: "E-commerce/Marketing"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Achieve top rankings for target products on Amazon using optimized keyword research, with measurable improvements in sales and product visibility.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Target Product Name(s) or Category (e.g., "Wireless Earbuds", "Men's Running Shoes")
   - Format: Text
   - Validation: Ensure product names are valid Amazon UPC/EAN identifiers or clearly defined categories.

2. **Input 2:** Desired Search Intent (Commercial, Niche Research)
   - Format: Enum ("commercial", "niche")
   - Validation: Must align with business strategy.

3. **Input 3:** Target Market (Geography, Language, Currency)
   - Format: Text
   - Validation: Match Amazon marketplace locale settings.

4. **Input 4:** Budget and Resources Available
   - Format: Numeric or Enum ("Limited", "Moderate", "Extensive")
   - Validation: Ensure resources align with available budget for tools and software.

5. **Input 5 (Optional):** Historical Performance Data (Current Sales, Click-Through Rate)
   - Format: JSON/CSV
   - Validation: If provided, must be in consistent format.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (15 Topics)

**Topic 1:** Keyword Intent Analysis  
- **Research Focus:** Understand commercial vs. informational search intents.
- **Target Sources:** Amazon product pages, Google Trends, competitor analysis tools.
- **Deliverable:** Categorization of keywords by intent.

**Topic 2:** Competitor Keyword Mapping  
- **Research Focus:** Identify top-ranking competitors' keywords.
- **Target Sources:** SEMrush, Ahrefs (free alternatives like Moz or Ubersuggest), Amazon product pages.
- **Deliverable:** List of competitor keywords and their rankings.

**Topic 3:** Search Volume Trends  
- **Research Focus:** Analyze search volume trends for target keywords over the last 6 months.
- **Target Sources:** Google Keyword Planner, free alternatives like AnswerThePublic or Ubersuggest.
- **Deliverable:** Time-series analysis of keyword search volumes.

**Topic 4:** Amazon Specific Search Queries  
- **Research Focus:** Identify long-tail and session-specific queries on Amazon (e.g., "Wireless Earbuds under $50").
- **Target Sources:** Amazon product pages, customer reviews, Q&A sections.
- **Deliverable:** List of Amazon-specific search terms.

**Topic 5:** Seasonality and Trend Analysis  
- **Research Focus:** Determine seasonal trends for target keywords.
- **Target Sources:** Google Trends, social media analytics tools like Brandwatch or BuzzSumo.
- **Deliverable:** Seasonal keyword performance chart.

**Topic 6:** Keyword Difficulty Assessment  
- **Research Focus:** Evaluate difficulty of ranking for selected keywords based on competition level and search volume.
- **Target Sources:** Moz, Ahrefs (free alternatives), Google Ads Keyword Planner.
- **Deliverable:** Scoring matrix of keywords by difficulty.

**Topic 7:** Content Gap Analysis  
- **Research Focus:** Identify gaps in existing content that your product can fill to rank better.
- **Target Sources:** Competitor analysis, SEO auditing tools like Screaming Frog or Site Reliability Tools.
- **Deliverable:** List of content gaps and opportunities for optimization.

**Topic 8:** User Experience (UX) Considerations  
- **Research Focus:** Align keywords with user experience on Amazon to improve conversion rates.
- **Target Sources:** Amazon best practices, UX research tools like Hotjar or Crazy Egg.
- **Deliverable:** UX recommendations aligned with keyword strategy.

**Topic 9:** Technical SEO for Listings  
- **Research Focus:** Optimize product listing metadata (title, bullet points, images) to rank better.
- **Target Sources:** SEO best practices, Amazon SEO guides.
- **Deliverable:** Checklist of technical SEO improvements for listings.

**Topic 10:** Voice Search Optimization  
- **Research Focus:** Prepare keywords for voice search trends (e.g., "how to...").
- **Target Sources:** Google Home Insights, smart speaker usage data.
- **Deliverable:** List of long-tail voice-search keywords.

**Topic 11:** Localized Keywords  
- **Research Focus:** Identify local variations and language-specific terms relevant to target markets.
- **Target Sources:** Google Autocomplete, regional forums or social media groups.
- **Deliverable:** Localization strategy for keyword targeting.

**Topic 12:** Sponsored Product Keyword Analysis  
- **Research Focus:** Analyze keywords used in sponsored product ads for competitive analysis.
- **Target Sources:** Amazon Advertising Console, SEMrush.
- **Deliverable:** Competitive benchmark report for sponsored keywords.

**Topic 13:** Brand and Product Keywords  
- **Research Focus:** Identify brand-specific and product-specific terms that drive conversions.
- **Target Sources:** Customer reviews, social media mentions, SEO tools.
- **Deliverable:** List of high-performing brand/product keywords.

**Topic 14:** Competitor Backlink Analysis  
- **Research Focus:** Analyze backlinks from competitor websites to understand their link-building strategies.
- **Target Sources:** Ahrefs (free alternatives like Moz Link Index).
- **Deliverable:** Backlink profile analysis for competitors.

**Topic 15:** Market Entry Strategies Based on Keyword Trends  
- **Research Focus:** Develop entry or exit strategies based on keyword trend analysis and competitive landscape.
- **Target Sources:** Industry reports, competitor activity monitoring tools.
- **Deliverable:** Strategic recommendations for market positioning.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Data Collection**
- **Action:** Gather product name(s), search intent, target market, and budget details.
- **Tools Needed:** Structured form input or API call to Amazon catalog.
- **Success Criteria:** All required inputs are collected accurately and validated.
- **Common Pitfalls:** Incorrect product identifiers leading to wrong data sets.
- **Time Estimate:** 10 minutes

**STEP 2: Keyword Discovery**
- **Action:** Use tools like Google Trends, Ahrefs (free alternatives), or SEMrush to identify high-volume keywords related to target products.
- **Tools Needed:** Google Trends API, Ahrefs/SEMrush free trial, keyword research plugins for browsers.
- **Success Criteria:** At least 50 relevant keywords identified with search volume > 500/month.
- **Common Pitfalls:** Overlooking long-tail keywords that are high conversion but low volume.
- **Time Estimate:** 2 hours

**STEP 3: Competitor Analysis**
- **Action:** Identify top-ranking competitors on Amazon and analyze their keyword usage, listing optimization, and backlink profile.
- **Tools Needed:** SEMrush, Ahrefs (free alternatives), Amazon competitor checker tools, Moz Link Index.
- **Success Criteria:** Top 10 keywords from competitors identified with ranking positions captured.
- **Common Pitfalls:** Missing third-tier competitors who could outrank larger players.
- **Time Estimate:** 2 hours

**STEP 4: Keyword Prioritization**
- **Action:** Rank discovered keywords based on commercial intent, search volume, competition level, and relevance to product features.
- **Tools Needed:** Spreadsheet with custom scoring matrix or SEO software like BrightLocal for ranking analysis.
- **Success Criteria:** Top 20 prioritized keywords selected for further action.
- **Common Pitfalls:** Bias towards high-volume keywords without considering conversion potential.
- **Time Estimate:** 1 hour

**STEP 5: Content Strategy Development**
- **Action:** Create a content plan to incorporate top-ranked keywords into product listings, blog posts, and ads.
- **Tools Needed:** Keyword clustering software like LS Insights, content management system (CMS) for listing updates.
- **Success Criteria:** Detailed content calendar with keyword integration plans mapped out.
- **Common Pitfalls:** Overstuffing keywords leading to SEO penalties.
- **Time Estimate:** 2 hours

**STEP 6: Technical Optimization**
- **Action:** Optimize Amazon product pages, titles, bullet points, and backend descriptions using prioritized keywords.
- **Tools Needed:** SEO optimization tools like Yoast SEO for WordPress or specialized Amazon SEO software (e.g., MaxCDN).
- **Success Criteria:** All key areas of the product listing are optimized with target keywords.
- **Common Pitfalls:** Keyword density too high leading to unnatural phrasing.
- **Time Estimate:** 4 hours

**STEP 7: Campaign Setup**
- **Action:** Set up Amazon Sponsored Products campaign using prioritized keywords and bid strategies based on competition analysis.
- **Tools Needed:** Amazon Advertising Console, Google Ads for keyword bidding strategies.
- **Success Criteria:** Active campaigns with targeted keywords running across relevant marketplaces.
- **Common Pitfalls:** Overbidding leading to wasted ad spend.
- **Time Estimate:** 2 hours

**STEP 8: Monitoring and Iteration**
- **Action:** Implement tracking mechanisms (UTM parameters, conversion pixels) to monitor keyword performance. Adjust bids and content based on data insights.
- **Tools Needed:** Google Analytics, Amazon Ads Manager, UTM builder tools like Bitly.
- **Success Criteria:** Keyword ranking improvements tracked with at least 15% increase in sales or traffic within the first month.
- **Common Pitfalls:** Lack of regular monitoring leading to stagnation in performance.
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Keyword Rankings  
   - Target: Top 3 positions for at least 75% of targeted keywords within the first quarter.
   - Measurement Method: Manual check and SEO tool rankings.

2. **Secondary Metrics:**  
   - Sales Increase: Minimum 20% growth in sales from keyword-optimized products.
   - Click-Through Rate (CTR): Achieve average CTR > 3% across sponsored ads.
   - Conversion Rate: Target conversion rate > 5%.

### Iterative Improvement Loop
1. **Measure Current Performance:** Use SEO tools and Amazon analytics to assess current rankings and sales impact.
2. **Identify Top Opportunities:** Prioritize keywords with the lowest rank or highest potential for growth.
3. **Implement Changes:** Adjust bids, refresh content, or test new ad variations.
4. **Re-measure Results:** After changes, re-evaluate performance against targets.
5. **Repeat Cycle:** Continue refining based on data-driven insights.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- Current State vs. Target State
- Key Actions Taken (e.g., "Identified top 50 keywords", "Optimized 10 product listings")
- Results Achieved (e.g., "Top rankings for 30 keywords")

**2. Detailed Report**
- Methodology Overview: Keyword research process, tools used, competitor analysis framework.
- Findings Summary: Key insights from keyword analysis and competitive landscape.
- Recommendations: Actionable steps prioritized by impact.
- Implementation Timeline: Gantt chart or roadmap of tasks.

**3. Maintenance Plan**
- Ongoing Tasks: Monthly keyword monitoring, bid adjustments, content refresh schedule.
- Monitoring Schedule: Weekly performance reviews using SEO and Amazon analytics tools.
- Update Frequency: Quarterly review of competitive landscape and search trends.
- Contingency Procedures: Steps to recover from sudden ranking drops or algorithm updates.

**4. Knowledge Transfer**
- Training Materials: Checklist for keyword research best practices, SOPs for content optimization.
- Standard Operating Procedures (SOPs): Documented processes for ongoing SEO tasks.
- Best Practices Documentation: Updated library of Amazon SEO strategies and competitor analysis frameworks.
- Troubleshooting Guide: FAQs on common issues like ranking fluctuations or ad policy changes.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "2 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Keyword Intent Analysis]"
    focus: "Commercial vs. Niche Research"
    sources: ["Amazon product reviews", "Google Trends"]
    deliverable: "Intent categorization report with sample queries"

  - agent_id: 2
    topic: "[Competitor Keyword Mapping]"
    focus: "Top-ranking competitor analysis"
    sources: ["SEMrush", "Ahrefs (free alternative)"]
    deliverable: "Competitor keyword list with rankings and gaps"

  # [Continue for agents 3-15]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings across agents
  3. Resolve conflicts by source authority
  4. Prioritize keywords based on commercial intent and competition
  5. Generate unified keyword research report
```

---

## SUCCESS VALIDATION

### Final Checklist

Before marking the Amazon FBA Specialist task as COMPLETE:

- [ ] **Keyword Rankings Achieved?** [Target ranking positions reached]
- [ ] **Sales Impact Verified?** [Sales metrics meet or exceed targets]
- [ ] **User Experience Meets Standards?** [Product listings optimized for conversion and compliance with Amazon guidelines]
- [ ] **Competitive Edge Established?** [Market position validated against top competitors]
- [ ] **Budget Compliance Confirmed?** [All spend aligned with allocated resources]

### Continuous Improvement
- Document all optimizations made during the campaign.
- Update keyword research methods based on emerging trends or tool capabilities.
- Share insights gained with team members for collective growth.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Amazon Seller Central, Google Trends, SEMrush (Free Alternatives: Ahrefs Free Version)  
**Success Rate:** [To be determined after multiple implementations]  
**Average Time to Goal:** 4 weeks

---

*This template should now be ready for implementation by an Amazon FBA Specialist aiming to achieve advanced keyword research capabilities.*

