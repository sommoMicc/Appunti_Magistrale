from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver
from csp.queens import CSPQueenSolver
from utils.generator import BlockedQueensGenerator

from typing import Dict, Tuple, List
from timeit import default_timer as timer

from matplotlib import pyplot as plt

from utils.solution_printer import SolutionPrinter


class Benchmark:
    def __init__(self, n: int, n_blocked: int):
        self.n = n
        self.n_blocked = n_blocked

        self.attempt_numbers = 3

    @staticmethod
    def _run_test(solver: Solver, name) -> Tuple[int, float]:
        start_time: float = timer()
        solutions, iterations = solver.solve()
        end_time: float = timer()
        elapsed_time: float = end_time - start_time

        print("- %s in %d iterazioni e %f secondi:" % (name, iterations, elapsed_time))
        # solver.print_solutions()

        return iterations, elapsed_time

    def run(self) -> Dict[str, Tuple[float, float, float]]:
        print("\n#Queens: %d, #Blocked: %d" % (self.n, self.n_blocked))
        output: Dict[str, Tuple[float, float, float]] = {}

        avg_csp_iterations, avg_csp_time, max_csp_time, min_csp_time = (.0, .0, -1, -1)
        avg_mc_iterations, avg_mc_time, max_mc_time, min_mc_time = (.0, .0, -1, -1)

        for attempt in range(self.attempt_numbers):
            # Faccio un tentativo diverso con una configurazione di regine bloccate diversa
            blocked_queens: Dict[int, int] = BlockedQueensGenerator(self.n, self.n_blocked).generate()
            print("Blocked queens: %r" % blocked_queens)

            csp_iterations, csp_time = Benchmark._run_test(CSPQueenSolver(self.n, blocked_queens), "CSP")

            if csp_time > max_csp_time:
                max_csp_time = csp_time
            if csp_time < min_csp_time or min_csp_time < 0:
                min_csp_time = csp_time

            avg_csp_iterations += csp_iterations
            avg_csp_time += csp_time

            mc_iterations, mc_time = Benchmark._run_test(MinConflictsSolver(self.n, blocked_queens),
                                                         "MIN-CONFLICTS")

            if mc_time > max_mc_time:
                max_mc_time = mc_time
            if mc_time < min_mc_time or min_mc_time < 0:
                min_mc_time = mc_time

            avg_mc_iterations += mc_iterations
            avg_mc_time += mc_time

        output["CSP"] = (avg_csp_iterations / self.attempt_numbers,
                         avg_csp_time / self.attempt_numbers,
                         max_csp_time-min_csp_time)

        output["MIN-CONFLICTS"] = (avg_mc_iterations / self.attempt_numbers,
                                   avg_mc_time / self.attempt_numbers,
                                   max_mc_time-min_mc_time)

        return output


def test_1():
    result: Dict[int, Dict[str, Tuple[float, float, float]]] = {}
    for n in range(4, 21, 1):
        result[n] = Benchmark(n, 2).run()

    x_axis_values = list(result.keys())

    y_csp, y_min_conflicts = [], []
    y_var_min_conflicts, y_var_csp = [], []

    for n in result.keys():
        y_min_conflicts.append(result[n]["MIN-CONFLICTS"][1])
        y_var_min_conflicts.append(result[n]["MIN-CONFLICTS"][2])

        y_csp.append(result[n]["CSP"][1])
        y_var_csp.append(result[n]["CSP"][2])

    print("result.keys(): %r, y: %r" % (x_axis_values, y_csp))

    _, time_ax = plt.subplots()
    time_ax.plot(x_axis_values, y_csp, label="CSP")
    time_ax.plot(x_axis_values, y_min_conflicts, label="MIN-CONFLICTS")
    time_ax.set(xlabel='Number of queens (board size)', ylabel='time (s)',
           title='CSP vs Min Conflicts')
    time_ax.legend()

    _, delta_ax = plt.subplots()
    delta_ax.plot(x_axis_values, y_var_csp, label="CSP")
    delta_ax.plot(x_axis_values, y_var_min_conflicts, label="MIN-CONFLICTS")
    delta_ax.set(xlabel='Number of queens (board size)', ylabel='Time variability (s)',
           title='CSP vs Min Conflicts - Time variability')
    delta_ax.legend()

    plt.show()


if __name__ == "__main__":
    test_1()
