import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the app directory to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

def test_get_flights():
    response = client.get("/flights/")
    assert response.status_code == 200
    flights = response.json()
    assert isinstance(flights, list)
    assert len(flights) > 0
    for flight in flights:
        assert "flight_id" in flight
        assert "flight_no" in flight
        assert "scheduled_departure" in flight
        assert "scheduled_arrival" in flight
        assert "departure_airport" in flight
        assert "arrival_airport" in flight
        assert "status" in flight
        assert "aircraft_code" in flight
