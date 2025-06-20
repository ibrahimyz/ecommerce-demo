from fastapi.testclient import TestClient
from main import app        

client = TestClient(app)

def test_list_products():
    r = client.get("/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_add_product():
    new = {"name": "Monitor"}
    r = client.post("/products", json=new)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 3 and data["name"] == "Monitor"
