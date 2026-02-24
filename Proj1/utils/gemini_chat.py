import google.generativeai as genai
from config import GEMINI_API_KEY
from data.ttd_knowledge_base import TTD_KNOWLEDGE, FAQ_DATA
from data.booking_calendar import (
    BOOKING_SCHEDULE_2026, 
    SEVA_AVAILABILITY, 
    SEVA_DETAILS,
    get_next_booking_date,
    get_current_booking_status
)

class TTDChatbot:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found. Please set it in .env file")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = None
        self.initialize_chat()
    
    def initialize_chat(self):
        """Initialize chat with TTD context"""
        
        # Get current booking status
        booking_status = get_current_booking_status()
        next_booking = get_next_booking_date()
        
        booking_info = ""
        if booking_status["status"] == "OPEN":
            booking_info = f"\n\nCURRENT BOOKING STATUS: OPEN\nBooking for {booking_status['for_month']} is currently open and closes on {booking_status['closes']}"
        elif next_booking:
            booking_info = f"\n\nNEXT BOOKING: Opens on {next_booking['opens']} for {next_booking['for_month']} sevas"
        
        system_prompt = f"""You are a helpful assistant for Tirumala Tirupati Devasthanams (TTD).
Your role is to help devotees with information about:
- Seva timings and schedules
- Booking procedures and dates
- Darshan types and timings
- Accommodation information
- Temple guidelines and dress code
- Customer care contact information
- Transportation and facilities

Use the following knowledge base to answer questions accurately:

{TTD_KNOWLEDGE}

IMPORTANT BOOKING INFORMATION:
- Bookings open on the FIRST FRIDAY of each month at 10:00 AM
- Bookings close on the FOLLOWING TUESDAY at 10:00 AM
- Bookings are for sevas 3 MONTHS in advance
- Example: January booking (opens Jan 2) is for April sevas
{booking_info}

SEVA AVAILABILITY BY DAY:
- Archana: Tuesday, Wednesday, Thursday ONLY
- Astadala Pada Padmaradhana: Friday ONLY
- Kalyanotsavam, Arjitha Brahmotsavam, Dolotsavam, Vasanthotsavam, Sahasra Deepalankara: DAILY

Guidelines:
1. Be respectful and use appropriate religious terminology
2. Provide accurate information from the knowledge base
3. When asked about booking dates, provide specific dates from the monthly schedule
4. When asked about seva availability, mention which days they are available
5. If you don't know something, direct users to official TTD contacts
6. Always include relevant contact information when helpful
7. Be concise but comprehensive
8. For booking queries, mention the official website: www.tirumala.org
9. Respond in the same language as the user's query when possible
"""
        self.chat = self.model.start_chat(history=[])
        # Send system context
        self.chat.send_message(system_prompt)
    
    def get_response(self, user_message):
        """Get chatbot response"""
        try:
            response = self.chat.send_message(user_message)
            return response.text
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again or contact TTD customer care at 0877-2277777."
    
    def reset_chat(self):
        """Reset chat history"""
        self.initialize_chat()
