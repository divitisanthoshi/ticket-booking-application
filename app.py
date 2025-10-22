import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for tickets
if 'tickets' not in st.session_state:
    st.session_state.tickets = []

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #1f77b4;
    }
    .stHeader {
        color: #ff7f0e;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎟️ Event Ticket Hub")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Book Ticket", "View Bookings", "About Us"])

if menu == "Home":
    st.header("Welcome to Ticket Booking")
    st.write("Book tickets for your favorite events!")

    # Display sample events
    events = [
        {"name": "Movie Marathon", "date": "2024-12-15", "price": 25},
        {"name": "Stand-Up Comedy", "date": "2024-12-20", "price": 35},
        {"name": "Basketball Game", "date": "2024-12-25", "price": 60},
    ]

    st.subheader("Available Events")
    for event in events:
        with st.expander(f"**{event['name']}**"):
            col1, col2 = st.columns([1, 1])
            col1.write(f"Date: {event['date']}")
            col2.write(f"Price: ${event['price']}")
            st.write("Click to expand for more details!")

elif menu == "Book Ticket":
    st.header("Book Your Ticket")

    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        event = st.selectbox("Select Event", ["Movie Marathon", "Stand-Up Comedy", "Basketball Game"])
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

elif menu == "About Us":
    st.header("About Event Ticket Hub")
    st.write("Welcome to Event Ticket Hub, your go-to platform for booking tickets to exciting events!")
    st.write("We offer a seamless experience for movie marathons, stand-up comedy shows, and sports games.")
    st.write("Contact us at support@eventtickethub.com for any inquiries.")
