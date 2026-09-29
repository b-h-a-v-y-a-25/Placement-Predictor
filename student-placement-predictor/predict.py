"""
predict.py
Inference Engine and Input Validation for Student Exam Performance & Placement Predictor.

Handles:
- Loading saved Random Forest model and StandardScaler artifacts
- Strict input validation and sanitization
- Feature scaling
- Model inference with class probability calculation
- Student Readiness Tier assessment
- Personalized AI-driven recommendations based on individual weaknesses
"""

import os
import sys
import json
import joblib
import numpy as np

# Ensure standard console output on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class PlacementPredictor:
    def __init__(self, model_dir=None):
        if model_dir is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            model_dir = os.path.join(base_dir, 'model')

        self.model_dir = model_dir
        self.model_path = os.path.join(model_dir, 'placement_model.pkl')
        self.scaler_path = os.path.join(model_dir, 'scaler.pkl')
        self.metadata_path = os.path.join(model_dir, 'model_metadata.json')

        self.model = None
        self.scaler = None
        self.metadata = None

        self._load_artifacts()

    def _load_artifacts(self):
        """Loads serialized model, scaler, and metadata from disk."""
        if not os.path.exists(self.model_path) or not os.path.exists(self.scaler_path):
            raise FileNotFoundError(
                f"Model or Scaler not found in '{self.model_dir}'. Run train.py first."
            )

        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)

        if os.path.exists(self.metadata_path):
            with open(self.metadata_path, 'r') as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}

    def validate_inputs(self, data):
        """
        Validates and sanitizes raw input dictionary.
        Returns: (cleaned_dict, error_message)
        """
        required_fields = [
            'cgpa',
            'internships',
            'projects',
            'coding_test_score',
            'aptitude_test_score',
            'soft_skills_rating',
            'extracurriculars',
            'backlogs'
        ]

        if not isinstance(data, dict):
            return None, "Invalid input payload: Expected JSON object or dictionary."

        cleaned = {}

        # Check for missing fields
        for field in required_fields:
            if field not in data or data[field] is None or str(data[field]).strip() == "":
                return None, f"Missing required input field: '{field}'."

        # Validate numeric ranges
        try:
            cgpa = float(data['cgpa'])
            if not (0.0 <= cgpa <= 10.0):
                return None, "CGPA must be between 0.0 and 10.0."
            cleaned['cgpa'] = cgpa

            internships = int(float(data['internships']))
            if not (0 <= internships <= 20):
                return None, "Internships count must be between 0 and 20."
            cleaned['internships'] = internships

            projects = int(float(data['projects']))
            if not (0 <= projects <= 30):
                return None, "Projects count must be between 0 and 30."
            cleaned['projects'] = projects

            coding_score = float(data['coding_test_score'])
            if not (0.0 <= coding_score <= 100.0):
                return None, "Coding test score must be between 0 and 100."
            cleaned['coding_test_score'] = coding_score

            aptitude_score = float(data['aptitude_test_score'])
            if not (0.0 <= aptitude_score <= 100.0):
                return None, "Aptitude test score must be between 0 and 100."
            cleaned['aptitude_test_score'] = aptitude_score

            soft_skills = float(data['soft_skills_rating'])
            if not (1.0 <= soft_skills <= 5.0):
                return None, "Soft skills rating must be between 1.0 and 5.0."
            cleaned['soft_skills_rating'] = soft_skills

            extracurriculars = int(float(data['extracurriculars']))
            if extracurriculars not in (0, 1):
                return None, "Extracurriculars must be 0 (No) or 1 (Yes)."
            cleaned['extracurriculars'] = extracurriculars

            backlogs = int(float(data['backlogs']))
            if not (0 <= backlogs <= 30):
                return None, "Backlogs count must be a non-negative integer."
            cleaned['backlogs'] = backlogs

        except ValueError as e:
            return None, f"Data type error: All inputs must be numeric values. ({str(e)})"

        return cleaned, None

    def _generate_recommendations(self, data, is_placed, prob_placed):
        """Generates explainable, actionable recommendations tailored to the student."""
        recommendations = []

        # Backlogs Check
        if data['backlogs'] > 0:
            recommendations.append(
                f"Priority 1: Clear all {data['backlogs']} active backlog(s). "
                "Over 85% of tier-1 campus recruiters require 0 active backlogs."
            )

        # CGPA Check
        if data['cgpa'] < 7.0:
            recommendations.append(
                f"Academic Recovery: Current CGPA ({data['cgpa']:.2f}) is below typical cutoff (7.0). "
                "Aim for higher marks in upcoming semester exams to raise your aggregate."
            )
        elif data['cgpa'] >= 8.5:
            recommendations.append(
                f"Academic Strength: Excellent CGPA ({data['cgpa']:.2f}) makes you eligible for elite R&D and core roles."
            )

        # Coding Score Check
        if data['coding_test_score'] < 60:
            recommendations.append(
                f"Technical Skill Enhancement: Coding score ({data['coding_test_score']:.0f}/100) is low. "
                "Practice Data Structures & Algorithms (LeetCode / HackerRank) 1-2 hours daily."
            )
        elif data['coding_test_score'] >= 80:
            recommendations.append(
                f"Technical Strength: High coding aptitude ({data['coding_test_score']:.0f}/100) will be a major differentiator in technical rounds."
            )

        # Internships & Practical Experience
        if data['internships'] == 0:
            recommendations.append(
                "Industrial Exposure: You have 0 internships. Seek a 4-8 week internship or open-source fellowship before placement season."
            )

        # Projects
        if data['projects'] < 2:
            recommendations.append(
                "Portfolio Building: Complete at least 2 full-stack, AI, or domain-specific projects with GitHub repositories."
            )

        # Soft Skills
        if data['soft_skills_rating'] < 3.2:
            recommendations.append(
                "Communication & HR Prep: Soft skills rating is below 3.2. Join Toastmasters or participate in mock group discussions."
            )

        # Aptitude Test
        if data['aptitude_test_score'] < 60:
            recommendations.append(
                "Aptitude Practice: Practice Quantitative Aptitude, Logical Reasoning, and Verbal Ability for preliminary screening rounds."
            )

        if not recommendations:
            recommendations.append(
                "Profile is well-rounded across all dimensions! Focus on mock interviews and company-specific test pattern practice."
            )

        return recommendations

    def predict(self, raw_input_data):
        """
        Processes raw input data and returns full prediction breakdown.
        """
        cleaned_data, error = self.validate_inputs(raw_input_data)
        if error:
            return {
                "success": False,
                "error": error
            }

        feature_order = [
            'cgpa',
            'internships',
            'projects',
            'coding_test_score',
            'aptitude_test_score',
            'soft_skills_rating',
            'extracurriculars',
            'backlogs'
        ]

        import pandas as pd
        input_df = pd.DataFrame([[cleaned_data[feat] for feat in feature_order]], columns=feature_order)

        # Standardize features using training scaler
        scaled_vector = self.scaler.transform(input_df)

        # Run model inference
        prediction = int(self.model.predict(scaled_vector)[0])
        probabilities = self.model.predict_proba(scaled_vector)[0]
        prob_not_placed = round(float(probabilities[0]) * 100, 2)
        prob_placed = round(float(probabilities[1]) * 100, 2)

        # Determine Readiness Tier
        if prob_placed >= 80.0:
            tier = "High Probability (Top Tier Candidate)"
            badge_class = "success"
            summary = "The student demonstrates high placement readiness with strong credentials."
        elif prob_placed >= 50.0:
            tier = "Moderate Probability (Competitive Candidate)"
            badge_class = "warning"
            summary = "The student has viable placement prospects but has room for targeted skill upgrades."
        else:
            tier = "Low Probability (At-Risk / Needs Intervention)"
            badge_class = "danger"
            summary = "The student is currently at high risk of missing placement cutoffs without corrective action."

        recommendations = self._generate_recommendations(cleaned_data, prediction == 1, prob_placed)

        return {
            "success": True,
            "prediction": prediction,
            "prediction_label": "Likely to be Placed" if prediction == 1 else "Placement at Risk",
            "placement_probability": prob_placed,
            "not_placed_probability": prob_not_placed,
            "readiness_tier": tier,
            "badge_class": badge_class,
            "summary": summary,
            "recommendations": recommendations,
            "input_data": cleaned_data
        }

