from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver
from csp.queens import CSPQueenSolver, ValuesSorter
from utils.generator import BlockedQueensGenerator

from typing import Dict, Tuple, List
from timeit import default_timer as timer

from matplotlib import pyplot as plt

from utils.solution_printer import SolutionPrinter


class Benchmark:
    def __init__(self, n: int, n_blocked: int):
        self.n = n
        self.n_blocked = n_blocked

    @staticmethod
    def _run_test(solver: Solver, name) -> Tuple[int, float]:
        start_time: float = timer()
        solutions, iterations = solver.solve()
        end_time: float = timer()
        elapsed_time: float = end_time - start_time

        print("- %s in %d iterazioni e %f secondi:" % (name, iterations, elapsed_time))
        # solver.print_solutions()

        return iterations, elapsed_time

    def csp_internal_comparison(self, attempt_number: int = 3):
        avg_iterations, avg_times, max_times, min_times = [0] * 4, [0] * 4, [-1] * 4, [-1] * 4

        for attempt in range(attempt_number):
            print("Attempt #%d/%d" % (attempt + 1, attempt_number))
            blocked_queens: Dict[int, int] = BlockedQueensGenerator(self.n, self.n_blocked).generate()

            solvers: List[CSPQueenSolver] = []
            standard_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                          False, False, False)
            solvers.append(standard_CSP)

            ac3_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                     True, False, False)
            solvers.append(ac3_CSP)
            ac3_fc_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                        True, True, False)
            solvers.append(ac3_fc_CSP)
            complete_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                          True, True, True)
            solvers.append(complete_CSP)

            for i in range(len(solvers)):
                iteration, time = self._run_test(solvers[i], "CSP %d" % i)
                avg_iterations[i] += iteration
                avg_times[i] += time

                if time > max_times[i]:
                    max_times[i] = time
                if time < min_times[i] or min_times[i] < 0:
                    min_times[i] = time

        avg_iterations, avg_times = list((x / attempt_number for x in avg_iterations)), \
                                    list((x / attempt_number for x in avg_times))

        return avg_times, min_times, max_times

    def csp_min_conflict_comparison(self, attempt_numbers: int = 3) -> Dict[str, Tuple[float, float, float]]:
        print("\n#Queens: %d, #Blocked: %d" % (self.n, self.n_blocked))
        output: Dict[str, Tuple[float, float, float]] = {}

        avg_csp_iterations, avg_csp_time, max_csp_time, min_csp_time = (.0, .0, -1, -1)
        avg_mc_iterations, avg_mc_time, max_mc_time, min_mc_time = (.0, .0, -1, -1)

        for attempt in range(attempt_numbers):
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

        output["CSP"] = (avg_csp_iterations / attempt_numbers,
                         avg_csp_time / attempt_numbers,
                         max_csp_time - min_csp_time)

        output["MIN-CONFLICTS"] = (avg_mc_iterations / attempt_numbers,
                                   avg_mc_time / attempt_numbers,
                                   max_mc_time - min_mc_time)

        return output


def test_1():
    result: Dict[int, Dict[str, Tuple[float, float, float]]] = {}
    n_blocked_queens: int = 2

    for n in range(4, 31, 1):
        result[n] = Benchmark(n, n_blocked_queens).csp_min_conflict_comparison(5)

    x_axis_values = list(result.keys())

    y_csp, y_min_conflicts = [], []
    y_var_min_conflicts, y_var_csp = [], []

    for n in result.keys():
        y_min_conflicts.append(result[n]["MIN-CONFLICTS"][1])
        y_var_min_conflicts.append(result[n]["MIN-CONFLICTS"][2])

        y_csp.append(result[n]["CSP"][1])
        y_var_csp.append(result[n]["CSP"][2])

    print("result.keys(): %r, y: %r" % (x_axis_values, y_csp))

    fig, (time_ax, delta_ax) = plt.subplots(2, sharex="all")
    fig.set_figheight(8)
    fig.set_figwidth(5)

    # fig.suptitle('CSP vs Min conflicts: %d blocked queens' % n_blocked_queens)

    time_ax.plot(x_axis_values, y_csp, label="CSP")
    time_ax.plot(x_axis_values, y_min_conflicts, label="MIN-CONFLICTS")
    time_ax.set(title='CSP vs Min Conflicts', ylabel='Time (s)')
    time_ax.legend(loc="upper left")

    delta_ax.plot(x_axis_values, y_var_csp, label="CSP")
    delta_ax.plot(x_axis_values, y_var_min_conflicts, label="MIN-CONFLICTS")
    delta_ax.set(xlabel='Number of queens (board size)', ylabel='Delta time (s)',
                 title='CSP vs Min Conflicts - Time variability')
    delta_ax.legend(loc="upper left")

    delta_ax.grid()
    time_ax.grid()

    plt.savefig("plots/test_1.png", dpi=410)
    plt.show()


csp_variants: List[str] = ["Standard", "AC3", "AC3+FC", "AC3+FC+MRV"]


def test_2():
    """
    Testo le varie implementazioni di CSP
    :return:
    """
    avg_times, min_times, max_times = Benchmark(15, 2).csp_internal_comparison(10)

    variants_range: range = range(len(avg_times))

    max_bar = plt.bar(variants_range, max_times)
    avg_bar = plt.bar(variants_range, avg_times)
    min_bar = plt.bar(variants_range, min_times)

    plt.legend((avg_bar[0], min_bar[0], max_bar[0]), ('AVG', 'Min', 'Max'))

    plt.xticks(variants_range, csp_variants)

    plt.yscale('log')
    plt.ylabel('Time (in seconds)')

    plt.show()


def test_3():
    x: List[List[int]] = []
    y: List[List[float]] = []

    for i in range(4):
        n_queens: int = i * 5 + 5

        x.append([])
        y.append([])

        avg_times, min_times, max_times = Benchmark(n_queens, 2).csp_internal_comparison(5)
        for j in range(len(csp_variants)):
            x[i].append(i)
            y[i].append(avg_times[j])

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    # test_2()
    test_3()
