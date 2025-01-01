import sqlite3

'''
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
'''

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    for i in range(1, 6):
        cursor.execute(f"INSERT INTO Products VALUES('{i}', 'Продукт {i}', 'Описание {i}', {i * 100})")

        connection.commit()


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor.execute("SELECT * FROM Products")
    # cursor.execute("SELECT title, description, price FROM Products")
    # "Название: <title> | Описание: <description> | Цена: <price>"
    # products = cursor.fetchall()
    # for product in products:
    #     print('Название:%s | Описание:%s | Цена:%d' % (product[0], product[1], product[2]))
    # connection.commit()
    # print(products)
    connection.commit()
    connection.close()


# initiate_db()

# get_all_products()



