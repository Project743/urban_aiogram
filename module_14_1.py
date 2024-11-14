import sqlite3

connection = sqlite3.Connection('not_telegram.db')
crs = connection.cursor()

crs.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

for i in range(1,11):
    crs.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?,? )", (f'User{i}', f'example{i}@gmail.com', 10*i, 1000))

crs.execute("SELECT * FROM Users")
users = crs.fetchall()
count = 0
while count < len(users):
    crs.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, users[count][0]))
    count += 2

count = 0
while count < len(users):
    crs.execute("DELETE FROM Users WHERE username =?", (users[count][1],))
    count += 3

crs.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users_= crs.fetchall()
for user in users_:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()
