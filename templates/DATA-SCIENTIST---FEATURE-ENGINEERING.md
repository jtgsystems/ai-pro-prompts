# Data Scientist - AI Agent Template
## Feature Engineering

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve data scientist-specific ultimate goals related to feature engineering.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Data Scientist"
profession_category: "Technology/Analytics"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal
**Primary Objective:** Successfully engineer high-quality features from raw data that significantly improve the performance of predictive models, while maintaining interpretability and scalability.

Example:
- **Success Metrics:** Achieve a 15% increase in model accuracy (e.g., AUC) on validation datasets; maintain feature selection metrics within acceptable ranges; ensure computational efficiency for deployment.
- **Validations:** Regularly test engineered features against baseline models to ensure improvements.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Dataset(s) containing raw data (e.g., CSV, SQL database)
   - Format: File paths or database connection strings.
   - Validation: Confirm dataset availability and access permissions.

2. **Input 2:** Target variable(s) for prediction/analysis
   - Format: Column names in the dataset.
   - Validation: Ensure target variable is present and correctly labeled.

3. **Input 3:** Business problem/domain knowledge (e.g., customer churn, fraud detection)
   - Format: Brief description of use case.
   - Validation: Verify relevance to feature engineering tasks.

4. **Input 4:** Model performance metrics (baseline AUC, accuracy, etc.)
   - Format: Numeric values or ranges.
   - Validation: Ensure these are current and accurate.

5. **Input 5:** Computational resources available (CPU cores, memory)
   - Format: Resource specifications.
   - Validation: Confirm system can handle feature engineering tasks.

### Initial Assessment Checklist
- [ ] Verify all required inputs received.
- [ ] Validate input quality and completeness.
- [ ] Identify immediate red flags or blockers.
- [ ] Establish baseline metrics (current state performance).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Data Cleaning Techniques
- Research Focus: Methods for handling missing data, outliers, and inconsistencies.
- Target Sources: Kaggle notebooks, academic papers on preprocessing.

**Topic 2:** Feature Scaling and Normalization
- Research Focus: Best practices for scaling features using Z-score or Min-Max normalization.
- Target Sources: Scikit-learn documentation, research articles on feature scaling impact.

**Topic 3:** Encoding Categorical Variables
- Research Focus: Techniques such as one-hot encoding, label encoding, ordinal encoding.
- Target Sources: DataCamp tutorials, Stack Overflow discussions.

**Topic 4:** Dimensionality Reduction Methods
- Research Focus: Principal Component Analysis (PCA), t-SNE, autoencoders.
- Target Sources: AppliedML guide, academic papers on dimensionality reduction for ML.

**Topic 5:** Time Series Feature Engineering
- Research Focus: Lag features, rolling statistics, seasonality extraction.
- Target Sources: Time Series Analysis books, Kaggle competitions.

**Topic 6:** Text Feature Extraction
- Research Focus: TF-IDF, word embeddings (Word2Vec, BERT), NLP preprocessing steps.
- Target Sources: NLTK tutorials, Hugging Face documentation.

**Topic 7:** Image Feature Engineering
- Research Focus: Color histograms, texture features, CNN-based feature extraction.
- Target Sources: OpenCV guides, PyTorch image models.

**Topic 8:** Interaction and Polynomial Features
- Research Focus: Creating higher-order interaction terms, polynomial expansions.
- Target Sources: Statistical modeling books, scikit-learn API docs.

**Topic 9:** Domain-Specific Feature Engineering Techniques
- Research Focus: Industry-specific transformations (e.g., financial ratios for banking).
- Target Sources: Case studies from domain experts, industry whitepapers.

**Topic 10:** Automated Feature Engineering Tools
- Research Focus: Libraries like Featuretools, AutoFeatureEngine.
- Target Sources: Official documentation, GitHub repositories with examples.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on model performance.
4. Create master action plan.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Data Loading and Inspection**
- **Action:** Load datasets into a DataFrame using pandas; perform exploratory data analysis (EDA) to understand distributions, missing values, and correlations.
- **Tools Needed:** Python scripts with `pandas`, `numpy`.
- **Success Criteria:** Dataset successfully loaded without errors; summary statistics provided.
- **Common Pitfalls:** Incorrect file paths, incompatible data types.
- **Time Estimate:** 30 minutes

