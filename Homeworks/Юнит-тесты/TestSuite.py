import unittest
from test_runner import TestRunner
from test_tournament import TournamentTest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestRunner),
        unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest),
    ])
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
