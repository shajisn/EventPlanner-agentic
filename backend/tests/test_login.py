from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/login", json={"email": "admin@inapp.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "user": {
            "id": 1,
            "name": "Admin User",
            "email": "admin@inapp.com",
            "role": "admin"
        }
    }

def test_login_invalid_credentials():
    response = client.post("/api/login", json={"email": "invalid@inapp.com", "password": "wrongpassword"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "error",
        "message": "Invalid credentials"
    }