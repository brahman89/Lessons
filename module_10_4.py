import threading
import time
from queue import Queue
from random import randint
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.daemon = False
        self.name = name

    def run(self):
        delay_ = randint(3, 10)
        time.sleep(delay_)
        print(f"end {self.name}")








class Cafe:

    def __init__(self, *tables):
        self.tables = tables

    # прибытие гостей
    def guest_arrival(self, *guests):
        queue = Queue()
        g = -len(guests)
        t = -len(tables)
        # print(guests[g].name)
        # print(tables[t].guest)
        while g != 0:
            if tables[t].guest == None:
                tables[t].guest = guests[g].name
                (Guest(guests[g].name)).start()
                print(f"{tables[t].guest} сел(-а) за стол номер {tables[t].number}")

                g += 1
                t += 1
            else:
                print(f"{guests[g].name} в очереди")
                queue.put(guests[g].name)
                g += 1

    # #обслужить гостей
    def discuss_guests(self):


        while True:
            for i in guests:
                if i.is_alive()==True:
                    print(i.name)





# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
