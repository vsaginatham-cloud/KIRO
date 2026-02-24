# 🚀 Quick Setup Guide for TTD Chatbot

## Step-by-Step Installation

### Method 1: Automated Installation (Recommended)

#### For Windows:
1. Open Command Prompt in the Proj1 folder
2. Run the installation script:
```bash
install.bat
```

#### For Linux/Mac:
1. Open Terminal in the Proj1 folder
2. Make the script executable:
```bash
chmod +x install.sh
```
3. Run the installation script:
```bash
./install.sh
```

The script will:
- ✓ Check Python installation
- ✓ Upgrade pip
- ✓ Install all dependencies
- ✓ Verify installation

---

### Method 2: Manual Installation

### 1. Get Google Gemini API Key (FREE)

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### 2. Install Python Dependencies

Open terminal/command prompt in the Proj1 folder and run:

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

### 3. Configure API Key

1. Copy `.env.example` to create `.env`:
   
**Windows:**
```bash
copy .env.example .env
```

**Linux/Mac:**
```bash
cp .env.example .env
```

2. Open `.env` file in a text editor
3. Replace `your_gemini_api_key_here` with your actual API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

**Important:** Never share your API key or commit the `.env` file to version control!

### 4. Test Installation

Run the test script to verify everything is installed correctly:

**Windows:**
```bash
python test_installation.py
```

**Linux/Mac:**
```bash
python3 test_installation.py
```

If all tests pass, you'll see: ✅ SUCCESS: All tests passed!

### 5. Run the Application

**Windows:**
```bash
streamlit run app.py
```

**Linux/Mac:**
```bash
streamlit run app.py
```

The chatbot will open in your browser at: http://localhost:8501

---

## 🎯 Testing the Chatbot

Try these sample questions:

**English:**
- "What are the seva timings?"
- "How to book darshan online?"
- "What is the dress code for temple?"
- "When is the next booking date?"
- "Which sevas are available on Friday?"

**Hindi:**
- "सेवा का समय क्या है?"
- "ऑनलाइन बुकिंग कैसे करें?"
- "अगली बुकिंग कब है?"

**Telugu:**
- "సేవ సమయాలు ఏమిటి?"
- "ఆన్‌లైన్ బుకింగ్ ఎలా చేయాలి?"
- "తదుపరి బుకింగ్ ఎప్పుడు?"

**Tamil:**
- "சேவை நேரம் என்ன?"
- "ஆன்லைன் முன்பதிவு எப்படி செய்வது?"
- "அடுத்த முன்பதிவு எப்போது?"

---

## ⚠️ Troubleshooting

### Issue: "GEMINI_API_KEY not found"
**Solution:** 
- Make sure you created `.env` file (not `.env.txt`)
- Verify your API key is correctly set in `.env`
- Check there are no extra spaces or quotes around the key

### Issue: Module not found errors
**Solution:** 
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Translation not working
**Solution:** 
- Check your internet connection
- The app uses deep-translator which requires internet access

### Issue: "googletrans" error
**Solution:**
- We've replaced googletrans with deep-translator
- Run: `pip uninstall googletrans`
- Then: `pip install deep-translator`

### Issue: Streamlit won't start
**Solution:**
```bash
# Upgrade streamlit
pip install --upgrade streamlit

# Clear streamlit cache
streamlit cache clear
```

### Issue: Port 8501 already in use
**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

---

## 📱 Features to Explore

1. **Language Selector** - Switch between English, Hindi, Telugu, Tamil in sidebar
2. **Quick Questions** - Click pre-defined questions in sidebar for instant answers
3. **Booking Calendar** - Select any month to view booking dates
4. **Seva Availability** - Select any day to see available sevas
5. **Customer Care Info** - Find contact details in sidebar
6. **Quick Links** - Access official TTD websites
7. **Clear Chat** - Reset conversation anytime

---

## 🎨 Customization Options

### Add More Languages
Edit `config.py` and add language codes to `LANGUAGES` dictionary:
```python
LANGUAGES = {
    "English": "en",
    "हिंदी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te",
    "தமிழ் (Tamil)": "ta",
    "ಕನ್ನಡ (Kannada)": "kn",  # Add new language
}
```

### Update Knowledge Base
Edit `data/ttd_knowledge_base.py` to add/modify TTD information

### Update Booking Calendar
Edit `data/booking_calendar.py` to add new year schedules

### Change UI Theme
Modify CSS in `app.py` under the `st.markdown()` section with custom styles

---

## 📞 Need Help?

### For TTD-related queries:
- **Phone:** 0877-2277777, 0877-2233333
- **Email:** complaints@tirumala.org
- **Website:** www.tirumala.org

### For Technical Issues:
- Check the troubleshooting section above
- Review README.md for detailed documentation
- Run `python test_installation.py` to diagnose issues

---

## 🚀 Next Steps

Once the chatbot is running:

1. **Explore Features** - Try all sidebar options
2. **Test Languages** - Switch between different languages
3. **Ask Questions** - Type naturally in any supported language
4. **Check Calendar** - View booking dates for planning
5. **Share** - Help other devotees by sharing the chatbot

---

## 📊 System Requirements

- **Python:** 3.8 or higher
- **RAM:** 2GB minimum (4GB recommended)
- **Internet:** Required for AI and translation
- **Browser:** Chrome, Firefox, Safari, or Edge
- **OS:** Windows, macOS, or Linux

---

## 🔒 Security Notes

- Never share your `.env` file
- Keep your API key confidential
- The `.env` file is in `.gitignore` to prevent accidental commits
- Regularly rotate your API keys for security

---

**Happy Chatting! 🙏 Om Namo Venkatesaya**
