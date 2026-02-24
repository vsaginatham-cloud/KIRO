import streamlit as st
from utils.gemini_chat import TTDChatbot
from utils.translator import translate_text, detect_language, get_language_name
from config import LANGUAGES, TTD_URLS, CUSTOMER_CARE
from data.booking_calendar import (
    BOOKING_SCHEDULE_2026, 
    SEVA_AVAILABILITY, 
    SEVA_DETAILS,
    get_next_booking_date,
    get_current_booking_status
)
from datetime import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="TTD Chatbot - Tirumala Tirupati Devasthanams",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF6B35;
        padding: 20px;
        background: linear-gradient(135deg, #FFF8DC 0%, #FFE4B5 100%);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 5px solid #2196F3;
    }
    .bot-message {
        background-color: #FFF8E1;
        border-left: 5px solid #FF6B35;
    }
    .info-box {
        background-color: #F0F8FF;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #FF6B35;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = TTDChatbot()
    except ValueError as e:
        st.error(str(e))
        st.stop()
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "en"

# Header
st.markdown("""
<div class="main-header">
    <h1>🕉️ Tirumala Tirupati Devasthanams Chatbot</h1>
    <p>Your Virtual Assistant for TTD Services | आपका TTD सेवा सहायक | మీ TTD సేవా సహాయకుడు | உங்கள் TTD சேவை உதவியாளர்</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x150/FF6B35/FFFFFF?text=TTD+Logo", use_container_width=True)
    
    st.markdown("### 🌐 Select Language / भाषा चुनें")
    selected_lang_name = st.selectbox(
        "Choose your preferred language",
        options=list(LANGUAGES.keys()),
        index=0
    )
    st.session_state.selected_language = LANGUAGES[selected_lang_name]
    
    st.markdown("---")
    st.markdown("### 📞 Customer Care")
    st.markdown(f"""
    <div class="info-box">
        <strong>Phone:</strong> {CUSTOMER_CARE['phone']}<br>
        <strong>Email:</strong> {CUSTOMER_CARE['email']}<br>
        <strong>Timings:</strong> {CUSTOMER_CARE['timings']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.markdown(f"[🏛️ TTD Main Website]({TTD_URLS['main']})")
    st.markdown(f"[📅 Online Booking]({TTD_URLS['booking']})")
    st.markdown(f"[🙏 Sevas Information]({TTD_URLS['sevas']})")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Questions")
    quick_questions = [
        "What are the seva timings?",
        "When is the next booking date?",
        "Which sevas are available on Friday?",
        "How to book darshan online?",
        "What is the dress code?",
        "Accommodation booking process",
        "Show me March 2026 booking dates",
        "Temple opening hours"
    ]
    
    for question in quick_questions:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
            with st.spinner("Getting response..."):
                response = st.session_state.chatbot.get_response(question)
                st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    st.markdown("---")
    
    # Booking Calendar Section
    st.markdown("### 📅 Booking Calendar 2026")
    
    # Show current booking status
    booking_status = get_current_booking_status()
    if booking_status["status"] == "OPEN":
        st.success(f"🟢 **BOOKING OPEN NOW!**\n\nFor: {booking_status['for_month']}\n\nCloses: {booking_status['closes']}")
    else:
        next_booking = get_next_booking_date()
        if next_booking:
            st.info(f"📆 **Next Booking**\n\nOpens: {next_booking['opens']}\n\nFor: {next_booking['for_month']}")
    
    # Month selector for booking dates
    selected_month = st.selectbox(
        "View booking dates for:",
        options=list(BOOKING_SCHEDULE_2026.keys()),
        key="month_selector"
    )
    
    if selected_month:
        month_data = BOOKING_SCHEDULE_2026[selected_month]
        st.markdown(f"""
        <div class="info-box">
            <strong>📅 {selected_month} 2026 Booking</strong><br>
            <strong>Opens:</strong> {month_data['booking_opens']}<br>
            <strong>Closes:</strong> {month_data['booking_closes']}<br>
            <strong>For Sevas in:</strong> {month_data['for_month']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🗓️ Seva Availability")
    
    # Day selector for seva availability
    selected_day = st.selectbox(
        "View sevas available on:",
        options=list(SEVA_AVAILABILITY.keys()),
        key="day_selector"
    )
    
    if selected_day:
        sevas = SEVA_AVAILABILITY[selected_day]
        st.markdown(f"**Sevas on {selected_day}:**")
        for seva in sevas:
            st.markdown(f"✓ {seva}")
    
    st.markdown("---")
    if st.button("🔄 Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chatbot.reset_chat()
        st.rerun()

# Main Chat Interface
st.markdown("### 💬 Chat with TTD Assistant")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>👤 You:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 TTD Assistant:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Ask me anything about TTD services... (Type in any language)")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get bot response
    with st.spinner("🙏 Getting information..."):
        # Detect input language
        detected_lang = detect_language(user_input)
        
        # Translate to English if needed for processing
        if detected_lang != "en":
            english_query = translate_text(user_input, "en")
        else:
            english_query = user_input
        
        # Get response from chatbot
        response = st.session_state.chatbot.get_response(english_query)
        
        # Translate response back to user's language if needed
        if st.session_state.selected_language != "en":
            response = translate_text(response, st.session_state.selected_language)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>🕉️ Developed for Tirumala Tirupati Devasthanams Devotees</p>
    <p><em>This is an unofficial chatbot. For official information, please visit <a href="https://www.tirumala.org" target="_blank">www.tirumala.org</a></em></p>
</div>
""", unsafe_allow_html=True)
