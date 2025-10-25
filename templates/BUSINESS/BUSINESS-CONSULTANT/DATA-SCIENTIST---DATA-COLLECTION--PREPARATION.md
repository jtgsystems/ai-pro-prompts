# Data Scientist - AI Agent Template
## Data Collection & Preparation

### Success Definition (Measurable)
**Primary Objective:** To collect, clean, preprocess, and prepare high-quality datasets suitable for advanced analytics, machine learning model training, and statistical analysis within a 45-day period.

- **Data Quality Score**: Minimum of 90% with <5% missing values after cleaning
- **Feature Engineering Completeness**: At least 80 features engineered from raw data
- **Documentation Completion Rate**: All datasets documented with version control (Git)
- **Model Training Success Rate**: Achieve ≥85% accuracy on a baseline model using the prepared dataset

### Critical Knowledge Areas for Data Scientist

1. **Data Ingestion & APIs**
   - Understanding RESTful and GraphQL APIs
   - Using tools like Postman, Insomnia for testing endpoints
   - Handling rate limits and pagination

2. **Web Scraping Techniques**
   - Navigating dynamic content with Selenium/Playwright
   - Capturing structured data using BeautifulSoup/pandas
   - Rate limiting and IP rotation best practices

3. **Database Management Systems (DBMS)**
   - SQL fundamentals for querying relational databases
   - NoSQL basics: MongoDB, Cassandra, DynamoDB schema design
   - ORM tools like SQLAlchemy/ORM

4. **Data Storage & Staging**
   - Cloud storage options: AWS S3, Azure Blob, Google Cloud Storage
   - Data warehouses: Amazon Redshift, Snowflake, BigQuery
   - Implementing staging environments for data transformation

5. **ETL Processes**
   - Extract: Using Python libraries like Pandas, SQLalchemy
   - Transform: Cleaning missing values, encoding categorical variables, feature scaling
   - Load: Into databases, data lakes, or ML platforms

6. **Data Validation & Quality Assurance**
   - Statistical checks for outliers and distributions
   - Consistency rules across datasets
   - Data lineage tracking using tools like Apache Atlas

7. **Feature Engineering Techniques**
   - Encoding strategies (one-hot, label encoding)
   - Normalization/Standardization methods
   - Time series feature creation (lag features, rolling stats)

8. **Missing Value Imputation Strategies**
   - Mean/Median imputation for numerical data
   - Mode imputation for categorical variables
   - Advanced: KNN, MICE techniques

9. **Outlier Detection & Treatment**
   - Statistical methods: Z-score, IQR
   - Visualization techniques: Boxplots, scatter plots
   - Transformations to reduce impact (log/sqrt)

10. **Data Normalization & Standardization**
    - Min-Max Scaling for bounded data
    - Z-Score normalization for Gaussian distributions

11. **Dimensionality Reduction Techniques**
    - Principal Component Analysis (PCA)
    - t-Distributed Stochastic Neighbor Embedding (t-SNE)
    - Feature selection methods: Lasso, Ridge Regression

12. **Data Validation Frameworks**
    - Great Expectations for defining business rules
    - Pandera for declarative data validation schemas

13. **Version Control & Collaboration Tools**
    - Git for code versioning and documentation
    - GitHub/GitLab projects for workflow management
    - Jupyter Notebook integration with Git hooks

14. **Automated Data Pipelines**
    - Airflow or Prefect orchestration platforms
    - Dagster event-driven pipeline framework
    - AWS Glue, Azure Data Factory as ETL execution engines

### Execution Workflow (Detailed Steps)

#### Step 1: Define Project Requirements & Objectives
- **Action**: Conduct stakeholder interviews to understand business questions and data needs.
- **Tools**: Confluence for requirements documentation; Miro for collaborative mapping.
- **Success Criteria**: Documented project charter with SMART objectives, approved by stakeholders.
- **Timeline**: Complete within 5 days.

#### Step 2: Ingest Data from Diverse Sources
- **Action**: Identify all data sources (APIs, databases, files).
- **Tools**: Postman for API testing; Python scripts using `requests` library for automated calls.
- **Success Criteria**: Raw datasets stored in a secure staging area with timestamps and source metadata.
- **Timeline**: 10 days.

#### Step 3: Perform Initial Data Cleaning
- **Action**: Handle missing values, inconsistent formats, duplicates.
- **Tools**: Pandas for DataFrame operations; Great Expectations for validation rules.
- **Success Criteria**: Clean datasets meet the data quality score of ≥90% with <5% missing values.
- **Timeline**: 7 days.

#### Step 4: Feature Engineering
- **Action**: Create engineered features from raw data to support ML models or statistical analysis.
- **Tools**: Python (NumPy, Pandas); scikit-learn for feature transformations; PySpark for large datasets.
- **Success Criteria**: At least 80% of planned features successfully implemented and validated.
- **Timeline**: 10 days.

#### Step 5: Data Validation & Testing
- **Action**: Validate data quality using statistical tests and business rules.
- **Tools**: Great Expectations, Pandera for validation schemas; JUnit for automated testing in Python.
- **Success Criteria**: All validation checks pass with >95% success rate across datasets.
- **Timeline**: 5 days.

