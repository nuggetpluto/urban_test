import unittest
import logging
from rt_with_exceptions import Runner


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    format='%(levelname)s:%(message)s',
    encoding='utf-8'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', e)
            self.fail("test_walk failed due to invalid speed")

    def test_run(self):
        try:
            runner = Runner(123, 5)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner: %s', e)
            self.fail("test_run failed due to invalid name type")


if __name__ == '__main__':
    unittest.main()
