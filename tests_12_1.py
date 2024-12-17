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

    def test_run2(self):
        test_Runner5 = Runner(5)
        test_Runner5.run()
        self.assertEqual(test_Runner5.distance, 10)


if __name__ == "__main__":
    unittest.main()
