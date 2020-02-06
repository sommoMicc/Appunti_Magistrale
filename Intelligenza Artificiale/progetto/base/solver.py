from abc import ABC, abstractmethod
from typing import TypeVar, Dict, Optional
from utils.solution_printer import SolutionPrinter

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class Solver(ABC):
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        self.n: int = n
        self.blocked_queens: Dict[V, D] = blocked_queens

    @abstractmethod
    def solve(self) -> Optional[Dict[int, int]]:
        ...

    def print_solutions(self, queen_positions: Dict[int, int]):
        SolutionPrinter.print_solutions(self.n, queen_positions)

