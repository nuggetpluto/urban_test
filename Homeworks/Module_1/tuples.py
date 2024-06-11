immutable_var = 1, '2', True, [4,5]
print(immutable_var)
#immutable_var[0] = 2# Неизменяемый тип данных,выведет ошибку(нельзя обращаться по элементам)

mutable_list = [1, 2, 3]

mutable_list.append('Modified')
print(mutable_list)

mutable_list.extend('Modified')
print(mutable_list)
