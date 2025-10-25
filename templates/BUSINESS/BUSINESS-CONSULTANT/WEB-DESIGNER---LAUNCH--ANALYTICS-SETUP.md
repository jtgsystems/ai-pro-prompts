# Web Designer - AI Agent Template
## Launch & Analytics Setup

### Success Definition (Measurable)
**Success Metrics:**
- **Website Live:** The website is live on a public server.
- **Analytics Integration:** Google Analytics installed and tracking correctly for page views, bounce rate, session duration, device usage, referral sources, geographic distribution, and user behavior flows.
- **Conversion Tracking:** Goals are set up in Google Analytics to track form submissions, downloads, or purchases.
- **Performance Monitoring:** Core Web Vitals (LCP, CLS, FID) meet the recommended thresholds.

### Critical Knowledge Areas
1. Latest Web Design Trends & Best Practices (2024-2025)
2. Responsive Web Design Principles
3. Accessibility Standards (WCAG 2.1 AA)
4. SEO Fundamentals for Web Designers
5. Typography and Color Theory
6. UI/UX Design Process
7. User Research Methods
8. Wireframing & Prototyping Tools
9. Visual Hierarchy and Information Architecture
10. Cross-Browser Compatibility Testing
11. Performance Optimization Techniques (Image Compression, Lazy Loading)
12. Accessibility Compliance (Screen Readers, Keyboard Navigation)

### Step-by-Step Workflow

**STEP 1: Domain Registration & Hosting**
- **Action:** Register a domain name relevant to your brand.
- **Tools Needed:** [GoDaddy, Namecheap] or alternatives like [Hover]
- **Success Criteria:** Domain is active and points to the correct hosting server.
- **Common Pitfalls:** Incorrect DNS settings, forgetting to renew registration.
- **Time Estimate:** 1 hour

**STEP 2: Website Framework Setup**
- **Action:** Choose a framework (WordPress, Squarespace, Webflow) or build a static site with HTML/CSS/JS.
- **Tools Needed:** [WordPress.org, WordPress.com, Elementor, Divi, Adobe XD]
- **Success Criteria:** Framework is installed and configured on the hosting server.
- **Common Pitfalls:** Forgetting SSL certificate settings, missing plugin dependencies.
- **Time Estimate:** 2 hours

**STEP 3: Site Structure & Navigation Design**
- **Action:** Plan site architecture including sitemap, menu structure, taxonomy, and user flows.
- **Tools Needed:** [MindMuse, Milanote]
- **Success Criteria:** Sitemap is created and shared with stakeholders for feedback.
- **Common Pitfalls:** Overcrowded navigation or confusing hierarchy.
- **Time Estimate:** 3 hours

**STEP 4: Content Creation**
- **Action:** Develop content strategy including SEO keywords, copywriting, images, videos, and interactive elements.
- **Tools Needed:** [Google Keyword Planner, SEMrush]
- **Success Criteria:** All assets are created or sourced with licenses for commercial use.
- **Common Pitfalls:** Copyrighted images, missing alt text for accessibility.
- **Time Estimate:** 4 hours

**STEP 5: Design Implementation**
- **Action:** Implement design mockups using CSS frameworks (Bootstrap, Tailwind) and custom code.
- **Tools Needed:** [Figma, Sketch, Adobe XD]
- **Success Criteria:** Designs are coded without errors and visually match the mockups across devices.
- **Common Pitfalls:** Browser inconsistencies, missing responsive breakpoints.
- **Time Estimate:** 8 hours

**STEP 6: Accessibility Compliance**
- **Action:** Validate designs against WCAG 2.1 AA standards using tools like Axe or Lighthouse.
- **Tools Needed:** [Axe Core, Google Lighthouse]
- **Success Criteria:** All pages pass WCAG 2.1 AA with no critical issues.
- **Common Pitfalls:** Missing alt attributes for images, insufficient color contrast.
- **Time Estimate:** 2 hours

**STEP 7: SEO Setup**
- **Action:** Configure site structure and meta tags for search engines.
- **Tools Needed:** [Google Search Console, Yoast SEO]
- **Success Criteria:** Robots.txt, sitemap.xml are correctly set up and submitted to Google.
- **Common Pitfalls:** Incorrect robots directives, missing canonical URLs.
- **Time Estimate:** 1 hour

**STEP 8: Analytics Setup**
- **Action:** Install Google Analytics tracking code on all pages.
- **Tools Needed:** [Google Tag Manager]
- **Success Criteria:** GA4 property is active and collecting data for page views, sessions, and conversions.
- **Common Pitfalls:** Incorrect UTM parameters, not tracking specific goals.
- **Time Estimate:** 30 minutes

**STEP 9: Performance Optimization**
- **Action:** Optimize images, minify CSS/JS, enable browser caching, set up lazy loading.
- **Tools Needed:** [ImageOptim, Webpack, PurifyCSS]
- **Success Criteria:** Page load time is under 3 seconds on average for desktop and mobile.
- **Common Pitfalls:** Overlooked image sizes, missing minification of JS/CSS.
- **Time Estimate:** 2 hours

