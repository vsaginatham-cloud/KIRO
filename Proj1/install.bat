@echo off
echo ========================================
echo TTD Chatbot - Installation Script
echo ========================================
echo.

echo Step 1: Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
echo.

echo Step 2: Upgrading pip...
python -m pip install --upgrade pip
echo.

echo Step 3: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Please check the error messages above
    pause
    exit /b 1
)
echo.

echo Step 4: Checking installation...
python test_installation.py
if errorlevel 1 (
    echo.
    echo Installation test failed. Please fix the errors above.
    pause
    exit /b 1
)
echo.

echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Create .env file from .env.example
echo 2. Add your Gemini API key to .env
echo 3. Run: streamlit run app.py
echo.
pause
