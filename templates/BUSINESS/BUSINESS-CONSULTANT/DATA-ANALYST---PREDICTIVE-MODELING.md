# Data Analyst - AI Agent Template
## Predictive Modeling

### Success Definition (Measurable)
Predictive modeling success is defined as:
1. A model achieving an R² score of ≥ 0.8 on a holdout test dataset.
2. Feature importance scores explaining at least 70% variance in target variable.
3. Latency under 100ms for real-time predictions with batch processing ≤ 5 minutes per 1 million records.

### Critical Knowledge Areas (Specific to Data Analyst)

**Topic 1:** Statistical Analysis
- Focus: Descriptive statistics, probability distributions, hypothesis testing  
- Sources: Books, courses - "Statistical Methods" by David Moore

**Topic 2:** Machine Learning Fundamentals
- Focus: Supervised learning algorithms, feature engineering, model evaluation metrics  
- Tools: Scikit-learn (free), TensorFlow (optional)

**Topic 3:** Data Cleaning & Preprocessing
- Focus: Handling missing data, outliers, categorical encoding, normalization  
- Techniques: Imputation strategies, One-Hot Encoding

**Topic 4:** Exploratory Data Analysis (EDA)
- Focus: Visualizing distributions, correlations, identifying patterns in large datasets using pandas and matplotlib/seaborn  

**Topic 5:** Feature Selection & Engineering
- Focus: Correlation analysis, Principal Component Analysis, time-series features  
- Tools: Pandas-profiling (free), Scikit-learn

**Topic 6:** Model Deployment Best Practices
- Focus: API integration, monitoring, automated retraining pipelines  
- Platforms: AWS SageMaker (free tier available), Azure ML

**Topic 7:** Data Governance & Ethics
- Focus: Compliance with regulations (GDPR), bias mitigation techniques  
- Tools: IBM AI Fairness 360 (free)

**Topic 8:** Predictive Analytics Use Cases
- Focus: Customer churn, demand forecasting, fraud detection  
- Applications: Retail sales, banking, e-commerce

**Topic 9:** Data Visualization for Insights
- Focus: Interactive dashboards, heatmaps, probability distributions, decision boundaries  
- Tools: Plotly (free), Tableau Public (optional)

**Topic 10:** Cloud-Based Data Infrastructure
- Focus: Scalable storage solutions, compute resources for big data analysis  
- Platforms: AWS S3 (free tier), Google BigQuery

### Execution Steps with Specific Actions

**STEP 1: [Data Collection & Ingestion]**
- **Action:** Identify and extract relevant datasets from various sources:
  - Transactional databases
  - Customer relationship management systems
  - External data providers (credit bureaus, market trends)
- **Tools Needed:** SQL queries for database extraction, APIs for external data access (e.g., RapidAPI), Pandas Dataframe in Python
- **Success Criteria:** All required datasets are ingested and stored in a unified format.
- **Common Pitfalls:** Missing or incompatible data formats; Time delays exceeding 2 hours.
- **Time Estimate:** 4-6 hours

**STEP 2: [Data Cleaning & Preprocessing]**
- **Action:** Handle missing values, outliers, and categorical variables:
  - Use imputation techniques for missing numerical data (mean/median imputation)
  - Encode categorical features using one-hot encoding
  - Identify outliers using Z-score or IQR method and treat accordingly
- **Tools Needed:** Python Pandas library for data manipulation; Scikit-learn for advanced preprocessing.
- **Success Criteria:** Data quality score ≥ 90% (no missing critical fields, no null values in required columns).
- **Common Pitfalls:** Incomplete imputation leading to biased models; Incorrect encoding causing multicollinearity.
- **Time Estimate:** 6 hours

**STEP 3: [Exploratory Data Analysis]**
- **Action:** Perform initial analysis to understand data distribution and relationships:
  - Visualize distributions using histograms/boxplots
  - Use correlation matrices to identify feature dependencies
  - Apply dimensionality reduction techniques like PCA for high-dimensional datasets
- **Tools Needed:** Python libraries: Matplotlib, Seaborn; Pandas-profiling for automated EDA reports.
- **Success Criteria:** Generate a comprehensive EDA report with key insights (e.g., top correlated features).
- **Common Pitfalls:** Ignoring multicollinearity leading to unstable models; Overlooking data drift over time.
- **Time Estimate:** 8 hours

**STEP 4: [Feature Engineering]**
- **Action:** Create new features that may improve model performance:
  - Time-based features (e.g., day of week, rolling averages)
  - Interaction terms between categorical and numerical features
  - Domain-specific engineered variables
- **Tools Needed:** Python Pandas for feature creation; Scikit-learn for advanced transformations.
- **Success Criteria:** Model achieves ≥ 0.75 R² score with these engineered features as baseline.
- **Common Pitfalls:** Overfitting due to too many engineered features; Missing domain knowledge leading to irrelevant features.
- **Time Estimate:** 6 hours

**STEP 5: [Model Selection & Training]**
- **Action:** Choose appropriate machine learning algorithms and train models:
  - Start with simple models (Linear Regression, Decision Trees) for baseline
  - Experiment with ensemble methods (Random Forest, Gradient Boosting)
  - Use cross-validation to tune hyperparameters
- **Tools Needed:** Scikit-learn for model training; Hyperopt or Optuna for automated hyperparameter tuning.
- **Success Criteria:** Model achieves ≥ 0.8 R² score on holdout dataset and < 10% error rate on validation set.
- **Common Pitfalls:** Overfitting due to complex models; Ignoring feature importance affecting interpretability.
- **Time Estimate:** 12 hours

