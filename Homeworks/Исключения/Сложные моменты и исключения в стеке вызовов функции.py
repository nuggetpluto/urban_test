def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_count = personal_sum(numbers)
        average = result / len(numbers)
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Ожидаем TypeError, так как это строка, а не список
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Ожидаем сумму только чисел
print(f'Результат 3: {calculate_average(567)}')  # Ожидаем TypeError, так как это число, а не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать корректно
