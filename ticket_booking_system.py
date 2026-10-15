
"""Movie theater ticket booking and seating management module."""

import hashlib
import hmac
import secrets

theater_seats = {
    "A1": {"tier": "Standard", "price": 12.0, "is_sold": False},
    "A2": {"tier": "Standard", "price": 12.0, "is_sold": True},
    "B1": {"tier": "Premium", "price": 20.0, "is_sold": False},
}


def reserve_seat(seat_id, customer, order_history=None):
    """Reserve an available seat and record the booking."""
    if order_history is None:
        order_history = []

    if seat_id not in theater_seats or theater_seats[seat_id]["is_sold"]:
        return False

    theater_seats[seat_id]["is_sold"] = True
    order_history.append(f"Reserved seat {seat_id} for customer {customer}")
    return True


def cancel_seat(seat_id):
    """Cancel a booking if the seat exists."""
    if seat_id not in theater_seats:
        return False

    theater_seats[seat_id]["is_sold"] = False
    return True


def check_seat_status(seat_id):
    """Return whether a known seat is available."""
    seat = theater_seats.get(seat_id)
    if seat is None:
        return False
    return not seat["is_sold"]


def compute_discounted_price(seat_id, discount_percent=20):
    """Calculate a discounted price using a validated percentage."""
    if seat_id not in theater_seats:
        raise ValueError("Unknown seat ID.")

    if not isinstance(discount_percent, (int, float)):
        raise ValueError("Discount must be numeric.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    base_price = theater_seats[seat_id]["price"]
    return round(base_price * (1 - discount_percent / 100), 2)


def generate_ticket_hash(ticket_code):
    """Return a SHA-256 digest of the ticket code."""
    return hashlib.sha256(ticket_code.encode("utf-8")).hexdigest()


def generate_booking_pin():
    """Generate a cryptographically secure four-digit booking PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def verify_ticket_code(ticket_code, stored_digest):
    """Compare a ticket code's digest with a stored digest."""
    return hmac.compare_digest(
        generate_ticket_hash(ticket_code), stored_digest
    )


def export_seating_chart(filename="seating_chart.txt"):
    """Export the current seating chart to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as seating_file:
        seating_file.write(str(theater_seats))
    print(f"Seating chart exported to: {filename}")


def get_theater_summary(seats=None):
    """Return the number of sold seats."""
    if seats is None:
        seats = theater_seats
    return sum(details["is_sold"] for details in seats.values())


def main():
    """Demonstrate ticket booking and seating management."""
    reserve_seat("A1", "Sarah Connor")
    cancel_seat("A2")
    print("Is B1 available:", check_seat_status("B1"))
    print("Promo price:", compute_discounted_price("B1", 20))

    ticket_digest = generate_ticket_hash("TKT_882")
    print("Ticket Hash:", ticket_digest)
    print("Ticket verification:", verify_ticket_code("TKT_882", ticket_digest))
    print("Booking PIN:", generate_booking_pin())

    export_seating_chart()
    print("Sold count:", get_theater_summary())


if __name__ == "__main__":
    main()
