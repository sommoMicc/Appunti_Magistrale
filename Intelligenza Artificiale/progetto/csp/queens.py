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
from csp.csp import Constraint, VariableValuesSorter, CSP

from typing import Dict, List, Optional, TypeVar, Tuple

import random
from enum import Enum

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


class DefaultConstraintValueSorter(VariableValuesSorter):

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]):
        return domains[variable]


class RandomConstraintValueSorter(VariableValuesSorter):

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]):
        random.shuffle(domains[variable])
        return domains[variable]


class LeastConstraintValueSorter(VariableValuesSorter):

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]) -> D:
        """
        Ordina gli elementi del dominio di "variable" in base al numero di conflitti: valori che portano ad un numero
        di conflitti minore verranno posizionati prima di quelli che portano ad un numero di conflitti più alto (è il
        contrario di quello che fa min_conflicts)
        :param variable:
        :param domains:
        :param assignment:
        :return:
        """
        domain: D = domains[variable]
        domain.sort(key=lambda row: LeastConstraintValueSorter.number_of_conflicts(variable, row, assignment))
        return domain

    @staticmethod
    def number_of_conflicts(queen_column: V, queen_row: D, assignment: Dict[V, D]) -> int:
        """
        Calcola il numero di conflitti che si avrebbero nell'assegnamento "assignment" se alla variabile "queen_column"
        venisse assegnato il valore "queen_row"
        :param queen_column:
        :param queen_row:
        :param assignment:
        :return:
        """
        conflicts: int = 0

        for other_queen_column in assignment:
            other_queen_row: D = assignment[other_queen_column]
            if other_queen_row == queen_row or abs(queen_row - other_queen_row) == abs(
                    queen_column - other_queen_column):
                conflicts += 1

        return conflicts


class ValuesSorter(Enum):
    DEFAULT = 1
    RANDOM = 2
    LEAST_CONSTRAINT = 3


class CSPQueenSolver(Solver):
    def print_solutions(self):
        return CSPQueenSolver._print_solutions(self.n, self.solution)

    def __init__(self, n: int, blocked_queens: Dict[V, D], value_sorter: ValuesSorter = ValuesSorter.DEFAULT,
                 use_ac3: bool = True, use_fc: bool = True, use_mrv: bool = True):
        super().__init__(n, blocked_queens)
        self.solution: Optional[Dict[int, int]] = None

        self.value_sorter: VariableValuesSorter = DefaultConstraintValueSorter()

        if value_sorter == ValuesSorter.RANDOM:
            self.value_sorter = RandomConstraintValueSorter()
        elif value_sorter == ValuesSorter.LEAST_CONSTRAINT:
            self.value_sorter = LeastConstraintValueSorter()

        self.use_ac3: bool = use_ac3
        self.use_fc: bool = use_fc
        self.use_mrv: bool = use_mrv

    def solve(self) -> Tuple[Optional[Dict[int, int]], int]:
        blocked_queens_constraint: BlockedQueensConstraint = BlockedQueensConstraint(self.blocked_queens)

        queens: List[int] = list(range(self.n))
        domains: Dict[int, List[int]] = {}

        for column in queens:
            domains[column] = list(range(self.n))

        csp: CSP[int, int] = CSP(queens, domains, self.value_sorter, ac3=self.use_ac3, mrv=self.use_mrv, fc=self.use_fc)

        csp.add_constraint(QueensConstraint(queens))
        csp.add_constraint(blocked_queens_constraint)

        solution, iterations = csp.backtracking()
        self.solution = solution
        return solution, iterations
