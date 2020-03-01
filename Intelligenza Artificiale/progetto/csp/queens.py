from base.solver import Solver
from csp.csp import Constraint, VariableValuesSorter, CSP

from typing import Dict, List, Optional, TypeVar, Tuple

import random
from enum import Enum

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class QueensConstraint(Constraint[int, int]):
    """
    Classe che rappresenta un vincolo di una regina libera.
    """

    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        """
        Verifica che le regine presenti in "assignment" non siano nella stessa riga, colonna o diagonale
        Args:
            assignment: un assegnamento di variabili/regine

        Returns:
            True se l'assegnamento è consistente
        """
        for queen1_col, queen1_row in assignment.items():
            for queen2_col in range(queen1_col + 1, len(self.columns) + 1):
                if queen2_col in assignment:
                    queen2_row: int = assignment[queen2_col]
                    if queen1_row == queen2_row:  # le regine si trovano sulla stessa riga
                        return False
                    if abs(queen1_row - queen2_row) == abs(queen1_col - queen2_col):  # le regine si trovano
                        # sulla stessa diagonale
                        return False
        return True  # no conflict


class BlockedQueensConstraint(Constraint[int, int]):
    def __init__(self, positions: Dict[int, int]) -> None:
        super().__init__(list(positions.keys()))
        self.positions = positions

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for queen in self.positions.keys():
            if queen in assignment.keys() and assignment[queen] != self.positions[queen]:
                return False
        return True


class DefaultConstraintValueSorter(VariableValuesSorter):
    """
    Classe che implementa l'ordinamento di default dei valori delle variabili. In pratica, non fa nessun cambiamento
    all'ordine dei loro domini (mantiene l'ordinamento statico/predefinito)
    """

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]) -> D:
        """
        Ritorna semplicemente il dominio della variabile "variable", senza svolgere altre operazioni.
        Args:
            variable: la variabile di cui si vuole ordinare il dominio
            domains: dizionario contenente i domini di tutte le variabili
            assignment: l'assegnamento corrente

        Returns:
            il dominio della variabile "variable" senza modificarne l'ordine
        """
        return domains[variable]


class RandomConstraintValueSorter(VariableValuesSorter):
    """
    Classe che implementa l'ordinamento casuale dei valori del dominio di una variabile.
    """

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]) -> D:
        """
        Scombina l'ordine dei valori del dominio della variabile "variable"
        Args:
            variable: la variabile/regina di cui si vuole scombinare il dominio
            domains: dizionario contenente i domini di tutte le variabili
            assignment: l'assegnamento corrente

        Returns:
            Il dominio della variabile "variable" scombinato
        """
        random.shuffle(domains[variable])
        return domains[variable]


class LeastConstraintValueSorter(VariableValuesSorter):
    """
    Classe che implementa l'euristica LCV per l'ordinamento dei valori del dominio di una variabile.
    """

    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]) -> D:
        """
        Ordina gli elementi del dominio di "variable" in base al numero di conflitti: valori che portano ad un numero
        di conflitti minore verranno posizionati prima di quelli che portano ad un numero di conflitti più alto (è il
        contrario di quello che fa min_conflicts)

        Args:
            variable: la variabile di cui si vogliono ordinare i valori del dominio
            domains: dizionario dei domini di tutte le variabili
            assignment: l'assegnamento corrente

        Returns:
            Il dominio del parametro "variable" ordinato in modo LCV
        """

        domain: D = domains[variable]
        domain.sort(key=lambda row: LeastConstraintValueSorter.number_of_conflicts(variable, row, assignment))
        return domain

    @staticmethod
    def number_of_conflicts(queen_column: V, queen_row: D, assignment: Dict[V, D]) -> int:
        """
        Calcola il numero di conflitti che si avrebbero nell'assegnamento "assignment" se alla variabile "queen_column"
        venisse assegnato il valore "queen_row"

        Args:
            queen_column: colonna della regina considerata
            queen_row: riga che si vorrebbe assegnare alla regina considerata
            assignment: l'assegnamento corrente

        Returns:
            Numero di conflitti che si avrebbero se alla regina avente colonna "queen_column" venisse assegnata la riga
            "queen_row"
        """
        conflicts: int = 0

        for other_queen_column in assignment:
            other_queen_row: D = assignment[other_queen_column]
            if other_queen_row == queen_row or abs(queen_row - other_queen_row) == abs(
                    queen_column - other_queen_column):
                conflicts += 1

        return conflicts


class ValuesSorter(Enum):
    """
    Enumerazione che serve a rendere configurabile più facilmente il tipo di ordinamento dei valori dei domini che si
    vuole utilizzare
    """
    DEFAULT = 1
    RANDOM = 2
    LEAST_CONSTRAINT = 3


class CSPQueenSolver(Solver):
    """
    Solver per il problema N-Queens Completion che utilizza l'algoritmo di Backtracking.
    """

    def print_solutions(self):
        """
        Stampa la scacchiera contenente la soluzione
        Returns:
            Void
        """
        return CSPQueenSolver._print_solutions(self.n, self.solution)

    def __init__(self, n: int, blocked_queens: Dict[V, D], value_sorter: ValuesSorter = ValuesSorter.DEFAULT,
                 use_ac3: bool = True, use_fc: bool = True, use_mrv: bool = True):
        """
        Costruttore
        Args:
            n: la dimensione (lato) della scacchiera
            blocked_queens: dizionario contenente la posizione delle regine bloccate. Ad esempio, se blocked_queens = {
                1: 3}, la regina della seconda colonna sarà bloccata sulla quarta riga.
            value_sorter: valore dell'enumerazione "ValuesSorter" che permette di scegliere quale criterio utilizzare
                per l'ordinamento dei valori del dominio di una variabile
            use_ac3: True se si vuole usare AC-3 per la constraint propagation PRIMA dell'esecuzione di Backtracking
            use_fc: True se si vuole usare Forward Checking DURANTE l'esecuzione di Backtracking per la constraint
                propagation
            use_mrv: True se si vuole usare l'euristica Minimum Remaining Values per la selezione della variabile da
                assegnare. Se False, le variabili vengono estratte in ordine numerico (prima 1, poi 2, poi 3 ecc..)
        """
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
        """
        Prova a risolvere il problema.
        Returns:
            Una tupla formata da:
            - Un dizionario, che associa ad ogni regina (colonna) una riga.
            - Un intero, che rappresenta il numero di passi svolti dall'algoritmo.

            In caso non sia stato possibile arrivare ad una soluzione (anche a causa del timeout),
             il metodo ritorna una tupla avente "None" come primo parametro e -1 come secondo parametro.
        """
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
