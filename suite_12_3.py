'''Часть 1. TestSuit.'''
import unittest
import tests_12_1
import tests_12_2




SportST = unittest.TestSuite()
SportST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
SportST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(SportST)




