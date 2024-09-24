def apply_all_func(int_list, *functions):
    results = {}  # Словарь для хранения результатов
    for func in functions:
        # Вызываем функцию и сохраняем результат в словарь с ключом, равным названию функции
        results[func.__name__] = func(int_list)
    return results

# Пример использования
def test_functions():
    # Определение списка чисел
    numbers = [6, 20, 15, 9]

    # Первый вызов с функциями max и min
    result1 = apply_all_func(numbers, max, min)
    print(result1)

    # Второй вызов с функциями len, sum и sorted
    result2 = apply_all_func(numbers, len, sum, sorted)
    print(result2)

# Вызов функции тестирования
test_functions()
