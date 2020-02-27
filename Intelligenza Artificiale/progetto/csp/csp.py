from typing import Generic, TypeVar, Dict, List, Optional, Tuple
from abc import ABC, abstractmethod
from timeit import default_timer as timer
import utils.config as config
import copy

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class Constraint(Generic[V, D], ABC):
    """
    Classe base per tutti vincoli
    """

    def __init__(self, variables: List[V]) -> None:
        """
        Costruttore
        Args:
            variables: le variabili che il vincolo deve considerare
        """
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        """
        Verifica se l'assegnamento passato come parametro è consistente
        Args:
            assignment: un assegnamento di variabili

        Returns:
            True se l'assegnamento è consistente, False altrimenti
        """
        ...


class VariableValuesSorter(Generic[V, D], ABC):
    """
    Classe che implementa la politica di ordinamento dei valori di una variabile
    """

    @abstractmethod
    def sort_variable_values(self, variable: V, domains: Dict[V, D], assignment: Dict[V, D]):
        """
        Ordina in-place i valori di "variable" presenti in "domain", tenendo conto (se necessario) dell'assegnamento
        delle altre variabili.
        Args:
            variable: la variabile di cui ordinare i valori del dominio
            domains: i domini di tutte le variabili del problema
            assignment: l'assegnamento corrente

        Returns:
            Void, perché l'ordinamento avviene in-place
        """
        ...


