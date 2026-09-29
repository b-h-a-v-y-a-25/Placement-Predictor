"""
test_app.py
Automated test suite verifying all routes, input validations,
and machine learning predictions for EduPredict AI.
"""

import unittest
import json
from app import app

class EduPredictTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_01_home_page(self):
        """Test home route loads correctly with 200 OK and expected HTML elements."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')
        self.assertIn("EduPredict AI", html)
        self.assertIn("Predict Placement Outcome", html)
        self.assertIn("Random Forest", html)

    def test_02_health_endpoint(self):
        """Test /health returns healthy status and model_loaded=True."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'healthy')
        self.assertTrue(data.get('model_loaded'))

    def test_03_metrics_endpoint(self):
        """Test /api/metrics returns accurate model metadata."""
        response = self.client.get('/api/metrics')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('accuracy', data['metadata']['metrics'])
        self.assertIn('feature_importances', data['metadata'])

    def test_04_sample_profiles(self):
        """Test /api/sample/topper returns the sample preset profile."""
        response = self.client.get('/api/sample/topper')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['profile']['cgpa'], 9.15)

    def test_05_predict_topper_profile(self):
        """Test prediction for top-tier student (Expected: Placed)."""
        payload = {
            "cgpa": 9.2,
            "backlogs": 0,
            "coding_test_score": 92,
            "projects": 3,
            "internships": 2,
            "aptitude_test_score": 88,
            "soft_skills_rating": 4.5,
            "extracurriculars": 1
        }
        response = self.client.post(
            '/predict',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['prediction'], 1)
        self.assertGreaterEqual(data['placement_probability'], 80.0)
        self.assertEqual(data['prediction_label'], "Likely to be Placed")
        self.assertGreater(len(data['recommendations']), 0)

    def test_06_predict_at_risk_profile(self):
        """Test prediction for at-risk student (Expected: At Risk)."""
        payload = {
            "cgpa": 5.8,
            "backlogs": 2,
            "coding_test_score": 40,
            "projects": 1,
            "internships": 0,
            "aptitude_test_score": 45,
            "soft_skills_rating": 2.2,
            "extracurriculars": 0
        }
        response = self.client.post(
            '/predict',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['prediction'], 0)
        self.assertLess(data['placement_probability'], 50.0)
        self.assertEqual(data['prediction_label'], "Placement at Risk")
        self.assertGreater(len(data['recommendations']), 0)

    def test_07_predict_empty_payload(self):
        """Test prediction with empty payload returns 400 error."""
        response = self.client.post(
            '/predict',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_08_predict_invalid_data_types(self):
        """Test prediction with non-numeric / invalid inputs returns 400 error."""
        payload = {
            "cgpa": "ABC_INVALID",
            "backlogs": 0,
            "coding_test_score": 80,
            "projects": 2,
            "internships": 1,
            "aptitude_test_score": 75,
            "soft_skills_rating": 4.0,
            "extracurriculars": 1
        }
        response = self.client.post(
            '/predict',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn("error", data)

    def test_09_predict_out_of_range_cgpa(self):
        """Test prediction with CGPA > 10.0 returns 400 error."""
        payload = {
            "cgpa": 14.5,
            "backlogs": 0,
            "coding_test_score": 80,
            "projects": 2,
            "internships": 1,
            "aptitude_test_score": 75,
            "soft_skills_rating": 4.0,
            "extracurriculars": 1
        }
        response = self.client.post(
            '/predict',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn("CGPA must be between 0.0 and 10.0", data['error'])

if __name__ == '__main__':
    unittest.main()
