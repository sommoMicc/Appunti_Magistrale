from base.solver import Solver
import random
from typing import List, Dict, Optional, Tuple


class MinConflictsSolver2(Solver):
    def __init__(self, n: int, blocked_queens: Dict[int, int]):
        super().__init__(n, blocked_queens)
        random.seed(10)

        self.rows: Dict[int, int] = {}
        self.randomize()

    def randomize(self):
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
                new_column: int = random.randint(0, self.n - 1)
                self.rows[column], self.rows[new_column] = self.rows[new_column], self.rows[column]

    def conflicts(self, row: int, column: int) -> int:
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
        movements: int = 0
        candidates: List[int] = []

        solution_found: bool = False
        while not solution_found:
            max_conflicts: int = 0
            candidates.clear()

            # Cerco la regina avente il massimo numero di conflitti
            # Per identificare la regina uso la sua colonna
            for column in range(self.n):
                conflicts: int = self.conflicts(self.rows[column], column)
                if conflicts == max_conflicts:
                    candidates.append(column)

                elif conflicts > max_conflicts:
                    max_conflicts = conflicts
                    candidates.clear()
                    candidates.append(column)

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
        return self._print_solutions(self.n, self.rows)
