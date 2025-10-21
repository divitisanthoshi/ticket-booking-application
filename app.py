import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for tickets
if 'tickets' not in st.session_state:
    st.session_state.tickets = []

st.title("🎫 Ticket Booking Application")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Book Ticket", "View Bookings"])

if menu == "Home":
    st.header("Welcome to Ticket Booking")
    st.write("Book tickets for your favorite events!")

    # Display sample events
    events = [
        {"name": "Concert A", "date": "2024-12-01", "price": 50},
        {"name": "Theater B", "date": "2024-12-05", "price": 30},
        {"name": "Sports C", "date": "2024-12-10", "price": 40},
    ]

    st.subheader("Available Events")
    for event in events:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.write(f"**{event['name']}**")
            col2.write(f"Date: {event['date']}")
            col3.write(f"Price: ${event['price']}")

elif menu == "Book Ticket":
    st.header("Book Your Ticket")

    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        event = st.selectbox("Select Event", ["Concert A", "Theater B", "Sports C"])
        seats = st.number_input("Number of Seats", min_value=1, max_value=10, value=1)

        submitted = st.form_submit_button("Book Ticket")

        if submitted:
            if name and email and event:
                ticket = {
                    "name": name,
                    "email": email,
                    "event": event,
                    "seats": seats,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.tickets.append(ticket)
                st.success("Ticket booked successfully!")
            else:
                st.error("Please fill in all fields.")

elif menu == "View Bookings":
    st.header("Your Bookings")

    if st.session_state.tickets:
        df = pd.DataFrame(st.session_state.tickets)
        st.dataframe(df)
    else:
        st.write("No bookings yet.")
