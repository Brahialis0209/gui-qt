import numpy as np
import copy as cp
from src.alg.simplex.lin_prog_problem import LinearProgramProblem
from src.alg.exceptions import SimplexAlgorithmException, \
    NotSolveSimplex
from src.alg.simplex.simplex_method import start_simplex_method


# Задача линейного программирования
class SimplexValues:
    def __init__(self, c, extreme, A, signs, b, var_signs):
        self.c = np.array(c, float)
        self.extreme = extreme
        self.A = np.array(A, float)
        self.signs = signs
        self.b = np.array(b, float)
        self.var_signs = var_signs

    def give_plot_dates(self):
        return list(self.A), list(self.b)

    def extreme_value(self):
        lp = LinearProgramProblem(self.c, self.extreme,
                                  self.A, self.signs, self.b, self.var_signs)
        lp.print_task()
        canon_lp = cp.deepcopy(lp)
        canon_lp.convert_canon_type()
        plot_points = list()
        plot_points_to_true_form = list()

        # ищем решение канон формы симплекс методом
        try:
            X, plot_points = start_simplex_method(canon_lp.A, canon_lp.b,
                                                  canon_lp.c)

        except SimplexAlgorithmException:
            raise SimplexAlgorithmException()

        except Exception:
            raise NotSolveSimplex()

        # решение прямой из решения канонической
        result_X = canon_lp.find_init_X(X)

        for point in plot_points:
            plot_points_to_true_form.append(canon_lp.find_init_X(point))

        return np.dot(lp.c.transpose(), result_X), plot_points_to_true_form