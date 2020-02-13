from typing import Generic, TypeVar, Dict, List, Optional, Tuple
from abc import ABC, abstractmethod

import copy

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]], ac3: bool = True, forward_checking: bool = True) -> None:
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        self.attempts: int = 0  # numero di tentativi di assegnazione

        self.use_ac3: bool = ac3
        self.use_forward_checking: bool = forward_checking

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking(self) -> Tuple[Optional[Dict[V, D]], int]:
        domains: Dict[V, List[D]] = self.domains
        if self.use_ac3:
            domains = self.ac3(self.domains)

        return self.backtracking_search({}, domains)

    def backtracking_search(self, assignment=None,
                            domains: Dict[V, List[D]] = None) -> Tuple[Optional[Dict[V, D]], int]:

        # assignment is complete if every variable is assigned (our base case)
        if assignment is None:
            assignment = {}

        if len(assignment) == len(self.variables):
            return assignment, 0

        if domains is None:
            return None, 0

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # euristica MRV (ordino in base al numero di elementi del dominio, in ordine crescente)
        # questo significa che veranno assegnati prima i valori delle regine "bloccate"
        unassigned.sort(key=lambda v: len(domains[v]))

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        current_iterations = 0
        for value in domains[first]:
            current_iterations = current_iterations + 1
            local_assignment = assignment.copy()
            local_assignment[first] = value

            self.attempts = self.attempts + 1

            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                # Forward checking
                inferred_domain: Dict[V, List[D]] = domains
                if self.use_forward_checking:
                    inferred_domain = self.forward_checking(domains, first, value)

                if inferred_domain is not None:
                    result, iterations = self.backtracking_search(local_assignment,
                                                                  inferred_domain)

                    current_iterations = current_iterations + iterations
                    # if we didn't find the result, we will end up backtracking
                    if result is not None:
                        return result, current_iterations
        return None, current_iterations

    # Rimuove dal dominio di tutte le variabili il valore che è appena stato assegnato ad
    # una variabile
    @staticmethod
    def forward_checking(old_domains: Dict[V, List[D]], variable: V, value: int) -> Optional[Dict[V, D]]:
        domains: Dict[V, D] = copy.deepcopy(old_domains)
        keys: List[V] = list(domains.keys())

        keys.sort(key=lambda v: len(domains[v]))

        for key in keys:
            if key != variable and value in domains[key]:
                domains[key].remove(value)

            # Una variabile ha il proprio dominio vuoto, quindi non sarà mai assegnabile
            if len(domains[key]) < 1:
                return None
        return domains

    def remove_inconsistent(self, domains: Dict[V, List[D]], x1: V, x2: V):
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

    def ac3(self, domains: Dict[V, List[D]]) -> Optional[Dict[V, List[D]]]:
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
            x1, x2 = queue.pop()
            if x1 == x2:
                continue

            if self.remove_inconsistent(domains, x1, x2):
                if len(domains[x1]) == 0:
                    return None

                for var in self.variables:
                    if var != x1:
                        # print("Appendo (%d, %d) alla coda" % (var, x1))
                        queue.append((var, x1))

        return domains
