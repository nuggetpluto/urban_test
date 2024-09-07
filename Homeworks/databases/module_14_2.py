import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Удаление записи с id = 6
cursor.execute('''
DELETE FROM Users
WHERE id = 6
''')

# Подсчет общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Общее количество записей: {total_users}')

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f'Сумма всех балансов: {total_balance}')

# Вычисление среднего баланса
if total_users > 0:
    average_balance = total_balance / total_users
    print(f'Средний баланс: {average_balance:.2f}')
else:
    print('Записей в таблице нет.')

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
