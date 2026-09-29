"""
train.py
Machine Learning Training Pipeline for Student Exam Performance & Placement Predictor.

AI Syllabus Alignment:
- Supervised Machine Learning (Binary Classification)
- Feature Engineering & Preprocessing (StandardScaler)
- Train/Test Split with Stratified Sampling
- Ensemble Learning (Random Forest Classifier) vs Baseline (Decision Tree Classifier)
- Model Evaluation Metrics (Accuracy, Precision, Recall, F1-Score, Confusion Matrix)
- Feature Importance Analysis & Model Serialization (joblib, json)
"""

import os
import sys
import json
import joblib
import numpy as np
import pandas as pd

# Ensure standard UTF-8 console output on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

def train_model():
    print("=" * 65)
    print("[*] STUDENT PLACEMENT & PERFORMANCE PREDICTOR - MODEL TRAINING [*]")
    print("=" * 65)

    # Resolve paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'dataset', 'student_data.csv')
    model_dir = os.path.join(base_dir, 'model')
    os.makedirs(model_dir, exist_ok=True)

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Run generate_dataset.py first.")

    # 1. Load Data
    print(f"\n[Step 1] Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"-> Total records loaded: {len(df)}")
    print(f"-> Features: {list(df.columns)}")

    # Check for missing values
    missing_count = df.isnull().sum().sum()
    print(f"-> Missing values in dataset: {missing_count} (Clean dataset)")

    # 2. Define Features and Target
    feature_names = [
        'cgpa',
        'internships',
        'projects',
        'coding_test_score',
        'aptitude_test_score',
        'soft_skills_rating',
        'extracurriculars',
        'backlogs'
    ]
    target_name = 'placed'

    X = df[feature_names]
    y = df[target_name]

    print(f"\n[Step 2] Feature and Target Separation:")
    print(f"-> Inputs ({len(feature_names)}): {feature_names}")
    print(f"-> Target: {target_name} (0 = Not Placed / At-Risk, 1 = Placed)")
    print(f"-> Class balance: Placed={sum(y==1)}, Not Placed={sum(y==0)}")

    # 3. Train-Test Split (80% Train, 20% Test)
    print(f"\n[Step 3] Splitting dataset (80% Train / 20% Test, Stratified)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"-> Training samples: {X_train.shape[0]}")
    print(f"-> Testing samples:  {X_test.shape[0]}")

    # 4. Feature Scaling (StandardScaler: (x - mean) / std)
    print(f"\n[Step 4] Applying StandardScaler for feature normalization...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Train Baseline Model (Decision Tree)
    print(f"\n[Step 5] Training Baseline Model: Decision Tree Classifier...")
    dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
    dt_model.fit(X_train_scaled, y_train)
    y_pred_dt = dt_model.predict(X_test_scaled)
    dt_acc = accuracy_score(y_test, y_pred_dt)
    dt_f1 = f1_score(y_test, y_pred_dt)
    print(f"-> Decision Tree Test Accuracy: {dt_acc * 100:.2f}% | F1-Score: {dt_f1:.4f}")

    # 6. Train Primary Model: Random Forest (Ensemble Learning)
    print(f"\n[Step 6] Training Primary Model: Random Forest Classifier (100 Trees)...")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=6,
        min_samples_split=4,
        random_state=42
    )
    rf_model.fit(X_train_scaled, y_train)
    y_pred_rf = rf_model.predict(X_test_scaled)

    # 7. Model Evaluation
    print(f"\n[Step 7] Evaluating Model Performance on Unseen Test Set:")
    acc = accuracy_score(y_test, y_pred_rf)
    prec = precision_score(y_test, y_pred_rf)
    rec = recall_score(y_test, y_pred_rf)
    f1 = f1_score(y_test, y_pred_rf)
    cm = confusion_matrix(y_test, y_pred_rf)

    print("-" * 50)
    print(f"  Accuracy  : {acc * 100:.2f}%")
    print(f"  Precision : {prec * 100:.2f}%")
    print(f"  Recall    : {rec * 100:.2f}%")
    print(f"  F1-Score  : {f1:.4f}")
    print("-" * 50)
    print("Confusion Matrix:")
    print(f"  [TN={cm[0][0]:3d}  FP={cm[0][1]:3d}]")
    print(f"  [FN={cm[1][0]:3d}  TP={cm[1][1]:3d}]")
    print("-" * 50)
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred_rf, target_names=["Not Placed", "Placed"]))

    # 8. Feature Importance Analysis
    importances = rf_model.feature_importances_
    feat_imp_dict = {feat: round(float(imp), 4) for feat, imp in zip(feature_names, importances)}
    sorted_importances = sorted(feat_imp_dict.items(), key=lambda x: x[1], reverse=True)

    print("\n[Step 8] Key Feature Importances (What drives placement?):")
    for feat, val in sorted_importances:
        bar = "#" * int(val * 40)
        print(f"  {feat:20s}: {val:.4f} {bar}")

    # 9. Save Models and Metadata
    print(f"\n[Step 9] Saving trained model artifacts to '{model_dir}'...")
    model_path = os.path.join(model_dir, 'placement_model.pkl')
    scaler_path = os.path.join(model_dir, 'scaler.pkl')
    metadata_path = os.path.join(model_dir, 'model_metadata.json')

    joblib.dump(rf_model, model_path)
    joblib.dump(scaler, scaler_path)

    metadata = {
        "model_name": "Random Forest Classifier",
        "n_estimators": 100,
        "max_depth": 6,
        "training_samples": int(X_train.shape[0]),
        "testing_samples": int(X_test.shape[0]),
        "feature_names": feature_names,
        "metrics": {
            "accuracy": round(float(acc) * 100, 2),
            "precision": round(float(prec) * 100, 2),
            "recall": round(float(rec) * 100, 2),
            "f1_score": round(float(f1), 4),
            "confusion_matrix": cm.tolist()
        },
        "baseline_comparison": {
            "model_name": "Decision Tree Classifier",
            "accuracy": round(float(dt_acc) * 100, 2),
            "f1_score": round(float(dt_f1), 4)
        },
        "feature_importances": dict(sorted_importances)
    }

    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)

    print(f"-> Model saved: {model_path}")
    print(f"-> Scaler saved: {scaler_path}")
    print(f"-> Metadata saved: {metadata_path}")
    print("\n[SUCCESS] Model training complete and ready for deployment!")
    print("=" * 65)

if __name__ == '__main__':
    train_model()
