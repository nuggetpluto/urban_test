import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrey = Runner("Andrey", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            formatted_result = {place: runner.name for place, runner in result.items()}
            print(formatted_result)

    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain vs Nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Nick")

    def test_andrey_vs_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Andrey vs Nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Nick")

    def test_usain_andrey_vs_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain, Andrey vs Nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Nick")


if __name__ == '__main__':
    unittest.main()
