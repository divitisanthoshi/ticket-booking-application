// EventBook JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize events
    renderEvents(events);
    loadTickets();

    // Search functionality
    document.getElementById('searchInput').addEventListener('input', function() {
        const query = this.value.toLowerCase();
        const filteredEvents = events.filter(event =>
            event.name.toLowerCase().includes(query) ||
            event.description.toLowerCase().includes(query) ||
            event.venue.toLowerCase().includes(query)
        );
        renderEvents(filteredEvents);
    });

    // Booking form submission
    document.getElementById('bookingForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const data = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            event: document.getElementById('eventName').value,
            seats: parseInt(document.getElementById('seats').value)
        };

        try {
            const response = await fetch('/book', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await response.json();
            showAlert(result.message, 'success');
            bootstrap.Modal.getInstance(document.getElementById('bookingModal')).hide();
            document.getElementById('bookingForm').reset();
            loadTickets();
        } catch (error) {
            showAlert('Error booking ticket. Please try again.', 'danger');
        }
    });

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

let events = [
    { id: 1, name: "Rock Concert 2023", date: "2023-12-15", venue: "Stadium A", price: 50, description: "An amazing rock concert featuring top bands.", category: "Music" },
    { id: 2, name: "Jazz Night", date: "2023-12-20", venue: "Jazz Club", price: 30, description: "Relaxing jazz evening with live performances.", category: "Music" },
    { id: 3, name: "Comedy Show", date: "2023-12-25", venue: "Theater B", price: 25, description: "Hilarious stand-up comedy by famous comedians.", category: "Comedy" },
    { id: 4, name: "Sports Match", date: "2023-12-30", venue: "Arena C", price: 40, description: "Exciting football match between top teams.", category: "Sports" },
    { id: 5, name: "Theater Play", date: "2024-01-05", venue: "Grand Theater", price: 35, description: "Classic theater performance of Romeo and Juliet.", category: "Theater" },
    { id: 6, name: "Tech Conference", date: "2024-01-10", venue: "Convention Center", price: 75, description: "Latest trends in technology and innovation.", category: "Conference" }
];

function renderEvents(eventsToShow) {
    const eventsDiv = document.getElementById('eventsList');
    eventsDiv.innerHTML = '';

    if (eventsToShow.length === 0) {
        eventsDiv.innerHTML = '<div class="col-12"><div class="alert alert-info">No events found matching your search.</div></div>';
        return;
    }

    eventsToShow.forEach(event => {
        const eventCard = `
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card event-card h-100">
                    <div class="card-body d-flex flex-column">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <span class="badge bg-primary">${event.category}</span>
                            <span class="text-muted small">${event.date}</span>
                        </div>
                        <h5 class="card-title">${event.name}</h5>
                        <p class="card-text"><i class="fas fa-map-marker-alt me-2"></i>${event.venue}</p>
                        <p class="card-text"><i class="fas fa-dollar-sign me-2"></i>$${event.price}</p>
                        <p class="card-text small text-muted">${event.description}</p>
                        <button class="btn btn-book mt-auto" onclick="openBookingModal('${event.name}')">
                            <i class="fas fa-ticket-alt me-2"></i>Book Now
                        </button>
                    </div>
                </div>
            </div>
        `;
        eventsDiv.innerHTML += eventCard;
    });
}

function openBookingModal(eventName) {
    document.getElementById('eventName').value = eventName;
    new bootstrap.Modal(document.getElementById('bookingModal')).show();
}

async function loadTickets() {
    try {
        const response = await fetch('/tickets');
        const tickets = await response.json();
        const ticketsDiv = document.getElementById('ticketsList');

        if (tickets.length === 0) {
            ticketsDiv.innerHTML = '<div class="col-12"><div class="alert alert-info">No tickets booked yet. Start exploring events above!</div></div>';
        } else {
            let html = '';
            tickets.forEach(ticket => {
                html += `
                    <div class="col-md-6 col-lg-4 mb-3">
                        <div class="card border-success">
                            <div class="card-body">
                                <div class="d-flex justify-content-between align-items-start mb-2">
                                    <h6 class="card-title text-success">${ticket.event}</h6>
                                    <span class="badge bg-success">${ticket.seats} seats</span>
                                </div>
                                <p class="card-text mb-1"><strong>${ticket.name}</strong></p>
                                <p class="card-text small text-muted">${ticket.email}</p>
                                <small class="text-success"><i class="fas fa-check-circle me-1"></i>Booked successfully</small>
                            </div>
                        </div>
                    </div>
                `;
            });
            ticketsDiv.innerHTML = html;
        }
    } catch (error) {
        document.getElementById('ticketsList').innerHTML = '<div class="col-12"><div class="alert alert-danger">Error loading tickets. Please refresh the page.</div></div>';
    }
}

function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);

    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}
