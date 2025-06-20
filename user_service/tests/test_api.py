from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_users():
    r = client.get("/users")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert "username" in r.json()[0]

def test_get_single_user():
    r = client.get("/users/1")
    assert r.status_code == 200
    assert r.json()["username"] == "alice"

def test_create_user():
    new = {"username": "carol", "email": "carol@example.com"}
    r = client.post("/users", json=new)
    assert r.status_code == 201
    assert r.json()["id"] == 3
