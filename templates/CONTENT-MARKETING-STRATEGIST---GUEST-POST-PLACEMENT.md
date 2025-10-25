# Content Marketing Strategist - AI Agent Template

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Content Marketing Strategist"
profession_category: "Marketing"
experience_level: "Beginner/Intermediate"
```

## PHASE 1: INFORMATION GATHERING

### Required Inputs
1. **Target Publication Platform:** List of websites/blogs open to guest posts (e.g., Medium, Forbes, IndustryWeek)
2. **Audience Profile:** Demographics and psychographics of the target readership
3. **Topic Interest:** Core themes your content will focus on (e.g., AI in marketing, Content strategy frameworks)
4. **Content Type:** Blog post length preferences, format (long-form article, listicle, case study)

### Initial Assessment Checklist
- [ ] Verify all required inputs received and are valid.
- [ ] Validate input quality by checking:
  - Target platforms have active submission guidelines.
  - Audience profiles align with your content strategy.
- [ ] Establish baseline metrics such as current backlink profile or social engagement.

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Content Strategy Frameworks
- **Research Focus:** Latest frameworks for creating engaging guest posts.
- **Target Sources:** Content marketing blogs, academic papers on content strategy.

**Topic 2:** SEO Best Practices for Guest Posts
- **Research Focus:** On-page and off-page SEO tactics specific to guest posting in 2024.
- **Target Sources:** Moz, Search Engine Journal updates.

**Topic 3:** Audience Engagement Tactics
- **Research Focus:** How to structure content to maximize reader interaction (comments, shares).
- **Target Sources:** Social media analytics reports, engagement studies.

**Topic 4:** Platform-Specific Content Guidelines
- **Research Focus:** Submission requirements for each target platform.
- **Target Sources:** Publisher guidelines pages.

**Topic 5:** Guest Post Payment Structures
- **Research Focus:** Trends in payment for guest posts across different platforms.
- **Target Sources:** Industry reports, freelance marketplaces data.

**Topic 6:** Content Curation Strategies
- **Research Focus:** How to curate existing content into guest post pitches effectively.
- **Target Sources:** Curator case studies, tools like Feedly.

**Topic 7:** Brand Alignment Techniques
- **Research Focus:** Aligning guest posts with brand messaging and values.
- **Target Sources:** Marketing blogs, corporate communications guidelines.

**Topic 8:** Call-to-Action (CTA) Optimization
- **Research Focus:** Best practices for incorporating CTAs in guest post content without being salesy.
- **Target Sources:** Conversion rate optimization studies.

**Topic 9:** Distribution Channels for Guest Posts
- **Research Focus:** Effective channels to distribute and promote guest posts post-publication.
- **Target Sources:** Social media analytics, email marketing platforms.

**Topic 10:** Analytics Tools for Measuring Impact
- **Research Focus:** Tools that track performance of guest posts in terms of traffic, engagement, backlinks.
- **Target Sources:** Google Analytics, SEMrush reports.

**Topic 11:** Ethical Considerations in Guest Posting
- **Research Focus:** Best practices to maintain authenticity and avoid plagiarism.
- **Target Sources:** Ethical guidelines from professional organizations.

**Topic 12:** Legal Aspects of Guest Posting
- **Research Focus:** Terms of service compliance, copyright considerations.
- **Target Sources:** Platform policies, legal resources.

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Platform Research & Outreach]**
- **Action:** Compile a list of suitable platforms based on audience profile and platform-specific guidelines.
- **Tools Needed:** Google Sheets for organizing data; LinkedIn Sales Navigator for outreach tracking.
- **Success Criteria:** At least 10 potential platforms identified with submission details.
- **Common Pitfalls:** Ignoring submission guidelines or not verifying platform active status.
- **Time Estimate:** 3 days

**STEP 2: [Content Ideation & Planning]**
- **Action:** Brainstorm and prioritize content topics based on relevance to audience and platform trends.
- **Tools Needed:** Notion for brainstorming; Trello for task tracking.
- **Success Criteria:** 5 top content ideas selected with brief outlines.
- **Common Pitfalls:** Overlooking seasonal or trending topics.
- **Time Estimate:** 2 days

**STEP 3: [Pitch Creation]**
- **Action:** Draft tailored pitches highlighting value propositions, platform alignment, and unique angles.
- **Tools Needed:** Canva for professional templates; Hemingway Editor for readability checks.
- **Success Criteria:** 5 polished pitch emails ready for sending.
- **Common Pitfalls:** Generic pitches or failure to address the platform's editorial focus.
- **Time Estimate:** 1 day

**STEP 4: [Submission and Follow-Up]**
- **Action:** Submit content to selected platforms, then follow up politely if no response within a week.
- **Tools Needed:** Email client; Asana for tracking submissions and follow-ups.
- **Success Criteria:** All pitches submitted with at least one response by the end of Week 1.
- **Common Pitfalls:** Not following submission guidelines or losing track of follow-up attempts.
- **Time Estimate:** Ongoing

**STEP 5: [Post-Publication Strategy]**
- **Action:** Develop a plan to promote published guest posts through social media and email outreach.
- **Tools Needed:** Buffer for scheduling social posts; Mailchimp for newsletters.
- **Success Criteria:** Content promoted on at least two platforms within the first week.
- **Common Pitfalls:** Lack of promotion or neglecting post-publication activity.
- **Time Estimate:** Weekly

### Quality Checkpoints
- **Checkpoint 1:** After Step 3 - Verify all pitches include unique value proposition and platform-specific tone.
- **Checkpoint 2:** After Step 4 - Confirm submission guidelines followed; track response rates.

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Number of Guest Posts Accepted
   - Target: At least 3 accepted by end of quarter
   - Measurement Method: Track submissions and responses via CRM system.

2. **Secondary Metrics:**
   - Average response time from publishers.
   - Increase in backlinks to core domain after guest post publication.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 areas for improvement (e.g., pitch conversion, platform selection).
3. Implement changes such as refining subject lines or adjusting outreach cadence.
4. Re-measure outcomes and repeat until goals are met.

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
1. **Executive Summary:** Overview of strategies used, results achieved, and insights gained.
2. **Detailed Report:** Methodology, research findings, pitch drafts, response logs, post-publication analysis.
3. **Maintenance Plan:** Ongoing tasks for monitoring and promoting guest posts.
4. **Knowledge Transfer:** Training materials on best practices for new team members.

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. Replace bracketed placeholders with specific names, URLs, or data relevant to the content marketing strategist's context.
2. Define 10-20 critical topics based on current industry trends and platform updates in 2024-2025.

### Latest 2024-2025 Practices Integration

- **AI Tools:** Use GPT-4 for drafting pitches; integrate with Grammarly for automated edits.
- **Automation:** Implement Zapier workflows to automate follow-up emails after submission rejections.
- **Collaboration:** Leverage Notion for shared task lists and analytics tracking among team members.

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Content Strategy Frameworks"
    focus: "Latest frameworks for guest post creation in 2024"
    sources: ["HubSpot blog", "Content Marketing Institute"]
    deliverable: "Framework comparison table with best practices"

  # [Other agents follow similar structure]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize recommendations by impact on guest post acceptance rate
  5. Generate unified report with actionable insights
```

## SUCCESS VALIDATION

### Final Checklist
- [ ] **Ultimate Goal Achieved?** At least 3 guest posts accepted.
- [ ] **All Metrics Met?** Performance metrics as defined above are met or exceeded.
- [ ] **Quality Validated?** All submissions adhere to platform guidelines and showcase professionalism.
- [ ] **Documentation Complete?** All deliverables compiled in the specified format.

### Continuous Improvement
- Schedule quarterly reviews of guest post performance and strategy effectiveness.
- Update research topics based on emerging trends in content marketing.
- Share successes and lessons learned with the broader community through webinars or blog posts.

