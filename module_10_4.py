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
        self.name = name

    def run(self):
        delay_ = randint(3, 10)
        time.sleep(delay_)
        # print(f"end {self.name}")


class Cafe:

    def __init__(self, *tables):
        self.tables = tables

    # прибытие гостей
    def guest_arrival(self, *guests):
        g = -len(guests)
        t = -len(tables)
        while g != 0:
            if tables[t].guest is None:
                tables[t].guest = guests[g]
                guests[g].start()
                print(f"{guests[g].name} сел(-а) за стол номер {tables[t].number}")

                g += 1
                t += 1
            else:
                print(f"{guests[g].name} в очереди")
                queue.put(guests[g])
                deq.append(1)
                g += 1

    # #обслужить гостей
    def discuss_guests(self):
        k = 0
        # print(len(guests))
        while k <= len(guests):
            for table in tables:
                if table.guest != None:
                    if table.guest.is_alive() == False:
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest = None
                        k += 1
                        # print(k)
                        print(f"Стол номер {table.number} свободен")

                        if queue.empty() == False:
                            table.guest = queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        else:
                            k += 1
                            # print(k)


queue = Queue()
deq = []
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
