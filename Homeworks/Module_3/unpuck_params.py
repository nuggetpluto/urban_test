# 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1)  # С одним параметром
print_params(2, 3)  # два параметра
print_params(4, 5, 6)  # три параметра
print_params()  # без параметров
print_params(b=25)  # работает:)
print_params(c=[1, 2, 3])  # работает:)

values_list = [1, 'string', 2.5]
values_dict = {'a': 'str', 'b': 1, 'c': 2.6}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'str']
print_params(*values_list_2, 42)  # работает:)
