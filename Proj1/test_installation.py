import os

"""
Test script to verify all dependencies are installed correctly
Run this before starting the main application
"""

import sys

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    errors = []
    
    # Test standard library imports
    try:
        import os
        print("✓ os")
    except ImportError as e:
        errors.append(f"✗ os: {e}")
    
    try:
        from datetime import datetime
        print("✓ datetime")
    except ImportError as e:
        errors.append(f"✗ datetime: {e}")
    
    # Test third-party imports
    try:
        import streamlit as st
        print(f"✓ streamlit (version: {st.__version__})")
    except ImportError as e:
        errors.append(f"✗ streamlit: {e}")
    
    try:
        import google.generativeai as genai
        print("✓ google-generativeai")
    except ImportError as e:
        errors.append(f"✗ google-generativeai: {e}")
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv")
    except ImportError as e:
        errors.append(f"✗ python-dotenv: {e}")
    
    try:
        from deep_translator import GoogleTranslator
        print("✓ deep-translator")
    except ImportError as e:
        errors.append(f"✗ deep-translator: {e}")
    
    try:
        from langdetect import detect
        print("✓ langdetect")
    except ImportError as e:
        errors.append(f"✗ langdetect: {e}")
    
    try:
        import requests
        print("✓ requests")
    except ImportError as e:
        errors.append(f"✗ requests: {e}")
    
    try:
        from bs4 import BeautifulSoup
        print("✓ beautifulsoup4")
    except ImportError as e:
        errors.append(f"✗ beautifulsoup4: {e}")
    
    return errors

def test_project_structure():
    """Test if all required files exist"""
    print("\nTesting project structure...")
    errors = []
    
    required_files = [
        "app.py",
        "config.py",
        "requirements.txt",
        ".env.example",
        "utils/gemini_chat.py",
        "utils/translator.py",
        "utils/__init__.py",
        "data/ttd_knowledge_base.py",
        "data/booking_calendar.py",
        "data/__init__.py"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            errors.append(f"✗ {file} not found")
            print(f"✗ {file} not found")
    
    return errors

def test_env_file():
    """Test if .env file exists and has API key"""
    print("\nTesting environment configuration...")
    errors = []
    
    if not os.path.exists(".env"):
        errors.append("✗ .env file not found. Please create it from .env.example")
        print("✗ .env file not found")
        print("  → Copy .env.example to .env and add your GEMINI_API_KEY")
    else:
        print("✓ .env file exists")
        
        # Check if API key is set
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            errors.append("✗ GEMINI_API_KEY not set in .env file")
            print("✗ GEMINI_API_KEY not set in .env file")
        elif api_key == "your_gemini_api_key_here":
            errors.append("✗ GEMINI_API_KEY still has placeholder value")
            print("✗ GEMINI_API_KEY still has placeholder value")
            print("  → Get your API key from: https://makersuite.google.com/app/apikey")
        else:
            print("✓ GEMINI_API_KEY is set")
    
    return errors

def test_module_imports():
    """Test if custom modules can be imported"""
    print("\nTesting custom module imports...")
    errors = []
    
    try:
        from config import GEMINI_API_KEY, LANGUAGES, TTD_URLS, CUSTOMER_CARE
        print("✓ config module")
    except ImportError as e:
        errors.append(f"✗ config module: {e}")
        print(f"✗ config module: {e}")
    
    try:
        from utils.translator import translate_text, detect_language, get_language_name
        print("✓ utils.translator module")
    except ImportError as e:
        errors.append(f"✗ utils.translator module: {e}")
        print(f"✗ utils.translator module: {e}")
    
    try:
        from utils.gemini_chat import TTDChatbot
        print("✓ utils.gemini_chat module")
    except ImportError as e:
        errors.append(f"✗ utils.gemini_chat module: {e}")
        print(f"✗ utils.gemini_chat module: {e}")
    
    try:
        from data.ttd_knowledge_base import TTD_KNOWLEDGE, FAQ_DATA
        print("✓ data.ttd_knowledge_base module")
    except ImportError as e:
        errors.append(f"✗ data.ttd_knowledge_base module: {e}")
        print(f"✗ data.ttd_knowledge_base module: {e}")
    
    try:
        from data.booking_calendar import (
            BOOKING_SCHEDULE_2026,
            SEVA_AVAILABILITY,
            SEVA_DETAILS,
            get_next_booking_date,
            get_current_booking_status
        )
        print("✓ data.booking_calendar module")
    except ImportError as e:
        errors.append(f"✗ data.booking_calendar module: {e}")
        print(f"✗ data.booking_calendar module: {e}")
    
    return errors

def main():
    """Run all tests"""
    print("=" * 60)
    print("TTD Chatbot - Installation Test")
    print("=" * 60)
    
    all_errors = []
    
    # Test imports
    all_errors.extend(test_imports())
    
    # Test project structure
    all_errors.extend(test_project_structure())
    
    # Test environment file
    all_errors.extend(test_env_file())
    
    # Test module imports
    all_errors.extend(test_module_imports())
    
    # Summary
    print("\n" + "=" * 60)
    if all_errors:
        print(f"❌ FAILED: {len(all_errors)} error(s) found")
        print("=" * 60)
        print("\nErrors:")
        for error in all_errors:
            print(f"  {error}")
        print("\nPlease fix the errors above before running the application.")
        print("\nQuick fixes:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Create .env file: copy .env.example to .env")
        print("3. Add your Gemini API key to .env file")
        sys.exit(1)
    else:
        print("✅ SUCCESS: All tests passed!")
        print("=" * 60)
        print("\nYou're ready to run the application:")
        print("  streamlit run app.py")
        sys.exit(0)

if __name__ == "__main__":
    main()
