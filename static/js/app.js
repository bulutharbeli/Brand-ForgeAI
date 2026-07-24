// Brand Forge AI - Main JavaScript File

// API Base URL
const API_BASE = window.location.origin;

// Utility Functions
function showLoading() {
    document.getElementById('loading-modal').classList.add('active');
}

function hideLoading() {
    document.getElementById('loading-modal').classList.remove('active');
}

function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

function watchDemo() {
    showToast('Demo video feature coming soon!', 'info');
}

// Tab Navigation
function switchTab(tabName) {
    // Update sidebar buttons
    const tabs = document.querySelectorAll('.demo-tab');
    tabs.forEach(tab => tab.classList.remove('active'));
    event.target.classList.add('active');
    
    // Update panels
    const panels = document.querySelectorAll('.panel');
    panels.forEach(panel => panel.classList.remove('active'));
    
    const targetPanel = document.getElementById(`${tabName}-panel`);
    if (targetPanel) {
        targetPanel.classList.add('active');
    }
}

// Feature Showcase
function showFeature(featureName) {
    scrollToSection('demo');
    setTimeout(() => {
        const targetTab = document.querySelector(`.demo-tab[onclick*="${featureName}"]`);
        if (targetTab) {
            targetTab.click();
        }
    }, 500);
}

// API Communication
async function apiRequest(endpoint, method = 'POST', data = null) {
    showLoading();
    
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };
        
        if (data && method === 'POST') {
            options.body = JSON.stringify(data);
        }
        
        const response = await fetch(`${API_BASE}/api/${endpoint}`, options);
        const result = await response.json();
        
        hideLoading();
        
        if (result.success) {
            return result;
        } else {
            showToast(result.error || 'An error occurred', 'error');
            return null;
        }
    } catch (error) {
        hideLoading();
        showToast('Failed to connect to the server. Please try again.', 'error');
        console.error('API Error:', error);
        return null;
    }
}

// Brand Name Generator
async function generateBrandNames() {
    const industry = document.getElementById('industry-select').value;
    const keywords = document.getElementById('keywords-input').value
        .split(',')
        .map(k => k.trim())
        .filter(k => k.length > 0);
    
    const style = document.querySelector('input[name="style"]:checked')?.value || 'modern';
    
    const result = await apiRequest('generate-brand-name', 'POST', {
        industry,
        keywords,
        style
    });
    
    if (result && result.names) {
        displayBrandNames(result.names);
        showToast('Brand names generated successfully!', 'success');
    }
}

