// Brand Forge AI - Dashboard JavaScript

// Load brands on page load
document.addEventListener('DOMContentLoaded', function() {
    loadBrands();
});

// Load all brands from API
async function loadBrands() {
    const container = document.getElementById('brands-container');
    const loadingState = document.getElementById('loading-state');
    const emptyState = document.getElementById('empty-state');
    
    // Show loading state
    if (loadingState) loadingState.style.display = 'block';
    if (emptyState) emptyState.style.display = 'none';
    
    try {
        const response = await fetch(`${API_BASE}/api/list-brands`);
        const result = await response.json();
        
        if (result.success && result.brands) {
            if (result.brands.length === 0) {
                // Show empty state
                if (loadingState) loadingState.style.display = 'none';
                if (emptyState) emptyState.style.display = 'block';
                container.innerHTML = '';
                container.appendChild(emptyState);
            } else {
                // Display brands
                displayBrands(result.brands);
            }
        } else {
            showToast('Failed to load brands', 'error');
        }
    } catch (error) {
        console.error('Error loading brands:', error);
        showToast('Failed to connect to server', 'error');
    } finally {
        if (loadingState) loadingState.style.display = 'none';
    }
}

// Display brands in grid
function displayBrands(brands) {
    const container = document.getElementById('brands-container');
    
    let html = '';
    
    brands.forEach(brand => {
        const date = new Date(brand.created_at).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
        
        html += `
            <div class="brand-card" onclick="viewBrand('${brand.id}')">
                <div class="brand-card-header">
                    <div>
                        <h3 class="brand-name">${brand.brand_name}</h3>
                        <span class="brand-industry">${brand.industry}</span>
                    </div>
                </div>
                <div class="brand-card-footer">
                    <span class="brand-date">Created: ${date}</span>
                    <div class="brand-actions">
                        <button class="btn-icon" onclick="event.stopPropagation(); viewBrand('${brand.id}')" title="View">👁️</button>
                        <button class="btn-icon" onclick="event.stopPropagation(); exportBrand('${brand.id}')" title="Export">📥</button>
                        <button class="btn-icon" onclick="event.stopPropagation(); confirmDelete('${brand.id}', '${brand.brand_name}')" title="Delete">🗑️</button>
                    </div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// View brand details
async function viewBrand(brandId) {
    try {
        const response = await fetch(`${API_BASE}/api/get-brand/${brandId}`);
        const result = await response.json();
        
        if (result.success && result.brand) {
            displayBrandModal(result.brand);
        } else {
            showToast('Failed to load brand details', 'error');
        }
    } catch (error) {
        console.error('Error loading brand:', error);
        showToast('Failed to connect to server', 'error');
    }
}

// Display brand in modal
function displayBrandModal(brand) {
    const modal = document.getElementById('brand-modal');
    const modalBody = document.getElementById('modal-body');
    const modalBrandName = document.getElementById('modal-brand-name');
    
    modalBrandName.textContent = brand.brand_name;
    
    let html = '';
    
    // Brand Overview
    html += `
        <div class="brand-detail-section">
            <h3>📖 Brand Overview</h3>
            <p><strong>Industry:</strong> ${brand.industry}</p>
            <p><strong>Slogan:</strong> ${brand.slogan || 'Not specified'}</p>
            <p><strong>Voice Tone:</strong> ${brand.voice_tone}</p>
            <p><strong>Created:</strong> ${new Date(brand.created_at).toLocaleDateString()}</p>
        </div>
    `;
    
    // Color Palette
    if (brand.colors && Object.keys(brand.colors).length > 0) {
        html += `
            <div class="brand-detail-section">
                <h3>🎨 Color Palette</h3>
                <div class="brand-detail-colors">
                    ${brand.colors.hex_codes ? brand.colors.hex_codes.map((hex, index) => {
                        const roles = ['Primary', 'Secondary', 'Accent', 'Neutral'];
                        const role = roles[index] || `Color ${index + 1}`;
                        return `
                            <div class="detail-color-item">
                                <div class="detail-color-box" style="background: ${hex};"></div>
                                <div class="detail-color-label">${role}</div>
                                <div class="detail-color-label" style="color: ${hex};">${hex}</div>
                            </div>
                        `;
                    }).join('') : '<p>No colors specified</p>'}
                </div>
            </div>
        `;
    }
    
    // Guidelines Summary
    if (brand.guidelines && brand.guidelines.guidelines) {
        const guidelines = brand.guidelines.guidelines;
        
        html += `
            <div class="brand-detail-section">
                <h3>📋 Brand Guidelines Summary</h3>
                <div class="brand-guidelines-preview">
        `;
        
        if (guidelines.logo_usage) {
            html += `
                <div class="guidelines-section">
                    <h4>Logo Usage</h4>
                    <ul>
                        ${guidelines.logo_usage.slice(0, 3).map(rule => `<li>${rule}</li>`).join('')}
                    </ul>
                </div>
            `;
        }
        
        if (guidelines.typography) {
            html += `
                <div class="guidelines-section">
                    <h4>Typography</h4>
                    <p><strong>Heading Font:</strong> ${guidelines.typography.heading_font}</p>
                    <p><strong>Body Font:</strong> ${guidelines.typography.body_font}</p>
                </div>
            `;
        }
        
        html += `
                </div>
            </div>
        `;
    }
    
    // Action Buttons
    html += `
        <div class="brand-detail-section" style="border: none; padding: 0; margin-top: 2rem;">
            <div style="display: flex; gap: 1rem; justify-content: center;">
                <button class="btn-primary" onclick="exportBrand('${brand.id}')">
                    📥 Export Brand Package
                </button>
                <button class="btn-secondary" onclick="closeModal()">
                    Close
                </button>
            </div>
        </div>
    `;
    
    modalBody.innerHTML = html;
    modal.classList.add('active');
}

// Close modal
function closeModal() {
    const modal = document.getElementById('brand-modal');
    modal.classList.remove('active');
}

// Export brand
async function exportBrand(brandId) {
    try {
        showToast('Preparing export...', 'info');
        
        const response = await fetch(`${API_BASE}/api/export-brand/${brandId}`);
        const result = await response.json();
        
        if (result.success && result.brand_data) {
            // For now, download as JSON
            const dataStr = JSON.stringify(result.brand_data, null, 2);
            const dataBlob = new Blob([dataStr], { type: 'application/json' });
            
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `${result.brand_data.brand_name.replace(/\s+/g, '_')}_brand_package.json`;
            link.click();
            
            URL.revokeObjectURL(url);
            
            showToast('Brand exported successfully!', 'success');
        } else {
            showToast('Failed to export brand', 'error');
        }
    } catch (error) {
        console.error('Error exporting brand:', error);
        showToast('Failed to connect to server', 'error');
    }
}

// Confirm delete
let brandToDelete = null;

function confirmDelete(brandId, brandName) {
    brandToDelete = brandId;
    const modal = document.getElementById('delete-modal');
    const confirmBtn = document.getElementById('confirm-delete-btn');
    
    // Update modal text
    modal.querySelector('p').textContent = `Are you sure you want to delete "${brandName}"? This action cannot be undone.`;
    
    // Set up confirm button
    confirmBtn.onclick = () => deleteBrand(brandId);
    
    modal.classList.add('active');
}

function closeDeleteModal() {
    const modal = document.getElementById('delete-modal');
    modal.classList.remove('active');
    brandToDelete = null;
}

// Delete brand
async function deleteBrand(brandId) {
    try {
        const response = await fetch(`${API_BASE}/api/delete-brand/${brandId}`, {
            method: 'DELETE'
        });
        
        const result = await response.json();
        
        if (result.success) {
            showToast('Brand deleted successfully', 'success');
            closeDeleteModal();
            loadBrands(); // Reload the list
        } else {
            showToast('Failed to delete brand', 'error');
        }
    } catch (error) {
        console.error('Error deleting brand:', error);
        showToast('Failed to connect to server', 'error');
    }
}

// Refresh brands
function refreshBrands() {
    loadBrands();
    showToast('Refreshing brands...', 'info');
}

// Close modals on outside click
window.addEventListener('click', function(event) {
    const brandModal = document.getElementById('brand-modal');
    const deleteModal = document.getElementById('delete-modal');
    
    if (event.target === brandModal) {
        closeModal();
    }
    
    if (event.target === deleteModal) {
        closeDeleteModal();
    }
});
