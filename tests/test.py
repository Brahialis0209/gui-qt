import sys

sys.path.append('../')

from tests.dates.test_dates import give_second_test_dates, give_first_test_dates
from tests.logic.example import solve_example

if __name__ == "__main__":
    example_first_dates = give_first_test_dates()
    assert (solve_example(*example_first_dates) == 48.5)

    example_second_dates = give_second_test_dates()
    assert (solve_example(*example_second_dates) == 16.4)
