import sys
import unittest

sys.path.append('../')

from tests.dates.test_dates import give_second_test_dates, give_first_test_dates
from tests.example import solve_example


class TestGui(unittest.TestCase):

    def test_first(self):
        self.assertEqual(solve_example(*give_first_test_dates()), 48.5)

    def test_second(self):
        self.assertEqual(solve_example(*give_second_test_dates()), 16.4)


if __name__ == '__main__':
    unittest.main()
