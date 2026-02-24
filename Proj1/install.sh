#!/bin/bash

echo "========================================"
echo "TTD Chatbot - Installation Script"
echo "========================================"
echo ""

echo "Step 1: Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
python3 --version
echo ""

echo "Step 2: Upgrading pip..."
python3 -m pip install --upgrade pip
echo ""

echo "Step 3: Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    echo "Please check the error messages above"
    exit 1
fi
echo ""

echo "Step 4: Checking installation..."
python3 test_installation.py
if [ $? -ne 0 ]; then
    echo ""
    echo "Installation test failed. Please fix the errors above."
    exit 1
fi
echo ""

echo "========================================"
echo "Installation completed successfully!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Create .env file from .env.example"
echo "2. Add your Gemini API key to .env"
echo "3. Run: streamlit run app.py"
echo ""