#### Step 6: Dimensionality Reduction & Feature Selection
- **Action**: Apply techniques to reduce dataset size without losing predictive power.
- **Tools**: scikit-learn for PCA, Lasso; Python notebooks integrated with JupyterHub.
- **Success Criteria**: Reduced datasets meet model training requirements within computational constraints.
- **Timeline**: 5 days.

#### Step 7: Data Validation Framework Deployment
- **Action**: Set up automated data quality checks in the pipeline.
- **Tools**: Great Expectations CI/CD integration; GitHub Actions for continuous validation.
- **Success Criteria**: Automated alerts triggered on any data quality breach detected by the framework.
- **Timeline**: 3 days.

#### Step 8: Documentation & Knowledge Transfer
- **Action**: Document every step of the process, including raw data provenance and transformation logic.
- **Tools**: Confluence pages; Git for version-controlled documentation.
- **Success Criteria**: Comprehensive README files for each dataset, clear lineage diagrams.
- **Timeline**: Ongoing throughout execution.

#### Step 9: Validation with Sample Data
- **Action**: Use a subset of the data to validate model training processes.
- **Tools**: scikit-learn for baseline ML models; Jupyter Notebooks for experimentation.
- **Success Criteria**: Achieve ≥85% accuracy on the sample dataset using chosen models.
- **Timeline**: 5 days.

#### Step 10: Continuous Monitoring & Maintenance Plan
- **Action**: Set up a monitoring system to track data quality over time and trigger alerts for anomalies.
- **Tools**: Prometheus + Grafana dashboards; Sentry for error tracking in production pipelines.
- **Success Criteria**: Automated alerts are functional, and the monitoring dashboard shows stable metrics.
- **Timeline**: Ongoing.

### Troubleshooting Common Issues

1. **API Rate Limiting**
   - Solution: Implement exponential backoff strategy with retries
   - Tool: `requests` library with `Retry` middleware

2. **Inconsistent Data Formats**
   - Solution: Standardize using schemas (JSON Schema, Avro)
   - Tool: Great Expectations for schema validation

3. **Memory Errors During Transformation**
   - Solution: Use Dask or PySpark for out-of-core processing
   - Tool: Python `pandas` with chunksize option; Spark cluster on AWS EMR

4. **Data Leakage in Model Training**
   - Solution: Ensure temporal splitting of data if time series models are used
   - Tool: scikit-learn's `TimeSeriesSplit`

5. **Feature Engineering Complexity**
   - Solution: Break down into smaller microservices or functions
   - Tool: Python decorators for reusable transformations

### Recommended Tool Stack (2024-2025)

#### Primary Tools (Free/Open Source)
1. **Data Ingestion & APIs**: Python `requests`, Postman, Insomnia
2. **Database Access**: SQLAlchemy ORM, psycopg2 (PostgreSQL), MySQL Connector
3. **ETL Processing**: Apache Spark (PySpark) for big data; Pandas for smaller datasets
4. **Feature Engineering**: scikit-learn, pandas-profiling for exploratory analysis
5. **Data Validation**: Great Expectations, Pandera
6. **Documentation & Collaboration**: Confluence, Miro, GitHub, GitLab
7. **Version Control & CI/CD**: Git, GitHub Actions, Docker Compose
8. **Monitoring & Alerting**: Prometheus + Grafana, Sentry

#### Optional Paid Tools (Premium Alternatives)
1. **ETL Orchestration**: Apache Airflow Enterprise Edition (paid components), Prefect Cloud
2. **Data Warehousing**: Snowflake Unlimited tier, Redshift Serverless
3. **Machine Learning Experiment Tracking**: MLflow with server component (premium)
4. **Advanced Feature Engineering**: AWS Glue DataBrew for automated feature discovery

### Realistic Timeline to Achieve Data Collection & Preparation

**Phase 1: Planning and Requirements Gathering**
- Days: 5-7
- Deliverables:
  - Project charter approved by stakeholders
  - Initial requirements document in Confluence

**Phase 2: Ingestion, Cleaning, and Validation**
- Days: 22-28
- Deliverables:
  - Raw datasets stored securely with metadata
  - Cleaned datasets meeting ≥90% data quality score
  - Automated validation framework operational

**Phase 3: Feature Engineering & Modeling Prep**
- Days: 21-30
- Deliverables:
  - Engineered features ready for ML models
  - Data documentation complete and version-controlled
  - Baseline model trained on prepared dataset achieving ≥85% accuracy

**Phase 4: Deployment, Monitoring, and Maintenance**
- Ongoing
- Deliverables:
  - Production-ready pipeline deployed (Airflow/Prefect)
  - Automated monitoring dashboard in Prometheus/Grafana
  - Documentation updated for future maintenance tasks

### Final Review Checklist Before Project Closure

1. **Data Quality**: All datasets meet the defined quality metrics.
2. **Feature Completeness**: At least 80% of planned features implemented and validated.
3. **Model Training Success**: Baseline model meets accuracy requirement on sample data.
4. **Validation Framework**: Fully integrated into CI/CD pipeline with automated tests passing.
5. **Documentation**: All processes documented in Confluence with version control in Git.
6. **Monitoring Setup**: Dashboards live, alerts configured for critical metrics.
7. **Stakeholder Sign-off**: Final review and approval from business owners.

By following this structured template, a Data Scientist can efficiently collect, clean, prepare, and validate datasets ready for advanced analytics or machine learning projects within the specified 45-day timeframe.

