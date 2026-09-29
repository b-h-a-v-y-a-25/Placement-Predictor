"""
generate_ppt.py
Generates a polished, professional 12-slide PowerPoint presentation (.pptx)
for the EduPredict AI college project presentation.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 widescreen
    prs.slide_height = Inches(7.5)

    # Color Palette: Modern Navy / Tech Blue
    PRIMARY_COLOR = RGBColor(30, 58, 138)     # Navy #1e3a8a
    ACCENT_COLOR = RGBColor(37, 99, 235)      # Royal Blue #2563eb
    TEXT_DARK = RGBColor(15, 23, 42)          # Slate Dark #0f172a
    TEXT_MUTED = RGBColor(71, 85, 105)        # Slate Muted #475569
    CARD_BG = RGBColor(248, 250, 252)         # Light Gray Card #f8fafc
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(22, 163, 74)             # Success Green

    def add_header(slide, title_text, category_text="COLLEGE MINI-PROJECT PRESENTATION"):
        # Header banner bar
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        banner.fill.solid()
        banner.fill.fore_color.rgb = PRIMARY_COLOR
        banner.line.fill.background()

        # Category text
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        cat_tf = cat_box.text_frame
        cat_tf.word_wrap = True
        p_cat = cat_tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(191, 219, 254)

        # Title text
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.5), Inches(0.65))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = WHITE

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY_COLOR
    bg.line.fill.background()

    # Title Box
    t_box = slide.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(2.2))
    t_tf = t_box.text_frame
    t_tf.word_wrap = True

    p0 = t_tf.paragraphs[0]
    p0.text = "EduPredict AI"
    p0.font.size = Pt(44)
    p0.font.bold = True
    p0.font.color.rgb = WHITE

    p1 = t_tf.add_paragraph()
    p1.text = "Student Academic Performance & Campus Placement Predictor"
    p1.font.size = Pt(26)
    p1.font.color.rgb = RGBColor(191, 219, 254)
    p1.space_before = Pt(8)

    p2 = t_tf.add_paragraph()
    p2.text = "An End-to-End Supervised Machine Learning Mini-Project using Random Forest Ensemble & Flask"
    p2.font.size = Pt(15)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(12)

    # Student Details Box
    s_box = slide.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.0))
    s_tf = s_box.text_frame
    s_tf.word_wrap = True

    sp1 = s_tf.paragraphs[0]
    sp1.text = "Presented By: [Your Name] | Roll No: [Your Roll No]"
    sp1.font.size = Pt(16)
    sp1.font.bold = True
    sp1.font.color.rgb = WHITE

    sp2 = s_tf.add_paragraph()
    sp2.text = "Department of Computer Science & Engineering / Information Technology"
    sp2.font.size = Pt(14)
    sp2.font.color.rgb = RGBColor(203, 213, 225)
    sp2.space_before = Pt(6)

    sp3 = s_tf.add_paragraph()
    sp3.text = "Guided By: [Professor / Guide Name] | Academic Year: 2026"
    sp3.font.size = Pt(14)
    sp3.font.color.rgb = RGBColor(203, 213, 225)
    sp3.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: Introduction & Motivation
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "1. Introduction & Background Motivation")

    # Card 1: The Context
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Campus Placement Landscape"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    points1 = [
        "Campus recruitment is the primary gateway for engineering students transitioning into industry careers.",
        "Graduating batches face intense competition and stringent multi-stage screening filters.",
        "Companies look beyond semester GPA: coding assessments, aptitude logic, internships, and communication are equally vital.",
        "Early diagnostic awareness allows students to fix weaknesses before the placement drives commence."
    ]
    for pt in points1:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Card 2: The Core Motivation
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Why Machine Learning?"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    points2 = [
        "Complex Non-Linear Relationships: Placement readiness is not a simple linear cutoff; it's a multi-factor interaction.",
        "Proactive Intervention: Predicts outcomes in advance rather than post-rejection analysis.",
        "Personalized Guidance: Pinpoints whether the student needs to focus on backlogs, coding practice, or mock interviews.",
        "Empowers Placement Cells: Enables Training and Placement Officers (TPOs) to organize targeted remedial bootcamps."
    ]
    for pt in points2:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 3: Problem Statement & Objectives
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "2. Problem Statement & Project Objectives")

    # Left: Problem Statement
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Problem Statement"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)  # Red

    prob_points = [
        "Unidimensional Evaluation: Students focus solely on CGPA, neglecting coding and practical projects until 7th semester.",
        "Strict Backlog Filters: 85%+ of recruitment drives enforce strict 0-backlog eligibility rules.",
        "Late Remediation: Absence of diagnostic tools leaves at-risk students unaware of their true placement risk.",
        "Lack of Transparent AI: Many proposed ML solutions act as black boxes without explainable feedback."
    ]
    for pt in prob_points:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Right: Project Objectives
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Project Objectives"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN

    obj_points = [
        "Build a Complete ML Pipeline: Preprocessing, StandardScaler normalization, model training, and evaluation.",
        "Train an Ensemble Classifier: Random Forest (100 trees) benchmarked against a baseline Decision Tree.",
        "Achieve High Predictive Accuracy: Deliver >88% accuracy and >95% recall to protect at-risk students.",
        "Generate Actionable Feedback: Automatically diagnose weaknesses and provide student-specific tips.",
        "Deploy a Local Web App: Interactive Flask interface with 1-click demo presets running 100% offline."
    ]
    for pt in obj_points:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 4: Technologies & Architecture
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "3. System Architecture & Tech Stack")

    # 3 Column Cards
    col_w = Inches(3.55)
    gap = Inches(0.4)

    # Tech 1: ML & Python
    x = Inches(0.9)
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), col_w, Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.8), col_w - Inches(0.4), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Machine Learning"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    t_pts1 = [
        "Python 3.14: Core programming language.",
        "Scikit-learn: Random Forest, Decision Tree, StandardScaler, metrics.",
        "Pandas & NumPy: Dataset loading, matrix operations & preprocessing.",
        "Joblib: Binary serialization of trained model & scaler (.pkl)."
    ]
    for pt in t_pts1:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Tech 2: Backend
    x = x + col_w + gap
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), col_w, Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.8), col_w - Inches(0.4), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Backend & API"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    t_pts2 = [
        "Flask WSGI: Lightweight Python web microframework.",
        "RESTful POST /predict: Handles JSON payload and returns prediction probability.",
        "GET /api/metrics: Exposes model evaluation & feature rankings.",
        "Strict Validation: Rejects invalid ranges or corrupt types."
    ]
    for pt in t_pts2:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Tech 3: Frontend
    x = x + col_w + gap
    c3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), col_w, Inches(5.2))
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_BG
    c3.line.color.rgb = RGBColor(226, 232, 240)

    tb3 = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.8), col_w - Inches(0.4), Inches(4.8))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "Frontend Interface"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    t_pts3 = [
        "HTML5 & Modern CSS3: Clean responsive grid, cards, custom color themes.",
        "Vanilla JavaScript: Asynchronous fetch() API requests without page reloads.",
        "Dynamic Gauges: Animated probability progress bar and status badges.",
        "1-Click Demo Presets: Instant testing for Topper, Average, and At-Risk profiles."
    ]
    for pt in t_pts3:
        p = tf3.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 5: Dataset & Features
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "4. Dataset & Multi-Dimensional Features")

    # Table of Features
    rows, cols = 9, 4
    left, top, width, height = Inches(0.9), Inches(1.6), Inches(11.5), Inches(5.2)
    table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(2.0)
    table.columns[2].width = Inches(1.8)
    table.columns[3].width = Inches(5.5)

    headers = ["Feature Name", "Category", "Range", "Academic Significance"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_COLOR
        for p in cell.text_frame.paragraphs:
            p.font.bold = True
            p.font.size = Pt(12)
            p.font.color.rgb = WHITE

    feat_data = [
        ("cgpa", "Academic", "5.0 - 10.0", "Semester grade point average; primary screening cutoff"),
        ("backlogs", "Academic", "0 - 5", "Uncleared subjects; primary negative filter (>85% companies require 0)"),
        ("coding_test_score", "Technical", "0 - 100", "Data Structures & Algorithms assessment; key technical indicator"),
        ("aptitude_test_score", "Aptitude", "0 - 100", "Quantitative & logical reasoning; preliminary round filter"),
        ("projects", "Practical", "0 - 6", "Completed engineering/software projects demonstrating applied skills"),
        ("internships", "Practical", "0 - 4", "Industry exposure through verified corporate internships"),
        ("soft_skills_rating", "Interpersonal", "1.0 - 5.0", "Communication, HR interview readiness, and professional presentation"),
        ("placed (Target)", "Outcome", "0 or 1", "Ground truth target: 1 = Placed / Top Tier, 0 = Placement at Risk")
    ]

    for row_idx, row_data in enumerate(feat_data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if row_idx % 2 == 0 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_DARK
                if col_idx == 0:
                    p.font.bold = True

    # =========================================================================
    # SLIDE 6: Machine Learning Methodology & Algorithm
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "5. ML Methodology: Random Forest Ensemble")

    # Left: Steps
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Pipeline Steps"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    m_steps = [
        "1. Train-Test Partitioning: 800 training samples (80%) and 200 testing samples (20%) using stratified sampling (stratify=y).",
        "2. Feature Standardization: Z-score normalization: z = (x - μ) / σ using StandardScaler fitted strictly on training data.",
        "3. Baseline Model: Decision Tree Classifier (max_depth=5).",
        "4. Primary Model: Random Forest Classifier (n_estimators=100, max_depth=6).",
        "5. Probability Estimation: Soft voting across 100 trees via predict_proba()."
    ]
    for pt in m_steps:
        p = tf1.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right: Why Random Forest Works
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Why Random Forest Ensemble?"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    rf_pts = [
        "Bootstrap Aggregation (Bagging): Trains 100 individual trees on random subsets of data with replacement.",
        "Feature Sub-sampling: Evaluates a random subset of features (√p ≈ 3) at each split, decorrelating trees.",
        "Variance Reduction: Single decision trees suffer from high variance and overfitting; bagging smooths out decision boundaries.",
        "Gini Impurity Metric: Measures impurity reduction to determine the most informative splits: I_G(t) = 1 - Σ(p_i²).",
        "Built-in Feature Importance: Quantifies exactly which factors carry the highest predictive power."
    ]
    for pt in rf_pts:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 7: Model Performance & Results
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "6. Model Performance & Evaluation Metrics")

    # 4 Metric Stat Cards across top
    stats = [
        ("TEST ACCURACY", "90.00%", "High overall correctness"),
        ("PRECISION", "89.68%", "Minimal false placement alarms"),
        ("RECALL", "97.20%", "Finds 97.2% of placed students"),
        ("F1-SCORE", "0.9329%", "Harmonic balance")
    ]

    card_w = Inches(2.65)
    gap = Inches(0.3)
    start_x = Inches(0.9)

    for i, (label, val, sub) in enumerate(stats):
        x = start_x + i * (card_w + gap)
        sc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), card_w, Inches(1.5))
        sc.fill.solid()
        sc.fill.fore_color.rgb = CARD_BG
        sc.line.color.rgb = RGBColor(226, 232, 240)

        sctb = slide.shapes.add_textbox(x, Inches(1.7), card_w, Inches(1.3))
        sctf = sctb.text_frame
        sctf.word_wrap = True

        p = sctf.paragraphs[0]
        p.text = label
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_MUTED

        p = sctf.add_paragraph()
        p.text = val
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_COLOR

        p = sctf.add_paragraph()
        p.text = sub
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_MUTED

    # Bottom Left: Confusion Matrix
    c_cm = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(3.4), Inches(5.6), Inches(3.4))
    c_cm.fill.solid()
    c_cm.fill.fore_color.rgb = CARD_BG
    c_cm.line.color.rgb = RGBColor(226, 232, 240)

    tb_cm = slide.shapes.add_textbox(Inches(1.1), Inches(3.5), Inches(5.2), Inches(3.2))
    tf_cm = tb_cm.text_frame
    tf_cm.word_wrap = True

    p = tf_cm.paragraphs[0]
    p.text = "Confusion Matrix (200 Test Records)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    cm_lines = [
        "• True Negatives (TN = 41): At-risk students accurately caught.",
        "• False Positives (FP = 16): At-risk students predicted as placed.",
        "• False Negatives (FN = 4): Placed students predicted as at-risk.",
        "• True Positives (TP = 139): Placed candidates accurately validated.",
        "-> Crucial Takeaway: Only 4 False Negatives proves exceptionally high sensitivity (97.2% Recall)!"
    ]
    for l in cm_lines:
        p = tf_cm.add_paragraph()
        p.text = l
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(6)

    # Bottom Right: Baseline Comparison Table
    c_bs = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.4), Inches(5.6), Inches(3.4))
    c_bs.fill.solid()
    c_bs.fill.fore_color.rgb = CARD_BG
    c_bs.line.color.rgb = RGBColor(226, 232, 240)

    tb_bs = slide.shapes.add_textbox(Inches(7.0), Inches(3.5), Inches(5.2), Inches(3.2))
    tf_bs = tb_bs.text_frame
    tf_bs.word_wrap = True

    p = tf_bs.paragraphs[0]
    p.text = "Model Comparison: Baseline vs Random Forest"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    cmp_lines = [
        "• Baseline Model: Single Decision Tree (depth=5)",
        "   - Accuracy: 91.00% | F1-Score: 0.9371",
        "• Primary Ensemble: Random Forest (100 trees, depth=6)",
        "   - Accuracy: 90.00% | F1-Score: 0.9329 | Recall: 97.20%",
        "• Advantage of Random Forest: Far lower variance on unobserved data; avoids single-tree bias and offers built-in probability confidence scoring."
    ]
    for l in cmp_lines:
        p = tf_bs.add_paragraph()
        p.text = l
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 8: Feature Importance (Gini Analysis)
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "7. Explainable AI: Feature Importance Analysis")

    # Left: Explanation
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.6), Inches(4.8), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(4.4), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "What Drives Placement?"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    fi_insights = [
        "The Random Forest model extracts Gini Impurity reduction to rank feature contributions.",
        "Top 3 Factors account for ~77% of predictive power:",
        "  1. CGPA (33.4%): Acts as the fundamental gateway for campus recruitment eligibility.",
        "  2. Backlogs (22.1%): Severe negative filter; disqualifies candidates at registration.",
        "  3. Coding Score (21.1%): Technical qualifier for written rounds.",
        "Practical & Soft Skills (Aptitude, Projects, Internships, Soft Skills) decide final offer conversions."
    ]
    for pt in fi_insights:
        p = tf1.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right: Visual Ranking Table
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.0), Inches(1.6), Inches(6.4), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(6.2), Inches(1.8), Inches(6.0), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Gini Importance Hierarchy"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    fi_bars = [
        ("CGPA (Grade Point Average)", "33.41%", "██████████████"),
        ("Active Backlogs / Arrears", "22.13%", "█████████"),
        ("Coding Test Score", "21.13%", "█████████"),
        ("Aptitude & Logic Score", "10.75%", "████"),
        ("Soft Skills / HR Rating", "4.61%", "██"),
        ("Projects Completed", "4.58%", "██"),
        ("Internships Completed", "2.95%", "█"),
        ("Extracurricular Activities", "0.43%", "▎")
    ]
    for feat, pct, bar in fi_bars:
        p = tf2.add_paragraph()
        p.text = f"{feat}: {pct}  {bar}"
        p.font.size = Pt(12)
        p.font.bold = True if "CGPA" in feat or "Backlogs" in feat or "Coding" in feat else False
        p.font.color.rgb = PRIMARY_COLOR if "CGPA" in feat or "Backlogs" in feat else TEXT_DARK
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 9: Web Application & UI Features
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "8. Web Application & Live Demo Features")

    # 4 Feature Boxes (2x2 Grid)
    box_w, box_h = Inches(5.4), Inches(2.4)
    x1, x2 = Inches(0.9), Inches(7.0)
    y1, y2 = Inches(1.6), Inches(4.3)

    grid_items = [
        (x1, y1, "1. Responsive Input Form", [
            "Grouped into Academic, Technical, and Soft Skills sections.",
            "Complete validation: restricts CGPA to 0-10, scores to 0-100.",
            "Prevents empty inputs and rejects non-numeric entries gracefully."
        ]),
        (x2, y1, "2. 1-Click Demo Presets", [
            "🏆 Top Achiever Preset: Fills 9.15 CGPA, 0 backlogs -> 99.1% Placed.",
            "⚖️ Average Student Preset: Fills 7.30 CGPA, 0 backlogs -> 94.4% Placed.",
            "⚠️ At-Risk Student Preset: Fills 5.75 CGPA, 2 backlogs -> 1.2% At-Risk."
        ]),
        (x1, y2, "3. Visual Placement Gauge", [
            "Dynamic color-coded probability bar (Green for ≥50%, Red for <50%).",
            "Readiness Tier Classification (Top Tier, Competitive, At-Risk).",
            "Full evaluation breakdown card summarizing submitted profile."
        ]),
        (x2, y2, "4. Personalized AI Advice Engine", [
            "Translates raw probability into actionable advice.",
            "Flags backlogs with priority 1 warning to clear arrears.",
            "Recommends LeetCode/HackerRank DSA practice if coding < 60."
        ])
    ]

    for gx, gy, gtitle, gpoints in grid_items:
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx, gy, box_w, box_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(226, 232, 240)

        tb = slide.shapes.add_textbox(gx + Inches(0.2), gy + Inches(0.15), box_w - Inches(0.4), box_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = gtitle
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_COLOR

        for pt in gpoints:
            p = tf.add_paragraph()
            p.text = "• " + pt
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 10: Testing & Verification
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "9. Testing & Quality Assurance")

    # Left: Test Suite
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.6), Inches(5.3), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(4.9), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Automated Unit Tests (test_app.py)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    tests = [
        "Test 01: Home page loads with 200 OK and expected HTML elements.",
        "Test 02: /health endpoint confirms model is loaded.",
        "Test 03: /api/metrics exposes accuracy and feature rankings.",
        "Test 04: /api/sample/topper returns preset data.",
        "Test 05: Top candidate produces prediction=1 & prob >= 80%.",
        "Test 06: At-risk candidate produces prediction=0 & prob < 50%.",
        "Test 07: Empty payload safely rejected with HTTP 400.",
        "Test 08: Non-numeric strings rejected with HTTP 400.",
        "Test 09: Out-of-bounds inputs (CGPA=14.5) caught with clear error."
    ]
    for t in tests:
        p = tf1.add_paragraph()
        p.text = "✔ " + t
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(4)

    # Right: Test Results Summary Card
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.2), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Verification Summary"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = GREEN

    v_pts = [
        "100% Pass Rate: All 9 unit tests execute and pass in 0.44 seconds.",
        "Dual-Layer Validation: Client-side JavaScript validation + Server-side Python range validation.",
        "Zero Cloud Dependency: Operates completely on local localhost without requiring an internet connection.",
        "Zero API Cost: Uses purely open-source libraries (Scikit-learn, Flask, Pandas).",
        "Student Laptop Friendly: Entire training and inference pipeline runs smoothly on minimal CPU/RAM."
    ]
    for v in v_pts:
        p = tf2.add_paragraph()
        p.text = "• " + v
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 11: Limitations & Future Scope
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, "10. Limitations & Future Roadmap")

    # Left: Limitations
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(226, 232, 240)

    tb1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Current Limitations"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)

    lim_pts = [
        "Binary Outcome Only: Predicts placement eligibility rather than specific company salary packages (CTC).",
        "Manual Input Required: Students must manually type their metrics rather than uploading a PDF resume.",
        "Static Rule Guidance: Advice engine uses heuristic thresholds rather than dynamic market trends.",
        "Synthetic Data Baseline: Dataset reflects academic patterns but does not account for macroeconomic hiring freezes."
    ]
    for pt in lim_pts:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Right: Future Scope
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(1.6), Inches(5.3), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = slide.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(4.9), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Future Scope & Enhancements"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    fut_pts = [
        "Multi-Class CTC Prediction: Predict salary tiers (e.g., 3-6 LPA, 6-12 LPA, 12+ LPA Super Dream).",
        "NLP Resume Parsing: Extract technical skills, GitHub links, and projects automatically from uploaded PDF resumes.",
        "College ERP Integration: Direct integration with university student database for automated batch analysis.",
        "What-If Counterfactual Simulator: Show students how a 10-point coding score boost directly improves placement odds."
    ]
    for pt in fut_pts:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 12: Conclusion & Q&A
    # =========================================================================
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY_COLOR
    bg.line.fill.background()

    # Center Box
    t_box = slide.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(10.333), Inches(4.0))
    t_tf = t_box.text_frame
    t_tf.word_wrap = True

    p0 = t_tf.paragraphs[0]
    p0.text = "Conclusion & Summary"
    p0.alignment = PP_ALIGN.CENTER
    p0.font.size = Pt(36)
    p0.font.bold = True
    p0.font.color.rgb = WHITE

    p1 = t_tf.add_paragraph()
    p1.text = "EduPredict AI successfully demonstrates the power of Machine Learning in Academic Advising.\n" \
              "By combining Random Forest classification (90% Accuracy, 97.2% Recall) with an explainable web dashboard,\n" \
              "it bridges the gap between raw data and actionable student guidance."
    p1.alignment = PP_ALIGN.CENTER
    p1.font.size = Pt(16)
    p1.font.color.rgb = RGBColor(226, 232, 240)
    p1.space_before = Pt(16)

    p2 = t_tf.add_paragraph()
    p2.text = "Thank You!"
    p2.alignment = PP_ALIGN.CENTER
    p2.font.size = Pt(40)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(191, 219, 254)
    p2.space_before = Pt(24)

    p3 = t_tf.add_paragraph()
    p3.text = "Questions & Answers (Viva Voce)"
    p3.alignment = PP_ALIGN.CENTER
    p3.font.size = Pt(18)
    p3.font.color.rgb = WHITE
    p3.space_before = Pt(8)

    # Save presentation
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "EduPredict_AI_Presentation.pptx")
    prs.save(output_path)
    print(f"[SUCCESS] PowerPoint presentation saved at: {output_path}")

if __name__ == '__main__':
    create_presentation()
