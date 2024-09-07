import sqlite3
import random
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')


for i in range(10):
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) 
    VALUES(?, ?, ?, ?)''',
                   (f"User{i}", f"example{i}@gmail.com", random.randint(20, 60), 1000))

# Обновление баланса у каждой 2-й записи, начиная с 1-й
cursor.execute('''
UPDATE Users 
SET balance = ?
WHERE id % 2 = ?
''', (500, 1))

# Удаление каждой 3-й записи, начиная с 1-й
cursor.execute('''
DELETE FROM Users 
WHERE id % 3 = ?
''',(0,))


# Выборка всех записей, где возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# cursor.execute("SELECT username, age FROM Users GROUP BY age")

users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()