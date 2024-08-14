import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_walk(self):
        runner = Runner('Иван')
        for _ in range(10):
            runner.walk()
            self.assertEqual(runner.distance, 50)

    def test_runner_run(self):
        runner = Runner('Иван(run)')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge_runner(self):
        runner1 = Runner('Иван(challenge)')
        runner2 = Runner('Петр(challenge)')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()

