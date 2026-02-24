from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
import streamlit as st

def detect_language(text):
    """Detect the language of input text"""
    try:
        if not text or len(text.strip()) == 0:
            return "en"
        lang = detect(text)
        return lang
    except LangDetectException:
        return "en"
    except Exception as e:
        st.warning(f"Language detection error: {e}")
        return "en"

def translate_text(text, target_lang="en"):
    """Translate text to target language"""
    try:
        if not text or len(text.strip()) == 0:
            return text
            
        if target_lang == "en":
            return text
        
        # Detect source language
        source_lang = detect_language(text)
        
        # If already in target language, return as is
        if source_lang == target_lang:
            return text
        
        # Translate using deep-translator
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(text)
        return translated
        
    except Exception as e:
        st.warning(f"Translation error: {e}. Showing original text.")
        return text

def get_language_name(lang_code):
    """Get language name from code"""
    lang_map = {
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "ta": "Tamil"
    }
    return lang_map.get(lang_code, "English")
