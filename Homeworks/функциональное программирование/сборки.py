my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def square(x):
    return x ** 2
def parity(x):
    if x % 2 != 0:
        return x ** 2


mappping = map(square,filter(parity,my_numbers))
print(list(mappping))