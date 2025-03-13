from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/api/events", json={
        "title": "Test Event",
        "description": "This is a test event.",
        "date": "2025-09-01",
        "time": "10:00",
        "location": "Test Location",
        "coordinator": "Test Coordinator",
        "status": "upcoming"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_events():
    response = client.get("/api/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_event():
    response = client.get("/api/events/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_update_event():
    response = client.put("/api/events/1", json={
        "title": "Updated Event",
        "description": "This is an updated test event.",
        "date": "2025-09-01",
        "time": "10:00",
        "location": "Updated Location",
        "coordinator": "Updated Coordinator",
        "status": "upcoming"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_delete_event():
    response = client.delete("/api/events/1")
    assert response.status_code == 200
    assert response.json()["status"] == "success"