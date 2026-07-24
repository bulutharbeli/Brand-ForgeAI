#!/bin/bash

echo "🚀 Setting up Brand Forge AI Platform..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python is installed"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p static/css static/js static/images templates utils ai_engines exports

# Set up environment variables
echo "⚙️ Setting up environment..."
if [ ! -f .env ]; then
    echo "FLASK_APP=app.py" > .env
    echo "FLASK_ENV=development" >> .env
    echo "SECRET_KEY=brand-forge-ai-secret-key-2024" >> .env
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "  source venv/bin/activate"
echo "  python app.py"
echo ""
echo "Then visit: http://localhost:5000"
echo ""
