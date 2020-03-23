from src.logic.simplex.lin_prog_problem import np


def give_first_test_dates():
    c = np.array([2, 3, 1, 5], float)
    extreme = 'max'
    A = np.array([[-2, 6, 1, 0],
                  [3, 2, 0, 1],
                  [2, -1, 0, 0],
                  [1, 2, 4, 1]], float)
    signs = ['<=', '=', '>=', '=']
    b = np.array([40, 28, 14, 12], float)
    var_signs = ['any', 'positive', 'any', 'any']
    return c, extreme, A, signs, b, var_signs


def give_second_test_dates():
    c = np.array([20, 20], float)
    extreme = 'min'
    A = np.array([[4, 2],
                  [6, 3],
                  [5, 8]], float)
    signs = ['>=', '>=', '=']
    b = np.array([2, 4, 5], float)
    var_signs = ['positive', 'positive']
    return c, extreme, A, signs, b, var_signs
