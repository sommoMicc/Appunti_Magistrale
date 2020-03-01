from abc import ABC, abstractmethod
from typing import TypeVar, Dict, Optional, Tuple
from utils.solution_printer import SolutionPrinter

V = TypeVar('V')  # Tipo di variabile
D = TypeVar('D')  # Tipo di dominio


class Solver(ABC):
    """
    Classe base che definisce la struttura di un risolutore del problema N-Queens Completion.
    """
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        self.n: int = n
        self.blocked_queens: Dict[V, D] = blocked_queens

    @abstractmethod
    def solve(self) -> Tuple[Optional[Dict[V, D]], int]:
        """
        Il metodo astratto dovrebbe implementare, nelle classi derivate, la soluzione al problema N-Queens Completion
        coerentemente con i dati di input

        Returns:
            Una tupla formata da:
            - Un dizionario, che associa ad ogni colonna (chiave) una posizione (valore) SE la soluzione è stata trovata
            - Il numero di iterazioni effettuate
        """
        ...

    @abstractmethod
    def print_solutions(self):
        """
        Metodo astratto che dovrebbe permettere di stampare a console la soluzione ottenuta.
        """
        ...

    @staticmethod
    def _print_solutions(n: int, queen_positions: Dict[V, D]):
        """
        Metodo ausiliario che permette di stampare le regine, ordinando prima per chiave il dizionario delle soluzioni,
        in modo da stamparle "in ordine alfabetico"
        Args:
            n (int): la grandezza (numero di righe o di colonne) della scacchiera
            queen_positions (Dict[V,D]): dizionario che associa ad ogni colonna la posizione (riga) della regina
                                         corrispondente

        """
        sorted_queen_positions: Dict[V, D] = {}
        if queen_positions is not None:
            for key in sorted(queen_positions):
                sorted_queen_positions[key] = queen_positions[key]
        SolutionPrinter.print_solutions(n, sorted_queen_positions)

