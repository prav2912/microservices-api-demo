from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user