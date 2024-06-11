class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля"


class Nissan(Vehicle, Car):
    def __init__(self):
        Vehicle.__init__(self)
        Car.__init__(self)
        self.vehicle_type = "Nissan"
        self.price = 1500000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля Nissan"


nissan_car = Nissan()

print("Тип транспортного средства:", nissan_car.vehicle_type)
print("Цена:", nissan_car.price)
print(nissan_car.horse_powers())
