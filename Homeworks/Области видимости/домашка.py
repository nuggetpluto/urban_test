def test_function():
    pass

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()# ничего не выводит,до момента пока не вызвать глобальную функцию


test_function()
# inner_function() при запуске дает ошибку,где такая функция не найдена