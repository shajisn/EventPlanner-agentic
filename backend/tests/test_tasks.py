from fastapi.testclient import TestClient
from app.main import app
from app.db.init_db import init_db

client = TestClient(app)

def setup_module(module):
    init_db()

def test_create_task():
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "This is a test task.",
        "coordinator": "Test Coordinator",
        "deadline": "2025-03-15",
        "priority": "High",
        "status": "pending"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    # First create a task to update
    create_response = client.post("/api/tasks", json={
        "title": "Task to Update",
        "description": "This task will be updated.",
        "coordinator": "Test Coordinator",
        "deadline": "2025-03-15",
        "priority": "High",
        "status": "pending"
    })
    task_id = create_response.json()["id"]

    # Now update the task
    update_response = client.put(f"/api/tasks/{task_id}", json={
        "title": "Updated Task",
        "description": "This task has been updated.",
        "coordinator": "Test Coordinator",
        "deadline": "2025-03-20",
        "priority": "Medium",
        "status": "pending"
    })
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "success"

def test_get_coordinator_tasks():
    response = client.get("/api/tasks/coordinator/Test Coordinator")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    # First create a task to delete
    create_response = client.post("/api/tasks", json={
        "title": "Task to Delete",
        "description": "This task will be deleted.",
        "coordinator": "Test Coordinator",
        "deadline": "2025-03-15",
        "priority": "High",
        "status": "pending"
    })
    task_id = create_response.json()["id"]

    # Now delete the task
    delete_response = client.delete(f"/api/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["status"] == "success"