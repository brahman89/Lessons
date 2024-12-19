import logging
import unittest

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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            first = Runner('Вося', -10)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")


    def test_run(self):
        try:
            second = Runner(5, 5)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")


# class TournamentTest(unittest.TestCase):
#
#     def setUp(self):
#         self.runner_1 = Runner("Усэйн", 10)
#         self.runner_2 = Runner("Андрей", 9)
#         self.runner_3 = Runner("Ник", 3)
#
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = dict()
#
#     @classmethod
#     def tearDownClass(cls):
#         print(*cls.all_results.values(), sep="\n")
#
#     def test1_on_dist_90(self):
#         self.tournament_1 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
#         self.all_results[1] = (self.tournament_1.start())
#         self.assertTrue(self.all_results[1][max(self.all_results[1])] == self.runner_3.name)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8", format="%(levelname)s | %(message)s")



    # SportST = unittest.TestSuite()
    # SportST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.test_walk()))
    # SportST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.test_run()))
    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(SportST)

# first = Runner('Вося', -10)
# second = Runner(5, 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())