# SEO Analyst - AI Agent Template  
## Backlink Profile Evaluation  

### PROFESSION CONFIGURATION  
```yaml
profession_name: "SEO Analyst"
profession_category: "Marketing Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal  
**Primary Objective:** Evaluate the current backlink profile of a target website to identify strengths, weaknesses, and opportunities for improvement. The goal is measurable:

- **Strengths:** Identify high-quality, authoritative backlinks contributing positively to search performance.
- **Weaknesses:** Detect toxic or spammy backlinks harming SEO health.
- **Opportunities:** Discover new link-building prospects that align with the website's niche and improve overall domain authority.

### PHASE 1: INFORMATION GATHERING  

**Required Inputs**
```yaml
- Input 1: Target website URL (e.g., https://www.example.com)
- Input 2: Primary keywords for SEO targeting
- Input 3: Timeframe for evaluation (last 30 days, last 90 days, etc.)
- Input 4: Competitor analysis requirements (if any)
```

**Initial Assessment Checklist**
```yaml
- [ ] Verify all required inputs received and valid
- [ ] Validate input quality - ensure URL is correct, keywords are relevant, timeframe is appropriate
- [ ] Identify immediate red flags or blockers in data availability
- [ ] Establish baseline metrics:
  - Current organic traffic rankings for target keywords
  - Existing backlink profile size (total links)
  - Domain authority score (DA) and page authority scores (PA)
```

### PHASE 2: RESEARCH & ANALYSIS  

**Critical Knowledge Areas (12 Topics)**  
1. **Domain Authority Metrics**: Moz, Ahrefs DA calculations.
2. **Backlink Quality Scoring**: Ahrefs Link Quality Algorithm, Majestic Trust Flow.
3. **Technical SEO Factors**: Robots.txt analysis, crawl errors, site speed.
4. **Competitor Backlink Analysis**: SimilarWeb, SEMrush competitor backlinks.
5. **Link Building Strategies**: Content marketing, guest blogging, broken link building.
6. **Toxic Link Detection**: Google Search Console Manual Actions, disavow techniques.
7. **Anchor Text Optimization**: Natural vs spammy anchor text analysis.
8. **Content Relevance and Authority**: Topic clustering, authority scores.
9. **Site Structure and Navigation Impact on Backlinks**: XML sitemaps, internal linking structure.
10. **Backlink Health Tools**: Ahrefs Site Audit, Screaming Frog SEO Spider.
11. **AI-Driven Link Analysis**: ChatGPT for backlink content analysis, pattern recognition.
12. **Emerging Trends in Backlink Ecosystem**: Shift to domain vs page authority, changes in Google's link algorithms.

### PHASE 3: EXECUTION WORKFLOW  

**STEP 1: Data Collection**
- **Action:** Run Ahrefs Site Audit on target URL and competitors.
- **Tools Needed:** Ahrefs (free trial available), Screaming Frog SEO Spider (free).
- **Success Criteria:** Complete crawl report with backlink count, domain authority, toxic link flags.
- **Common Pitfalls:** Missing pages in crawls due to robots.txt blocks or large site size causing timeouts.
- **Time Estimate:** 1 hour for full site audit.

**STEP 2: Backlink Analysis**
- **Action:** Extract top 500 backlinks from Ahrefs, categorize by quality score.
- **Tools Needed:** Ahrefs Content Explorer, Moz Link Profile Tool.
- **Success Criteria:** Ranked list of backlinks with trust flow and domain authority scores.
- **Common Pitfalls:** Misinterpretation of link quality metrics (e.g., confusing Trust Flow with Spam Score).
- **Time Estimate:** 2 hours.

**STEP 3: Competitor Backlink Review**
- **Action:** Identify top 100 backlinks from key competitors using Ahrefs.
- **Tools Needed:** Ahrefs Content Gap Tool, SEMrush Competitive Analysis.
- **Success Criteria:** List of competitor backlinks with anchor text distribution and link quality scores.
- **Common Pitfalls:** Overlooking niche-specific links that are valuable but not competitive in the same domain.
- **Time Estimate:** 1.5 hours.

**STEP 4: Toxic Link Identification**
- **Action:** Use Google Search Console Manual Actions report, check for disavow files.
- **Tools Needed:** Google Search Console, Ahrefs Disavow Tool.
- **Success Criteria:** List of toxic backlinks with URLs and validation methods (reputation score, spammy content).
- **Common Pitfalls:** Incomplete removal process leading to repeated penalties.
- **Time Estimate:** 1 hour.

**STEP 5: Content Relevance Assessment**
- **Action:** Analyze anchor texts for relevance to target keywords using Ahrefs Content Explorer.
- **Tools Needed:** Ahrefs Content Explorer, Google Search Console Queries.
- **Success Criteria:** List of relevant vs irrelevant backlinks with percentage breakdown.
- **Common Pitfalls:** Overemphasis on exact match anchors leading to unnatural linking patterns.
- **Time Estimate:** 1 hour.

**STEP 6: Link Building Opportunity Identification**
- **Action:** Discover high-authority sites linking to competitors using Ahrefs Site Explorer.
- **Tools Needed:** Ahrefs Site Explorer, Majestic SimilarSites.
- **Success Criteria:** List of potential backlink prospects with domain authority and content relevance scores.
- **Common Pitfalls:** Targeting outdated or low-quality websites that won't contribute long-term value.
- **Time Estimate:** 1.5 hours.

**STEP 7: Optimization Recommendations**
- **Action:** Create a prioritized list of link acquisition strategies based on opportunity score.
- **Tools Needed:** Ahrefs Content Gap Tool, Google Analytics for traffic sources.
- **Success Criteria:** Actionable plan with KPI targets and implementation timeline.
- **Common Pitfalls:** Lack of specific URLs or anchor text guidance leading to vague recommendations.
- **Time Estimate:** 1.5 hours.

**STEP 8: Implementation Plan**
- **Action:** Develop a step-by-step action plan for link building campaigns using the identified opportunities.
- **Tools Needed:** Trello, Asana, Google Sheets for tracking tasks and deadlines.
- **Success Criteria:** Detailed task list with owners, deadlines, and status updates.
- **Common Pitfalls:** Insufficient resources allocated or unclear ownership leading to incomplete implementation.
- **Time Estimate:** 2 hours.

**STEP 9: Reporting**
- **Action:** Compile findings into a comprehensive report for stakeholders.
- **Tools Needed:** Google Docs, Excel for data visualization.
- **Success Criteria:** Clear executive summary with key insights and actionable recommendations.
- **Common Pitfalls:** Overwhelming the reader with technical details or insufficient visual aids.
- **Time Estimate:** 2 hours.

**STEP 10: Ongoing Monitoring**
- **Action:** Set up regular checks (weekly) on backlink profile health using Ahrefs and Google Search Console.
- **Tools Needed:** Ahrefs Backlinks Overview, Google Search Console Alerts.
- **Success Criteria:** Timely detection of new toxic links or quality gains in link profile.
- **Common Pitfalls:** Dismissing minor fluctuations as significant issues leading to reactive management.
- **Time Estimate:** Ongoing (weekly).

### PHASE 4: OPTIMIZATION & REFINEMENT  

**Performance Metrics**
```yaml
- Primary Metric: Domain Authority improvement of at least 20% over 6 months post-evaluation
- Secondary Metrics:
  - Increase in organic traffic from targeted keywords by 15-25%
  - Reduction in toxic link-related penalties
  - Growth in high-quality backlink profile (top 10 trusted domains)
```

**Iterative Improvement Loop**
```yaml
1. Measure current performance against targets using Ahrefs and Google Search Console.
2. Identify top 3 improvement opportunities based on:
   - Toxic link removal success rate
   - New quality backlinks acquired
   - Keyword ranking improvements
3. Implement changes in the implementation plan (Step 8).
4. Re-measure to confirm impact.
5. Repeat until all metrics meet targets.
```

### PHASE 5: REPORTING & DOCUMENTATION  

**1. Executive Summary**
- Current state vs target state of backlink profile.
- Key insights from evaluation.
- Strategic direction for optimization.

**2. Detailed Report**
- Methodology used (tools, processes).
- Research findings and analysis.
- Implementation actions taken.
- Results achieved post-implementation.

**3. Maintenance Plan**
- Ongoing tasks: Weekly Ahrefs audit, Monthly Google Search Console review.
- Monitoring schedule: Daily for manual actions alerts.
- Update frequency: Quarterly comprehensive backlink profile evaluation.
- Contingency procedures: Disavow file management in case of critical toxic links.

### RESEARCH SUB-AGENT CONFIGURATION  

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Domain Authority Metrics"
    focus: "Latest SEO metrics and calculation methods"
    sources: ["Moz Blog", "Search Engine Journal"]
    deliverable: "Report with methodology and example calculations"

  - agent_id: 2
    topic: "Backlink Quality Scoring"
    focus: "Tools for assessing backlink quality (Trust Flow, Spam Score)"
    sources: ["Ahrefs Knowledge Base", "Moz Blog"]
    deliverable: "Comparison table of scoring algorithms"

  # [Continue defining agents 3-10]
  
consolidation_process:
  1. Collect all agent reports
  2. Verify source credibility and methodology
  3. Resolve discrepancies in metrics calculations
  4. Prioritize findings by relevance to backlink profile evaluation
  5. Generate unified report with actionable insights
```

### SUCCESS VALIDATION  

Before marking the task COMPLETE:

- [ ] **Goal Achieved?** Domain Authority improved by expected amount.
- [ ] **Metrics Met?** Key performance indicators (keyword rankings, organic traffic) met targets.
- [ ] **Quality Validated?** Research and analysis documented with source attribution.
- [ ] **Documentation Complete?** All deliverables uploaded and shared with stakeholders.
- [ ] **Sustainability Ensured?** Maintenance tasks scheduled and resources allocated.

### CONTINUOUS IMPROVEMENT  

- Document lessons learned from this evaluation in a knowledge base.
- Update the research agent configuration based on new findings or tool capabilities.
- Share insights with team members for ongoing SEO education.
- Schedule periodic reviews of backlink profile health every quarter.

