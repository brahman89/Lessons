import threading
import time
import random
from random import randint

from arcade.examples.tetris import colors


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count1 = 0
        self.lock.acquire()
        while count1 != 100:
            # print(f'count1-{count1}, {self.lock.locked()}')
            count1 += 1

            dep = randint(50, 500)
            self.balance += dep
            print(f"Пополнение: {dep}. Баланс: {self.balance}\n")
            time.sleep(0.001)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):

        count2 = 0

        while count2 != 100:
            # print(f'count2-{count2}')
            count2 += 1
            tak = randint(50, 500)
            print(f"Запрос на {tak}")

            if self.balance <= tak:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= tak
                print(f"Снятие: {tak}. Баланс: {self.balance}\n")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
