import random
from typing import Dict, Optional
from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver


class NQueensCompletionGenerator:
    def __init__(self, n_queens: int, n_blocked_queens: int):
        self.n_queens = n_queens
        self.n_blocked_queens = n_blocked_queens

    def _generate(self) -> Optional[Dict[int, int]]:
        if self.n_blocked_queens < 1:
            return None

        solver: Solver = MinConflictsSolver(self.n_queens, {})
        solution, _ = solver.solve()

        # devo eliminare delle colonne qua!!!
        while len(solution.keys()) > self.n_blocked_queens:
            queen_to_delete: int = random.randint(0, len(solution.keys()) - 1)
            solution.pop(list(solution.keys())[queen_to_delete])

        return solution

    def generate(self) -> Dict[int, int]:
        answer: Dict[int, int] = self._generate()
        sorted_answer: Dict[int, int] = {}

        if answer is not None:
            for column in sorted(answer.keys()):
                sorted_answer[column] = answer[column]

        return sorted_answer