**STEP 6: [Model Evaluation & Validation]**
- **Action:** Validate model performance using appropriate metrics:
  - For regression tasks, use R² score, RMSE (Root Mean Square Error), MAE (Mean Absolute Error)
  - Perform K-fold cross-validation to ensure robustness
  - Analyze feature importance and SHAP values for interpretability
- **Tools Needed:** Scikit-learn for evaluation metrics; SHAP library for model explainability.
- **Success Criteria:** Achieve ≥ 0.8 R² score, RMSE ≤ threshold (e.g., < 5), Feature importance explained ≥ 70% variance.
- **Common Pitfalls:** Using incorrect evaluation metric leading to suboptimal models; Ignoring feature interaction effects.
- **Time Estimate:** 6 hours

**STEP 7: [Deployment Preparation]**
- **Action:** Prepare model for deployment:
  - Export trained model using Pickle or joblib
  - Create API endpoints for real-time predictions (using FastAPI)
  - Set up automated retraining pipelines triggered by new data availability
- **Tools Needed:** Python Pickle/Joblib; Docker for containerization; AWS SageMaker or Azure ML for cloud deployment.
- **Success Criteria:** Model deployed in production environment with < 100ms latency for single predictions and batch processing ≤ 5 minutes per 1 million records.
- **Common Pitfalls:** Missing data dependencies leading to runtime errors; Security vulnerabilities in API endpoints.
- **Time Estimate:** 8 hours

**STEP 8: [Monitoring & Maintenance]**
- **Action:** Establish continuous monitoring and maintenance processes:
  - Track model performance metrics over time (e.g., R², latency)
  - Set up alerts for data drift or quality degradation
  - Schedule periodic retraining with new data batches
- **Tools Needed:** Prometheus/Grafana for real-time monitoring; AWS CloudWatch or Azure Monitor.
- **Success Criteria:** Model maintains ≥ 0.8 R² score and <100ms latency after each deployment cycle.
- **Common Pitfalls:** Lack of monitoring leading to gradual performance degradation; Overlooking data drift causing biased predictions.
- **Time Estimate:** Ongoing

### Tools & Software (Primary Free Tools)

**Data Ingestion:**
1. SQL for relational databases
2. REST APIs with Python requests library
3. AWS S3 or Google Cloud Storage for raw data storage

**Data Processing & Engineering:**
1. Python Pandas library for DataFrame manipulation
2. Jupyter Notebooks for interactive analysis and documentation
3. Scikit-learn for machine learning algorithms and feature engineering

**Visualization:**
1. Matplotlib, Seaborn for statistical plots
2. Plotly for interactive dashboards (free tier available)

**Model Deployment:**
1. FastAPI framework for API endpoints
2. Docker containers for deployment consistency
3. AWS SageMaker or Azure ML for cloud hosting (SageMaker is free tier accessible)

**Monitoring & Maintenance:**
1. Prometheus/Grafana stack for real-time metrics
2. Airflow for workflow orchestration and scheduling
3. Jupyter Notebooks for retraining pipelines

### Troubleshooting Common Issues

**Data Ingestion Failures:**
- Verify API endpoints are reachable (use curl or Postman)
- Check database credentials and connection strings
- Ensure rate limits are not exceeded

**Model Training Errors:**
- Inspect data types - ensure numerical columns are float/integer
- Remove outliers temporarily to isolate issues
- Run training in a smaller subset for debugging

**Deployment Failures:**
- Verify container image size is within free tier limits
- Check API gateway configurations (e.g., CORS, rate limiting)
- Test with simple unit tests before scaling up

**Monitoring Drifts:**
- Use anomaly detection on key performance metrics
- Compare feature distributions between training and live data
- Schedule periodic manual checks for critical failures

### Recommended Tool Stack (2024-2025)

**Primary Tools (Free/Open Source)**
1. **Python 3.x** with libraries:
   - Pandas: Data manipulation
   - NumPy: Numerical operations
   - Scikit-learn: Machine learning models
   - Matplotlib/Seaborn: Visualization
   - Plotly: Interactive dashboards

2. **SQL**: For relational database queries (e.g., MySQL Community Edition)

3. **FastAPI + Docker**: API development and containerization for deployment

**Optional Premium Tools**
1. **AWS SageMaker**: Cloud-based model hosting with managed infrastructure
2. **Azure ML**: Similar cloud capabilities with Azure ecosystem integration
3. **Tableau Public**: Advanced data visualization (free tier available)
4. **IBM AI Fairness 360**: Bias detection tools for fairness audits

**Timeline to Achieve Predictive Modeling**

**Week 1-2: Data Collection & Ingestion**
- Focus on gathering all necessary datasets, ensuring quality and structure.

**Week 3: Data Cleaning & Preprocessing**
- Dedicate time to handle missing values, outliers, and encode categorical variables.

**Week 4: Exploratory Data Analysis**
- Allocate for initial analysis to uncover patterns and relationships in data.

**Week 5: Feature Engineering & Model Selection**
- Spend on creating new features and experimenting with different algorithms.

**Week 6: Training & Evaluation**
- Core development phase focusing on model training, validation, and evaluation.

**Week 7: Deployment Preparation**
- Prepare for moving the model to production environment, ensuring scalability and security.

**Week 8: Monitoring & Maintenance Setup**
- Establish processes for ongoing monitoring, maintenance, and updates of the deployed model.

