import random
from typing import Dict, Optional
from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver


class NQueensCompletionGenerator:
    """
    Classe che genera una configurazione casuale di regine bloccate
    """
    def __init__(self, n_queens: int, n_blocked_queens: int):
        """
        Costruttore
        Args:
            n_queens: numero di regine (dimensione della scacchiera)
            n_blocked_queens: numero di regine bloccate
        """
        self.n_queens = n_queens
        self.n_blocked_queens = n_blocked_queens

    def _generate(self) -> Optional[Dict[int, int]]:
        """
        Genera un assegnamento consistente di k=n_blocked_queens posizioni su una scacchiera NxN, dove N = n_queens
        Returns:
            Un assegnamento consistente. Se n_blocked_queens == 0, ritorna None
        """
        if self.n_blocked_queens < 1:
            return None

        solver: Solver = MinConflictsSolver(self.n_queens, {})
        solution, _ = solver.solve()

        # Qua vengono eliminate le colonne "in eccesso" in maniera casuale
        while len(solution.keys()) > self.n_blocked_queens:
            queen_to_delete: int = random.randint(0, len(solution.keys()) - 1)
            solution.pop(list(solution.keys())[queen_to_delete])

        return solution

    def generate(self) -> Dict[int, int]:
        """
        Genera un assegnamento consistente di k=n_blocked_queens posizioni su una scacchiera NxN, dove N = n_queens, le
        cui chiavi sono ordinate in ordine "alfabetico" (se le regine bloccate sono Q2 e Q4, nelle chiavi del dizionario
        Q2 sarà prima di Q4), in modo che sia più facile la stampa.

        Returns:
            Un assegnamento consistente ordinato alfabeticamente. Se n_blocked_queens == 0, ritorna None
        """
        answer: Dict[int, int] = self._generate()
        sorted_answer: Dict[int, int] = {}

        if answer is not None:
            for column in sorted(answer.keys()):
                sorted_answer[column] = answer[column]

        return sorted_answer
