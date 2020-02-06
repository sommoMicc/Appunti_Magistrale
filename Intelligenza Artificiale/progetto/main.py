from min_conflicts.min_conflict import MinConflictSolver
from csp.queens import CSPQueenSolver
from utils.generator import BlockedQueensGenerator

from typing import TypeVar, Dict, Optional

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


grid_size: int = 10
blocked_queens_number = 2

blocked_queens: Dict[V, D] = BlockedQueensGenerator(grid_size, blocked_queens_number)\
                                .generate()

csp_solver: CSPQueenSolver = CSPQueenSolver(grid_size, blocked_queens)
min_conflicts_solver: MinConflictSolver = MinConflictSolver(grid_size, blocked_queens)

csp_solution = csp_solver.solve()
min_conflict_solution = min_conflicts_solver.solve()

print("CSP Solution: %r" % csp_solution)
print("MIN_conflicts_solution: %r" % min_conflict_solution)
