from abc import ABC

from min_conflicts import blocked_n_queens
from utils import generator as Generator
from typing import TypeVar, Dict, Optional

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type

import base.solver


class MinConflictSolver(base.solver.Solver, ABC):
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        super.__init__(n, blocked_queens)

    def solve(self) -> Optional[Dict[int, int]]:
        n = 8
        NQ = blocked_n_queens.BlockedNQueens(n, {
            2: 3,
            3: 5
        })
        timer = 0
        while not NQ.all_queens_safe():
            minAttacks = n + 1  # n + 1 is greater than any possibility of attacks so this is guaranteed to get minimized
            pickedQueen = NQ.pick_random_queen()

            positions = NQ.available_positions(pickedQueen)
            minConflictPosition = (-1, -1)
            for pos in positions:  # iterate through all positions of pickedQueen and move to position of minimum conflict
                NQ.move_queen(pickedQueen, pos)
                newNumberOfConflicts = NQ.queen_number_conflicts(pos)
                if newNumberOfConflicts < minAttacks:
                    minConflictPosition = pos
                    minAttacks = newNumberOfConflicts
                NQ.move_queen(pos, pickedQueen)  # move queen back

            NQ.move_queen(pickedQueen, minConflictPosition)  # move queen to least conflict spot

        print(NQ.print_board())

        return None
