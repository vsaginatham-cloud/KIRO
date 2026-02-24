"""
Detailed Booking Calendar and Seva Availability Schedule
"""

from datetime import datetime

# Monthly Booking Schedule for 2026
BOOKING_SCHEDULE_2026 = {
    "January": {
        "booking_opens": "Friday, January 2, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, January 6, 2026 at 10:00 AM",
        "for_month": "April 2026",
        "open_date": datetime(2026, 1, 2, 10, 0),
        "close_date": datetime(2026, 1, 6, 10, 0)
    },
    "February": {
        "booking_opens": "Friday, February 6, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, February 10, 2026 at 10:00 AM",
        "for_month": "May 2026",
        "open_date": datetime(2026, 2, 6, 10, 0),
        "close_date": datetime(2026, 2, 10, 10, 0)
    },
    "March": {
        "booking_opens": "Friday, March 6, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, March 10, 2026 at 10:00 AM",
        "for_month": "June 2026",
        "open_date": datetime(2026, 3, 6, 10, 0),
        "close_date": datetime(2026, 3, 10, 10, 0)
    },
    "April": {
        "booking_opens": "Friday, April 3, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, April 7, 2026 at 10:00 AM",
        "for_month": "July 2026",
        "open_date": datetime(2026, 4, 3, 10, 0),
        "close_date": datetime(2026, 4, 7, 10, 0)
    },
    "May": {
        "booking_opens": "Friday, May 1, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, May 5, 2026 at 10:00 AM",
        "for_month": "August 2026",
        "open_date": datetime(2026, 5, 1, 10, 0),
        "close_date": datetime(2026, 5, 5, 10, 0)
    },
    "June": {
        "booking_opens": "Friday, June 5, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, June 9, 2026 at 10:00 AM",
        "for_month": "September 2026",
        "open_date": datetime(2026, 6, 5, 10, 0),
        "close_date": datetime(2026, 6, 9, 10, 0)
    },
    "July": {
        "booking_opens": "Friday, July 3, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, July 7, 2026 at 10:00 AM",
        "for_month": "October 2026",
        "open_date": datetime(2026, 7, 3, 10, 0),
        "close_date": datetime(2026, 7, 7, 10, 0)
    },
    "August": {
        "booking_opens": "Friday, August 7, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, August 11, 2026 at 10:00 AM",
        "for_month": "November 2026",
        "open_date": datetime(2026, 8, 7, 10, 0),
        "close_date": datetime(2026, 8, 11, 10, 0)
    },
    "September": {
        "booking_opens": "Friday, September 4, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, September 8, 2026 at 10:00 AM",
        "for_month": "December 2026",
        "open_date": datetime(2026, 9, 4, 10, 0),
        "close_date": datetime(2026, 9, 8, 10, 0)
    },
    "October": {
        "booking_opens": "Friday, October 2, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, October 6, 2026 at 10:00 AM",
        "for_month": "January 2027",
        "open_date": datetime(2026, 10, 2, 10, 0),
        "close_date": datetime(2026, 10, 6, 10, 0)
    },
    "November": {
        "booking_opens": "Friday, November 6, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, November 10, 2026 at 10:00 AM",
        "for_month": "February 2027",
        "open_date": datetime(2026, 11, 6, 10, 0),
        "close_date": datetime(2026, 11, 10, 10, 0)
    },
    "December": {
        "booking_opens": "Friday, December 4, 2026 at 10:00 AM",
        "booking_closes": "Tuesday, December 8, 2026 at 10:00 AM",
        "for_month": "March 2027",
        "open_date": datetime(2026, 12, 4, 10, 0),
        "close_date": datetime(2026, 12, 8, 10, 0)
    }
}

# Seva Availability by Day of Week
SEVA_AVAILABILITY = {
    "Monday": [
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ],
    "Tuesday": [
        "Archana (4:00 AM - 4:30 AM)",
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ],
    "Wednesday": [
        "Archana (4:00 AM - 4:30 AM)",
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ],
    "Thursday": [
        "Archana (4:00 AM - 4:30 AM)",
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ],
    "Friday": [
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)",
        "Astadala Pada Padmaradhana (Special)"
    ],
    "Saturday": [
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ],
    "Sunday": [
        "Kalyanotsavam (10:00 AM - 12:00 PM)",
        "Arjitha Brahmotsavam (12:30 PM - 2:00 PM)",
        "Dolotsavam/Unjal Seva (11:00 AM - 1:00 PM)",
        "Vasanthotsavam (2:30 PM - 3:00 PM)",
        "Sahasra Deepalankara Seva (5:00 PM - 5:30 PM)"
    ]
}

# Detailed Seva Information
SEVA_DETAILS = {
    "Kalyanotsavam": {
        "timing": "10:00 AM - 12:00 PM",
        "price": "Rs. 1000",
        "availability": "Daily",
        "tickets_per_booking": 2,
        "description": "Celestial wedding ceremony of Lord Venkateswara"
    },
    "Arjitha Brahmotsavam": {
        "timing": "12:30 PM - 2:00 PM",
        "price": "Rs. 200",
        "availability": "Daily",
        "tickets_per_booking": 1,
        "description": "Festival procession seva"
    },
    "Dolotsavam": {
        "timing": "11:00 AM - 1:00 PM",
        "price": "Rs. 300",
        "availability": "Daily",
        "tickets_per_booking": 1,
        "description": "Swing seva (Unjal Seva)"
    },
    "Vasanthotsavam": {
        "timing": "2:30 PM - 3:00 PM",
        "price": "Rs. 300",
        "availability": "Daily",
        "tickets_per_booking": 1,
        "description": "Spring festival seva"
    },
    "Sahasra Deepalankara Seva": {
        "timing": "5:00 PM - 5:30 PM",
        "price": "Rs. 300",
        "availability": "Daily",
        "tickets_per_booking": 1,
        "description": "Thousand lamps decoration seva"
    },
    "Archana": {
        "timing": "4:00 AM - 4:30 AM",
        "price": "Rs. 220",
        "availability": "Tuesday, Wednesday, Thursday",
        "tickets_per_booking": 1,
        "description": "Chanting of Lord's names with offerings"
    },
    "Astadala Pada Padmaradhana": {
        "timing": "Special timing",
        "price": "Rs. 2000",
        "availability": "Friday only",
        "tickets_per_booking": 1,
        "description": "Eight-petaled lotus worship"
    },
    "Suprabhatam": {
        "timing": "2:30 AM - 3:00 AM",
        "price": "FREE",
        "availability": "Daily",
        "tickets_per_booking": "N/A",
        "description": "Morning wake-up hymns for the Lord"
    }
}

def get_next_booking_date():
    """Get the next upcoming booking date"""
    now = datetime.now()
    for month, details in BOOKING_SCHEDULE_2026.items():
        if details["open_date"] > now:
            return {
                "month": month,
                "opens": details["booking_opens"],
                "closes": details["booking_closes"],
                "for_month": details["for_month"]
            }
    return None

def get_current_booking_status():
    """Check if booking is currently open"""
    now = datetime.now()
    for month, details in BOOKING_SCHEDULE_2026.items():
        if details["open_date"] <= now <= details["close_date"]:
            return {
                "status": "OPEN",
                "month": month,
                "closes": details["booking_closes"],
                "for_month": details["for_month"]
            }
    return {"status": "CLOSED"}

def get_sevas_for_day(day_name):
    """Get available sevas for a specific day"""
    return SEVA_AVAILABILITY.get(day_name, [])
