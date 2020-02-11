from base.solver import Solver
from min_conflicts.min_conflict import MinConflictSolver
from csp.queens import CSPQueenSolver
from utils.generator import BlockedQueensGenerator

from typing import TypeVar, Dict, Tuple
from timeit import default_timer as timer

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class Benchmark:
    def __init__(self, n: int, n_blocked: int):
        self.n = n
        self.n_blocked = n_blocked

    @staticmethod
    def _run_test(solver: Solver, name) -> Tuple[float, float]:
        start_time: float = timer()
        solutions, iterations = solver.solve()
        end_time: float = timer()
        elapsed_time: float = end_time - start_time

        print("- %s in %d iterazioni e %f secondi:" % (name, iterations, elapsed_time))
        solver.print_solutions()

        return iterations, elapsed_time

    def run(self):
        print("\n#Queens: %d, #Blocked: %d" % (self.n, self.n_blocked))
        blocked_queens: Dict[V, D] = BlockedQueensGenerator(self.n, self.n_blocked).generate()

        print("blocked: %r" % blocked_queens)

        csp_iterations, csp_time = Benchmark._run_test(CSPQueenSolver(self.n, blocked_queens), "CSP")
        mc_iterations, mc_time = Benchmark._run_test(MinConflictSolver(self.n, blocked_queens), "MIN-CONFLICTS")

        return {
            "CSP": (csp_iterations, csp_time),
            "MIN_CONFLICT": (mc_iterations, mc_time)
        }


for n_queens in range(10, 30, 5):
    n_blocked_queens: int = 2  # round(n_queens / 10.0 * 2)
    Benchmark(n_queens, n_blocked_queens).run()