import sqlite3

'''
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)'''

connection = sqlite3.connect("not_telegram_2.db")
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
## Код из предыдущего задания
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{10*i}', '1000' ))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id  = ?", ('500', f'{i}'))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id  = ?", (f'{i}',))

#
# cursor.execute("SELECT username, email, age, balance FROM Users")
# # '''Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>'''
# users = cursor.fetchall()
# for user in users:
#     print('Имя:%s | Почта:%s | Возраст:%d | Баланс:%d' % (user[0],user[1],user[2],user[3]))
#


# Удаление пользователя с id=6
# cursor.execute("DELETE FROM Users WHERE id  = ?", (6,))


# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