# Quick CLI test mode
if __name__ == '__main__':
    predictor = PlacementPredictor()
    print("Testing PlacementPredictor with 3 diverse sample profiles...\n")

    test_samples = [
        {
            "name": "High Performer",
            "data": {
                'cgpa': 9.2, 'internships': 2, 'projects': 4,
                'coding_test_score': 92, 'aptitude_test_score': 88,
                'soft_skills_rating': 4.5, 'extracurriculars': 1, 'backlogs': 0
            }
        },
        {
            "name": "Average Student",
            "data": {
                'cgpa': 7.1, 'internships': 1, 'projects': 2,
                'coding_test_score': 65, 'aptitude_test_score': 62,
                'soft_skills_rating': 3.3, 'extracurriculars': 0, 'backlogs': 0
            }
        },
        {
            "name": "At-Risk Student",
            "data": {
                'cgpa': 5.8, 'internships': 0, 'projects': 1,
                'coding_test_score': 42, 'aptitude_test_score': 45,
                'soft_skills_rating': 2.5, 'extracurriculars': 0, 'backlogs': 2
            }
        }
    ]

    for sample in test_samples:
        print(f"--- Profile: {sample['name']} ---")
        result = predictor.predict(sample['data'])
        print(f"Result: {result['prediction_label']} ({result['placement_probability']}%)")
        print(f"Tier:   {result['readiness_tier']}")
        print(f"Recommendations count: {len(result['recommendations'])}")
        print()