function displayBrandNames(names) {
    const container = document.getElementById('brand-names-results');
    
    let html = '<div class="brand-names-grid">';
    
    names.forEach(name => {
        html += `
            <div class="brand-name-card" onclick="selectBrandName('${name}')">
                ${name}
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

function selectBrandName(name) {
    // Copy to clipboard
    navigator.clipboard.writeText(name).then(() => {
        showToast(`"${name}" copied to clipboard!`, 'success');
    }).catch(() => {
        showToast(`Selected: ${name}`, 'info');
    });
}

// Color Palette Generator
async function generateColorPalette() {
    const industry = document.getElementById('color-industry-select').value;
    const mood = document.getElementById('mood-select').value;
    const primaryColor = document.getElementById('primary-color-input').value;
    
    const result = await apiRequest('generate-color-palette', 'POST', {
        industry,
        mood,
        primary_color: primaryColor
    });
    
    if (result && result.palette) {
        displayColorPalette(result.palette);
        showToast('Color palette generated successfully!', 'success');
    }
}

function displayColorPalette(palette) {
    const container = document.getElementById('color-palette-results');
    
    let html = '<div class="color-palette-container">';
    
    // Palette Display
    html += '<div class="palette-display">';
    palette.hex_codes.forEach((hex, index) => {
        const role = ['primary', 'secondary', 'accent', 'neutral', 'success', 'warning', 'error', 'info'][index];
        html += `<div class="color-swatch" style="background: ${hex};" data-hex="${hex}" data-role="${role}"></div>`;
    });
    html += '</div>';
    
    // Color Details
    html += '<div class="color-details">';
    
    const roles = ['Primary', 'Secondary', 'Accent', 'Neutral', 'Success', 'Warning', 'Error', 'Info'];
    palette.hex_codes.forEach((hex, index) => {
        html += `
            <div class="color-detail-card">
                <h4>${roles[index]} Color</h4>
                <p style="font-family: monospace; color: ${hex}; font-weight: bold;">${hex}</p>
                <p style="font-size: 0.875rem; color: #666;">${palette.color_names[index]}</p>
                <p style="font-size: 0.8rem; color: #888; margin-top: 0.5rem;">
                    ${palette.usage_guidelines[roles[index].toLowerCase()] || 'Use as appropriate'}
                </p>
            </div>
        `;
    });
    
    html += '</div></div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

// Logo Concept Generator
async function generateLogoConcepts() {
    const brandName = document.getElementById('logo-brand-name').value;
    const industry = document.getElementById('logo-industry-select').value;
    const style = document.getElementById('logo-style-select').value;
    
    if (!brandName) {
        showToast('Please enter a brand name', 'error');
        return;
    }
    
    const result = await apiRequest('generate-logo-concepts', 'POST', {
        brand_name: brandName,
        industry,
        style
    });
    
    if (result && result.concepts) {
        displayLogoConcepts(result.concepts);
        showToast('Logo concepts generated successfully!', 'success');
    }
}

function displayLogoConcepts(concepts) {
    const container = document.getElementById('logo-concepts-results');
    
    let html = '<div class="logo-concepts-grid">';
    
    concepts.forEach(concept => {
        html += `
            <div class="logo-concept-card">
                <div class="logo-concept-header">
                    <span class="logo-concept-type">${concept.type}</span>
                </div>
                <h4 class="logo-concept-title">${concept.title}</h4>
                <p class="logo-concept-description">${concept.description}</p>
                
                <div class="logo-design-elements">
                    <h5>Design Elements</h5>
                    <div class="logo-elements-list">
                        ${concept.design_elements.map(el => `<span class="logo-element-tag">${el}</span>`).join('')}
                    </div>
                </div>
                
                <div class="logo-design-elements" style="margin-top: 1rem;">
                    <h5>Color Suggestions</h5>
                    <div class="logo-elements-list">
                        <span class="logo-element-tag" style="background: ${concept.color_suggestions.primary}; color: white;">Primary</span>
                        <span class="logo-element-tag" style="background: ${concept.color_suggestions.secondary}; color: white;">Secondary</span>
                        <span class="logo-element-tag" style="background: ${concept.color_suggestions.accent}; color: white;">Accent</span>
                    </div>
                </div>
                
                <div class="logo-design-elements" style="margin-top: 1rem;">
                    <h5>Typography</h5>
                    <p style="font-size: 0.9rem; color: #666;">${concept.typography.recommended_fonts[0]}</p>
                </div>
                
                <button class="btn-primary" style="margin-top: 1rem; width: 100%;" onclick="showToast('Logo download feature coming soon!', 'info')">
                    Download Concept
                </button>
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

// Slogan Generator
async function generateSlogans() {
    const brandName = document.getElementById('slogan-brand-name').value;
    const industry = document.getElementById('slogan-industry-select').value;
    const values = document.getElementById('values-input').value
        .split(',')
        .map(v => v.trim())
        .filter(v => v.length > 0);
    
    if (!brandName) {
        showToast('Please enter a brand name', 'error');
        return;
    }
    
    const result = await apiRequest('generate-slogan', 'POST', {
        brand_name: brandName,
        industry,
        values
    });
    
    if (result && result.slogans) {
        displaySlogans(result.slogans);
        showToast('Slogans generated successfully!', 'success');
    }
}

function displaySlogans(slogans) {
    const container = document.getElementById('slogan-results');
    
    let html = '<div class="slogans-grid">';
    
    slogans.forEach(slogan => {
        html += `
            <div class="slogan-card" onclick="selectSlogan('${slogan}')">
                "${slogan}"
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

function selectSlogan(slogan) {
    // Copy to clipboard
    navigator.clipboard.writeText(slogan).then(() => {
        showToast('Slogan copied to clipboard!', 'success');
    }).catch(() => {
        showToast(`Selected: ${slogan}`, 'info');
    });
}

// Competitor Analysis
async function analyzeCompetitors() {
    const industry = document.getElementById('analysis-industry-select').value;
    const competitors = document.getElementById('competitors-input').value
        .split(',')
        .map(c => c.trim())
        .filter(c => c.length > 0);
    
    if (competitors.length === 0) {
        showToast('Please enter at least one competitor', 'error');
        return;
    }
    
    const result = await apiRequest('analyze-competitors', 'POST', {
        industry,
        competitors
    });
    
    if (result && result.analysis) {
        displayCompetitorAnalysis(result.analysis);
        showToast('Competitor analysis complete!', 'success');
    }
}

function displayCompetitorAnalysis(analysis) {
    const container = document.getElementById('competitor-results');
    
    let html = '<div class="analysis-container">';
    
    // Market Overview
    html += `
        <div class="analysis-section">
            <h4>📊 Market Overview</h4>
            <p><strong>Market Size:</strong> ${analysis.market_overview.market_size}</p>
            <p><strong>Growth Rate:</strong> ${analysis.market_overview.growth_rate}</p>
            <p><strong>Competitive Intensity:</strong> ${analysis.market_overview.competitive_intensity}</p>
            <div style="margin-top: 1rem;">
                <strong>Key Trends:</strong>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    ${analysis.market_overview.key_trends.map(trend => `<li>${trend}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
    
    // Competitor Profiles
    html += `
        <div class="analysis-section">
            <h4>🏢 Competitor Profiles</h4>
            ${analysis.competitor_profiles.map(comp => `
                <div class="competitor-card">
                    <h5>${comp.name}</h5>
                    <div class="competitor-details">
                        <div class="competitor-detail">
                            <strong>Positioning</strong>
                            ${comp.estimated_positioning}
                        </div>
                        <div class="competitor-detail">
                            <strong>Brand Archetype</strong>
                            ${comp.brand_archetype}
                        </div>
                        <div class="competitor-detail">
                            <strong>Pricing Strategy</strong>
                            ${comp.probable_pricing_strategy}
                        </div>
                        <div class="competitor-detail">
                            <strong>Brand Voice</strong>
                            ${comp.brand_voice}
                        </div>
                    </div>
                    <div style="margin-top: 0.75rem;">
                        <strong>Strengths:</strong> ${comp.strengths.join(', ')}
                        <br>
                        <strong>Weaknesses:</strong> ${comp.weaknesses.join(', ')}
                    </div>
                </div>
            `).join('')}
        </div>
    `;
    
    // Brand Gaps
    html += `
        <div class="analysis-section">
            <h4>🎯 Identified Brand Gaps</h4>
            <ul style="margin-left: 1.5rem;">
                ${analysis.brand_gaps.map(gap => `<li>${gap}</li>`).join('')}
            </ul>
        </div>
    `;
    
    // Opportunities
    html += `
        <div class="analysis-section">
            <h4>💡 Opportunities</h4>
            <ul style="margin-left: 1.5rem;">
                ${analysis.opportunities.map(opp => `<li>${opp}</li>`).join('')}
            </ul>
        </div>
    `;
    
    // Recommendations
    html += `
        <div class="analysis-section">
            <h4>📋 Recommendations</h4>
            ${analysis.recommendations.map(rec => `
                <div style="margin-bottom: 1rem; padding: 1rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid ${rec.priority === 'High' ? '#EF4444' : rec.priority === 'Medium' ? '#F59E0B' : '#10B981'};">
                    <strong>Priority: ${rec.priority}</strong>
                    <p style="margin-top: 0.5rem;">${rec.recommendation}</p>
                    <p style="font-size: 0.875rem; color: #666; margin-top: 0.5rem;"><em>${rec.rationale}</em></p>
                </div>
            `).join('')}
        </div>
    `;
    
    html += '</div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

// Brand Guidelines Generator
async function generateGuidelines() {
    const brandName = document.getElementById('guidelines-brand-name').value;
    const industry = document.getElementById('guidelines-industry-select').value;
    const slogan = document.getElementById('guidelines-slogan').value;
    const voiceTone = document.getElementById('voice-select').value;
    
    if (!brandName) {
        showToast('Please enter a brand name', 'error');
        return;
    }
    
    // For demo, we'll generate a color palette first
    const colorResult = await apiRequest('generate-color-palette', 'POST', {
        industry,
        mood: 'professional'
    });
    
    if (!colorResult) return;
    
    const result = await apiRequest('generate-brand-guidelines', 'POST', {
        brand_name: brandName,
        industry,
        colors: {
            primary: colorResult.palette.hex_codes[0],
            secondary: colorResult.palette.hex_codes[1],
            accent: colorResult.palette.hex_codes[2]
        },
        slogan,
        voice_tone: voiceTone
    });
    
    if (result && result.guidelines) {
        displayGuidelines(result.guidelines);
        showToast('Brand guidelines generated successfully!', 'success');
    }
}

function displayGuidelines(guidelines) {
    const container = document.getElementById('guidelines-results');
    
    let html = '<div class="guidelines-container">';
    
    // Brand Overview
    html += `
        <div class="guidelines-section">
            <h4>📖 Brand Overview</h4>
            <div class="guidelines-content">
                <p><strong>Brand Name:</strong> ${guidelines.brand_name}</p>
                <p><strong>Industry:</strong> ${guidelines.industry}</p>
                <p><strong>Slogan:</strong> ${guidelines.slogan || 'Not specified'}</p>
                <p><strong>Brand Voice:</strong> ${guidelines.voice_tone}</p>
                <p style="margin-top: 1rem;">${guidelines.guidelines.brand_overview}</p>
            </div>
        </div>
    `;
    
    // Logo Usage
    html += `
        <div class="guidelines-section">
            <h4>🎨 Logo Usage</h4>
            <div class="guidelines-content">
                <ul>
                    ${guidelines.guidelines.logo_usage.map(rule => `<li>${rule}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
    
    // Color Palette
    html += `
        <div class="guidelines-section">
            <h4>🌈 Color Palette</h4>
            <div class="guidelines-content">
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <div style="flex: 1; height: 80px; background: ${guidelines.colors.primary || '#000000'}; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                        Primary
                    </div>
                    <div style="flex: 1; height: 80px; background: ${guidelines.colors.secondary || '#666666'}; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                        Secondary
                    </div>
                    <div style="flex: 1; height: 80px; background: ${guidelines.colors.accent || '#CCCCCC'}; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                        Accent
                    </div>
                </div>
                <ul>
                    <li><strong>Primary:</strong> ${guidelines.guidelines.color_usage.primary}</li>
                    <li><strong>Secondary:</strong> ${guidelines.guidelines.color_usage.secondary}</li>
                    <li><strong>Accent:</strong> ${guidelines.guidelines.color_usage.accent}</li>
                </ul>
            </div>
        </div>
    `;
    
    // Typography
    html += `
        <div class="guidelines-section">
            <h4>✏️ Typography</h4>
            <div class="guidelines-content">
                <p><strong>Heading Font:</strong> ${guidelines.guidelines.typography.heading_font}</p>
                <p><strong>Body Font:</strong> ${guidelines.guidelines.typography.body_font}</p>
                <p><em>${guidelines.guidelines.typography.note}</em></p>
            </div>
        </div>
    `;
    
    // Imagery Style
    html += `
        <div class="guidelines-section">
            <h4>📸 Imagery Style</h4>
            <div class="guidelines-content">
                <ul>
                    ${guidelines.guidelines.imagery_style.map(rule => `<li>${rule}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
    
    // Voice and Tone
    html += `
        <div class="guidelines-section">
            <h4>🗣️ Voice and Tone</h4>
            <div class="guidelines-content">
                <p><strong>Recommended Voice:</strong> ${guidelines.voice_tone}</p>
                <p>Maintain a consistent ${guidelines.voice_tone} tone across all communications.</p>
            </div>
        </div>
    `;
    
    // Do's and Don'ts
    html += `
        <div class="guidelines-section">
            <h4>✅❌ Do's and Don'ts</h4>
            <div class="guidelines-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <h5 style="color: #10B981;">Do's</h5>
                        <ul>
                            ${guidelines.guidelines.do_dont.do.map(item => `<li>${item}</li>`).join('')}
                        </ul>
                    </div>
                    <div>
                        <h5 style="color: #EF4444;">Don'ts</h5>
                        <ul>
                            ${guidelines.guidelines.do_dont.dont.map(item => `<li>${item}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Download Button
    html += `
        <div style="text-align: center; margin-top: 2rem;">
            <button class="btn-primary btn-large" onclick="showToast('PDF download feature coming soon!', 'info')">
                📥 Download Full Brand Guidelines (PDF)
            </button>
        </div>
    `;
    
    html += '</div>';
    container.innerHTML = html;
    container.classList.add('fade-in');
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    console.log('Brand Forge AI Platform Initialized');
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add scroll effect to navbar
    let lastScroll = 0;
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > lastScroll && currentScroll > 80) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
});
