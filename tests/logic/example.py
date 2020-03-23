from src.logic.simplex.simplex_method import start_simplex_method
from src.logic.simplex.lin_prog_problem import LinearProgramProblem, np, cp


def solve_example(*example_dates):
    lp = LinearProgramProblem(*example_dates)
    canon_lp = cp.deepcopy(lp)
    canon_lp.convert_canon_type()
    X, plot_points = start_simplex_method(canon_lp.A, canon_lp.b,
                                          canon_lp.c)
    result_X_example = canon_lp.find_init_X(X)
    decision_example: float = float(np.dot(lp.c.transpose(), result_X_example))
    return round(decision_example, 1)
