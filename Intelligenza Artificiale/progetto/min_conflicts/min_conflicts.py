from base.solver import Solver
import utils.config as config
import random
from typing import List, Dict, Optional, Tuple
from timeit import default_timer as timer


class MinConflictsSolver(Solver):
    """
    La classe rappersenta l'impelentazione dell'algoritmo di Min-Conflicts al problema N-Queens Completion
    """
    def __init__(self, n: int, blocked_queens: Dict[int, int]):
        """
        Costruisce una scacchiera n x n con delle regine bloccate coerentemente con quanto definito dal parametro
        "blocked_queens"

        Args:
            n: dimensione della scacchiera
            blocked_queens: mappa delle regine bloccate, dove la chiave rappresenta la colonna, il valore la riga. Ad
                            esempio, blocked_queens[3] = 2 indica che nella quarta colonna c'è una regina bloccata
                            posizionata sulla terza riga.
        """
        super().__init__(n, blocked_queens)

        self.rows: Dict[int, int] = {}

        self.start_time: float = -1

        self.randomize()

    def randomize(self):
        """
        Genera uno stato inziale pseudo casuale: le regine libere vengono posizionate una per colonna e riga, mentre
        alle regine bloccate viene assegnata la loro posizione staticamente definita.

        Returns:
            Void
        """
        # Posiziono le regine libere sulla diagonale della scacchiera
        # mentre quelle bloccate sulle loro posizioni
        for i in range(self.n):
            if i in self.blocked_queens.keys():
                self.rows[i] = self.blocked_queens[i]
            else:
                self.rows[i] = i

        # Mescolo le righe in cui si trovano le regine
        for column in range(len(self.rows)):
            # Ovviamente non modifico le righe delle regine bloccate
            if column not in self.blocked_queens.keys():
                # Scelgo una colonna a caso che non sia assegnata ad una regina bloccata
                new_column: int = random.choice([x for x in range(self.n) if x not in self.blocked_queens.keys()])
                self.rows[column], self.rows[new_column] = self.rows[new_column], self.rows[column]

    def conflicts(self, row: int, column: int) -> int:
        """
        Calcola il numero di conflitti a cui una regina in posizione (row, column) è soggetta
        Args:
            row: la riga (coordinata)
            column: la colonna (coordinata)

        Returns:
            numero di conflitti della regina in posizione (row, column)
        """

        n_conflicts: int = 0
        for current_column in range(self.n):
            if current_column == column:
                continue
            current_row: int = self.rows[current_column]
            if current_row == row or abs(current_row - row) == abs(current_column - column):
                # se due regine aventi la stessa colonna hanno la stessa riga o stessa diagonale
                n_conflicts += 1

        return n_conflicts

    def solve(self) -> Tuple[Optional[Dict[int, int]], int]:
        """
        Risolve il problema.

        Returns:
            Una tupla formata da un dizionario, che è la disposizione delle regine (la chiave rappresenta la colonna),
            e un intero, che rappresenta il numero di passi svolto dall'algoritmo.
        """
        self.start_time = timer()
        movements: int = 0
        candidates: List[int] = []

        solution_found: bool = False
        while not solution_found:
            if timer() - self.start_time > config.timeout:
                return None, -1

            max_conflicts: int = 0
            candidates.clear()

            # Cerco la regina avente il massimo numero di conflitti
            # Per identificare la regina uso la sua colonna
            for column in range(self.n):
                # Se la colonna è di una regina bloccata, non la considero
                if column in self.blocked_queens.keys():
                    continue

                conflicts: int = self.conflicts(self.rows[column], column)
                if conflicts == max_conflicts:
                    candidates.append(column)

                elif conflicts > max_conflicts:
                    max_conflicts = conflicts
                    candidates.clear()
                    candidates.append(column)

            # print("MAX CONFLICTS %d, CANDIDATES: %r" % (max_conflicts, candidates))
            # Se non ho più conflitti, ho trovato la soluzione
            if max_conflicts == 0:
                solution_found = True
                continue

            # Prendo una regina a caso tra quelle che hanno il numero maggiore di conflitti
            worst_queen_column = candidates[random.randint(0, len(candidates) - 1)]

            # Cerco la posizione con il numero minore di conflitti
            min_conflicts_number: int = self.n
            candidates.clear()

            # Per farlo, itero su tutte le righe, perché la regina la sposterò solo da riga a riga, mantenendo la
            # colonna (perché sono già una regina per colonna)
            for current_row in range(self.n):
                current_conflicts: int = self.conflicts(current_row, worst_queen_column)
                if current_conflicts == min_conflicts_number:
                    # Ho trovato una delle posizioni che minimizzano i conflitti
                    candidates.append(current_row)

                elif current_conflicts < min_conflicts_number:
                    # Ho trovato una posizione migliore delle precedenti (contenute in candidates)
                    min_conflicts_number = current_conflicts
                    candidates.clear()
                    candidates.append(current_row)

            if len(candidates) > 0:
                self.rows[worst_queen_column] = candidates[random.randint(0, len(candidates) - 1)]

            movements += 1

            # Random reboot
            if movements % (self.n * 2) == 0:
                self.randomize()

        return self.rows, movements

    def print_solutions(self):
        """
        Metodo che stampa la scacchiera con le soluzioni

        Returns:
            Void
        """
        return self._print_solutions(self.n, self.rows)
