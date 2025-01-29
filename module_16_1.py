from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def root():
    return {"Вы вошли как администратор"}


@app.get("/user")
async def user_paginator(username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}

#
#
# # Определение базового маршрута
# @app.get("/")
# async def root():
#     return {"message": "Hello, FastAPI!"}
#
#
# # GET-запрос — получение данных:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
#
# # POST-запрос — добавление данных
# class Item(BaseModel):
#     name: str
#     price: float
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return {"name": item.name, "price": item.price}
#
# # PUT-запрос — обновление данных (Рис.5):
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "name": item.name, "price": item.price}
#
# # DELETE-запрос — удаление данных (Рис.6):
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"message": "Item deleted", "item_id": item_id}
#
# @app.post("/products/")
# async def create_product():
#     """
#     Создает новый продукт в системе.
#     - **name**: название продукта
#     - **price**: цена продукта
#     - **quantity**: количество на складе
#     """
#     return
