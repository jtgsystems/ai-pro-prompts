# Data Scientist - AI Agent Template
## Model Development & Testing

### Professional Configuration
```yaml
profession_name: "Data Scientist"
profession_category: "Technology/Analytics"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal Definition
**Primary Objective:** Develop, Test, and Deploy a Production-Ready Machine Learning Model that Achieves 95%+ Accuracy on Validation Data within 3 Months.

---

## Phase 1: Information Gathering

### Required Inputs
1. **Input 1:** Target Business Problem or Question ([e.g., customer churn prediction])
   - Format: Text
   - Validation: Clear, specific business problem statement

2. **Input 2:** Dataset(s) Available ([e.g., historical customer data CSV])
   - Format: File paths / URLs
   - Validation: Accessible and relevant to the problem

3. **Input 3:** Performance Metrics Defined ([e.g., accuracy >= 95%])
   - Format: Metric definitions
   - Validation: Specific, measurable criteria

### Initial Assessment Checklist
- [ ] All required inputs received and validated
- [ ] Business problem is well-defined and quantifiable
- [ ] Data quality checked (missing values, outliers)
- [ ] Success metrics are SMART and aligned with business needs

---

## Phase 2: Research & Analysis

### Critical Knowledge Areas (15 Topics)

1. **Python for Data Science** ([Research Focus]: Libraries like Pandas, NumPy, SciKit-Learn]
   - Target Sources: Official documentation, Kaggle tutorials
   - Deliverable: Python script skeleton with imports

2. **Machine Learning Fundamentals**
   - Research Focus: Supervised vs Unsupervised learning, Feature Engineering
   - Target Sources: Andrew Ng's Machine Learning course videos
   - Deliverable: List of algorithms suitable for the problem

3. **Feature Selection & Engineering**
   - Research Focus: Correlation analysis, One-Hot Encoding methods
   - Target Sources: Scikit-learn documentation, DataCamp lessons
   - Deliverable: Selected features and transformation plan

4. **Model Evaluation Techniques** ([Research Focus]: Cross-validation, ROC-AUC)
   - Target Sources: Coursera Machine Learning course notes
   - Deliverable: Evaluation metrics table with definitions

5. **Hyperparameter Tuning**
   - Research Focus: Grid Search vs Random Search
   - Target Sources: Kaggle articles on hyperparameter optimization
   - Deliverable: Hyperparameters to tune and search space definition

6. **Deployment Strategies** ([Research Focus]: REST API, Docker)
   - Target Sources: Real Python deployment guides
   - Deliverable: Deployment stack recommendation

7. **Model Monitoring & Maintenance**
   - Research Focus: Anomaly detection in model performance
   - Target Sources: Arize AI documentation
   - Deliverable: Monitoring KPI list and alert thresholds

8. **Data Privacy & Ethics**
   - Research Focus: GDPR compliance, Bias mitigation techniques
   - Target Sources: EU Data Protection guidelines, MIT's CS50 ethics course
   - Deliverable: Compliance checklist and bias audit plan

9. **Cloud Platforms for ML** ([Research Focus]: AWS SageMaker vs Google AI Platform)
   - Target Sources: Pricing tables, user reviews on Capterra
   - Deliverable: Recommended cloud platform with cost breakdown

10. **Version Control for Data Science**
    - Research Focus: Git branching strategies for experiments
    - Target Sources: DataCamp version control tutorials
    - Deliverable: Repository structure plan

11. **Automated Machine Learning (AutoML)**
    - Research Focus: Feature importance, model interpretability
    - Target Sources: H2O.ai documentation, Papers with Code
    - Deliverable: AutoML pipeline design and comparison of results

12. **Explainable AI Techniques** ([Research Focus]: SHAP values)
    - Target Sources: IBM's Explainable AI guide
    - Deliverable: Methodology for model interpretability

13. **Stakeholder Communication**
    - Research Focus: Visualizations, Business Case templates
    - Target Sources: Tableau tutorials, McKinsey reports
    - Deliverable: Presentation deck outline and KPI dashboard mockup

14. **Advanced Topics** ([Optional])
    - Reinforcement Learning for sequential decision problems
    - Graph Neural Networks for complex relationships in data

15. **Ethical AI & Bias Mitigation**
    - Research Focus: Fairness metrics, Model Auditing Tools
    - Target Sources: NIST AI risk management framework
    - Deliverable: Ethical compliance checklist and bias mitigation plan

---

## Phase 3: Execution Workflow

### Step-by-Step Process

**STEP 1: Data Preparation**
- **Action:** Clean data, handle missing values, encode categorical variables
- **Tools Needed:** Python (pandas), Jupyter Notebook
- **Success Criteria:** Dataset is clean and ready for modeling
- **Common Pitfalls:** Overfitting due to improper encoding or ignoring class imbalance
- **Time Estimate:** 1 week

**STEP 2: Exploratory Data Analysis**
- **Action:** Visualize distributions, check correlations, identify outliers
- **Tools Needed:** Python (matplotlib, seaborn), Excel for basic analysis
- **Success Criteria:** Insights on feature relationships and potential model performance
- **Common Pitfalls:** Drawing conclusions without statistical validation
- **Time Estimate:** 2 days

**STEP 3: Feature Engineering**
- **Action:** Create new features, transform existing ones, handle text data
- **Tools Needed:** Python (pandas), NLTK for text processing
- **Success Criteria:** Selected features are relevant and improve model performance
- **Common Pitfalls:** Overengineering leading to increased complexity
- **Time Estimate:** 3 days

**STEP 4: Model Selection**
- **Action:** Choose algorithms based on problem type, experiment with parameters
- **Tools Needed:** Python (scikit-learn), Hyperopt for tuning
- **Success Criteria:** Selected model achieves target accuracy
- **Common Pitfalls:** Choosing the most complex model without validation
- **Time Estimate:** 2 weeks

**STEP 5: Model Training**
- **Action:** Split data into training/validation/test sets, train models
- **Tools Needed:** Python (scikit-learn), GPU for deep learning
- **Success Criteria:** Model achieves >90% accuracy on validation set
- **Common Pitfalls:** Data leakage during split
- **Time Estimate:** 3 days

**STEP 6: Hyperparameter Tuning**
- **Action:** Use grid/random search to optimize model parameters
- **Tools Needed:** Python (Hyperopt), Cloud GPU instances for large models
- **Success Criteria:** Model performance improves by >5%
- **Common Pitfalls:** Overfitting during tuning process
- **Time Estimate:** 1 week

**STEP 7: Model Evaluation**
- **Action:** Use cross-validation, ROC-AUC, precision/recall metrics
- **Tools Needed:** Python (scikit-learn), Confusion Matrix visualization
- **Success Criteria:** Model meets >95% accuracy and business KPIs
- **Common Pitfalls:** Misinterpreting evaluation metrics
- **Time Estimate:** 2 days

**STEP 8: Deployment Planning**
- **Action:** Choose deployment method, containerize the model (Docker)
- **Tools Needed:** Python (Flask), Docker, AWS/GCP for cloud hosting
- **Success Criteria:** Model is deployable and accessible via API
- **Common Pitfalls:** Security vulnerabilities in container setup
- **Time Estimate:** 3 days

**STEP 9: Deployment & Monitoring**
- **Action:** Deploy model to production environment, set up monitoring alerts
- **Tools Needed:** AWS/GCP deployment tools, Prometheus for metrics monitoring
- **Success Criteria:** Model operates without errors for 1 week, no degradation in performance
- **Common Pitfalls:** Lack of post-deployment validation
- **Time Estimate:** Ongoing

**STEP 10: Documentation & Knowledge Transfer**
- **Action:** Document model architecture, deployment steps, maintenance plan
- **Tools Needed:** Confluence or Notion for documentation, Markdown files
- **Success Criteria:** Team can reproduce the project and understand the workflow
- **Common Pitfalls:** Incomplete documentation leading to knowledge gaps
- **Time Estimate:** 2 days

### Quality Checkpoints
1. **Checkpoint 1 (Post Step 3):** Validate EDA results with domain experts
   - Verify: Insights align with business problem and data quality checks

2. **Checkpoint 2 (Post Step 5):** Ensure model meets performance criteria on separate test set
   - Verify: Accuracy >=95%, other metrics meet thresholds

3. **Checkpoint 3 (Post Step 9):** Conduct load testing to ensure scalability
   - Verify: Model handles expected traffic without latency >200ms

---

## Phase 4: Optimization & Refinement

### Performance Metrics
1. **Primary Metric:** Validation Accuracy >= 95%
2. **Secondary Metrics:**
   - Training Time < 30 minutes per model iteration
   - Deployment Latency <= 100ms
3. **Long-term Metrics:**
   - Model Drift Detection Rate > 90%
   - Customer Satisfaction Score (if applicable) >= A

### Iterative Improvement Loop
1. Measure current performance against targets
2. Identify top 3 improvement opportunities
3. Implement changes based on:
   - Hyperparameter tuning, model selection
   - Additional feature engineering or data collection
4. Re-measure after each change to confirm impact
5. Repeat until all metrics are met and maintained

---

## Phase 5: Reporting & Documentation

### Deliverables

**1. Executive Summary**
- Current State vs Target State
- Key Actions Taken (list model development steps)
- Results Achieved (accuracy, latency, etc.)
- ROI or Impact Metrics

**2. Detailed Report**
- Methodology Document
- Research Findings Section
- Implementation Log with Screenshots/Code Snippets
- Before/After Performance Comparison Table

**3. Maintenance Plan**
- Ongoing Tasks: Model retraining every 30 days, data quality checks weekly
- Monitoring Schedule: Daily performance metrics, Weekly anomaly alerts
- Update Frequency: Quarterly review and upgrade process
- Contingency Procedures: Rollback plan if model fails to meet targets

**4. Knowledge Transfer**
- Training Materials: Python notebook for new team members
- SOPs: How to reproduce the project, Model version control procedures
- Best Practices Documentation: Data handling, Feature selection, Evaluation metrics
- Troubleshooting Guide: Common errors and fixes during deployment

---

## Tool Stack Recommendations (2024)

### Primary Tools (FREE/OPTIONAL)
1. **Python** ([Free] - essential for modeling): v3.9+
2. **Jupyter Notebook** ([Free]) for prototyping
3. **VS Code** ([Free, recommended]) or PyCharm Community Edition ([optional])
4. **Pandas**, **NumPy**, **SciKit-Learn** (all free) for data manipulation and modeling
5. **Matplotlib**, **Seaborn** (free) for visualization
6. **Docker** ([free]) for containerization during deployment
7. **Kubernetes** ([optional, paid alternatives: Amazon EKS, Google GKE])
8. **GitLab CI/CD** ([free]) or GitHub Actions for automated testing
9. **Slack/Discord** (free) for team communication

### Optional/Premium Tools
1. **AWS SageMaker** ([paid premium alternative]) - Managed MLOps platform
2. **Google AI Platform** ([paid premium alternative]) - Automated model tuning and deployment
3. **Hugging Face Accelerator** ([optional, free tier]) - For large language models
4. **Splunk Enterprise** ([paid, optional]) - Advanced logging and monitoring
5. **Dashing.io** ([paid, optional]) - Real-time dashboard for model performance

### Pricing Overview (2024)

| Tool | Free Tier | Paid Options |
|------|-----------|--------------|
| Python | Yes | N/A |
| VS Code | Yes | Community Edition ($0) |
| Jupyter Notebook | Yes | N/A |
| GitLab CI/CD | Yes | Premium modules available for teams (>5 members) |
| Docker | Yes | Cloud registry (Docker Hub) has free tier |
| Kubernetes | Free | Managed services like GKE, EKS are optional paid alternatives |
| Slack/Discord | Yes | Standard plan is free |

---

## Success Validation

Before marking the project as COMPLETE:

- [ ] **Did the model achieve 95%+ accuracy on independent validation data?** (Yes/No)
- [ ] **Is the deployment fully operational and accessible via API with <200ms latency?** (Yes/No)
- [ ] **Do monitoring tools detect any performance degradation or bias over time?** (Yes/No)
- [ ] **Are all stakeholders satisfied with the model's business impact?** (Yes/No)

---

## Continuous Improvement

1. Schedule a quarterly review to assess model drift and retraining needs
2. Document lessons learned from each project phase for future reference
3. Share best practices within team or open-source community via GitHub
4. Automate periodic audits of model fairness using tools like Elicit
5. Explore advanced techniques (e.g., federated learning) as they become available

---

This template provides a comprehensive roadmap for Data Scientists aiming to develop and test models that meet specific business objectives. It is structured to be highly actionable, with measurable success criteria, timelines, and detailed steps to follow, ensuring the project can be completed within the specified timeframe while maintaining quality and scalability.

