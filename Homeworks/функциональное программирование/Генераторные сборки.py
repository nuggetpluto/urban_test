# def function_factory(operation):
#     def add(x, y):
#         return x + y
#
#     def subtract(x, y):
#         return x - y
#
#     def multiply(x, y):
#         return x * y
#
#     def divide(x, y):
#         try:
#             return x / y
#         except ZeroDivisionError:
#             return 'нельзя делить на ноль!'
#
#     if operation == 'add':
#         return add
#     elif operation == 'subtract':
#         return subtract
#     elif operation == 'multiply':
#         return multiply
#     elif operation == 'divide':
#         return divide
#     else:
#         return None
#
#
# add_func = function_factory('add')
# print(add_func(2, 3))
#
#
# divide_func = function_factory('divide')
# print(divide_func(4, 0))
# print(divide_func(4, 2))
#
# add_func = function_factory('add')
# print(add_func(2, 3))
#
# multiply_func = function_factory('divide')
# print(multiply_func(4, 0))

# -----------------------------------------------------------------------------------------


# square_lambda = lambda x: x ** 2
#
#
# def square_def(x):
#     return x ** 2
#
#
# print(square_lambda(4))
# print(square_def(4))
# -----------------------------------------------------------------------------------------
# class Rect:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __call__(self):
#         return self.a * self.b
#
#
# rectangle = Rect(5, 10)
# print(rectangle())
