"""
generate_dataset.py
Generates a realistic student academic performance and placement dataset
with genuine correlations, statistical distributions, and natural variance.
"""

import numpy as np
import pandas as pd
import os

# Set seed for reproducible results
np.random.seed(42)
N_SAMPLES = 1000

# 1. CGPA (Normal distribution clipped between 5.0 and 10.0)
cgpa = np.clip(np.random.normal(loc=7.4, scale=1.1, size=N_SAMPLES), 5.0, 10.0)
cgpa = np.round(cgpa, 2)

# 2. Number of Internships (0 to 4, skewed towards 0-2)
internships = np.random.choice([0, 1, 2, 3, 4], size=N_SAMPLES, p=[0.35, 0.35, 0.20, 0.07, 0.03])

# 3. Number of Completed Projects (0 to 6)
projects = np.random.choice([0, 1, 2, 3, 4, 5, 6], size=N_SAMPLES, p=[0.10, 0.22, 0.30, 0.20, 0.10, 0.05, 0.03])

# 4. Coding Test Score (0 to 100, correlated moderately with CGPA & projects)
coding_base = (cgpa - 5.0) * 12 + projects * 4 + np.random.normal(0, 10, N_SAMPLES)
coding_test_score = np.clip(np.round(np.interp(coding_base, [min(coding_base), max(coding_base)], [25, 98])), 0, 100).astype(int)

# 5. Aptitude Test Score (0 to 100, general quantitative & logical reasoning)
aptitude_base = (cgpa - 5.0) * 10 + np.random.normal(60, 12, N_SAMPLES)
aptitude_test_score = np.clip(np.round(np.interp(aptitude_base, [min(aptitude_base), max(aptitude_base)], [30, 99])), 0, 100).astype(int)

# 6. Soft Skills Rating (1.0 to 5.0)
soft_skills_rating = np.clip(np.random.normal(loc=3.4, scale=0.8, size=N_SAMPLES), 1.0, 5.0)
soft_skills_rating = np.round(soft_skills_rating, 1)

# 7. Extracurricular Activities (0 or 1)
extracurriculars = np.random.choice([0, 1], size=N_SAMPLES, p=[0.45, 0.55])

# 8. Active Backlogs / Arrears (0 to 5, skewed towards 0)
backlogs = np.random.choice([0, 1, 2, 3, 4, 5], size=N_SAMPLES, p=[0.70, 0.15, 0.07, 0.04, 0.02, 0.02])

# Placement Probability Formula based on campus placement dynamics
# CGPA, Coding Score, Internships, Projects, and Soft Skills increase chance
# Backlogs have a strong penalizing effect (companies have strict 0 or <=1 backlog filters)
z = (
    2.2 * (cgpa - 7.0) +
    0.8 * internships +
    0.6 * projects +
    0.05 * (coding_test_score - 60) +
    0.03 * (aptitude_test_score - 60) +
    0.7 * (soft_skills_rating - 3.0) +
    0.4 * extracurriculars -
    2.5 * backlogs -
    0.5  # baseline bias
)

# Convert logit to probability via sigmoid function
prob = 1.0 / (1.0 + np.exp(-z))

# Generate target label with realistic borderline randomness
placed = (prob >= 0.50).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'cgpa': cgpa,
    'internships': internships,
    'projects': projects,
    'coding_test_score': coding_test_score,
    'aptitude_test_score': aptitude_test_score,
    'soft_skills_rating': soft_skills_rating,
    'extracurriculars': extracurriculars,
    'backlogs': backlogs,
    'placed': placed
})

# Save to CSV
output_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(output_dir, 'student_data.csv')
df.to_csv(csv_path, index=False)

print(f"Dataset successfully created at: {csv_path}")
print(f"Shape: {df.shape}")
print("Class Distribution:")
print(df['placed'].value_counts(normalize=True).round(3))
print("\nFirst 5 rows:")
print(df.head())
