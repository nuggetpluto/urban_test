class Vehicle:
    # Список допустимых цветов - атрибут класса
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец может меняться
        self.__model = model  # Модель не меняется после создания
        self.__engine_power = engine_power  # Мощность двигателя не меняется
        self.__color = color  # Цвет можно менять, но только на допустимый

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        # Метод выводит информацию о транспорте
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        # Метод проверяет, является ли предложенный цвет допустимым
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color  # Если допустим, изменяем цвет
        else:
            print(f"Нельзя сменить цвет на {new_color}")  # Иначе сообщаем о недопустимости

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Ограничение на количество пассажиров

# Пример использования классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Исходные свойства
vehicle1.print_info()

# Попытка сменить цвет на недопустимый
vehicle1.set_color('Pink')
# Смена цвета на допустимый
vehicle1.set_color('black')
# Изменение владельца
vehicle1.owner = 'Vasyok'

# Проверка изменений
vehicle1.print_info()
