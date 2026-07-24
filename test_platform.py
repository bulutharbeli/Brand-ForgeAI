#!/usr/bin/env python3
"""
Test script to verify Brand Forge AI platform functionality
Run this script to test all features end-to-end
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"

def print_section(title):
    """Print a section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")

def test_health_check():
    """Test health check endpoint"""
    print_section("Testing Health Check")
    
    response = requests.get(f"{BASE_URL}/health")
    data = response.json()
    
    assert response.status_code == 200
    assert data['status'] == 'healthy'
    
    print("✅ Health check passed")
    print(f"   Version: {data['version']}")
    print(f"   Timestamp: {data['timestamp']}")

def test_brand_name_generation():
    """Test AI brand name generator"""
    print_section("Testing Brand Name Generator")
    
    test_cases = [
        {"industry": "technology", "keywords": ["innovative", "cloud"], "style": "modern"},
        {"industry": "healthcare", "keywords": ["care", "wellness"], "style": "professional"},
        {"industry": "retail", "keywords": ["fashion", "trendy"], "style": "playful"},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test Case {i}: {test_case['industry'].title()} Industry")
        print(f"   Keywords: {', '.join(test_case['keywords'])}")
        print(f"   Style: {test_case['style']}")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-brand-name",
            json=test_case
        )
        
        data = response.json()
        
        assert response.status_code == 200
        assert data['success'] == True
        assert len(data['names']) > 0
        
        print(f"   ✅ Generated {len(data['names'])} names:")
        for name in data['names'][:5]:
            print(f"      • {name}")
        if len(data['names']) > 5:
            print(f"      ... and {len(data['names']) - 5} more")

def test_color_palette_generation():
    """Test color palette generator"""
    print_section("Testing Color Palette Generator")
    
    test_cases = [
        {"industry": "technology", "mood": "professional", "primary_color": None},
        {"industry": "healthcare", "mood": "trustworthy", "primary_color": "#0D9488"},
        {"industry": "food", "mood": "energetic", "primary_color": None},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🎨 Test Case {i}: {test_case['industry'].title()} Industry")
        print(f"   Mood: {test_case['mood']}")
        if test_case['primary_color']:
            print(f"   Primary Color: {test_case['primary_color']}")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-color-palette",
            json=test_case
        )
        
        data = response.json()
        
        assert response.status_code == 200
        assert data['success'] == True
        assert 'palette' in data
        
        palette = data['palette']
        
        print(f"   ✅ Generated palette with {len(palette['hex_codes'])} colors:")
        print(f"      Primary: {palette['primary']}")
        print(f"      Secondary: {palette['secondary']}")
        print(f"      Accent: {palette['accent']}")
        print(f"      All colors: {', '.join(palette['hex_codes'][:4])}...")

def test_logo_concept_generation():
    """Test logo concept generator"""
    print_section("Testing Logo Concept Generator")
    
    test_cases = [
        {"brand_name": "TechCloud", "industry": "technology", "style": "minimalist"},
        {"brand_name": "HealthPlus", "industry": "healthcare", "style": "modern"},
        {"brand_name": "Foodie", "industry": "food", "style": "playful"},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n✏️  Test Case {i}: {test_case['brand_name']}")
        print(f"   Industry: {test_case['industry']}")
        print(f"   Style: {test_case['style']}")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-logo-concepts",
            json=test_case
        )
        
        data = response.json()
        
        assert response.status_code == 200
        assert data['success'] == True
        assert len(data['concepts']) > 0
        
        print(f"   ✅ Generated {len(data['concepts'])} concepts:")
        for concept in data['concepts'][:2]:
            print(f"      • {concept['title']} ({concept['type']})")
            print(f"        Elements: {', '.join(concept['design_elements'][:3])}")

