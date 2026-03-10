import requests

USER_URL = "http://localhost:8001/users"
NOTES_URL = "http://localhost:8002/notes"

def test_create_user():
    data = {"id": 1, "name": "John Doe"}
    response = requests.post(USER_URL, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_create_note_valid_user():
    data = {"user_id": 1, "content": "Finish Docker tutorial"}
    response = requests.post(NOTES_URL, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_create_note_invalid_user():
    data = {"user_id": 999, "content": "Invalid user test"}
    response = requests.post(NOTES_URL, json=data)
    assert response.status_code == 404