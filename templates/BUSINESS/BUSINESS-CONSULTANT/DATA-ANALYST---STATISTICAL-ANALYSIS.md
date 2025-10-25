# Data Analyst - AI Agent Template
## Statistical Analysis

### Success Definition
**Primary Objective:** Achieve robust statistical analysis delivering accurate insights within 4 weeks, measured by:
- **Model Accuracy:** ≥90% R² for predictive models
- **Statistical Significance:** p-value <0.05 in hypothesis testing
- **Data Quality:** ≤5% missing data, no outliers affecting >10% of observations
- **Deliverable Completeness:** All required reports and visualizations produced

### Critical Knowledge Areas (15 Topics)
1. **Statistical Methods**
   - Regression Analysis
   - Time Series Forecasting
   - ANOVA & Design of Experiments
   - Bayesian Statistics
2. **Data Cleaning Techniques**
   - Handling Missing Data
   - Outlier Detection
   - Standardization vs. Normalization
3. **Exploratory Data Analysis (EDA)**
   - Univariate Visualization
   - Bivariate Correlation Metrics
   - Dimensionality Reduction Overview
4. **Machine Learning for Statistics**
   - Linear Regression Models
   - Decision Trees & Random Forests
   - Gradient Boosting Machines
5. **Statistical Testing Frameworks**
   - Hypothesis Testing Basics
   - T-Tests & ANOVA
   - Chi-Square Tests
6. **Advanced Statistical Concepts**
   - Bayesian Networks
   - Survival Analysis
   - Multivariate Regression
7. **Data Visualization Tools**
   - Matplotlib, Seaborn (Python)
   - ggplot2 (R)
8. **Database Interaction Skills**
   - SQL Queries for Data Extraction
   - ETL Processes
9. **Statistical Software Proficiency**
   - R Programming Language
   - Python Pandas & StatsModels
10. **Big Data Analytics Tools**
    - Apache Spark, Hive (for large datasets)
11. **Project Management Best Practices**
    - Agile Methodologies
    - Version Control with Git
12. **Documentation Standards**
    - Jupyter Notebooks for Reporting
    - Markdown Formatting
13. **Collaboration Platforms**
    - Confluence for Knowledge Sharing
    - Slack or Teams for Team Communication
14. **Data Governance Compliance**
    - GDPR, CCPA Principles
15. **Continuous Learning Resources**
    - Kaggle Competitions
    - Coursera Specializations

### Execution Workflow
**STEP 1: Project Initiation (Day 1-3)**
- **Action:** Define scope, objectives, and success metrics with stakeholders.
- **Tools Needed:** Confluence for project charter, Google Forms for requirements gathering.
- **Success Criteria:** Signed-off project brief, defined KPIs.
- **Common Pitfalls:** Scope creep, unclear stakeholder expectations.
- **Time Estimate:** 3 days

**STEP 2: Data Collection & Ingestion (Day 4-7)**
- **Action:** Identify data sources, extract data using SQL or APIs, load into data warehouse.
- **Tools Needed:** Python Pandas for ETL scripts, AWS S3 for storage.
- **Success Criteria:** All required datasets in staging environment with <5% missing values.
- **Common Pitfalls:** Data quality issues, integration errors.
- **Time Estimate:** 7 days

**STEP 3: Data Cleaning & Preprocessing (Day 8-12)**
- **Action:** Handle nulls, outliers, and inconsistencies; transform variables as needed.
- **Tools Needed:** Python Pandas for cleaning scripts, Jupyter Notebooks for workflow documentation.
- **Success Criteria:** Cleaned dataset with documented transformations, no critical data quality issues identified.
- **Common Pitfalls:** Over-imputation, loss of information due to aggressive filtering.
- **Time Estimate:** 4 days

**STEP 4: Exploratory Data Analysis (Day 13-16)**
- **Action:** Conduct EDA to understand variable distributions, relationships, and patterns.
- **Tools Needed:** Python Matplotlib/Seaborn or R ggplot2 for visualizations.
- **Success Criteria:** Comprehensive exploratory analysis report with key insights documented.
- **Common Pitfalls:** Misleading visualizations, failing to document assumptions.
- **Time Estimate:** 3 days

