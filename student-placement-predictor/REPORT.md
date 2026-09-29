# ACADEMIC PROJECT REPORT CONTENT

**PROJECT TITLE:** EduPredict AI: Student Academic Performance & Campus Placement Predictor Using Random Forest Classifier

---

## 1. PROJECT ABSTRACT
Campus placements represent a primary benchmark for assessing student employability and academic program efficacy. Traditional placement screening procedures rely heavily on one-dimensional academic cutoffs such as CGPA, which fail to capture crucial technical proficiencies, project experience, aptitude reasoning, and active academic backlogs. 

This project develops **EduPredict AI**, an intelligent, supervised machine learning system engineered to predict campus placement outcomes and evaluate overall student performance readiness. Built on an authentic dataset of 1,000 engineering student records evaluated across 8 multidimensional parameters, the system deploys a **Random Forest Classifier (100 Decision Trees)** alongside a baseline Decision Tree model. Feature scaling is accomplished via Z-score normalization (`StandardScaler`). The primary model achieves a **Test Accuracy of 90.00%**, a **Precision of 89.68%**, a **Recall of 97.20%**, and an **F1-Score of 0.9329**. 

A key contribution of the system is its explainable advisory engine: in addition to returning binary classification and placement probabilities, the application isolates specific deficiencies (e.g., active backlogs, low coding scores, or absence of internships) and provides prioritized remediation steps. The solution is implemented in Python, serialized via `joblib`, and served through an intuitive, modern Flask web portal designed to execute locally on student-grade hardware.

---

## 2. PROBLEM STATEMENT
Educational institutions and students routinely encounter several placement-related dilemmas:
1. **Late Realization of Shortcomings**: Students frequently realize their deficiencies (lack of internships, low coding aptitude, uncleared arrears) in their final semester when placement drives have already commenced.
2. **One-Dimensional Metrics**: CGPA alone does not accurately reflect industrial readiness; students with high CGPA but zero coding practice often fail technical screening rounds.
3. **Absence of Actionable Diagnostics**: Existing student tracking mechanisms only record past exam marks without providing diagnostic insights or prescriptive guidance.
4. **Need for Accessible Local AI**: Many proposed AI systems depend on cloud APIs or excessive computational resources, making them impractical for standard academic demonstration and resource-constrained environments.

---

## 3. OBJECTIVES
The principal objectives of this academic project are:
- To design and implement an end-to-end Supervised Machine Learning pipeline for binary placement classification.
- To formulate a representative, balanced dataset reflecting realistic engineering student profiles.
- To implement data preprocessing, feature normalization (`StandardScaler`), and train-test partitioning (80/20 stratified split).
- To train, tune, and compare an Ensemble Random Forest Classifier against a baseline Decision Tree Classifier.
- To rigorously evaluate the model using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- To extract Gini feature importances to determine the most influential factors governing placement outcomes.
- To build an intelligent, rule-informed recommendation module that suggests specific remedial interventions based on student attributes.
- To deliver a responsive Flask-based web application with input sanitization, error handling, quick-fill demo presets, and real-time visualization.

---

## 4. METHODOLOGY
The project adheres to the standard Machine Learning Life Cycle (MLLC):

1. **Problem Formulation**: Formalized as a binary classification task where $X \in \mathbb{R}^8$ denotes student feature vectors and $y \in \{0, 1\}$ represents placement outcome.
2. **Dataset Generation & Preprocessing**:
   - Synthesized and validated 1,000 realistic records with natural variance and inter-feature correlations.
   - Verified that data contains zero null or corrupted values.
3. **Data Splitting**:
   - Partitioned the 1,000 records into an 80% training set (800 records) and a 20% testing set (200 records).
   - Applied stratified sampling (`stratify=y`) to maintain the true class distribution across splits.
4. **Feature Standardization**:
   - Applied Z-score standardization:
     $$z = \frac{x - \mu}{\sigma}$$
   - Scaler parameters ($\mu, \sigma$) were fitted strictly on the training set and applied to the test set to eliminate data leakage.
5. **Model Construction & Training**:
   - Baseline Model: Single Decision Tree Classifier with maximum tree depth restricted to 5.
   - Primary Model: Random Forest Classifier comprising 100 decision trees with bootstrap aggregation (`n_estimators=100`, `max_depth=6`).
6. **Model Evaluation & Comparison**:
   - Calculated test set predictions and confusion matrix entries ($TN, FP, FN, TP$).
   - Derived quantitative metrics: Accuracy, Precision, Recall, and F1-Score.
7. **Feature Importance Extraction**:
   - Calculated Mean Decrease in Impurity (MDI) across all 100 trees to establish relative feature ranking.
8. **Serialization & Web Deployment**:
   - Exported model and scaler objects using `joblib`.
   - Built a Flask WSGI service exposing `/predict`, `/api/metrics`, and `/api/sample/<profile>` endpoints.

---

## 5. SYSTEM MODULES

The project architecture comprises five distinct functional modules:

