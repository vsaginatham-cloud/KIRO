import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Supported Languages
LANGUAGES = {
    "English": "en",
    "हिंदी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te",
    "தமிழ் (Tamil)": "ta"
}

# TTD Website URLs
TTD_URLS = {
    "main": "https://www.tirumala.org/",
    "booking": "https://ttdevasthanams.ap.gov.in/",
    "sevas": "https://www.tirumala.org/Advancebooking.aspx"
}

# Customer Care Information
CUSTOMER_CARE = {
    "phone": "0877-2277777, 0877-2233333",
    "email": "complaints@tirumala.org",
    "timings": "24x7 Available"
}
