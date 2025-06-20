from fastapi import FastAPI, HTTPException

app = FastAPI(title="Catalog Service")

_products = [
    {"id": 1, "name": "Mouse"},
    {"id": 2, "name": "Keyboard"},
]

@app.get("/products")
def list_products():
    return _products

@app.post("/products")
def add_product(item: dict):
    if "name" not in item:
        raise HTTPException(400, "Field 'name' is required")
    item["id"] = len(_products) + 1
    _products.append(item)
    return item
