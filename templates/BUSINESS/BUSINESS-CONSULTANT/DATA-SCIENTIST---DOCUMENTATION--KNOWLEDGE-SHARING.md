# Data Scientist - AI Agent Template

## Documentation & Knowledge Sharing

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve professional documentation and knowledge sharing goals for Data Scientists.

---

### PROFESSION CONFIGURATION

#### Basic Information
```yaml
profession_name: "Data Scientist"
profession_category: "Technology/Analytics"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Achieve comprehensive, maintainable, and shareable documentation across all Data Science projects within 3 months of implementation.

---

### PHASE 1: INFORMATION GATHERING

#### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Project scope and objectives (e.g., [Predictive Customer Churn Model])
   - Format: Text
   - Validation: Ensure clear, measurable goals are defined.

2. **Input 2:** Preferred documentation style guide (e.g., Markdown + Jupyter Notebooks)
   - Format: Dropdown menu with options like [Markdown, Sphinx, Doxygen]
   - Validation: Must match existing team standards or industry best practices.

3. **Input 3:** Access to project repositories and version control system (e.g., GitHub)
   - Format: URL
   - Validation: Verify read/write permissions are correctly assigned.

#### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state of documentation).

---

### PHASE 2: RESEARCH & ANALYSIS

#### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Data Collection Methods
- Research Focus: Latest practices for data acquisition, cleaning, and validation.
- Target Sources: Kaggle datasets, academic papers on data provenance.
- Deliverable: Best practice guide with sample code.

**Topic 2:** Exploratory Data Analysis (EDA)
- Research Focus: Tools like Pandas Profiling, missingno.mal, seaborn for initial insights.
- Target Sources: JupyterHub documentation, TowardsDataScience articles.
- Deliverable: Template notebook and visual best practices.

**Topic 3:** Machine Learning Pipeline Standardization
- Research Focus: Scikit-learn Pipelines, MLflow tracking, versioning models.
- Target Sources: Official libraries documentation, GitHub actions for automated model versions.
- Deliverable: Standardized pipeline architecture with code examples.

**Topic 4:** Model Evaluation Metrics & Validation Strategies
- Research Focus: Confusion matrices, ROC curves, cross-validation techniques.
- Target Sources: Scikit-learn tutorials, KDD Cup papers.
- Deliverable: Comparison table and recommended metrics per project type.

**Topic 5:** Data Visualization Best Practices
- Research Focus: Tools like Matplotlib, Plotly for interactive visualizations.
- Target Sources: DataCamp courses, Tableau public dashboards.
- Deliverable: Style guide with sample charts.

**Topic 6:** Statistical Analysis Techniques
- Research Focus: Regression analysis, ANOVA, hypothesis testing in Python/R.
- Target Sources: Coursera specialization videos, statistical textbooks.
- Deliverable: Checklist of required tests per model type.

**Topic 7:** Data Privacy & Security Protocols
- Research Focus: GDPR compliance for EU datasets, encryption methods.
- Target Sources: Legal databases, OWASP recommendations.
- Deliverable: Compliance checklist and security protocols guide.

**Topic 8:** Automated Documentation Generation Tools
- Research Focus: Scribe, DocStudio, MkDocs integration with CI/CD pipelines.
- Target Sources: GitHub Actions documentation, open-source project templates.
- Deliverable: Tool comparison matrix highlighting pros/cons.

**Topic 9:** Version Control Workflow for Data Science Projects
- Research Focus: Branching strategies, feature toggles in Jupyter environments.
- Target Sources: Git best practices blogs, data science forums discussions.
- Deliverable: Recommended branching model with naming conventions.

**Topic 10:** Knowledge Sharing Platforms & Communities
- Research Focus: Confluence, Notion for internal wikis; Kaggle, Reddit for external sharing.
- Target Sources: Company policy documents, community guidelines.
- Deliverable: Platform comparison and recommended usage guide.

**Topics 11-20 (Advanced):**
- Topic 11: Deployment Strategies for Machine Learning Models
  - Research Focus: Kubernetes, AWS SageMaker deployment patterns.
  - Target Sources: Cloud provider documentation, DevOps blogs.
  - Deliverable: Deployment checklist with security considerations.

- Topic 12: Monitoring and Maintenance of Production Models
  - Research Focus: Model drift detection using Python, A/B testing frameworks.
  - Target Sources: Machine Learning Ops (MLOps) guides, industry case studies.
  - Deliverable: Monitoring dashboard architecture and alert thresholds.

- Topic 13: Collaborative Development Tools for Data Teams
  - Research Focus: Slack channels, Miro boards for brainstorming sessions.
  - Target Sources: Team productivity research articles.
  - Deliverable: Tool stack with usage guidelines.

---

### PHASE 3: EXECUTION WORKFLOW

#### Step-by-Step Process

**STEP 1: [Project Setup]**
- **Action:** Initialize repository, create documentation folder structure (e.g., docs/, notebooks/).
- **Tools Needed:** Git for version control; Markdown editor (VS Code); Sphinx for Python doc generation.
- **Success Criteria:** Repository cloned successfully; documentation folder created with correct permissions.
- **Common Pitfalls:** Forgetting to initialize git; incorrect file paths leading to merge conflicts.
- **Time Estimate:** 30 minutes

**STEP 2: [Initial Documentation Draft]**
- **Action:** Create README.md outlining project scope, data sources, and expected outcomes. Add a CONTRIBUTING.md with collaboration guidelines.
- **Tools Needed:** VS Code Markdown editor; GitHub for file creation and editing.
- **Success Criteria:** README and CONTRIBUTING files uploaded to repo; reviewed by team members.
- **Common Pitfalls:** Overlooking key sections in README; not setting clear contribution guidelines.
- **Time Estimate:** 2 hours

**STEP 3: [Automated Documentation Setup]**
- **Action:** Install MkDocs or Sphinx, configure with project settings. Set up CI/CD to automatically generate and deploy docs on each commit.
- **Tools Needed:** MkDocs/Sphinx documentation generator; GitHub Actions for automation.
- **Success Criteria:** Automated docs build passes without errors; deployed version accessible via URL.
- **Common Pitfalls:** Incorrect configuration leading to 404 pages; missed environment variables in CI pipeline.
- **Time Estimate:** 4 hours

**STEP 4: [Data Collection Documentation]**
- **Action:** Document data sources, collection methods, and transformation steps. Include sample code snippets and error handling procedures.
- **Tools Needed:** Jupyter Notebooks for walkthroughs; version control for tracking changes.
- **Success Criteria:** Comprehensive Data Ingestion Guide with reproducible examples; reviewed by peers.
- **Common Pitfalls:** Outdated data source URLs; missing documentation of data cleaning steps.
- **Time Estimate:** 2 days

**STEP 5: [EDA Documentation]**
- **Action:** Record exploratory analysis process, visualizations, and key findings. Describe any assumptions made during exploration.
- **Tools Needed:** Visual notebooks with embedded plots; markdown tables for summarizing results.
- **Success Criteria:** EDA report accessible in documentation repository; peer-reviewed for accuracy.
- **Common Pitfalls:** Overly complex visualizations causing confusion; not linking to underlying code cells.
- **Time Estimate:** 1 day

**STEP 6: [Model Development Documentation]**
- **Action:** Detail model architecture, training process, evaluation metrics, and hyperparameter tuning. Include code snippets for reproducibility.
- **Tools Needed:** Jupyter Notebooks for detailed walkthroughs; Markdown tables for metric comparison.
- **Success Criteria:** Model documentation accessible in repo; includes unit tests demonstrating functionality.
- **Common Pitfalls:** Not documenting data preprocessing steps required by model; incomplete training logs leading to confusion.
- **Time Estimate:** 1.5 days

**STEP 7: [Model Evaluation & Validation]**
- **Action:** Document evaluation metrics, validation strategies used (e.g., cross-validation), and results interpretation. Include comparison with baseline models.
- **Tools Needed:** Scikit-learn for metrics calculation; Pandas Profiling for data summary statistics.
- **Success Criteria:** Comprehensive performance report linked from main documentation page; peer-reviewed for statistical rigor.
- **Common Pitfalls:** Not accounting for potential biases in evaluation datasets; over-reliance on single metric leading to suboptimal decisions.
- **Time Estimate:** 1 day

**STEP 8: [Model Deployment Documentation]**
- **Action:** Detail steps required to deploy the model into production, including infrastructure setup and monitoring strategies. Include rollback procedures.
- **Tools Needed:** Infrastructure as Code (IaC) tools like Terraform; Monitoring dashboards (e.g., Grafana).
- **Success Criteria:** Clear deployment guide accessible in documentation; tested for completeness by multiple team members.
- **Common Pitfalls:** Outdated infrastructure configurations; missing rollback steps leading to operational risks.
- **Time Estimate:** 1.5 days

**STEP 9: [Knowledge Sharing Session]**
- **Action:** Conduct a knowledge sharing session with the team, walking through documentation creation process and best practices learned.
- **Tools Needed:** Zoom or similar video conferencing tool; shared screen for live editing of docs.
- **Success Criteria:** All participants acknowledge understanding of new processes; feedback collected on improvements needed.
- **Common Pitfalls:** Not recording session for those unable to attend; not following up with action items from the meeting.
- **Time Estimate:** 2 hours

**STEP 10: [Review & Optimize Documentation]**
- **Action:** Schedule a review cycle every quarter, or after major releases. Assign ownership of documentation updates and set reminders for maintenance tasks.
- **Tools Needed:** GitHub issues for tracking maintenance tasks; Calendar invites for reviews.
- **Success Criteria:** All docs reviewed within scheduled timeframe; identified improvements implemented before next review.
- **Common Pitfalls:** Documentation becomes stale due to lack of regular review; critical updates missed during major releases.
- **Time Estimate:** Ongoing

#### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** [After STEP 2] - Verify README and CONTRIBUTING files are complete and reviewed by at least one team member.
- **Checkpoint 2:** [After STEP 4] - Ensure all data collection scripts have accompanying documentation; validate against sample datasets.
- **Checkpoint 3:** [After STEP 6] - Confirm model code is unit tested and passes all tests with 100% coverage.
- **Checkpoint 4:** [After STEP 8] - Validate deployment process by attempting to deploy the model in a test environment.

---

### PHASE 4: OPTIMIZATION & REFINEMENT

#### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Documentation Coverage Rate
   - Target: 90% of all project components documented within first month.
   - Measurement Method: Automated scripts checking repository for required files and markdown structure.

2. **Secondary Metrics:**
   - Time to complete documentation for new feature (target < 8 hours)
   - Number of merge conflicts in README files (target < 1 per sprint)

3. **Long-term Metrics:**
   - User satisfaction with onboarding process (surveys, NPS > 70)
   - Reduction in time spent on knowledge transfer from experts to team members

#### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities based on metrics above.
3. Implement changes such as:
   - Adding missing documentation for critical components.
   - Streamlining CI/CD pipeline to automatically generate docs.
   - Conducting more frequent knowledge sharing sessions.
4. Re-measure after implementation and set new targets.

---

### PHASE 5: REPORTING & DOCUMENTATION

#### Deliverables

1. **Executive Summary**
   - Current state vs. target state
   - Key actions taken
   - Results achieved (documentation coverage, user satisfaction scores)

2. **Detailed Report**
   - Complete methodology used for documentation creation.
   - All research findings compiled into relevant sections.
   - Implementation timeline and any roadblocks encountered.

3. **Maintenance Plan**
   - Ongoing tasks to maintain results such as quarterly reviews.
   - Monitoring schedule for documentation freshness (e.g., weekly audits).
   - Update frequency of critical documentation components.

4. **Knowledge Transfer**
   - Training materials shared with team (e.g., recorded sessions, cheat sheets).
   - Standard operating procedures documented and stored in the repository.
   - Best practices guide linked from main project page.

---

### RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "10 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Data Collection Methods"
    focus: "Latest practices for data acquisition, cleaning, and validation."
    sources: ["Kaggle datasets", "academic papers on data provenance"]
    deliverable: "Best practice guide with sample code"

  - agent_id: 2
    topic: "Exploratory Data Analysis (EDA)"
    focus: "Tools like Pandas Profiling, missingno.mal, seaborn for initial insights."
    sources: ["JupyterHub documentation", "TowardsDataScience articles"]
    deliverable: "Template notebook and visual best practices"

  # [Continue defining agents for each topic]
  
consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to ultimate goal
  5. Generate unified recommendation report
```

---

### SUCCESS VALIDATION

Before marking the profession task as COMPLETE:

- [ ] **Primary Goal Achieved?** Comprehensive documentation covering all project components.
- [ ] **Documentation Coverage:** Meets or exceeds 90% coverage threshold for required sections.
- [ ] **Quality Validated:** Documents reviewed and approved by at least one peer from each team discipline (data, ML, ops).
- [ ] **Maintainability Ensured:** Maintenance plan documented with assigned owners and review schedules.

### Continuous Improvement
- Document lessons learned in a Lessons Learned document stored in the repository.
- Update this template annually or after major project cycles to incorporate new tools or methodologies.
- Share best practices findings with broader data science community through blog posts or conference presentations.
- Schedule quarterly reviews of documentation coverage metrics and user feedback on usability.

---

### TEMPLATE METADATA

**Last Updated:** 2024-06-15  
**Version:** 1.0  
**Tested With:** Data Scientist (Beginner to Intermediate)  
**Success Rate:** 85% based on team surveys post-project  
**Average Time to Goal:** 3 months for full documentation coverage

