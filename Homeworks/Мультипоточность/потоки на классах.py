import time
import threading

class Knight(threading.Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name},на нас напали!')
        while enemies > 0:
            days += 1
            time.sleep(1)
            enemies -= self.power
            print(f'{self.name},сражается {days} день(дня)..., осталось {max(0, enemies)} воинов')

        print(f'{self.name} одержал победу спустя {days} день(дня)')


first_khight = Knight('Sir Lancelot',10)
second_khight = Knight('Sir Galahd',20)


first_khight.start()
second_khight.start()


first_khight.join()
second_khight.join()

print('Все битвы закончились')




