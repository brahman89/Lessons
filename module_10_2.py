import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self, daemon=True)
        self.name = name
        self.power = power

    def run(self):
        warriers = 100
        delay = 1
        time_ = 0
        print(f"{self.name}, на нас напали!")

        while warriers:
            time.sleep(delay)
            warriers -= self.power
            print(f"{self.name} сражается {time_} дней(дня)..., осталось {warriers} воинов.")
            time_ += delay
        print(f"{self.name} одержал победу спустя {time_} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
time.sleep(1.1)
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')



