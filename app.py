from flask import Flask, render_template, request, jsonify, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Initialize tickets in session
@app.before_request
def initialize_session():
    if 'tickets' not in session:
        session['tickets'] = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    event = data.get('event')
    seats = data.get('seats')

    if not all([name, email, event, seats]):
        return jsonify({'message': 'All fields are required'}), 400

    ticket = {
        'name': name,
        'email': email,
        'event': event,
        'seats': seats,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    tickets = session.get('tickets', [])
    tickets.append(ticket)
    session['tickets'] = tickets

    return jsonify({'message': 'Ticket booked successfully!'})

@app.route('/tickets')
def get_tickets():
    tickets = session.get('tickets', [])
    return jsonify(tickets)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
