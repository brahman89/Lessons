import unittest


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
            l=[participant for participant in self.participants]
            for i in l:
                i.run()
                if i.distance > self.full_distance:
                    finishers[place] = i.name
                    place += 1
                    self.participants.remove(i)

            # for participant in self.participants:
            #     participant.run()
                # if participant.distance > self.full_distance:
                #     finishers[place] = participant
                #     place += 1
                #     self.participants.remove(participant)



        return finishers


class TournamentTest(unittest.TestCase):

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

    def test1_on_dist_90(self):
        self.tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = (self.tournament_1.start())
        # print(self.all_results)
        # print(self.all_results[max(self.all_results)])
        self.assertTrue(self.all_results[1][max(self.all_results[1])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    def test2_on_dist_90(self):
        self.tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = (self.tournament_2.start())
        self.assertTrue(self.all_results[2][max(self.all_results[2])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    def test3_on_dist_90(self):
        self.tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = (self.tournament_3.start())
        self.assertTrue(self.all_results[3][max(self.all_results[3])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним")

    def test4_on_dist_6(self):
        self.tournament_4 = Tournament(6, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[4] = (self.tournament_4.start())
        self.assertTrue(self.all_results[4][max(self.all_results[4])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним!")

    def test5_on_dist_1(self):
        self.tournament_5 = Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[5] = (self.tournament_5.start())
        self.assertTrue(self.all_results[5][max(self.all_results[5])] == self.runner_3.name,
                        msg="Ник всегда должен быть последним!")


    # def test6_on_dist_0(self):
    #     self.tournament_6 = Tournament(0, self.runner_1, self.runner_2, self.runner_3)
    #     self.all_results[6] = (self.tournament_6.start())
    #     '''Ник всегда должен быть последним! но забег еще не начался'''


if __name__ == "__main__":
    unittest.main()
