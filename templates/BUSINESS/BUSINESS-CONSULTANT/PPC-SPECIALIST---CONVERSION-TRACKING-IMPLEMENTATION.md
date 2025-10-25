# PPC Specialist - AI Agent Template
## Conversion Tracking Implementation

### Ultimate Goal Definition:
Achieve 95% or higher data accuracy in conversion tracking across all Google Ads campaigns within a 4-week period for [PROFESSION NAME]: PPC Specialist.

---

### Critical Knowledge Areas (12 Topics)

1. **Data Collection Standards**
   - Research Focus: Data privacy regulations, tag placement best practices
   - Target Sources: GDPR/CCPA guidelines, Google Ads help articles

2. **Tag Management Systems**
   - Research Focus: Manual vs automated tag management tools
   - Target Sources: Vendor documentation, user reviews

3. **Conversion Event Tracking**
   - Research Focus: Types of conversions (form submissions, purchases), conversion tracking setup for various channels

4. **Analytics Integration**
   - Research Focus: Google Analytics 4 integration with Google Ads, data flow between platforms

5. **Debugging Techniques**
   - Research Focus: Tag validation tools, UTM parameters best practices
   - Target Sources: Browser extensions, developer forums

6. **Campaign Optimization Strategies**
   - Research Focus: Bidding strategies based on conversion data, dynamic search ads implementation

7. **Attribution Modeling**
   - Research Focus: Data-driven vs rule-based attribution models for conversions

8. **Data Quality Assurance**
   - Research Focus: Methods to validate tracking accuracy, handling of duplicate conversions
   - Target Sources: Industry whitepapers, QA frameworks

9. **Advanced Conversion Events**
   - Research Focus: Refined audiences based on conversion actions, transaction level data reporting

10. **Cross-Device Tracking**
    - Research Focus: Implementation for multi-device user flows in PPC campaigns

11. **Conversion Reporting Best Practices**
    - Research Focus: Standardized reports, dashboards for KPI tracking
    - Target Sources: Marketing analytics blogs, template repositories

12. **Future Trends in Conversion Tracking**
    - Research Focus: AI-powered conversion prediction, machine learning based bid optimization

---

### Execution Workflow (8 Steps)

#### STEP 1: [Foundation Setup]
- **Action:** Assess current campaign structure and identify all potential conversion events
- **Tools Needed:** Google Ads UI, spreadsheet for asset inventory
- **Success Criteria:** List of identified conversions documented with % coverage (goal: 100%)
- **Common Pitfalls:** Missing event tracking setup in existing campaigns
- **Time Estimate:** 3 days

#### STEP 2: [Tag Implementation]
- **Action:** Set up conversion tag management system (CMS) using Google Tag Manager (GTM)
- **Tools Needed:** GTM account, custom HTML/CSS for tags
- **Success Criteria:** All conversions tagged with valid GA4 event parameters
- **Common Pitfalls:** Incorrect parameter mapping in GTM variables
- **Time Estimate:** 2 days

#### STEP 3: [Conversion Verification]
- **Action:** Implement real-time conversion validation using browser extensions like Google Tag Assistant or GA Debugger
- **Tools Needed:** Chrome extension for tag validation, test URLs
- **Success Criteria:** All conversions logged in Google Analytics within 1 minute of completion
- **Common Pitfalls:** Tags firing only on first visit, missing event parameters
- **Time Estimate:** 2 days

#### STEP 4: [Data Integration Testing]
- **Action:** Cross-validate data between Google Ads and GA4 using sample queries for conversion metrics
- **Tools Needed:** BigQuery export of conversion data, SQL querying tools
- **Success Criteria:** 95%+ match rate across critical KPIs (CTR, CPC, Conversion Rate)
- **Common Pitfalls:** Discrepancies due to asynchronous tag firing
- **Time Estimate:** 3 days

#### STEP 5: [Attribution Modeling Setup]
- **Action:** Configure Data-Driven Attribution model in Google Ads with GA4 integration
- **Tools Needed:** Google Ads UI, GTM for signal passing
- **Success Criteria:** Data-driven attribution enabled and active on all relevant campaigns
- **Common Pitfalls:** Incorrect data flow due to missing conversion parameters
- **Time Estimate:** 1 day

#### STEP 6: [Reporting & Dashboard Creation]
- **Action:** Build a comprehensive dashboard in GA4 for real-time conversion tracking across all campaigns
- **Tools Needed:** Google Data Studio, GA4 custom reports
- **Success Criteria:** Interactive dashboard showing conversion trends by campaign, device, and channel
- **Common Pitfalls:** Lack of segmentation leading to incomplete insights
- **Time Estimate:** 2 days

#### STEP 7: [Optimization & A/B Testing]
- **Action:** Implement bid adjustments based on conversion data for high-performing assets
- **Tools Needed:** Google Ads UI, UTM parameter tracking
- **Success Criteria:** Increase in ROI by at least 20% within first month post-implementation
- **Common Pitfalls:** Over-optimizing due to short-term volatility
- **Time Estimate:** Ongoing

#### STEP 8: [Training & Knowledge Transfer]
- **Action:** Conduct training sessions for team members on new tracking setup and reporting dashboard
- **Tools Needed:** Video recordings, live walkthroughs in GA4
- **Success Criteria:** Team proficient in using new tools with >80% completion rate on training assessment
- **Common Pitfalls:** Lack of documentation leading to knowledge gaps
- **Time Estimate:** 1 day

---

### Tools & Software (Primary Free Tools)

**Tag Management:**
- Google Tag Manager (Free)
- GTM Extension for Chrome

**Analytics:**
- Google Analytics 4 (Free with GA4 Upgrade)
- BigQuery (Free tier available)

**Testing & Validation:**
- Google Tag Assistant (Chrome extension, free)
- GA Debugger (Chrome extension, free)

**Reporting:**
- Google Data Studio (Free)
- Google Sheets (Free)

**Project Management:**
- Trello or Asana (Free plans available)

---

### Troubleshooting Common Issues

1. **Tags Not Firing:** Check GTM triggers and ensure correct configuration of parameters
2. **Data Lag:** Verify real-time data refresh settings in GA4 Data Streams
3. **Attribution Discrepancies:** Ensure conversion events are tagged with `event` parameter for accurate modeling
4. **Conversion Rate Drops:** Investigate potential tag conflicts or incorrect event tracking setup
5. **Reporting Errors:** Validate dataset completeness and schema integrity in BigQuery

---

### Realistic Timeline to Achieve Conversion Tracking Implementation

| Week | Tasks Completed | Status |
|------|------------------|--------|
| 1    | Foundation Setup, Tag Implementation | [ ] |
| 2    | Data Integration Testing, Attribution Modeling Setup | [ ] |
| 3    | Reporting & Dashboard Creation, Optimization & A/B Testing Initiation | [ ] |
| 4    | Training & Knowledge Transfer, Final Validation | [ ] |

**Final Validation:** All metrics met (95%+ tracking accuracy), team trained, ongoing optimization enabled.

---

### Success Metrics

- **Tracking Accuracy:** ≥95%
- **ROI Improvement:** ≥20% within first month
- **Team Proficiency:** ≥80% completion on training assessment
- **Data Freshness:** <5 seconds lag in real-time data updates
- **Attribution Model Adoption:** 100% active on campaigns with high conversion value

By following this structured approach, a PPC Specialist can achieve robust Conversion Tracking Implementation within the defined timeline and meet all success criteria. The focus on measurable outcomes ensures accountability while leveraging the latest tools and best practices for optimal performance.

