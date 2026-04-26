from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, UserResponse

app = FastAPI()

users = []
user_id_counter = 1

# Create user
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    global user_id_counter

    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    user_id_counter += 1

    return new_user

# Get all users
@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users

# Get user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}