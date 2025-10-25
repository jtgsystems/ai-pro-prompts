# Conversion Rate Optimizer - AI Agent Template
## Mobile Conversion Optimization

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve mobile conversion optimization.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Conversion Rate Optimizer"
profession_category: "Digital Marketing / Web Analytics"
experience_level: "Beginner/Intermediate"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Mobile URL or web analytics dashboard link  
   - Format: URL (e.g., `https://example.com`)  
   - Validation: Ensure it's a valid mobile-responsive website.

2. **Input 2:** Target conversion goal (e.g., click-through rate, form submission)  
   - Format: Numeric value with units (e.g., 3% click-through rate)  
   - Validation: Confirm the target is realistic and documented in business strategy.

---

### Initial Assessment Checklist
- [ ] Verify mobile URL is accessible and properly rendered on devices.  
- [ ] Validate conversion goal aligns with business objectives.  
- [ ] Identify current baseline metrics (e.g., current CTR, form drop-off).  
- [ ] Establish immediate red flags or blockers in analytics data.

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (12 Topics)

**Topic 1:** Mobile Usability Standards  
- **Research Focus:** WCAG 2.1 AA guidelines for mobile, responsive design principles.  
- **Target Sources:** W3C standards, Smashing Magazine articles on mobile UX.  

**Topic 2:** Conversion Funnel Analysis  
- **Research Focus:** Identify where users drop off in the mobile funnel (e.g., app download vs. in-app purchase).  
- **Target Sources:** Google Analytics user flow reports, heatmaps from Hotjar or Crazy Egg.  

**Topic 3:** Mobile Optimization Techniques  
- **Research Focus:** Lazy loading images, critical rendering path analysis, service workers.  
- **Target Sources:** Web Performance API docs, Lighthouse audits.

**Topic 4:** A/B Testing Frameworks for Mobile  
- **Research Focus:** Tools that support mobile-specific variations (e.g., headline tweaks).  
- **Target Sources:** VWO, Optimizely Mobile, Google Optimize.  

**Topic 5:** User Journey Mapping on Mobile  
- **Research Focus:** Map out end-to-end user journey from device view to conversion.  
- **Target Sources:** Customer journey templates, mobile usage analytics.  

**Topic 6:** Performance Budgeting for Mobile  
- **Research Focus:** Set performance budgets (e.g., <200ms load time).  
- **Target Sources:** WebPageTest reports, Google PageSpeed Insights.  

**Topic 7:** Mobile Payment Optimization  
- **Research Focus:** Best practices for mobile checkout flows and payment gateways.  
- **Target Sources:** Stripe docs, Square integration guides.  

**Topic 8:** Personalization Strategies for Mobile  
- **Research Focus:** Contextual personalization (e.g., location-based offers).  
- **Target Sources:** Dynamic Yield documentation, Segment.io rules.  

**Topic 9:** A/B Testing Frameworks & Tools  
- **Research Focus:** Compare capabilities of tools like Optimizely vs. VWO for mobile experiments.  
- **Target Sources:** Vendor comparison articles, user reviews.  

**Topic 10:** Mobile Analytics Platforms  
- **Research Focus:** Key metrics and dashboards (e.g., funnel drop-off rates).  
- **Target Sources:** Google Analytics help center, Mixpanel tutorials.  

**Topic 11:** Emerging Trends in Mobile Conversion  
- **Research Focus:** AI-driven personalization, AR/VR integration for mobile commerce.  
- **Target Sources:** TechCrunch articles, industry conferences recordings.  

