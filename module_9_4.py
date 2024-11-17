'''Lambda-функция'''
first = 'Мама мыла раму'
second = 'Рамена мало было'
# print("Пример для сравнения\n[False, True, True, False, False, False, False, False, True, False, False, False, False, False]\n")
print(list(map(lambda x, y: x == y, first, second)))

'''Замыкание'''
print("\n")


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for i in data_set:
                file.write(str(i) + "\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

with open('example.txt', "r", encoding="utf-8") as file:
    text = file.read()
    print(text)

'''Метод __call__:'''
from random import choice, random


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
