'''Часть 2. Пропуск тестов.'''
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_Runner1 = Runner(1)
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        test_Runner1.walk()
        self.assertEqual(test_Runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_Runner2 = Runner(2)
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        test_Runner2.run()
        self.assertEqual(test_Runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_Runner3 = Runner(3)
        test_Runner4 = Runner(4)
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner3.walk()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        test_Runner4.run()
        self.assertNotEqual(test_Runner3.distance, test_Runner4.distance)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        test_Runner5 = Runner(5)
        test_Runner5.run()
        self.assertEqual(test_Runner5.distance, 10)


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            # l=[participant for participant in self.participants]
            # for i in l:
            #     i.run()
            #     if i.distance > self.full_distance:
            #         finishers[place] = i.name
            #         place += 1
            #         self.participants.remove(i)

            for participant in self.participants[:]:
                participant.run()
                if participant.distance > self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)



        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @ unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
        # print("start")

    @classmethod
    def tearDownClass(cls):
        # print("end")

        print(*cls.all_results.values(), sep="\n")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1_on_dist_90(self):
        self.tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = (self.tournament_1.start())
        # print(self.all_results)
        # print(self.all_results[max(self.all_results)])
        self.assertTrue(self.all_results[1][max(self.all_results[1])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2_on_dist_90(self):
        self.tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = (self.tournament_2.start())
        self.assertTrue(self.all_results[2][max(self.all_results[2])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3_on_dist_90(self):
        self.tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = (self.tournament_3.start())
        self.assertTrue(self.all_results[3][max(self.all_results[3])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test4_on_dist_6(self):
        self.tournament_4 = Tournament(6, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[4] = (self.tournament_4.start())
        self.assertTrue(self.all_results[4][max(self.all_results[4])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним!")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test5_on_dist_1(self):
        self.tournament_5 = Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[5] = (self.tournament_5.start())
        self.assertTrue(self.all_results[5][max(self.all_results[5])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним!")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test6_on_dist_0(self):
        self.tournament_6 = Tournament(0, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[6] = (self.tournament_6.start())
        '''Ник всегда должен быть последним! но забег еще не начался'''