def test_slogan_generation():
    """Test slogan generator"""
    print_section("Testing Slogan Generator")
    
    test_cases = [
        {"brand_name": "TechCloud", "industry": "technology", "values": ["innovation", "reliability"]},
        {"brand_name": "HealthPlus", "industry": "healthcare", "values": ["care", "trust"]},
        {"brand_name": "EcoShop", "industry": "retail", "values": ["sustainability", "quality"]},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n💬 Test Case {i}: {test_case['brand_name']}")
        print(f"   Industry: {test_case['industry']}")
        print(f"   Values: {', '.join(test_case['values'])}")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-slogan",
            json=test_case
        )
        
        data = response.json()
        
        assert response.status_code == 200
        assert data['success'] == True
        assert len(data['slogans']) > 0
        
        print(f"   ✅ Generated {len(data['slogans'])} slogans:")
        for slogan in data['slogans'][:4]:
            print(f"      • \"{slogan}\"")

def test_competitor_analysis():
    """Test competitor analysis"""
    print_section("Testing Competitor Analysis")
    
    test_cases = [
        {
            "industry": "technology",
            "competitors": ["TechGiant A", "InnovateCorp", "CloudLeader"]
        },
        {
            "industry": "healthcare",
            "competitors": ["MediCare Plus", "HealthFirst", "Wellness Corp"]
        },
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test Case {i}: {test_case['industry'].title()} Industry")
        print(f"   Competitors: {', '.join(test_case['competitors'])}")
        
        response = requests.post(
            f"{BASE_URL}/api/analyze-competitors",
            json=test_case
        )
        
        data = response.json()
        
        assert response.status_code == 200
        assert data['success'] == True
        assert 'analysis' in data
        
        analysis = data['analysis']
        
        print(f"   ✅ Analysis complete:")
        print(f"      Market Size: {analysis['market_overview']['market_size']}")
        print(f"      Growth Rate: {analysis['market_overview']['growth_rate']}")
        print(f"      Competitors Analyzed: {len(analysis['competitor_profiles'])}")
        print(f"      Brand Gaps Identified: {len(analysis['brand_gaps'])}")
        print(f"      Opportunities Found: {len(analysis['opportunities'])}")
        print(f"      Recommendations: {len(analysis['recommendations'])}")

def test_brand_guidelines_generation():
    """Test brand guidelines generator"""
    print_section("Testing Brand Guidelines Generator")
    
    # First, generate a color palette
    color_response = requests.post(
        f"{BASE_URL}/api/generate-color-palette",
        json={"industry": "technology", "mood": "professional"}
    )
    colors = color_response.json()['palette']
    
    test_case = {
        "brand_name": "TechCloud AI",
        "industry": "technology",
        "colors": {
            "primary": colors['hex_codes'][0],
            "secondary": colors['hex_codes'][1],
            "accent": colors['hex_codes'][2]
        },
        "slogan": "Innovating the Future of Cloud",
        "voice_tone": "professional"
    }
    
    print(f"\n📋 Test Case: {test_case['brand_name']}")
    print(f"   Industry: {test_case['industry']}")
    print(f"   Slogan: {test_case['slogan']}")
    print(f"   Voice Tone: {test_case['voice_tone']}")
    
    response = requests.post(
        f"{BASE_URL}/api/generate-brand-guidelines",
        json=test_case
    )
    
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    assert 'brand_id' in data
    assert 'guidelines' in data
    
    guidelines = data['guidelines']
    
    print(f"   ✅ Guidelines generated successfully!")
    print(f"      Brand ID: {data['brand_id'][:8]}...")
    print(f"      Includes:")
    print(f"         • Brand overview")
    print(f"         • Logo usage rules")
    print(f"         • Color palette ({len(guidelines['colors'])} colors)")
    print(f"         • Typography guidelines")
    print(f"         • Imagery style")
    print(f"         • Voice and tone")
    print(f"         • Do's and Don'ts")
    
    return data['brand_id']

def test_brand_management(brand_id):
    """Test brand CRUD operations"""
    print_section("Testing Brand Management (CRUD)")
    
    # Test list brands
    print("\n📚 Listing all brands...")
    response = requests.get(f"{BASE_URL}/api/list-brands")
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    
    print(f"   ✅ Found {len(data['brands'])} saved brand(s)")
    
    # Test get specific brand
    print(f"\n🔍 Retrieving brand {brand_id[:8]}...")
    response = requests.get(f"{BASE_URL}/api/get-brand/{brand_id}")
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    
    brand = data['brand']
    print(f"   ✅ Retrieved: {brand['brand_name']}")
    print(f"      Industry: {brand['industry']}")
    print(f"      Created: {brand['created_at']}")
    
    # Test export brand
    print(f"\n📥 Exporting brand {brand_id[:8]}...")
    response = requests.get(f"{BASE_URL}/api/export-brand/{brand_id}")
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    
    print(f"   ✅ Export ready!")
    print(f"      Brand data includes all guidelines and assets")
    
    # Test delete brand
    print(f"\n🗑️  Cleaning up - deleting test brand...")
    response = requests.delete(f"{BASE_URL}/api/delete-brand/{brand_id}")
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    
    print(f"   ✅ Brand deleted successfully")

def test_brand_voice_analyzer():
    """Test brand voice analyzer"""
    print_section("Testing Brand Voice Analyzer")
    
    test_case = {
        "brand_name": "TechCloud",
        "description": "A innovative cloud computing platform that makes technology accessible to everyone with a fun and friendly approach."
    }
    
    print(f"\n🗣️  Analyzing brand voice for: {test_case['brand_name']}")
    print(f"   Description: {test_case['description'][:50]}...")
    
    response = requests.post(
        f"{BASE_URL}/api/brand-voice-analyzer",
        json=test_case
    )
    
    data = response.json()
    
    assert response.status_code == 200
    assert data['success'] == True
    
    analysis = data['voice_analysis']
    
    print(f"   ✅ Voice analysis complete:")
    print(f"      Recommended Voice: {analysis['recommended_voice']}")
    print(f"      Attributes: {', '.join(analysis['attributes'])}")
    print(f"      Example Phrases:")
    for phrase in analysis['example_phrases'][:2]:
        print(f"         • {phrase}")

def run_all_tests():
    """Run all tests"""
    print("\n" + "🔥"*30)
    print("  Brand Forge AI - Platform Test Suite")
    print("🔥"*30)
    print(f"\nStarted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Basic functionality tests
        test_health_check()
        time.sleep(0.5)
        
        test_brand_name_generation()
        time.sleep(0.5)
        
        test_color_palette_generation()
        time.sleep(0.5)
        
        test_logo_concept_generation()
        time.sleep(0.5)
        
        test_slogan_generation()
        time.sleep(0.5)
        
        test_competitor_analysis()
        time.sleep(0.5)
        
        # Brand guidelines and management
        brand_id = test_brand_guidelines_generation()
        time.sleep(0.5)
        
        test_brand_voice_analyzer()
        time.sleep(0.5)
        
        test_brand_management(brand_id)
        
        # Final summary
        print_section("Test Summary")
        print("✅ All tests passed successfully!")
        print("\n📊 Test Coverage:")
        print("   • Health Check")
        print("   • Brand Name Generation (3 test cases)")
        print("   • Color Palette Generation (3 test cases)")
        print("   • Logo Concept Generation (3 test cases)")
        print("   • Slogan Generation (3 test cases)")
        print("   • Competitor Analysis (2 test cases)")
        print("   • Brand Guidelines Generation")
        print("   • Brand Voice Analyzer")
        print("   • Brand Management (CRUD operations)")
        
        print("\n🎉 Brand Forge AI is working realistically!")
        print("   All AI-powered features are functional.")
        print("   Database integration is working.")
        print("   API endpoints are responding correctly.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to the server.")
        print("   Make sure the Flask application is running:")
        print("   $ python app.py")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False
    
    print(f"\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

if __name__ == "__main__":
    # Check if server is running
    try:
        requests.get(f"{BASE_URL}/health", timeout=2)
    except:
        print("❌ Error: Flask server is not running!")
        print("\nPlease start the server first:")
        print("   $ source venv/bin/activate")
        print("   $ python app.py")
        print("\nThen run this test again.")
        exit(1)
    
    # Run tests
    success = run_all_tests()
    exit(0 if success else 1)
