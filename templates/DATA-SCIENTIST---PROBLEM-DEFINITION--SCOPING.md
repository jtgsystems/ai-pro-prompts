# Data Scientist - AI Agent Template
## Problem Definition & Scoping

### Success Criteria (Measurable)
- **Problem Clearly Defined:** All stakeholders agree on problem statement within 48 hours.
- **Scope Documented:** Scope of work defined with clear deliverables, constraints, and success metrics.
- **Data Requirements Identified:** At least 75% of required data sources identified and validated for quality.
- **Stakeholder Buy-In:** Signed-off requirements document from key stakeholders.

### Critical Knowledge Areas (Specific to Data Scientist)

**1. Statistical Foundations**
   - Research Focus: Understanding core statistical concepts, hypothesis testing, regression analysis
   - Target Sources: Textbooks, Khan Academy, Coursera

**2. Machine Learning Fundamentals**
   - Research Focus: Classification, regression, clustering techniques; model evaluation metrics
   - Target Sources: Andrew Ng's ML course (Coursera), Kaggle tutorials

**3. Data Preprocessing Techniques**
   - Research Focus: Handling missing data, feature scaling, dimensionality reduction
   - Target Sources: DataCamp courses on preprocessing, research papers

**4. Exploratory Data Analysis (EDA)**
   - Research Focus: Visualizing data distributions, identifying patterns and anomalies
   - Target Sources: Python's Matplotlib & Seaborn libraries documentation

**5. Programming for Data Science**
   - Research Focus: Proficiency in Python/R; version control with Git
   - Target Sources: Official docs (Python/R), GitHub best practices

**6. Big Data Technologies**
   - Research Focus: Hadoop, Spark fundamentals; cloud platforms like AWS Glue
   - Target Sources: Apache projects documentation, Coursera's Big Data MicroMasters

**7. Deep Learning Frameworks**
   - Research Focus: TensorFlow/Keras architectures for specific problems (e.g., NLP)
   - Target Sources: Official frameworks docs, Kaggle competitions

**8. Model Deployment Strategies**
   - Research Focus: Containerization with Docker; REST APIs on Kubernetes
   - Target Sources: Docker documentation, AWS SageMaker deployment guides

**9. Ethical AI Practices**
   - Research Focus: Bias detection methods, data privacy regulations (GDPR)
   - Target Sources: MIT Technology Review articles, NIST guidelines

**10. Agile Methodologies in Data Projects**
    - Research Focus: Iterative model development cycles; stakeholder feedback loops
    - Target Sources: Scrum guide, Lean UX principles**

### Execution Workflow
**STEP 1: Problem Definition & Framing (Days 1-2)**
   - **Action:** Conduct stakeholder interviews to understand business problem.
   - **Tools Needed:** Zoom/Teams for remote meetings, Notion/Crocodoc for documentation.
   - **Success Criteria:** Clear problem statement documented and approved by stakeholders.
   - **Common Pitfalls:** Ambiguous requirements leading to scope creep.
   - **Time Estimate:** 2 days

**STEP 2: Data Requirement Identification (Days 3-4)**
   - **Action:** Identify all data sources needed; assess quality, availability, latency.
   - **Tools Needed:** Python's Pandas for exploratory analysis of sample datasets.
   - **Success Criteria:** At least 75% of required data sources identified and validated.
   - **Common Pitfalls:** Missing key data sources causing project delays.
   - **Time Estimate:** 2 days

**STEP 3: Data Collection & Preparation (Days 5-7)**
   - **Action:** Extract raw data; clean, transform into a format suitable for modeling.
   - **Tools Needed:** SQL databases (PostgreSQL), Python libraries (Pandas, NumPy).
   - **Success Criteria:** Clean dataset ready for EDA with no critical errors.
   - **Common Pitfalls:** Data inconsistencies leading to inaccurate results.
   - **Time Estimate:** 3 days

**STEP 4: Exploratory Data Analysis (EDAs) & Insight Generation (Days 8-10)**
   - **Action:** Perform statistical analysis; visualize patterns, correlations, outliers.
   - **Tools Needed:** Python libraries (Matplotlib, Seaborn), Jupyter Notebooks for interactive analysis.
   - **Success Criteria:** Key insights documented with visualizations and summary statistics.
   - **Common Pitfalls:** Overlooking edge cases leading to incomplete model understanding.
   - **Time Estimate:** 3 days

**STEP 5: Hypothesis Generation & Initial Modeling (Days 11-14)**
   - **Action:** Define hypotheses based on EDAs; build initial machine learning models.
   - **Tools Needed:** Python libraries (Scikit-learn, TensorFlow), cloud platforms for compute resources.
   - **Success Criteria:** At least one viable model prototype meeting basic performance metrics (>70% accuracy).
   - **Common Pitfalls:** Model drift due to changing data distributions.
   - **Time Estimate:** 4 days

