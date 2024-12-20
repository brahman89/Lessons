import logging
import unittest
from unittest import TestCase

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# class Tournament:
#     def __init__(self, distance, *participants):
#         self.full_distance = distance
#         self.participants = list(participants)
#
#     def start(self):
#         finishers = {}
#         place = 1
#         while self.participants:
#             for participant in self.participants[:]:
#                 participant.run()
#                 if participant.distance >= self.full_distance:
#                     finishers[place] = participant
#                     place += 1
#                     self.participants.remove(participant)
#
#         return finishers


class RunnerTest(TestCase):


    def test_walk(self):
        try:
            first = Runner('Вося', -10)
            first.walk()
            self.assertEqual(first.distance, 10)
        except:
            logger.warning("Неверная скорость для Runner")


    def test_run(self):
        try:
            second = Runner(5, 5)
            second.run()
            self.assertEqual(second.distance, 10)
        except :
            logger.warning("Неверный тип данных для объекта Runner")



if __name__ == "__main__":
    unittest.main()



# first = Runner('Вося', -10)
# second = Runner(5, 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())
