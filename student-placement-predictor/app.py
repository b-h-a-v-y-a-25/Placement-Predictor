"""
app.py
Flask Web Application for Student Exam Performance & Campus Placement Predictor.

Features:
- Web UI serving dynamic prediction interface
- REST API endpoint for real-time model inference (/predict)
- Metrics endpoint for academic evaluation metrics (/api/metrics)
- Quick-fill preset profile endpoint (/api/sample/<profile_type>)
- Robust error handling and validation
"""

import os
import sys
import json
from flask import Flask, render_template, request, jsonify
from predict import PlacementPredictor

# Ensure utf-8 stdout
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

app = Flask(__name__)

# Initialize predictor singleton
predictor = None
try:
    predictor = PlacementPredictor()
    print("[INFO] PlacementPredictor model artifacts loaded successfully.")
except Exception as e:
    print(f"[WARNING] Could not load predictor on startup: {e}")

# Preset student profiles for live professor demonstrations
SAMPLE_PROFILES = {
    "topper": {
        "cgpa": 9.15,
        "internships": 2,
        "projects": 3,
        "coding_test_score": 90,
        "aptitude_test_score": 85,
        "soft_skills_rating": 4.6,
        "extracurriculars": 1,
        "backlogs": 0
    },
    "average": {
        "cgpa": 7.30,
        "internships": 1,
        "projects": 2,
        "coding_test_score": 68,
        "aptitude_test_score": 65,
        "soft_skills_rating": 3.4,
        "extracurriculars": 0,
        "backlogs": 0
    },
    "at_risk": {
        "cgpa": 5.75,
        "internships": 0,
        "projects": 1,
        "coding_test_score": 40,
        "aptitude_test_score": 42,
        "soft_skills_rating": 2.3,
        "extracurriculars": 0,
        "backlogs": 2
    }
}

@app.route('/')
def home():
    """Renders the main student prediction portal."""
    metrics = predictor.metadata if predictor and predictor.metadata else {}
    return render_template('index.html', metrics=metrics)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles student profile submission via JSON or Form.
    Returns prediction results with probabilities and guidance.
    """
    global predictor
    if predictor is None:
        try:
            predictor = PlacementPredictor()
        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"Model is not loaded. Please run 'python train.py' first. ({str(e)})"
            }), 500

    # Handle JSON and Form Data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if not data:
        return jsonify({
            "success": False,
            "error": "No input data received. Please fill out the form."
        }), 400

    result = predictor.predict(data)

    if not result.get("success"):
        return jsonify(result), 400

    return jsonify(result), 200

@app.route('/api/sample/<profile_name>', methods=['GET'])
def get_sample_profile(profile_name):
    """Returns sample student profiles for rapid testing."""
    profile_key = profile_name.lower().strip()
    if profile_key in SAMPLE_PROFILES:
        return jsonify({
            "success": True,
            "profile": SAMPLE_PROFILES[profile_key]
        }), 200
    return jsonify({
        "success": False,
        "error": f"Unknown sample profile '{profile_name}'. Options: {list(SAMPLE_PROFILES.keys())}"
    }), 404

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Returns model performance metrics and feature importances."""
    if predictor and predictor.metadata:
        return jsonify({
            "success": True,
            "metadata": predictor.metadata
        }), 200
    return jsonify({
        "success": False,
        "error": "Model metadata unavailable. Run train.py first."
    }), 404

@app.route('/health', methods=['GET'])
def health():
    """Basic health check endpoint."""
    return jsonify({
        "status": "healthy",
        "model_loaded": predictor is not None
    }), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "error": "Internal server error occurred"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n[SERVER] Starting EduPredict AI Flask Server on http://127.0.0.1:{port}")
    print("[SERVER] Press Ctrl+C to stop the server.\n")
    app.run(host='127.0.0.1', port=port, debug=True)
