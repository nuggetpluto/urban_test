def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения позиций строк
    line_number = 1  # Начинаем с первой строки

    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            # Запоминаем позицию начала строки
            start_position = file.tell()
            # Записываем строку в файл с новой строкой на конце
            file.write(string + '\n')
            # Сохраняем позицию и строку в словарь
            strings_positions[(line_number, start_position)] = string
            line_number += 1  # Увеличиваем номер строки

    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
