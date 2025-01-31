from fastapi import FastAPI, status, Body, HTTPException, Form
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

users = []


class Users(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[Users]:
    return users


@app.get(path="/users/{user_id}")
async def get_user(user_id: int) -> users:
    try:
        for i in users:
            if i.id == user_id:
                return i
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post(path="/users/{username}/{age}")
async def add_user(username: str, age: int, user: Users) -> users:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f"User {user} is registered!"


@app.put(path="/users/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for u in users:
        if u.id == user_id:
            u.username = str(username)
            u.age = int(age)
            return f"{u} is updated"
    raise HTTPException(status_code=404, detail="User not found")


@app.delete(path="/users/{user_id}", response_model=dict)
async def del_user(user_id: int):
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return {"detail": "User Delete"}
    raise HTTPException(status_code=404, detail="User not found")

# @app.post("/users/{username}/{age}")
# async def add_user(
#         username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
#         age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> list:
#
#     user_id = str(int(len(users) + 1)
#
#     user: List[User] = [User(id=user_id, username=username, age=age)]

# return f"User username - {username}, age - {age}  is registered!"

#
# @app.put("/users/{user_id}/{username}/{age}")
# async def update_user(user_id: int,
#                       username: Annotated[
#                           str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
#                       age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> list:
#     users[user_id] = f"Имя: {username}, возраст: {age}"
#     return f"The user {user_id} is updated"
#
#
# @app.delete("/users/{user_id}")
# async def delete_user(user_id: int) -> dict:
#     users.pop(str(user_id))
#     return f"User with ID {user_id} was deleted."
