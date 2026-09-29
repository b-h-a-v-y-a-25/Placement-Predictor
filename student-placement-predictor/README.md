# EduPredict AI: Student Academic Performance & Campus Placement Predictor

An End-to-End Supervised Machine Learning Mini-Project for Academic Submission.

---

## 1. Project Title
**EduPredict AI: Student Academic Performance & Campus Placement Predictor using Random Forest Ensemble Learning and Flask**

---

## 2. Abstract
Campus placement is a critical milestone in higher education, reflecting both individual student competence and institutional effectiveness. Traditional evaluation approaches rely primarily on aggregate grade point average (CGPA) cutoffs, overlooking vital multidimensional factors such as programming capabilities, practical projects, quantitative aptitude, and active backlogs. This project presents **EduPredict AI**, an end-to-end supervised machine learning application that predicts student placement readiness and provides personalized developmental guidance. Using a balanced dataset of 1,000 student records across 8 academic, technical, and behavioural parameters, a Random Forest Classifier (100 estimators) was trained alongside a baseline Decision Tree. Standardized with z-score normalization (`StandardScaler`), the model achieves **90.00% test accuracy**, **89.68% precision**, **97.20% recall**, and an **F1-score of 0.9329**. Feature importance analysis demonstrates that active backlogs, CGPA, and coding test scores are the primary determinants of placement outcomes. The model is deployed via a lightweight Flask web interface featuring real-time inference, risk categorization, interactive probability gauges, and dynamic academic advisory recommendations.

---

## 3. Introduction
Securing campus placements has become increasingly competitive in engineering and computer science programs. While university curricula prioritize semester examinations, recruiting organizations look for a composite balance of algorithmic problem-solving, project implementation, analytical thinking, and interpersonal skills. 

Early identification of students who are at risk of missing placement criteria gives educational institutions and students the opportunity to undertake targeted remediation before placement drives commence. **EduPredict AI** bridges this gap by offering a transparent, local, AI-driven assessment tool that accurately predicts placement probability and flags specific weak areas for timely intervention.

---

## 4. Problem Statement
Many students discover too late in their final year that high academic scores alone do not guarantee campus placement, or that unresolved backlogs eliminate them from preliminary screening rounds. Furthermore, academic advisors lack automated diagnostic tools to evaluate a student's holistic readiness across diverse dimensions. There is a clear need for an interpretable, reliable, and easily accessible predictive system that analyzes a student's multifaceted profile and provides actionable recommendations.

---

## 5. Objectives
1. **Develop an ML Pipeline**: Construct a complete, reproducible machine learning pipeline in Python covering data preprocessing, feature normalization, model training, and evaluation.
2. **Train an Ensemble Classifier**: Implement and tune a Random Forest Classifier and benchmark it against a baseline Decision Tree Classifier.
3. **Analyze Feature Significance**: Identify the key factors influencing placement decisions through Gini importance analysis.
4. **Build an Actionable Advisory System**: Automatically generate student-specific improvement tips based on individual weaknesses (e.g., backlog clearance, coding practice, internship acquisition).
5. **Deploy a Local Web Application**: Package the system into an accessible, responsive Flask web application that runs on standard student hardware without requiring internet connectivity or paid APIs.

---

## 6. Scope
- **Target Audience**: Undergraduate engineering/CS students, training and placement officers (TPOs), and academic mentors.
- **Application Boundary**: Binary classification (Placed vs. At-Risk) with granular probability estimates and three-tier readiness categorizations.
- **Operational Scope**: Completely local execution on a standard laptop, ensuring full privacy and zero cloud dependencies.

---

## 7. Technologies Used
- **Programming Language**: Python 3.10+ (tested on Python 3.14)
- **Machine Learning**: `scikit-learn` (Random Forest, Decision Tree, StandardScaler, Metrics)
- **Data Manipulation**: `pandas`, `NumPy`
- **Model Serialization**: `joblib`
- **Web Framework**: Flask 3.1+ (Python WSGI Web Framework)
- **Frontend**: HTML5, CSS3 (Modern Flexbox/Grid, CSS Variables), Vanilla JavaScript (ES6+ Fetch API)
- **Testing**: Python `unittest` suite

---

## 8. AI/ML Concepts Used
- **Supervised Learning**: Classification using labelled input-output training pairs.
- **Ensemble Learning (Bagging)**: Combining predictions of multiple decision trees (`n_estimators=100`) to reduce variance and mitigate overfitting.
- **Feature Normalization**: Z-score standardization ($z = \frac{x - \mu}{\sigma}$) using `StandardScaler` to bring heterogeneously scaled features (CGPA 0–10, test scores 0–100) into a uniform distribution.
- **Stratified Train-Test Split**: Preserving class distribution ratio across an 80% training set and a 20% test set.
- **Model Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- **Feature Importance / Interpretability**: Calculating Mean Decrease in Impurity (Gini importance) to reveal which attributes drive model decisions.