**STEP 5: Statistical Modeling (Day 17-22)**
- **Action:** Develop statistical models based on objectives (e.g., regression, time series).
- **Tools Needed:** Python StatsModels or R for model building, Jupyter Notebooks for reproducibility.
- **Success Criteria:** Models validated with ≥90% accuracy and statistically significant results.
- **Common Pitfalls:** Overfitting, ignoring assumptions of statistical tests.
- **Time Estimate:** 5 days

**STEP 6: Model Validation & Testing (Day 23-26)**
- **Action:** Validate models on holdout data, perform sensitivity analysis.
- **Tools Needed:** Python Scikit-learn for cross-validation, Excel for manual checks if needed.
- **Success Criteria:** Models pass validation criteria with no critical issues.
- **Common Pitfalls:** Data leakage during testing, ignoring model assumptions in testing phase.
- **Time Estimate:** 3 days

**STEP 7: Reporting & Visualization (Day 27-30)**
- **Action:** Create final reports, visualizations, and dashboards for stakeholders.
- **Tools Needed:** Jupyter Notebooks for combined documentation and visuals, Tableau or Power BI for interactive dashboards.
- **Success Criteria:** All deliverables completed with reviewer sign-off.
- **Common Pitfalls:** Ambiguous conclusions, over-complicated visualizations.
- **Time Estimate:** 3 days

### Tools & Software
**Primary Tools (Free/Open Source):**
1. **Data Ingestion:** Python Pandas for ETL scripts, SQL for database access
2. **Statistical Analysis:** StatsModels in Python, R for statistical modeling
3. **Visualization:** Matplotlib, Seaborn (Python) or ggplot2 (R)
4. **Collaboration & Documentation:** Confluence, Jupyter Notebooks, Git for version control

**Optional Tools (Paid):**
1. **Big Data Processing:** Apache Spark Enterprise (cloud), Hadoop Distributed File System
2. **Advanced Analytics Platforms:** Tableau (desktop) or Power BI Pro for dashboards
3. **Data Governance & Compliance:** IBM InfoSphere Information Governance Catalog, Collibra

### Success Criteria Timeline
- **Week 1:** Define project scope, gather requirements
- **Week 2:** Extract and load data into warehouse
- **Week 3:** Clean and preprocess data; begin EDA
- **Week 4:** Develop and validate statistical models
- **Week 5:** Create final reports and visualizations

### Troubleshooting Guide
**Common Issues & Solutions:**
1. **Missing Data >5%**
   - Solution: Impute with median/mode, or consider dropping if variable is critical.
2. **Outliers Affecting Analysis (>10% of data points)**
   - Solution: Investigate source error; apply winsorizing or robust regression techniques.
3. **Model Not Meeting Accuracy Threshold**
   - Solution: Re-examine feature set, try different modeling approach (e.g., logistic vs linear regression).
4. **Visualization Issues (Hard to Read/Interpret)**
   - Solution: Simplify color schemes, add annotations, consider interactive dashboard options.

### Recommended Tool Stack
**Primary Tools (Free):**
1. **Development Environment:** VS Code or PyCharm Professional (free community edition)
2. **Database Management:** PostgreSQL (open-source), MongoDB Atlas
3. **Data Analysis & Modeling:** Python 3.x (Anaconda Distribution), RStudio Community Edition
4. **Version Control:** Git with GitHub/GitLab

**Optional Tools (Paid):**
1. **Big Data Processing:** Apache Spark Enterprise, Hadoop Distributed File System on cloud platforms like AWS EMR
2. **Advanced Visualization:** Tableau Desktop Pro, Power BI Pro for enterprise-level dashboards and advanced interactive features.

### Timeline to Achieve Statistical Analysis Goals
- **Week 1:** Set up environment, define data sources, establish basic project structure.
- **Week 2-3:** Collect raw data, begin ETL process, document initial findings.
- **Week 4-5:** Develop statistical models, perform validation, refine approach based on results.
- **Week 6:** Finalize reports, create visualizations, prepare stakeholder presentation.

**Total Time Estimate:** 1.5 to 2 months for a medium-sized project with standard data volumes and complexity. Adjust timelines as needed based on data size and team capacity.

### Conclusion
This template provides a structured approach for Data Analysts to achieve statistical analysis goals. By following the defined phases, utilizing the recommended tools and methodologies, and adhering to best practices for documentation and validation, analysts can ensure robust and actionable insights are produced within tight timelines. Continuous improvement and adaptation based on project feedback will further enhance outcomes over time.