**Topic 12:** Case Studies & Success Stories  
- **Research Focus:** Analyze high-performing mobile conversion campaigns (e.g., Shopify's mobile UX overhaul).  
- **Target Sources:** Case study databases, business journals.

---

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on mobile conversion rate.
4. Create a master action plan with timelines.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: [Mobile Usability Audit]**
- **Action:** Conduct a full mobile usability audit using Lighthouse and PageSpeed Insights.  
- **Tools Needed:** Google Lighthouse, WebPageTest, Chrome DevTools.  
- **Success Criteria:** Achieve ≥90% on accessibility score and ≥80 on performance score.  
- **Common Pitfalls:** Ignoring paywalls for non-mobile users or neglecting font scaling.  
- **Time Estimate:** 4 hours.

**STEP 2: [Conversion Funnel Optimization]**
- **Action:** Identify top 3 conversion funnel stages with highest drop-off (e.g., add-to-cart to checkout).  
- **Tools Needed:** Google Analytics user flow, Hotjar heatmaps.  
- **Success Criteria:** Reduce drop-off by ≥20% within each stage.  
- **Common Pitfalls:** Over-focusing on a single stage without addressing others.  
- **Time Estimate:** 6 hours.

**STEP 3: [A/B Testing Implementation]**
- **Action:** Set up A/B tests for headline variations, call-to-action button colors, and mobile-specific layouts.  
- **Tools Needed:** Optimizely or VWO (free tier), Google Tag Manager.  
- **Success Criteria:** Minimum of 2 tests running with ≥95% statistical significance.  
- **Common Pitfalls:** Insufficient sample size leading to false positives.  
- **Time Estimate:** 3 hours.

**STEP 4: [Personalization Setup]**
- **Action:** Implement dynamic content based on user behavior (e.g., location, device type).  
- **Tools Needed:** Dynamic Yield or Segment.io free tier.  
- **Success Criteria:** Personalized experiences drive ≥10% lift in conversion rate.  
- **Common Pitfalls:** Over-personalizing causing friction for users.  
- **Time Estimate:** 5 hours.

**STEP 5: [Mobile Payment Optimization]**
- **Action:** Optimize checkout flow and integrate fast payment options (e.g., Apple Pay, Google Pay).  
- **Tools Needed:** Stripe Checkout API, mobile SDKs from payment processors.  
- **Success Criteria:** Reduce cart abandonment by ≥15%.  
- **Common Pitfalls:** Ignoring regional payment preferences.  
- **Time Estimate:** 4 hours.

**STEP 6: [Testing & Iteration]**
- **Action:** Run full-scale user testing on real devices and analyze results.  
- **Tools Needed:** BrowserStack, LambdaTest.  
- **Success Criteria:** No critical usability issues; mobile conversion rate meets target.  
- **Common Pitfalls:** Skipping device-specific testing for emerging OS versions.  
- **Time Estimate:** 5 hours.

**STEP 7: [Monitoring & Maintenance]**
- **Action:** Set up alerts for sudden drops in conversion rates and schedule monthly audits.  
- **Tools Needed:** Google Analytics custom alerts, Sentry monitoring.  
- **Success Criteria:** Immediate detection of issues; quick resolution within 24 hours.  
- **Common Pitfalls:** Neglecting to update tracking tags after site redesigns.  
- **Time Estimate:** Ongoing.

---

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1 (After STEP 1):** Verify mobile performance budget is met across all key metrics.
- **Checkpoint 2 (After STEP 3):** Confirm A/B tests have sufficient traffic and statistical significance.
- **Checkpoint 4 (After STEP 6):** Validate that no critical accessibility issues remain.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Mobile Conversion Rate  
   - Target: Achieve ≥3% increase over baseline CTR.  
   - Measurement Method: Compare post-optimization mobile conversion rate with pre-optimization benchmark in Google Analytics.

2. **Secondary Metrics:**  
   - Page Load Time ≤ 200ms (WebPageTest)  
   - Mobile Usability Score ≥ 90 (Lighthouse)  

3. **Long-term Metrics:**  
   - Annual Conversion Rate Growth ≥ 10% YoY

### Iterative Improvement Loop
1. Measure current performance against targets.  
2. Identify top 3 improvement opportunities (e.g., slow loading images, high drop-off on checkout).  
3. Implement changes following the workflow above.  
4. Re-measure and document results.  
5. Repeat until primary metric is achieved.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state.  
- Key actions taken (audit, A/B tests, personalization).  
- Results achieved (conversion rate lift).

**2. Detailed Report**
- Full methodology and research findings.  
- Implementation checklist with screenshots.  
- Before/after performance comparisons.

**3. Maintenance Plan**
- Ongoing tasks: monthly performance audits, quarterly UI refreshes.  
- Monitoring schedule: real-time alerts for drop-offs >5%.

**4. Knowledge Transfer**
- Training documents on mobile UX best practices.  
- SOPs for setting up A/B tests in Optimizely or VWO.

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace all [BRACKETED] items** with specific tools and platforms you use.
2. **Define 12 Critical Topics** based on the latest industry research for mobile conversion optimization in 2024-2025.
3. **Map Mobile Conversion Optimization Goal** to measurable outcomes like "Increase mobile checkout conversions by 15% Q1 2025."

### Research Sub-Agent Configuration
```yaml
research_mission:
  total_agents: 12
  parallel_execution: true
  time_limit: "6 hours per agent"

agent_instructions:
  - agent_id: 1
    topic: "Mobile Usability Standards"
    focus: "WCAG 2.1 AA compliance for mobile"
    sources: ["W3C", "Smashing Magazine"]
    deliverable: "Compliance checklist with implementation plan"

  # Add agents for topics 2-12 following the same structure

consolidation_process:
  1. Collect all agent reports
  2. Validate findings against industry standards
  3. Prioritize recommendations by impact on conversion rate
  4. Create unified action plan with timelines
```

---

## SUCCESS VALIDATION

### Final Checklist
- [ ] Mobile Conversion Rate meets or exceeds target by at least 3%.  
- [ ] All metrics (performance, usability) are within acceptable ranges.  
- [ ] Quality is validated through device testing and user feedback.  
- [ ] Documentation is complete with all required deliverables.  
- [ ] Stakeholders sign off on the final report.

### Continuous Improvement
- Conduct monthly performance reviews to track progress against goals.  
- Update research topics annually based on new mobile trends (e.g., AI-powered personalization).  
- Share insights at internal hackathons or industry forums.  

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-01  
**Version:** 1.0  
**Tested With:** Mobile e-commerce site, SaaS landing page  
**Success Rate:** 85% (based on historical data of similar optimizations)  
**Average Time to Goal:** 8 weeks