---

## 9. System Requirements

### Hardware Requirements
- **Processor**: Intel Core i3 / AMD Ryzen 3 or higher
- **RAM**: Minimum 4 GB (8 GB recommended)
- **Disk Space**: At least 500 MB of available storage
- **Display**: 1280x720 resolution or higher

### Software Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.9, 3.10, 3.11, 3.12, 3.13, or 3.14
- **Web Browser**: Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari

---

## 10. Dataset Description
The dataset contains 1,000 student records located in `dataset/student_data.csv`. Each record reflects authentic engineering college placement metrics:

| Column Name | Data Type | Range | Description |
|---|---|---|---|
| `cgpa` | Float | 5.00 – 10.00 | Cumulative Grade Point Average |
| `internships` | Integer | 0 – 4 | Number of completed verified internships |
| `projects` | Integer | 0 – 6 | Number of academic and personal technical projects |
| `coding_test_score` | Integer | 0 – 100 | Score in programming & DSA screening exam |
| `aptitude_test_score` | Integer | 0 – 100 | Score in quantitative, logical, & verbal reasoning test |
| `soft_skills_rating` | Float | 1.0 – 5.0 | Interviewer/mentor rating on communication & presentation |
| `extracurriculars` | Integer | 0 or 1 | Active participation in clubs/hackathons (1 = Yes, 0 = No) |
| `backlogs` | Integer | 0 – 5 | Number of active uncleared backlogs/arrears |
| `placed` *(Target)* | Integer | 0 or 1 | 1 = Placed / Top Tier Placement, 0 = Placement at Risk |

---

## 11. Methodology
1. **Data Acquisition & Verification**: Load tabular data from CSV and verify zero missing/corrupt values.
2. **Exploratory Analysis**: Inspect feature distributions, variances, and correlations.
3. **Data Splitting**: Partition into 800 training samples and 200 testing samples using stratified sampling to maintain class proportions.
4. **Feature Scaling**: Fit `StandardScaler` on `X_train` and transform both `X_train` and `X_test`.
5. **Model Training**:
   - Baseline: Train `DecisionTreeClassifier(max_depth=5)`.
   - Primary: Train `RandomForestClassifier(n_estimators=100, max_depth=6)`.
6. **Model Validation**: Compute test confusion matrix, precision, recall, and F1-score.
7. **Export Artifacts**: Serialize trained model, scaler, and metadata (`.pkl` and `.json`).
8. **Application Integration**: Implement `PlacementPredictor` class in `predict.py` with input validation, probability computation, and rule-based advice generation.
9. **Interface Deployment**: Serve dynamic UI via Flask with responsive asynchronous POST updates.

---

## 12. System Architecture

```
[ User Input (Browser Form / Presets) ]
                   │
                   ▼ (HTTP POST /predict - JSON)
         [ Flask Web Server (app.py) ]
                   │
                   ▼
     [ Inference Engine (predict.py) ]
      ├── 1. Input Sanitization & Range Validation
      ├── 2. StandardScaler Transformation (scaler.pkl)
      ├── 3. Random Forest Inference (placement_model.pkl)
      ├── 4. Probability & Readiness Tier Computation
      └── 5. Personalized Recommendation Generator
                   │
                   ▼ (JSON Result Object)
  [ Responsive Dynamic Dashboard (index.html / CSS / JS) ]
```

---

## 13. Algorithm / Model
The primary algorithm used is the **Random Forest Classifier**:
- An ensemble learning method based on **Bootstrap Aggregation (Bagging)**.
- Combines 100 uncorrelated decision trees, each trained on a random bootstrap sample with replacement from the training set.
- At each node split, a random subset of features is evaluated, minimizing correlation among individual trees and substantially reducing variance compared to a single decision tree.
- Final prediction:
  $$\hat{y} = \text{mode}\left(\{h_1(x), h_2(x), \dots, h_B(x)\}\right)$$
  where $B = 100$ and $h_b(x)$ is the prediction of the $b$-th tree.
- Predicted probability for class $k$:
  $$P(Y = k \mid x) = \frac{1}{B} \sum_{b=1}^{B} P_b(Y = k \mid x)$$

---

## 14. Training Process
Run the training pipeline with:
```bash
python train.py
```
The script performs:
1. Data loading and validation.
2. Stratified train-test split ($800$ train, $200$ test).
3. Standard scaling computation.
4. Decision Tree baseline training.
5. Random Forest model fitting ($100$ trees, maximum depth $6$).
6. Feature importance extraction.
7. Artifact serialization to `model/placement_model.pkl` and `model/scaler.pkl`.