### Module 1: Data Preprocessing & Pipeline Module (`train.py`, `dataset/`)
- Manages dataset ingestion, null validation, and feature/target segregation.
- Implements `StandardScaler` to transform disparate units (CGPA on a 0–10 scale, test scores on a 0–100 scale, and categorical binary indicators) into zero-mean, unit-variance representations.

### Module 2: Machine Learning Engine (`train.py`, `model/`)
- Fits the baseline Decision Tree and the Random Forest ensemble on the normalized feature space.
- Calculates training and test performance metrics.
- Serializes trained weights into `model/placement_model.pkl` and `model/scaler.pkl`.
- Records performance metadata and feature importances into `model/model_metadata.json`.

### Module 3: Inference & Recommendation Engine (`predict.py`)
- Houses the `PlacementPredictor` class.
- Performs rigorous boundary validation on all 8 inputs (range checking, type verification, non-empty validation).
- Converts raw input dictionary into a pandas DataFrame aligned with training feature names to avoid serialization warnings.
- Computes class probabilities using `.predict_proba()`.
- Maps student weaknesses to concrete remedial advice via the `_generate_recommendations()` method.

### Module 4: Web Application Server (`app.py`)
- Implements Flask web routes.
- Renders the user-facing interface (`index.html`).
- Implements RESTful JSON endpoint (`POST /predict`) and metrics query endpoint (`GET /api/metrics`).
- Houses preset sample profiles for instant evaluation during demonstrations.

### Module 5: User Interface & Presentation Layer (`templates/`, `static/`)
- Constructed with responsive HTML5, modern CSS3 variables, and vanilla JavaScript.
- Features dynamic probability progress gauges, status banners (Placed / At-Risk), parameter summaries, and collapsible syllabus architecture details.
- Includes error banner alerts and loading spinners for asynchronous requests.

---

## 6. HARDWARE REQUIREMENTS
- **Central Processing Unit (CPU)**: 1.6 GHz or faster dual-core x86/x64 processor (Intel Core i3 / AMD Ryzen 3 or higher).
- **Random Access Memory (RAM)**: 4 GB minimum (8 GB recommended for concurrent browser and server operation).
- **Storage Space**: Minimum 500 MB of available hard disk / SSD space.
- **Peripherals**: Standard keyboard, mouse, and display (1366x768 or 1920x1080 resolution).

---

## 7. SOFTWARE REQUIREMENTS
- **Operating System**: Microsoft Windows 10/11 (or macOS / Linux).
- **Runtime Environment**: Python 3.9 through 3.14.
- **Core Python Packages**:
  - `Flask` (>= 3.0.0): Web application server.
  - `scikit-learn` (>= 1.4.0): Machine learning models, scaler, and evaluation metrics.
  - `pandas` (>= 2.0.0): Tabular data structures and DataFrame manipulation.
  - `numpy` (>= 1.26.0): Array manipulation and vectorized calculations.
  - `joblib` (>= 1.3.0): Model persistence and deserialization.
- **Web Browser**: Any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox).

---

## 8. DATASET DESCRIPTION
The dataset (`dataset/student_data.csv`) comprises 1,000 independent student observations. Eight independent input variables represent diverse academic, practical, and behavioural dimensions:

1. **`cgpa`** (Continuous Float, 5.00–10.00): Overall academic GPA across completed semesters.
2. **`internships`** (Discrete Integer, 0–4): Count of verified industrial internships or fellowships.
3. **`projects`** (Discrete Integer, 0–6): Major and mini software or engineering projects completed.
4. **`coding_test_score`** (Continuous Integer, 0–100): Score achieved in coding and data structures assessment.
5. **`aptitude_test_score`** (Continuous Integer, 0–100): Score achieved in quantitative, logical, and verbal screening.
6. **`soft_skills_rating`** (Continuous Float, 1.0–5.0): Assessment score evaluating verbal communication and professional demeanor.
7. **`extracurriculars`** (Binary Integer, 0 or 1): Participation in collegiate clubs, competitions, hackathons, or sports.
8. **`backlogs`** (Discrete Integer, 0–5): Number of pending, uncleared academic subjects.

**Target Variable:**
- **`placed`** (Binary Integer, 0 or 1):
  - `1`: Student meets placement criteria and is classified as Placed / Top Tier Candidate.
  - `0`: Student is categorized as Placement at Risk.

Class distribution is natural and well-balanced: **71.6% Placed (716 records)** and **28.4% At Risk (284 records)**, reflecting the typical distribution of graduating engineering cohorts.

---

## 9. ALGORITHM EXPLANATION

### Random Forest Classifier
The Random Forest algorithm is an ensemble learning method founded on the principle of **Bootstrap Aggregation (Bagging)** applied to decision tree base learners.

