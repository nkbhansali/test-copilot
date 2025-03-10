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
    flights = conn.execute("SELECT * FROM flights").fetchall()
    conn.close()
    return [dict(flight) for flight in flights]