**STEP 6: Stakeholder Review & Iteration (Days 15-16)**
   - **Action:** Present findings and models to stakeholders; incorporate feedback.
   - **Tools Needed:** Zoom/Teams for review sessions, Google Docs for collaborative reviews.
   - **Success Criteria:** Updated project plan with refined scope and timeline approved by stakeholders.
   - **Common Pitfalls:** Misalignment between data team's technical recommendations and business needs.
   - **Time Estimate:** 2 days

**STEP 7: Final Model Development & Documentation (Days 17-18)**
   - **Action:** Refine model parameters; perform hyperparameter tuning, create comprehensive documentation.
   - **Tools Needed:** Python libraries (Scikit-learn), Confluence for documenting processes and models.
   - **Success Criteria:** Final model meets all success criteria defined at the beginning of the project.
   - **Common Pitfalls:** Documentation gaps leading to operational issues post-deployment.
   - **Time Estimate:** 2 days

**STEP 8: Deployment Planning & Strategy (Days 19-20)**
   - **Action:** Plan for deploying model into production environment; define monitoring and maintenance procedures.
   - **Tools Needed:** Docker, Kubernetes for containerization, Prometheus/Grafana for monitoring.
   - **Success Criteria:** Deployment plan approved by stakeholders; monitoring strategy defined.
   - **Common Pitfalls:** Inadequate error handling leading to unstable deployments.
   - **Time Estimate:** 2 days

**STEP 9: Documentation & Knowledge Transfer (Days 21-22)**
   - **Action:** Document entire project lifecycle, create user manuals, training materials for end-users.
   - **Tools Needed:** Confluence, Notion, Google Drive for version-controlled documentation.
   - **Success Criteria:** Comprehensive knowledge base created; training sessions conducted with stakeholders.
   - **Common Pitfalls:** Omitted critical steps leading to operational challenges post-project completion.
   - **Time Estimate:** 2 days

### Tools & Software (2024-2025 Recommended Stack)

**Primary Tools (Free/Open Source):**
1. **Programming Languages:** Python 3.x, R
2. **Data Manipulation:** Pandas (Python), dplyr (R)
3. **Machine Learning:** Scikit-learn, TensorFlow/Keras, PyTorch
4. **Visualization:** Matplotlib, Seaborn, Plotly
5. **Version Control:** Git (GitHub/GitLab)
6. **Cloud Platforms:** AWS SageMaker, Google Cloud AI Platform, Azure ML

**Alternative Tools (Paid):**
1. **Jupyter Notebooks:** Jupyter Enterprise Grid (subscription-based)
2. **Data Storage:** Snowflake (cloud data warehousing), Amazon Redshift
3. **Big Data Processing:** Apache Spark on Databricks (Databricks Runtime)
4. **Collaboration:** Slack Workspace for project communication, Miro for digital whiteboards

**Monitoring & Operations:**
1. **Container Orchestration:** Kubernetes (on GKE/AKS/EKS - managed services)
2. **Logging & Metrics:** Prometheus + Grafana, ELK Stack (Elasticsearch, Logstash, Kibana)

### Troubleshooting Common Issues
- **Data Quality Issues:**
  - Missing Values > 10% of dataset -> Flag for stakeholder review.
  - Outliers affecting model performance -> Apply Winsorization or Log Transformation.
  
- **Model Performance Degradation Post-Deployment:**
  - Data Drift Detected (KL-Divergence > 0.1) -> Re-train with recent data.

- **Scalability Problems in Deployment:**
  - CPU/Memory Utilization > 80% for extended periods -> Optimize model code or increase resources.

### Recommended Tool Stack
**Primary Tools (Free/Open Source):**
- Python (3.9+)
- Pandas, NumPy
- Scikit-learn
- TensorFlow/Keras
- Jupyter Notebook
- Git/GitHub

**Alternative/Optional Tools:**
- **Jupyter Enterprise Grid:** For enhanced collaborative notebook environments.
- **Snowflake:** For scalable cloud data warehousing solutions.
- **Databricks Databricks Runtime:** For managed Spark deployments.

### Realistic Timeline to Achieve Problem Definition & Scoping
The entire process from initial problem framing to final documentation typically spans 3-4 weeks for a medium-sized project. This timeline accounts for stakeholder interviews, data collection and cleaning, EDA, model prototyping, and iterative reviews. However, complex projects or those with limited data availability may extend beyond this range.

**Week 1:** Problem Definition & Data Requirement Identification
**Week 2:** Initial Data Collection & Basic Cleaning
**Week 3:** EDAs, Hypothesis Generation, First Model Prototypes
**Week 4:** Stakeholder Reviews, Final Model Refinement, Documentation

