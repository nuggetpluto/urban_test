import sqlite3

DATABASE_NAME = 'products.db'

def initiate_db():
    """Создает таблицу Products, если она еще не существует."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            photo_path TEXT NOT NULL  -- Новое поле для хранения пути к фото
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

def add_product(title, description, price, photo_path):
    """Добавляет продукт в таблицу Products."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Products (title, description, price, photo_path) 
        VALUES (?, ?, ?, ?)
    ''', (title, description, price, photo_path))

    conn.commit()
    conn.close()
