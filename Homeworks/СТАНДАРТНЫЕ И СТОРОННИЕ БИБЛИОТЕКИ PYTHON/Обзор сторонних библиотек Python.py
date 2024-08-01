import requests
import pandas as pd
import matplotlib.pyplot as plt

# ======== ЧАСТЬ 1: Использование библиотеки requests ========

# Выполним GET-запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверим статус ответа
print("===== ЧАСТЬ 1: Использование библиотеки requests =====")
print(f"Статус-код ответа: {response.status_code}")

# Выводим первые 3 поста в формате JSON
posts = response.json()
print("Первые 3 поста:")
for post in posts[:3]:
    print(post)
print("\n")

# ======== ЧАСТЬ 2: Использование библиотеки pandas ========

# Создадим простой DataFrame для анализа
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

print("===== ЧАСТЬ 2: Использование библиотеки pandas =====")
# Вывод первых пяти строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())

# Частотный анализ значений в колонке 'City'
print("\nЧастотный анализ значений в колонке 'City':")
print(df['City'].value_counts())
print("\n")

# ======== ЧАСТЬ 3: Использование библиотеки matplotlib ========

print("===== ЧАСТЬ 3: Использование библиотеки matplotlib =====")

# Создание данных для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Построение линейного графика
plt.plot(x, y, label='Простая линия')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Пример линейного графика')
plt.legend()
plt.show()

# Построение гистограммы
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, edgecolor='black')
plt.title('Пример гистограммы')
plt.show()

# Построение графика разброса
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Пример графика разброса')
plt.show()
# Импорт необходимых библиотек
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ======== ЧАСТЬ 1: Использование библиотеки requests ========

# Выполним GET-запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверим статус ответа
print("===== ЧАСТЬ 1: Использование библиотеки requests =====")
print(f"Статус-код ответа: {response.status_code}")

# Выводим первые 3 поста в формате JSON
posts = response.json()
print("Первые 3 поста:")
for post in posts[:3]:
    print(post)
print("\n")

# ======== ЧАСТЬ 2: Использование библиотеки pandas ========

# Создадим простой DataFrame для анализа
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

print("===== ЧАСТЬ 2: Использование библиотеки pandas =====")
# Вывод первых пяти строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())

# Частотный анализ значений в колонке 'City'
print("\nЧастотный анализ значений в колонке 'City':")
print(df['City'].value_counts())
print("\n")

# ======== ЧАСТЬ 3: Использование библиотеки matplotlib ========

print("===== ЧАСТЬ 3: Использование библиотеки matplotlib =====")

# Создание данных для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Построение линейного графика
plt.plot(x, y, label='Простая линия')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Пример линейного графика')
plt.legend()
plt.show()

# Построение гистограммы
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, edgecolor='black')
plt.title('Пример гистограммы')
plt.show()

# Построение графика разброса
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Пример графика разброса')
plt.show()