from base.solver import Solver
from min_conflicts.blocked_n_queens import BlockedNQueens
from typing import TypeVar, Dict, Optional, Tuple

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class MinConflictSolver(Solver):
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        super().__init__(n, blocked_queens)
        self.NQ = BlockedNQueens(self.n, self.blocked_queens)

    def print_solutions(self):
        return self._print_solutions(self.n, self.NQ.get_solution())

    def solve(self) -> Tuple[Optional[Dict[int, int]], int]:
        iterations: int = 0
        while not self.NQ.all_queens_safe():
            iterations = iterations + 1

            minAttacks: int = self.n + 1  # n + 1 is greater than any possibility of attacks so this is guaranteed to get minimized
            pickedQueen = self.NQ.pick_random_queen("MAIN")

            positions = self.NQ.available_positions(pickedQueen)
            minConflictPosition = (-1, -1)
            for pos in positions:  # iterate through all positions of pickedQueen and move to position of minimum conflict
                self.NQ.move_queen(pickedQueen, pos)
                newNumberOfConflicts = self.NQ.queen_number_conflicts(pos)
                if newNumberOfConflicts < minAttacks:
                    minConflictPosition = pos
                    minAttacks = newNumberOfConflicts
                self.NQ.move_queen(pos, pickedQueen)  # move queen back

            self.NQ.move_queen(pickedQueen, minConflictPosition)  # move queen to least conflict spot

        return self.NQ.get_solution(), iterations