**STEP 2: Initial Data Cleaning**
- **Action:** Identify and handle missing values using imputation or removal based on the distribution. Detect and treat outliers using statistical methods (e.g., Z-score).
- **Tools Needed:** Python scripts with `pandas`, `numpy`.
- **Success Criteria:** Missing data handled; outliers either removed or capped.
- **Common Pitfalls:** Over-imputation leading to artificial correlations.
- **Time Estimate:** 45 minutes

**STEP 3: Encoding Categorical Variables**
- **Action:** Convert categorical columns into numerical representations using one-hot encoding for nominal variables and label encoding for ordinal variables.
- **Tools Needed:** Python scripts with `pandas`, scikit-learn's `OneHotEncoder`.
- **Success Criteria:** All categorical features transformed to numeric without NaN values.
- **Common Pitfalls:** Misapplication of encoding leading to the curse of dimensionality.
- **Time Estimate:** 1 hour

**STEP 4: Feature Scaling**
- **Action:** Scale numerical features using Z-score normalization; ensure data distribution remains approximately Gaussian after scaling.
- **Tools Needed:** Python scripts with `scikit-learn`.
- **Success Criteria:** Features have zero mean and unit variance.
- **Common Pitfalls:** Incorrect application of scale to non-Gaussian distributions.
- **Time Estimate:** 30 minutes

**STEP 5: Dimensionality Reduction (if needed)**
- **Action:** Apply PCA or other methods to reduce feature space while retaining most variance.
- **Tools Needed:** Python scripts with `scikit-learn`.
- **Success Criteria:** Reduced dataset retains >95% of original variance; no significant drop in model performance.
- **Common Pitfalls:** Overfitting during reduction leading to loss of important information.
- **Time Estimate:** 2 hours

**STEP 6: Time Series Feature Engineering**
- **Action:** For time-series data, create lag features and rolling statistics (e.g., mean, standard deviation) over defined windows.
- **Tools Needed:** Python scripts with `pandas`.
- **Success Criteria:** All relevant time-based features added; no missing values introduced.
- **Common Pitfalls:** Incorrect window sizes leading to shifted or overlapping data points.
- **Time Estimate:** 1.5 hours

**STEP 7: Text Feature Engineering**
- **Action:** Tokenize text, remove stop words, apply TF-IDF transformation; for deep learning models, consider embedding layers.
- **Tools Needed:** Python scripts with `scikit-learn`, spaCy, Hugging Face Transformers.
- **Success Criteria:** Text data transformed into suitable numerical features without introducing noise.
- **Common Pitfalls:** Ignoring language-specific nuances leading to loss of semantic information.
- **Time Estimate:** 2 hours

**STEP 8: Image Feature Engineering**
- **Action:** Extract color histograms, texture descriptors; for deep learning, consider pre-trained CNN models for feature extraction.
- **Tools Needed:** Python scripts with `scikit-image`, TensorFlow/Keras for CNN features.
- **Success Criteria:** Images represented as numerical vectors suitable for model input.
- **Common Pitfalls:** Overlooking the impact of image rotations/scale on feature representation.
- **Time Estimate:** 1.5 hours

**STEP 9: Interaction and Polynomial Features**
- **Action:** Generate interaction terms (e.g., A*B) and polynomial expansions to capture non-linear relationships.
- **Tools Needed:** Python scripts with `pandas`, scikit-learn's polynomial features.
- **Success Criteria:** New features added without excessive dimensionality increase; model performance stable after feature addition.
- **Common Pitfalls:** Overfitting due to too many interaction terms.
- **Time Estimate:** 45 minutes

**STEP 10: Automated Feature Engineering (optional)**
- **Action:** Use libraries like Featuretools or AutoFeatureEngine to automatically generate relevant features based on the data schema.
- **Tools Needed:** Python scripts with `featuretools`, `autofeat`.
- **Success Criteria:** Automatically generated features are logically meaningful and improve model performance.
- **Common Pitfalls:** Over-reliance without validation of feature relevance.
- **Time Estimate:** 2 hours

