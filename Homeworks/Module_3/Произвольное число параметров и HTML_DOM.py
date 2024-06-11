def test(*params, **parameters):
    print(params, parameters)


test(1, 2, 3, 4, a=16, b=17)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('Факториал равен:', factorial(6))

