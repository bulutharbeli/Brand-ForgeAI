from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from flask_cors import CORS
import os
import json
import random
from datetime import datetime
from utils.brand_ai import BrandAIGenerator
from utils.color_generator import ColorPaletteGenerator
from utils.logo_generator import LogoConceptGenerator
from utils.competitor_analyzer import CompetitorAnalyzer
import uuid
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'brand-forge-ai-secret-key'
app.config['DATABASE'] = 'brand_forge.db'
app.config['MAX_BRANDS'] = 50

# Initialize AI generators
brand_ai = BrandAIGenerator()
color_gen = ColorPaletteGenerator()
logo_gen = LogoConceptGenerator()
comp_analyzer = CompetitorAnalyzer()

# Initialize database
def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect(app.config['DATABASE'])
    c = conn.cursor()
    
    # Create brands table
    c.execute('''CREATE TABLE IF NOT EXISTS brands
                 (id TEXT PRIMARY KEY,
                  brand_name TEXT,
                  industry TEXT,
                  colors TEXT,
                  slogan TEXT,
                  voice_tone TEXT,
                  guidelines TEXT,
                  created_at TEXT,
                  updated_at TEXT)''')
    
    # Create users table (simplified)
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id TEXT PRIMARY KEY,
                  session_id TEXT,
                  created_at TEXT)''')
    
    conn.commit()
    conn.close()

init_db()

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard to view saved brands"""
    return render_template('dashboard.html')

# API Endpoints
@app.route('/api/generate-brand-name', methods=['POST'])
def generate_brand_name():
    """Generate AI-powered brand names"""
    try:
        data = request.json
        industry = data.get('industry', '')
        keywords = data.get('keywords', [])
        style = data.get('style', 'modern')
        
        names = brand_ai.generate_brand_names(industry, keywords, style)
        return jsonify({'success': True, 'names': names})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/generate-color-palette', methods=['POST'])
def generate_color_palette():
    """Generate brand color palettes"""
    try:
        data = request.json
        industry = data.get('industry', '')
        mood = data.get('mood', 'professional')
        primary_color = data.get('primary_color', None)
        
        palette = color_gen.generate_palette(industry, mood, primary_color)
        return jsonify({'success': True, 'palette': palette})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/generate-logo-concepts', methods=['POST'])
def generate_logo_concepts():
    """Generate logo design concepts"""
    try:
        data = request.json
        brand_name = data.get('brand_name', '')
        industry = data.get('industry', '')
        style = data.get('style', 'minimalist')
        
        if not brand_name:
            return jsonify({'success': False, 'error': 'Brand name is required'}), 400
        
        concepts = logo_gen.generate_concepts(brand_name, industry, style)
        return jsonify({'success': True, 'concepts': concepts})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/generate-slogan', methods=['POST'])
def generate_slogan():
    """Generate brand slogans and taglines"""
    try:
        data = request.json
        brand_name = data.get('brand_name', '')
        industry = data.get('industry', '')
        values = data.get('values', [])
        
        if not brand_name:
            return jsonify({'success': False, 'error': 'Brand name is required'}), 400
        
        slogans = brand_ai.generate_slogans(brand_name, industry, values)
        return jsonify({'success': True, 'slogans': slogans})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/analyze-competitors', methods=['POST'])
def analyze_competitors():
    """Analyze competitor branding"""
    try:
        data = request.json
        industry = data.get('industry', '')
        competitors = data.get('competitors', [])
        
        if not competitors:
            return jsonify({'success': False, 'error': 'At least one competitor is required'}), 400
        
        analysis = comp_analyzer.analyze(industry, competitors)
        return jsonify({'success': True, 'analysis': analysis})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/generate-brand-guidelines', methods=['POST'])
def generate_brand_guidelines():
    """Generate complete brand guidelines document"""
    try:
        data = request.json
        brand_name = data.get('brand_name', '')
        industry = data.get('industry', '')
        colors = data.get('colors', {})
        slogan = data.get('slogan', '')
        voice_tone = data.get('voice_tone', 'professional')
        
        if not brand_name:
            return jsonify({'success': False, 'error': 'Brand name is required'}), 400
        
        brand_id = str(uuid.uuid4())
        
        guidelines = {
            'brand_id': brand_id,
            'brand_name': brand_name,
            'industry': industry,
            'colors': colors,
            'slogan': slogan,
            'voice_tone': voice_tone,
            'created_at': datetime.now().isoformat(),
            'guidelines': brand_ai.generate_guidelines(brand_name, industry, colors, slogan, voice_tone)
        }
        
        # Save to database
        conn = get_db()
        c = conn.cursor()
        c.execute('''INSERT INTO brands (id, brand_name, industry, colors, slogan, voice_tone, guidelines, created_at, updated_at)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (brand_id, brand_name, industry, json.dumps(colors), slogan, voice_tone, 
                   json.dumps(guidelines), datetime.now().isoformat(), datetime.now().isoformat()))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'brand_id': brand_id, 'guidelines': guidelines})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/get-brand/<brand_id>', methods=['GET'])
