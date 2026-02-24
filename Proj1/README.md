# 🕉️ TTD Chatbot - Tirumala Tirupati Devasthanams

A comprehensive multilingual chatbot for Tirumala Tirupati Devasthanams (TTD) devotees, providing information about sevas, bookings, timings, and more in multiple Indian languages.

## ✨ Features

- **Multilingual Support**: English, Hindi, Telugu, Tamil
- **Comprehensive Information**: 
  - Seva timings and schedules with day-wise availability
  - Complete 2026 monthly booking calendar with exact dates
  - Booking procedures and dates (First Friday to Tuesday schedule)
  - Darshan types and availability
  - Accommodation information
  - Temple guidelines and dress code
  - Customer care contact details
  - Transportation facilities

- **Interactive Booking Calendar**: 
  - View booking dates for any month in 2026
  - Check current booking status (Open/Closed)
  - See next upcoming booking date
  - Day-wise seva availability checker

- **User-Friendly Interface**: Clean Streamlit UI with easy navigation
- **AI-Powered**: Uses Google Gemini API for intelligent responses
- **Real-time Translation**: Automatic language detection and translation
- **Quick Access**: Pre-defined quick questions for common queries
- **Detailed Seva Information**: Timings, prices, and availability for all sevas

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Setup Steps

1. **Clone or navigate to the project directory**
```bash
cd Proj1
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Get your Gemini API key from: https://makersuite.google.com/app/apikey
   - Add your API key to `.env`:
```
GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the chatbot**
   - Open your browser and go to: http://localhost:8501

## 📖 Usage Guide

### Basic Usage
1. Select your preferred language from the sidebar
2. Type your question in the chat input (in any supported language)
3. Get instant responses with relevant information
4. Use quick question buttons for common queries

### Example Questions
- "What are the seva timings?"
- "When is the next booking date?"
- "Which sevas are available on Friday?"
- "Show me March 2026 booking dates"
- "How to book darshan online?"
- "सेवा बुकिंग कैसे करें?" (Hindi)
- "దర్శనం టైమింగ్స్ ఏమిటి?" (Telugu)
- "கோவில் நேரம் என்ன?" (Tamil)
- "When does booking open for June 2026?"
- "Is Archana available on Monday?"

### Features in Sidebar
- Language selection
- Customer care information
- Quick links to official TTD websites
- **Interactive Booking Calendar 2026** - View any month's booking dates
- **Seva Availability Checker** - See which sevas are available on each day
- Current booking status indicator
- Pre-defined quick questions
- Clear chat history option

## 🛠️ Project Structure

```
Proj1/
├── app.py                          # Main Streamlit application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── README.md                       # This file
├── SETUP_GUIDE.md                  # Quick setup instructions
├── BOOKING_SCHEDULE.md             # Complete booking calendar & seva availability
├── utils/
│   ├── gemini_chat.py             # Gemini AI chatbot logic
│   └── translator.py              # Translation utilities
└── data/
    ├── ttd_knowledge_base.py      # TTD information database
    └── booking_calendar.py        # 2026 booking schedule & seva availability
```

## 🔧 Configuration

### Supported Languages
- English (en)
- Hindi (hi)
- Telugu (te)
- Tamil (ta)

### API Configuration
The chatbot uses Google Gemini Pro model. You can modify the model in `utils/gemini_chat.py` if needed.

### Knowledge Base
The TTD information is stored in `data/ttd_knowledge_base.py`. You can update this file to add more information or modify existing data.

## 📞 TTD Contact Information

- **Phone**: 0877-2277777, 0877-2233333
- **Email**: complaints@tirumala.org
- **Website**: https://www.tirumala.org
- **Availability**: 24x7

## 🔐 Security Notes

- Never commit your `.env` file with actual API keys
- Keep your Gemini API key confidential
- Use environment variables for sensitive data

## 🐛 Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY not found" error**
   - Make sure you created `.env` file from `.env.example`
   - Verify your API key is correctly set in `.env`

2. **Translation not working**
   - Check internet connection
   - Verify googletrans package is installed correctly

3. **Chatbot not responding**
   - Check your Gemini API key is valid
   - Verify you haven't exceeded API rate limits

## 📝 Future Enhancements

- Web scraping for real-time updates
- Booking availability checker
- Push notifications for booking dates
- Voice input/output support
- Mobile app version
- Integration with TTD official APIs (when available)

## ⚠️ Disclaimer

This is an unofficial chatbot created to help TTD devotees. For official information and bookings, please visit:
- Official Website: https://www.tirumala.org
- Booking Portal: https://ttdevasthanams.ap.gov.in

## 📄 License

This project is created for educational and devotional purposes.

## 🙏 Acknowledgments

- Tirumala Tirupati Devasthanams for the information
- Google Gemini AI for the language model
- Streamlit for the UI framework

---

**Om Namo Venkatesaya** 🙏