### Quality Checkpoints
Insert checkpoints between major steps:
- **Checkpoint 1:** After Step 5 - Verify that dimensionality reduction does not significantly degrade model accuracy.
- **Checkpoint 2:** After Step 9 - Confirm no overfitting and reasonable computational cost.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Model Accuracy/AUC improvement (target >15% increase)
   - Target: Achieve at least a 15% increase in AUC compared to baseline.
   - Measurement Method: Cross-validation on validation dataset.

2. **Secondary Metrics:**
   - Feature Importance Stability: Ensure top features remain consistent across folds.
   - Computational Efficiency: Time taken for training and inference post-engineering.
   - Interpretability Score (if domain requires): Subjective score from domain experts.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 areas for improvement through feature engineering.
3. Implement changes iteratively, documenting each step.
4. Re-measure until all primary metrics are met.
5. Repeat the loop with secondary metrics if needed.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables

**1. Executive Summary**
- [ ] Current state vs. target state (e.g., baseline AUC = 0.75, Target = 0.90).
- [ ] Key actions taken (feature engineering techniques applied).
- [ ] Results achieved (metrics post-engineering).
- [ ] ROI or impact metrics (percentage increase in model performance).

**2. Detailed Report**
- [ ] Complete methodology document including data sources, cleaning steps, and feature engineering process.
- [ ] All research findings with citations to source documents.
- [ ] Implementation details of each step with code snippets.
- [ ] Before/after comparison tables showing metric improvements.

**3. Maintenance Plan**
- [ ] Ongoing tasks such as periodic retraining of models and updating features.
- [ ] Monitoring schedule (e.g., weekly performance checks).
- [ ] Update frequency for feature engineering based on model drift detection.
- [ ] Contingency procedures for handling data source changes or regulatory updates.

**4. Knowledge Transfer**
- [ ] Training materials for junior Data Scientists on the feature engineering process.
- [ ] Standard Operating Procedures (SOPs) document outlining best practices.
- [ ] Troubleshooting guide addressing common issues encountered during execution.
- [ ] Documentation of lessons learned and future research directions.

---

## RESEARCH SUB-AGENT CONFIGURATION

### Agent Deployment Template
```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "[Data Cleaning Techniques]"
    focus: "Best practices for handling missing data, outliers"
    sources: ["Kaggle notebooks", "Academic papers on preprocessing"]
    deliverable: "List of cleaning steps with code examples and rationales"

  - agent_id: 2
    topic: "[Feature Scaling Methods]"
    focus: "Impact of scaling on model performance"
    sources: ["Scikit-learn docs", "Research articles on feature scaling"]
    deliverable: "Recommended scaling method with parameter recommendations"

  # [Continue for agents 3-10]

consolidation_process:
  1. Collect all agent reports
  2. Cross-reference findings for consistency
  3. Resolve conflicts by source authority
  4. Prioritize by impact to ultimate goal
  5. Generate unified recommendation report
```

---

## SUCCESS VALIDATION

### Final Checklist
Before marking the profession task as COMPLETE:

- [ ] **Primary Objective Achieved?** [Model accuracy improved by target metrics]
- [ ] **All Metrics Met?** [AUC, AUPR, model stability, etc. all meet targets]
- [ ] **Quality Validated?** [Features are logically sound and technically feasible]
- [ ] **Documentation Complete?** [All deliverables provided in required formats]
- [ ] **Sustainability Ensured?** [Maintenance plan documented and resources allocated]

### Continuous Improvement
- Document lessons learned from the project.
- Update this template with new best practices discovered during implementation.
- Share insights with peers through knowledge-sharing sessions or publications.
- Schedule periodic reviews to assess ongoing relevance of features.

---

## TEMPLATE METADATA

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Data Scientist (Beginner to Intermediate)  
**Success Rate:** [To be updated post-completion]  
**Average Time to Goal:** Approximately 12 hours for a beginner with intermediate Python skills.

---

*This master template should be copied and customized for each specific profession or task. The framework remains constant, but the details within each section are profession-specific.*

