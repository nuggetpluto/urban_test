import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("TestRunner", 5)

    def test_walk(self):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    def test_run(self):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner1 = Runner("Runner1", 5)
        runner2 = Runner("Runner2", 7)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для заморозки тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        self.usain = Runner("Usain", 10)
        self.andrey = Runner("Andrey", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        if not cls.is_frozen:
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
