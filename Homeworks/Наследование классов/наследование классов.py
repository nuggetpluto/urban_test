class Car:
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        return 210


class Kia(Car):
    price = 1500000

    def horse_powers(self):
        return 220


car = Car()
nissan = Nissan()
kia = Kia()
print(car.price, car.horse_powers())
print(nissan.price, nissan.horse_powers())
print(kia.price, kia.horse_powers())


