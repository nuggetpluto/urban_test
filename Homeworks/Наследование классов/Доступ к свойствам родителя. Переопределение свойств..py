class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color.upper()  # Приведение к верхнему регистру для единообразия
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # ограничение на количество пассажиров в седане

    # Здесь все методы и атрибуты наследуются от Vehicle

# Создаем объект класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Попытка смены цвета на недопустимый
vehicle1.set_color('Pink')
# Попытка смены цвета на допустимый
vehicle1.set_color('BLACK')
# Изменение владельца
vehicle1.owner = 'Vasyok'

# Проверка изменений
vehicle1.print_info()
