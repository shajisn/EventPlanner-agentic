from fastapi.testclient import TestClient
from app.main import app
from app.db.init_db import init_db

client = TestClient(app)

def setup_module(module):
    init_db()

def test_create_guest():
    response = client.post("/api/guests", json={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "company": "Example Corp",
        "type": "VIP",
        "rsvp_status": "confirmed",
        "special_requirements": "None"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_guests():
    response = client.get("/api/guests")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_guest():
    # First, create a guest to update
    create_response = client.post("/api/guests", json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "company": "Example Corp",
        "type": "Regular",
        "rsvp_status": "pending",
        "special_requirements": "None"
    })
    guest_id = create_response.json()["id"]

    # Now update the guest
    update_response = client.put(f"/api/guests/{guest_id}", json={
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "company": "Example Corp",
        "type": "Regular",
        "rsvp_status": "confirmed",
        "special_requirements": "None"
    })
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "success"

def test_get_guest_by_id():
    # Create a guest to retrieve
    create_response = client.post("/api/guests", json={
        "name": "Alice",
        "email": "alice@example.com",
        "company": "Example Corp",
        "type": "VIP",
        "rsvp_status": "confirmed",
        "special_requirements": "None"
    })
    guest_id = create_response.json()["id"]

    response = client.get(f"/api/guests/{guest_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_delete_guest():
    # Create a guest to delete
    create_response = client.post("/api/guests", json={
        "name": "Bob",
        "email": "bob@example.com",
        "company": "Example Corp",
        "type": "Regular",
        "rsvp_status": "pending",
        "special_requirements": "None"
    })
    guest_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/guests/{guest_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["status"] == "success"

    # Verify the guest is deleted
    get_response = client.get(f"/api/guests/{guest_id}")
    assert get_response.status_code == 404