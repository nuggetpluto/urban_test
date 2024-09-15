import sqlite3

DATABASE_NAME = 'products.db'

def initiate_db():
    """Создает таблицы Products и Users, если они еще не существуют."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Создаем таблицу Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            photo_path TEXT NOT NULL
        )
    ''')

    # Создаем таблицу Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products

def add_user(username, email, age):
    """Добавляет нового пользователя в таблицу Users."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()

def is_included(username):
    """Проверяет, есть ли пользователь с данным именем в таблице Users."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user is not None