def get_brand(brand_id):
    """Retrieve a generated brand"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM brands WHERE id = ?', (brand_id,))
        row = c.fetchone()
        conn.close()
        
        if row:
            brand = {
                'id': row[0],
                'brand_name': row[1],
                'industry': row[2],
                'colors': json.loads(row[3]) if row[3] else {},
                'slogan': row[4],
                'voice_tone': row[5],
                'guidelines': json.loads(row[6]) if row[6] else {},
                'created_at': row[7],
                'updated_at': row[8]
            }
            return jsonify({'success': True, 'brand': brand})
        else:
            return jsonify({'success': False, 'error': 'Brand not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/save-brand', methods=['POST'])
def save_brand():
    """Save or update a brand profile"""
    try:
        data = request.json
        brand_id = data.get('brand_id', str(uuid.uuid4()))
        
        conn = get_db()
        c = conn.cursor()
        
        # Check if brand exists
        c.execute('SELECT id FROM brands WHERE id = ?', (brand_id,))
        exists = c.fetchone()
        
        if exists:
            # Update existing brand
            c.execute('''UPDATE brands 
                         SET brand_name = ?, industry = ?, colors = ?, slogan = ?, 
                             voice_tone = ?, guidelines = ?, updated_at = ?
                         WHERE id = ?''',
                      (data.get('brand_name', ''), data.get('industry', ''), 
                       json.dumps(data.get('colors', {})), data.get('slogan', ''),
                       data.get('voice_tone', ''), json.dumps(data.get('guidelines', {})),
                       datetime.now().isoformat(), brand_id))
        else:
            # Insert new brand
            c.execute('''INSERT INTO brands (id, brand_name, industry, colors, slogan, voice_tone, guidelines, created_at, updated_at)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (brand_id, data.get('brand_name', ''), data.get('industry', ''),
                       json.dumps(data.get('colors', {})), data.get('slogan', ''),
                       data.get('voice_tone', ''), json.dumps(data.get('guidelines', {})),
                       datetime.now().isoformat(), datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'brand_id': brand_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/list-brands', methods=['GET'])
def list_brands():
    """List all saved brands"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT id, brand_name, industry, created_at FROM brands ORDER BY created_at DESC')
        rows = c.fetchall()
        conn.close()
        
        brands = []
        for row in rows:
            brands.append({
                'id': row[0],
                'brand_name': row[1],
                'industry': row[2],
                'created_at': row[3]
            })
        
        return jsonify({'success': True, 'brands': brands})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/delete-brand/<brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    """Delete a brand"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('DELETE FROM brands WHERE id = ?', (brand_id,))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Brand deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/brand-voice-analyzer', methods=['POST'])
def analyze_brand_voice():
    """Analyze and suggest brand voice/tone"""
    try:
        data = request.json
        brand_name = data.get('brand_name', '')
        description = data.get('description', '')
        
        voice_analysis = brand_ai.analyze_brand_voice(brand_name, description)
        return jsonify({'success': True, 'voice_analysis': voice_analysis})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/export-brand/<brand_id>', methods=['GET'])
def export_brand(brand_id):
    """Export brand guidelines as JSON"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM brands WHERE id = ?', (brand_id,))
        row = c.fetchone()
        conn.close()
        
        if not row:
            return jsonify({'success': False, 'error': 'Brand not found'}), 404
        
        brand_data = {
            'id': row[0],
            'brand_name': row[1],
            'industry': row[2],
            'colors': json.loads(row[3]) if row[3] else {},
            'slogan': row[4],
            'voice_tone': row[5],
            'guidelines': json.loads(row[6]) if row[6] else {},
            'created_at': row[7],
            'updated_at': row[8]
        }
        
        # In production, generate PDF here
        # For now, return JSON
        return jsonify({'success': True, 'brand_data': brand_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