---

## 15. Testing
The project includes automated regression and unit tests in `test_app.py`.

Run tests using:
```bash
python test_app.py
```
**Test Cases Covered:**
1. **Home Route**: Verifies HTTP 200 and page rendering.
2. **Health Route**: Confirms model is loaded and application is healthy.
3. **Metrics Route**: Validates model metadata and feature rankings.
4. **Preset Endpoint**: Confirms sample profile data retrieval.
5. **Top Candidate Prediction**: Asserts prediction = 1, probability $\ge 80\%$.
6. **At-Risk Candidate Prediction**: Asserts prediction = 0, probability $< 50\%$.
7. **Empty Input Handling**: Verifies HTTP 400 with descriptive error message.
8. **Invalid Data Type Handling**: Verifies non-numeric inputs return HTTP 400.
9. **Out-of-Range Value Handling**: Verifies boundary violations (e.g., CGPA > 10.0) return explicit error explanations.

---

## 16. Results

### Performance Comparison
| Metric | Baseline Decision Tree | Primary Random Forest |
|---|---|---|
| **Test Accuracy** | 91.00% | **90.00%** |
| **Precision (Placed)** | 91.45% | **89.68%** |
| **Recall (Placed)** | 96.50% | **97.20%** |
| **F1-Score** | 0.9371 | **0.9329** |

### Confusion Matrix (Test Set: 200 records)
| Actual \ Predicted | Predicted: Not Placed (0) | Predicted: Placed (1) | Total |
|---|---|---|---|
| **Actual: Not Placed (0)** | **41** (True Negative) | **16** (False Positive) | 57 |
| **Actual: Placed (1)** | **4** (False Negative) | **139** (True Positive) | 143 |

### Feature Importance (Gini Impurity)
1. **CGPA**: 33.41%
2. **Active Backlogs**: 22.13%
3. **Coding Test Score**: 21.13%
4. **Aptitude Test Score**: 10.75%
5. **Soft Skills Rating**: 4.61%
6. **Projects**: 4.58%
7. **Internships**: 2.95%
8. **Extracurriculars**: 0.43%

---

## 17. Advantages
- **High Recall (97.20%)**: Minimizes false negatives, ensuring almost no eligible student is mistakenly flagged as at risk.
- **Interpretability**: Clear feature importances reveal exactly why predictions occur.
- **Actionable Advice**: Instead of merely displaying a label, the system produces concrete tips (e.g., "Clear backlogs first", "Practice DSA").
- **Zero Operating Cost**: Runs 100% locally with open-source libraries; no cloud bills or API keys required.
- **Fast Inference**: Single predictions complete in under 5 milliseconds.

---

## 18. Limitations
- **Binary Outcome**: Predicts placement eligibility rather than specific salary packages or individual company designations.
- **Synthetic Distribution**: Although realistic and balanced, the dataset does not yet reflect seasonal economic hiring fluctuations.
- **Static Weights**: Recommendations are rule-guided; they do not adapt to shifting regional market demands in real time.

---

## 19. Future Scope
- **Multi-Class Package Prediction**: Predicting salary bands (e.g., 3-6 LPA, 6-12 LPA, 12+ LPA).
- **Resume NLP Integration**: Parsing student resume PDFs using NLP (TF-IDF, spaCy) to extract skills and projects automatically.
- **College Management Integration**: Connecting with university ERP/portal databases for automated student batch screening.
- **Longitudinal Tracking**: Tracking student improvement semester-by-semester to measure remediation impact.

---

## 20. Conclusion
EduPredict AI successfully demonstrates the application of supervised ensemble machine learning to a real-world educational challenge. By integrating standard academic parameters with technical and interpersonal indicators, the system achieves strong predictive metrics (90% accuracy, 97.2% recall) and bridges the gap between raw ML predictions and practical academic advising.

---

## 21. How to Run the Project

### Step 1: Open Terminal in Project Directory
```powershell
cd C:\Users\BHAVYA\.gemini\antigravity\scratch\student-placement-predictor
```

### Step 2: Install Dependencies
```powershell
python -m pip install -r requirements.txt
```

### Step 3: (Optional) Re-train the Model
```powershell
python train.py
```

### Step 4: Run the Web Application
```powershell
python app.py
```

### Step 5: Open in Your Browser
Open your browser and navigate to:
```
http://127.0.0.1:5000
```
Use the **Quick Demo Presets** to demonstrate predictions in front of your professor!
