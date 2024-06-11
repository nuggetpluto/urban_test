file_name = 'text.txt'
with open(file_name,mode='r',encoding='utf-8') as file:
    for line in file:
        print(line)
print(file.closed)
print('Чем отличается использование оператора with open(file_name...) от простого использования file.close()?\n')
print('Оператор with гарантирует закрытие файла при заверешении блока кода под ним')