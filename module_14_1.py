import sqlite3

'''
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)'''

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
#
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{10*i}', '1000' ))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id  = ?", ('500', f'{i}'))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id  = ?", (f'{i}',))

cursor.execute("SELECT username, email, age, balance   FROM Users WHERE age != ?", (60,))
# '''Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>'''
users = cursor.fetchall()
for user in users:
    print('Имя:%s | Почта:%s | Возраст:%d | Баланс:%d' % (user[0],user[1],user[2],user[3]))

connection.commit()
connection.close()