class CSP(Generic[V, D]):
    """
    Definisce la struttura di un CSP. Esso consiste in variabili di tipo V che possono assumere una serie di valori di
    tipo D (dominio), i quali però devono soddisfare dei vincoli
    """

    def __init__(self, variables: List[V], domains: Dict[V, List[D]], variable_val_sorter: VariableValuesSorter,
                 ac3: bool = True, fc: bool = True, mrv: bool = True) -> None:
        """
        Costruttore della classe
        Args:
            variables: lista di tutte le variabili del problema
            domains: dizionario che associa ad ogni variabile una lista di possibili valori che essa potrebbe assumere
            variable_val_sorter: la politica di ordinamento dei valori delle variabili quando esse vengono selezionate
                                 per l'assegnazione
            ac3: True se si vuole usare AC-3 per la consistenza locale prima della ricerca
            fc: True se si vuole usare il Forward Checking come metodo di inferenza
            mrv: True se si vogliono estrarre le variabili secondo una politica Minimum Remaining Values (fail first).
                In caso sia impostato a False, le variabili vengono estratte nell'ordine in cui compaiono dentro
                la lista "variabiles"
        """
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        self.attempts: int = 0  # numero di tentativi di assegnazione

        self.use_ac3: bool = ac3
        self.use_forward_checking: bool = fc
        self.use_mrv: bool = mrv

        self.variable_val_sorter: VariableValuesSorter = variable_val_sorter
        self.start_time: float = -1

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]):
        """
        Aggiunge un vincolo al problema
        Args:
            constraint: il vincolo che si vuole aggiungere

        Returns:
            Void
        """
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        """
        Controlla se un assegnamento è consistente controllando se tutti i vincoli associati alla variabile di input
        sono soddisfatti
        Args:
            variable: la variabile di cui si vogliono controllare i vincoli
            assignment: l'assegnamento di input

        Returns:
            True se l'assegnamento è consistente per la variabile di input, ovvero se non viola nessun vincolo in cui
            essa è coinvolta
        """
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking(self) -> Tuple[Optional[Dict[V, D]], int]:
        """
        Inizializza la ricerca con Backtracking
        Returns:
            una soluzione, se è stata trovata. None altrimenti.
        """
        self.start_time = timer()

        domains: Dict[V, List[D]] = self.domains
        if self.use_ac3:
            domains = self._ac3(self.domains)

        return self._backtracking_search({}, domains)

    def _backtracking_search(self, assignment=None,
                             domains: Dict[V, List[D]] = None) -> Tuple[Optional[Dict[V, D]], int]:
        """
        Definisce un passo ricorsivo della ricerca con Backtracking.
        Args:
            assignment: l'assegnamento corrente
            domains: i domini ("sfoltiti", se è stato usato AC-3 o Forward Chaining) delle variabili del problema

        Returns:
            una soluzione che completa l'assegnamento passato come parametro, se esiste.
        """
        # Controllo sul timeout
        if timer() - self.start_time > config.timeout:
            return None, -1

        if assignment is None:
            assignment = {}

        # l'assegnamento è completo se è presente in esso ogni variabile (caso base)
        if len(assignment) == len(self.variables):
            return assignment, 0

        # se le variabili non hanno valori che possono assumere, è inutile proseguire con la ricerca
        if domains is None:
            return None, -1

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # euristica MRV (ordino in base al numero di elementi del dominio, in ordine crescente)
        # questo significa che veranno assegnati prima i valori delle regine "bloccate"
        if self.use_mrv:
            CSP._minimum_remaining_values(unassigned, domains)
        # unassigned.sort(key=lambda v: len(domains[v]))

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        current_iterations = 0
        for value in self.variable_val_sorter.sort_variable_values(first, domains, assignment):
            current_iterations = current_iterations + 1

            # Controllo sul timeout
            if timer() - self.start_time > config.timeout:
                return None, -1

            local_assignment = assignment.copy()
            local_assignment[first] = value

            self.attempts = self.attempts + 1

            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                # Forward checking
                inferred_domain: Dict[V, List[D]] = domains
                if self.use_forward_checking:
                    inferred_domain = self._forward_checking(domains, first, value)

                if inferred_domain is not None:
                    result, iterations = self._backtracking_search(local_assignment,
                                                                   inferred_domain)

                    current_iterations = current_iterations + iterations
                    # if we didn't find the result, we will end up backtracking
                    if result is not None:
                        return result, current_iterations
        return None, current_iterations

    @staticmethod
    def _minimum_remaining_values(variables: List[V], domains: Dict[V, D]):
        """
        Euristica MRV (minimum remaining values): ordine cresente basato sul numero di valori rimanenti nel dominio

        Nota: l'ordinamento avviene in-place (side effect)!
        :param variables:
        :param domains:
        :return:
        """
        variables.sort(key=lambda v: len(domains[v]))

    @staticmethod
    def _forward_checking(old_domains: Dict[V, List[D]], variable: V, value: D) -> Optional[Dict[V, D]]:
        """
        Implementa l'algoritmo di Forward Checking per fare inferenza ad ogni passo di Backtracking
        Args:
            old_domains: i domini correnti delle variabili
            variable: la variabile che si vuole assegnare
            value: il valore che si vuole dare a quella variabile

        Returns:
            una versione "ridotta" del dominio, oppure None se è presente una variabile a cui non sono rimasti
            assegnamenti possibili.
        """

        domains: Dict[V, D] = copy.deepcopy(old_domains)
        keys: List[V] = list(domains.keys())

        CSP._minimum_remaining_values(keys, domains)

        for key in keys:
            if key != variable and value in domains[key]:
                domains[key].remove(value)

            # Una variabile ha il proprio dominio vuoto, quindi non sarà mai assegnabile
            if len(domains[key]) < 1:
                return None
        return domains

    def _remove_inconsistent(self, domains: Dict[V, List[D]], x1: V, x2: V) -> bool:
        """
        Parte dell'algoritmo AC-3. Rimuove i valori inconsistenti ????
        Args:
            domains:
            x1:
            x2:

        Returns:

        """
        removed: bool = False
        assignment: Dict[V, D] = {}

        # print("Rimuovo inconsistenti tra x1: %d e x2: %d" % (x1, x2))

        for value1 in domains[x1]:
            assignment[x1] = value1

            is_valid: bool = False
            for value2 in domains[x2]:
                assignment[x2] = value2
                # print("Controllo consistenza di %r e %d" % (assignment, x2))
                if self.consistent(x2, assignment):
                    is_valid = True
                    break
            if not is_valid:
                # print("Rimuovo %d dal dominio di Q%d" % (value1, x1))
                domains[x1].remove(value1)
                removed = True

        return removed

    def _ac3(self, domains: Dict[V, List[D]]) -> Optional[Dict[V, List[D]]]:
        """
        Algoritmo di AC-3 per la consistenza locale
        Args:
            domains: I domini di ogni variabile

        Returns:
            una versione "scremata" dei domini passati come input, oppure None se almeno una variabile non ha valori
            ammissibili.
        """
        queue: List[Tuple[V, V]] = []
        n_queens = len(self.variables)

        for i in range(n_queens):
            for j in range(n_queens):
                if i == j:
                    continue

                queue.append((self.variables[i], self.variables[j]))

        queue.reverse()
        # print("Queue: \n%r" % queue)

        while queue:
            # Controllo sul timeout
            if timer() - self.start_time > config.timeout:
                return None

            x1, x2 = queue.pop()
            if x1 == x2:
                continue

            if self._remove_inconsistent(domains, x1, x2):
                if len(domains[x1]) == 0:
                    return None

                for var in self.variables:
                    if var != x1:
                        # print("Appendo (%d, %d) alla coda" % (var, x1))
                        queue.append((var, x1))

        return domains
