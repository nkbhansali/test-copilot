from fastapi import APIRouter, Depends
from ..database import get_db_connection
from ..models import Flight

router = APIRouter(
    prefix="/flights",
    tags=["flights"]
)

@router.get("/", response_model=list[Flight])
def get_flights():
    """
    Fetches flight details from the database.
    
    Establishes a connection to the database, executes an SQL query to retrieve selected flight
    fields (flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport,
    arrival_airport, status, aircraft_code, and airline_name), closes the connection, and returns
    the results as a list of dictionaries.
    """
    conn = get_db_connection()
    flights = conn.execute("SELECT flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code, airline_name FROM flights").fetchall()
    conn.close()
    return [dict(flight) for flight in flights]
