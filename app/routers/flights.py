from fastapi import APIRouter, Depends
from ..database import get_db_connection
from ..models import Flight

router = APIRouter(
    prefix="/flights",
    tags=["flights"]
)

@router.get("/", response_model=list[Flight])
def get_flights():
    conn = get_db_connection()
    flights = conn.execute("SELECT flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code, airline_name FROM flights").fetchall()
    conn.close()
    return [dict(flight) for flight in flights]
