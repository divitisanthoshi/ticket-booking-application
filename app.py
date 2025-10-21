from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for tickets (for simplicity)
tickets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    data = request.json
    ticket = {
        'name': data['name'],
        'email': data['email'],
        'event': data['event'],
        'seats': data['seats']
    }
    tickets.append(ticket)
    return jsonify({'message': 'Ticket booked successfully!', 'ticket': ticket})

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
