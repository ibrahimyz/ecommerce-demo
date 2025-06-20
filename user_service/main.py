from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="User Service")

# Veri Modeli 
class User(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr

# Sahte DB
_users: list[User] = [
    User(id=1, username="alice", email="alice@example.com"),
    User(id=2, username="bob",   email="bob@example.com"),
]

# Endpoint'ler
@app.get("/users", response_model=list[User])
def list_users():
    return _users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in _users:
        if u.id == user_id:
            return u
    raise HTTPException(404, "User not found")

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    user.id = (_users[-1].id if _users else 0) + 1
    _users.append(user)
    return user
