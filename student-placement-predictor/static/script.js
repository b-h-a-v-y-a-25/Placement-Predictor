/**
 * EduPredict AI - Frontend JavaScript
 * Handles AJAX predictions, preset profiles, input validation, and dynamic UI rendering.
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const predictBtn = document.getElementById('predict-btn');
    const btnText = predictBtn.querySelector('.btn-text');
    const spinner = predictBtn.querySelector('.spinner');
    const errorAlert = document.getElementById('error-alert');

    const resultsPlaceholder = document.getElementById('results-placeholder');
    const resultsCard = document.getElementById('results-card');

    const statusBanner = document.getElementById('status-banner');
    const statusIcon = document.getElementById('status-icon');
    const statusTitle = document.getElementById('status-title');
    const statusSummary = document.getElementById('status-summary');
    const tierBadge = document.getElementById('tier-badge');

    const probPlacedText = document.getElementById('prob-placed-text');
    const probNotPlacedText = document.getElementById('prob-not-placed-text');
    const progressFill = document.getElementById('progress-fill');

    const evaluatedProfileGrid = document.getElementById('evaluated-profile-grid');
    const recommendationsList = document.getElementById('recommendations-list');

    // Preset configurations for instant live demonstration
    const PRESETS = {
        topper: {
            cgpa: 9.15,
            backlogs: 0,
            coding_test_score: 90,
            projects: 3,
            internships: 2,
            aptitude_test_score: 85,
            soft_skills_rating: 4.6,
            extracurriculars: 1
        },
        average: {
            cgpa: 7.30,
            backlogs: 0,
            coding_test_score: 68,
            projects: 2,
            internships: 1,
            aptitude_test_score: 65,
            soft_skills_rating: 3.4,
            extracurriculars: 0
        },
        at_risk: {
            cgpa: 5.75,
            backlogs: 2,
            coding_test_score: 40,
            projects: 1,
            internships: 0,
            aptitude_test_score: 42,
            soft_skills_rating: 2.3,
            extracurriculars: 0
        }
    };

    // Global helper to load preset
    window.loadPreset = function (presetKey) {
        if (!PRESETS[presetKey]) return;
        const p = PRESETS[presetKey];

        document.getElementById('cgpa').value = p.cgpa;
        document.getElementById('backlogs').value = p.backlogs;
        document.getElementById('coding_test_score').value = p.coding_test_score;
        document.getElementById('projects').value = p.projects;
        document.getElementById('internships').value = p.internships;
        document.getElementById('aptitude_test_score').value = p.aptitude_test_score;
        document.getElementById('soft_skills_rating').value = p.soft_skills_rating;
        document.getElementById('extracurriculars').value = p.extracurriculars;

        hideError();
        // Automatically submit the preset to show instantaneous prediction
        submitPrediction();
    };

    // Reset Form
    window.resetForm = function () {
        form.reset();
        hideError();
        resultsCard.style.display = 'none';
        resultsPlaceholder.style.display = 'block';
    };

    // Toggle Collapsible Architecture Details
    window.toggleDetails = function () {
        const content = document.getElementById('details-content');
        const arrow = document.getElementById('details-arrow');
        if (content.classList.contains('collapsed')) {
            content.classList.remove('collapsed');
            arrow.innerHTML = '&#9660;';
        } else {
            content.classList.add('collapsed');
            arrow.innerHTML = '&#9658;';
        }
    };

    function showError(message) {
        errorAlert.textContent = message;
        errorAlert.style.display = 'block';
    }

    function hideError() {
        errorAlert.textContent = '';
        errorAlert.style.display = 'none';
    }

    // Form Submission Handler
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        submitPrediction();
    });

    async function submitPrediction() {
        hideError();

        // Collect fields
        const payload = {
            cgpa: document.getElementById('cgpa').value.trim(),
            backlogs: document.getElementById('backlogs').value.trim(),
            coding_test_score: document.getElementById('coding_test_score').value.trim(),
            projects: document.getElementById('projects').value.trim(),
            internships: document.getElementById('internships').value.trim(),
            aptitude_test_score: document.getElementById('aptitude_test_score').value.trim(),
            soft_skills_rating: document.getElementById('soft_skills_rating').value.trim(),
            extracurriculars: document.getElementById('extracurriculars').value.trim()
        };

        // Client-side quick check
        for (const [key, val] of Object.entries(payload)) {
            if (val === '') {
                showError(`Please provide a value for all fields. Missing: ${key.replace(/_/g, ' ')}`);
                return;
            }
        }

        // Loading UI state
        predictBtn.disabled = true;
        btnText.textContent = "Analyzing Profile...";
        spinner.style.display = 'inline-block';

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (!response.ok || !data.success) {
                throw new Error(data.error || "Failed to generate prediction.");
            }

            renderResults(data);

        } catch (err) {
            showError(err.message);
        } finally {
            predictBtn.disabled = false;
            btnText.textContent = "▶ Predict Placement Outcome";
            spinner.style.display = 'none';
        }
    }

    function renderResults(data) {
        // Switch views
        resultsPlaceholder.style.display = 'none';
        resultsCard.style.display = 'block';

        const isPlaced = data.prediction === 1;
        const prob = data.placement_probability;
        const riskProb = data.not_placed_probability;

        // Status Banner
        if (isPlaced) {
            statusBanner.className = 'status-banner status-placed';
            statusIcon.innerHTML = '&#10004;';
            statusTitle.textContent = data.prediction_label;
        } else {
            statusBanner.className = 'status-banner status-at-risk';
            statusIcon.innerHTML = '&#9888;';
            statusTitle.textContent = data.prediction_label;
        }
        statusSummary.textContent = data.summary;

        // Tier Badge
        tierBadge.textContent = data.readiness_tier;

        // Probability and Progress Bar
        probPlacedText.textContent = `${prob.toFixed(1)}%`;
        probNotPlacedText.textContent = `${riskProb.toFixed(1)}%`;

        progressFill.style.width = `${prob}%`;
        if (prob >= 50) {
            progressFill.className = 'progress-fill';
        } else {
            progressFill.className = 'progress-fill danger';
        }

        // Profile Parameters Mini-Grid
        const inp = data.input_data;
        evaluatedProfileGrid.innerHTML = `
            <div class="mini-stat-box">
                <span class="mini-stat-label">CGPA</span>
                <span class="mini-stat-val">${inp.cgpa.toFixed(2)}</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Backlogs</span>
                <span class="mini-stat-val">${inp.backlogs}</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Coding Score</span>
                <span class="mini-stat-val">${inp.coding_test_score}/100</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Aptitude Score</span>
                <span class="mini-stat-val">${inp.aptitude_test_score}/100</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Projects</span>
                <span class="mini-stat-val">${inp.projects}</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Internships</span>
                <span class="mini-stat-val">${inp.internships}</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Soft Skills</span>
                <span class="mini-stat-val">${inp.soft_skills_rating}/5.0</span>
            </div>
            <div class="mini-stat-box">
                <span class="mini-stat-label">Activities</span>
                <span class="mini-stat-val">${inp.extracurriculars === 1 ? 'Yes' : 'No'}</span>
            </div>
        `;

        // Recommendations List
        recommendationsList.innerHTML = '';
        if (data.recommendations && data.recommendations.length > 0) {
            data.recommendations.forEach(rec => {
                const li = document.createElement('li');
                li.textContent = rec;
                recommendationsList.appendChild(li);
            });
        }

        // Smooth scroll to result on mobile screens
        if (window.innerWidth < 992) {
            resultsCard.scrollIntoView({ behavior: 'smooth' });
        }
    }
});
