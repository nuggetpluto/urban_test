def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item  # Попытка прибавить число к результату
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):  # Проверяем, является ли numbers коллекцией
            raise TypeError('В numbers записан некорректный тип данных')

        sum_result, correct_count = personal_sum(numbers)  # Получаем сумму и количество корректных элементов
        if correct_count == 0:
            return 0  # Если корректных элементов нет, возвращаем 0
        return sum_result / correct_count  # Возвращаем среднее арифметическое
    except ZeroDivisionError:
        return 0  # В случае деления на ноль возвращаем 0
    except TypeError as e:
        print(e)
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Передана строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанный список
print(f'Результат 3: {calculate_average(567)}')  # Передано число
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Передан список чисел