**STEP 10: Cross-Browser Testing**
- **Action:** Test the site in Chrome, Firefox, Safari, Edge across all major devices (desktop, tablet, mobile).
- **Tools Needed:** [BrowserStack, LambdaTest]
- **Success Criteria:** All core functionalities work without issues.
- **Common Pitfalls:** Mobile layout collapsing on specific browsers.
- **Time Estimate:** 4 hours

**STEP 11: Launch & Promotion**
- **Action:** Deploy the site to production, notify stakeholders and users of the new launch.
- **Tools Needed:** [GitHub Actions, Netlify, Vercel]
- **Success Criteria:** Site is live on a public URL, all analytics tracking fires correctly.
- **Common Pitfalls:** Forgetting to update DNS settings after deployment.
- **Time Estimate:** 1 hour

**STEP 12: Post-Launch Monitoring**
- **Action:** Set up regular monitoring for uptime, performance, and security alerts.
- **Tools Needed:** [UptimeRobot, Pingdom]
- **Success Criteria:** Alerts are configured and tested; daily dashboards show site health metrics.
- **Common Pitfalls:** Ignoring early warning signs of downtime or slow performance.
- **Time Estimate:** 1 hour

### Tools & Software (Free/Primary vs. Paid/Optional)

**Primary Tools (Free)**
- **Domain Registrar:** Namecheap, GoDaddy
- **Hosting Platform:** GitHub Pages, Netlify, Vercel
- **CMS Frameworks:** WordPress.org, Jekyll
- **Design Tools:** Figma (free tier), Adobe XD (paid features free)
- **Prototyping:** InVision Freehand
- **Collaboration:** Slack, Discord

**Optional Paid Tools**
- **Project Management:** Asana, Trello (premium options available)
- **Version Control:** GitLab Enterprise Server
- **Analytics:** Google Analytics Pro
- **SEO Software:** SEMrush, Ahrefs
- **Performance Monitoring:** New Relic, Datadog
- **Testing Platforms:** BrowserStack, LambdaTest

### Troubleshooting Common Issues

**1. Site Not Loading**
- Check server status and DNS configuration.
- Ensure SSL certificate is installed correctly.

**2. Broken Links**
- Use a link checker tool like Broken Link Checker to identify issues.

**3. Mobile Responsiveness Failures**
- Verify responsive breakpoints in browser dev tools.
- Test on actual mobile devices using BrowserStack or local emulators.

**4. Analytics Not Tracking Events**
- Ensure events are properly wrapped with `event` parameters.
- Check GA4 property settings for event tracking.

**5. SEO Issues**
- Verify robots.txt and sitemap.xml are correctly set up.
- Use Google Search Console to identify crawl errors.

### Recommended Tool Stack (2024)

| Category | Primary Tool (Free) | Alternative Tools (Paid/Optional) |
|----------|---------------------|------------------------------------|
| Domain Management | Namecheap, GoDaddy | [Dyn] |
| Web Hosting | GitHub Pages, Netlify, Vercel | AWS Elastic Beanstalk, DigitalOcean App Platform |
| Content Management System | WordPress.org | Squarespace (paid), Webflow (premium) |
| Design & Prototyping | Figma (free tier), Adobe XD | Sketch, InVision Studio |
| Version Control | GitLab Community Edition | GitHub Enterprise Server, Bitbucket |
| Project Management | Trello, Asana | Jira, Monday.com |
| Analytics | Google Analytics 4 | Adobe Analytics |
| SEO Tools | SEMrush Free Trial, Ahrefs Lite Plan | Moz Pro, BrightLocal |
| Performance Monitoring | UptimeRobot (free tier), Pingdom | New Relic, Datadog |
| Testing & Accessibility | axe DevTools, Lighthouse in Chrome DevTools | BrowserStack, LambdaTest |

### Realistic Timeline to Achieve Launch & Analytics Setup

**Week 1: Planning & Framework Selection**
- Domain registration
- Hosting setup
- CMS/framework selection
- Project planning and backlog creation

**Week 2: Design & Content Creation**
- Sitemap and navigation design
- UI/UX research and mockups
- Content strategy and SEO keyword research
- Initial content creation (copy, images)

**Week 3: Development Phase**
- Front-end development (HTML/CSS/JS)
- Responsive testing across devices
- Cross-browser compatibility checks

**Week 4: Final Testing & Launch Preparation**
- Accessibility compliance testing
- Performance optimization
- Analytics setup verification
- Security audit and SSL configuration
- Uptime monitoring implementation

### Actionable Steps for Beginners
1. **Start with a Simple Framework:** Choose WordPress or Squarespace to minimize coding complexity.
2. **Focus on Core Content First:** Build the homepage and main landing pages before expanding site structure.
3. **Use Free Tools for Initial Setup:** Leverage GitHub Pages, Netlify, or Vercel for hosting; Figma for design; Google Analytics for tracking.
4. **Prioritize SEO from Day 1:** Use free tools like SEMrush to identify easy opportunities first (e.g., meta descriptions).
5. **Iterate Based on Analytics:** After launch, regularly review analytics data and make iterative improvements.

By following this comprehensive Web Designer AI agent template, beginners can efficiently establish a functional website with integrated analytics setup, ready for traffic and performance optimization. The focus on measurable success criteria ensures continuous improvement and alignment with industry best practices.