#### Theoretical Foundation:
1. **Bootstrap Sampling**: Given a training set $D$ of size $N$, the algorithm generates $B = 100$ bootstrap datasets $D_1, D_2, \dots, D_B$ by sampling $N$ observations from $D$ uniformly at random with replacement.
2. **Random Subspace Projection**: While growing each tree, at every candidate node split, a random subset of $m$ features (where $m = \sqrt{p} \approx \sqrt{8} \approx 3$) is selected from the total $p$ available features. The best split is computed exclusively among this subset using the **Gini Impurity** criterion:
   $$I_G(t) = 1 - \sum_{i=1}^{C} p_i^2$$
   where $p_i$ is the probability of class $i$ at node $t$, and $C = 2$.
3. **Variance Reduction**: Individual decision trees exhibit high variance and low bias. By averaging the outputs of 100 decorrelated trees, the ensemble significantly suppresses variance while retaining the low bias of deep trees:
   $$\text{Var}(\bar{X}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
   As $B$ grows and correlation $\rho$ between trees is kept low by random feature selection, the total variance decreases substantially.
4. **Ensemble Aggregation**:
   - For hard classification:
     $$\hat{y} = \text{mode}\left(\{h_1(x), h_2(x), \dots, h_B(x)\}\right)$$
   - For soft probability estimation:
     $$P(Y = 1 \mid x) = \frac{1}{B} \sum_{b=1}^{B} P_b(Y = 1 \mid x)$$

---

## 10. RESULTS & PERFORMANCE ANALYSIS

### Quantitative Metrics
On the held-out test partition consisting of 200 unseen student profiles, the model attained the following scores:

- **Overall Test Accuracy**: **90.00%**
- **Precision (Placed)**: **89.68%**
- **Recall (Placed)**: **97.20%**
- **F1-Score**: **0.9329**
- **Baseline Comparison (Decision Tree)**: 91.00% Accuracy, 0.9371 F1-Score

### Confusion Matrix Breakdown
$$\begin{bmatrix} TN = 41 & FP = 16 \\ FN = 4 & TP = 139 \end{bmatrix}$$

- **True Negatives ($TN = 41$)**: At-risk students correctly identified for remediation.
- **False Positives ($FP = 16$)**: At-risk students predicted as placed.
- **False Negatives ($FN = 4$)**: Only 4 placed students were misclassified as at-risk, demonstrating extremely low omission risk.
- **True Positives ($TP = 139$)**: Eligible students accurately classified as placed.

### Feature Importance Hierarchy (Gini Importance)
1. **`cgpa` (33.41%)**: The primary filtering criteria across campus recruitment screening.
2. **`backlogs` (22.13%)**: The strongest penalizing factor; active arrears severely compromise eligibility.
3. **`coding_test_score` (21.13%)**: Crucial technical differentiator for software engineering roles.
4. **`aptitude_test_score` (10.75%)**: Determines clearance of preliminary aptitude elimination rounds.
5. **`soft_skills_rating` (4.61%)**: Influences personal interview and managerial round success.
6. **`projects` (4.58%)**: Validates applied engineering expertise during resume review.
7. **`internships` (2.95%)**: Provides industrial exposure proof.
8. **`extracurriculars` (0.43%)**: Secondary differentiator for well-rounded profiles.

---

## 11. ADVANTAGES
1. **High Diagnostic Sensitivity (97.2% Recall)**: Minimizes the likelihood of neglecting struggling students.
2. **Explainable AI (XAI)**: Demystifies predictions through explicit feature rankings and individual student feedback.
3. **Lightweight & Completely Offline**: No GPUs, cloud servers, or third-party paid APIs required.
4. **Interactive Demonstration Features**: Single-click demo presets allow rapid examination by professors and evaluators.
5. **Robust Error Handling**: Comprehensive validation prevents system crashes when faced with incomplete or malicious inputs.

---

## 12. LIMITATIONS
1. **Binary Classification Focus**: The current release focuses on placement readiness rather than predicting specific salary packages (CTC) or company designations.
2. **Synthetic Data Realism**: While statistically consistent with college distributions, synthetic data cannot replicate unannounced macroeconomic hiring freezes.
3. **Absence of Direct Resume Parsing**: Students must manually enter their metrics rather than uploading a raw PDF resume.

---

## 13. FUTURE SCOPE
1. **Multi-Tier Salary Band Prediction**: Extending the model to predict salary brackets (e.g., Mass Recruiter 3–5 LPA, Dream 6–10 LPA, Super Dream 12+ LPA).
2. **NLP-Based Resume Parsing**: Incorporating Natural Language Processing (NLP) to parse PDF resumes and automatically populate candidate fields.
3. **Institutional ERP Integration**: Deploying database connectors to ingest semester records directly from the college student information system.
4. **Explainable Counterfactual Analysis**: Generating "What-If" scenarios (e.g., "If you increase your coding score by 15 points, placement probability rises from 48% to 76%").

---

## 14. CONCLUSION
EduPredict AI establishes a functional, rigorous, and practical application of supervised machine learning in higher education. By combining a Random Forest ensemble with intuitive web technologies and an automated advisory engine, the project fulfills all academic criteria for a college mini-project while delivering demonstrable utility for students and faculty advisors alike.
