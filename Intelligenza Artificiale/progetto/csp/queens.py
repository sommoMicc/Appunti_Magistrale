# queens.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from base.solver import Solver
from csp.csp import Constraint, CSP
from utils.generator import BlockedQueensGenerator

from typing import Dict, List, Optional, TypeVar

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]  # q2r = queen 2 row
                    if q1r == q2r:  # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):  # same diagonal?
                        return False
        return True  # no conflict


class BlockedQueensConstraint(Constraint[int, int]):
    def __init__(self, positions: Dict[int, int]) -> None:
        super().__init__(list(positions.keys()))
        self.positions = positions

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        for queen in self.positions.keys():
            if queen in assignment.keys() and assignment[queen] != self.positions[queen]:
                return False
        return True  # no conflict


class CSPQueenSolver(Solver):
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        super().__init__(n, blocked_queens)

    def solve(self) -> Optional[Dict[int, int]]:
        n_queens: int = 20
        n_blocked_queens: int = 2

        blocked_queens_constraint: BlockedQueensConstraint = BlockedQueensConstraint(self.blocked_queens)

        queens: List[int] = list(range(n_queens))
        domains: Dict[int, List[int]] = {}

        for column in queens:
            domains[column] = list(range(n_queens))

        csp: CSP[int, int] = CSP(queens, domains)

        csp.add_constraint(QueensConstraint(queens))
        csp.add_constraint(blocked_queens_constraint)

        solution: Optional[Dict[int, int]] = csp.backtracking()
        return solution
