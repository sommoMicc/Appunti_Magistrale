from base.solver import Solver
from min_conflicts.min_conflicts_2 import MinConflictsSolver2
from csp.queens import CSPQueenSolver
from utils.generator import BlockedQueensGenerator

from typing import Dict, Tuple
from timeit import default_timer as timer


class Benchmark:
    def __init__(self, n: int, n_blocked: int, run_csp: bool = True, run_mc:bool = True):
        self.n = n
        self.n_blocked = n_blocked
        self.run_csp = run_csp
        self.run_mc = run_mc

    @staticmethod
    def _run_test(solver: Solver, name) -> Tuple[int, float]:
        start_time: float = timer()
        solutions, iterations = solver.solve()
        end_time: float = timer()
        elapsed_time: float = end_time - start_time

        print("- %s in %d iterazioni e %f secondi:" % (name, iterations, elapsed_time))
        # solver.print_solutions()

        return iterations, elapsed_time

    def run(self) -> Dict[str, Tuple[int, float]]:
        print("\n#Queens: %d, #Blocked: %d" % (self.n, self.n_blocked))
        blocked_queens: Dict[int, int] = BlockedQueensGenerator(self.n, self.n_blocked).generate()

        # SolutionPrinter.print_solutions(self.n, blocked_queens)

        print("blocked: %r" % blocked_queens)

        output: Dict[str, Tuple[int, float]] = {}

        if self.run_csp:
            csp_iterations, csp_time = Benchmark._run_test(CSPQueenSolver(self.n, blocked_queens), "CSP")
            output["CSP"] = (csp_iterations, csp_time)

        if self.run_mc:
            mc_iterations, mc_time = Benchmark._run_test(MinConflictsSolver2(self.n, blocked_queens), "MIN-CONFLICTS")
            output["MC"] = (mc_iterations, mc_time)

        return output


def test_1():
    result: Dict[int, Dict[str, Tuple[int, float]]] = {}
    for n in range(100, 701, 100):
        result[n] = Benchmark(n, 0, run_csp=False).run()

    print("%r" % result)


if __name__ == "__main__":
    test_1()
