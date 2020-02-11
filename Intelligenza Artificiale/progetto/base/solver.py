from abc import ABC, abstractmethod
from typing import TypeVar, Dict, Optional, Tuple
from utils.solution_printer import SolutionPrinter

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class Solver(ABC):
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        self.n: int = n
        self.blocked_queens: Dict[V, D] = blocked_queens

    @abstractmethod
    def solve(self) -> Tuple[Optional[Dict[int, int]], int]:
        ...

    @abstractmethod
    def print_solutions(self):
        ...

    @staticmethod
    def _print_solutions(n: int, queen_positions: Dict[int, int]):
        sorted_queen_positions: Dict[int, int] = {}
        for key in sorted(queen_positions):
            sorted_queen_positions[key] = queen_positions[key]
        SolutionPrinter.print_solutions(n, sorted_queen_positions)

