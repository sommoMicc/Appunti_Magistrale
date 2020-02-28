from json import JSONDecodeError

from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver
from csp.queens import CSPQueenSolver, ValuesSorter
from utils.generator import NQueensCompletionGenerator
import utils.config as config

from typing import Dict, Tuple, List, TextIO
from timeit import default_timer as timer

from matplotlib import pyplot as plt
import numpy as np
import json
from os import path

from utils.solution_printer import SolutionPrinter

solver_names: List[str] = ["Standard", "AC3", "AC3+FC", "AC3+FC+MRV", "AC3+FC+MRV+LCV", "Min-Conflicts"]
alternative_solver_names: List[str] = ["Default", "Random", "LCV"]


class Benchmark:
    def __init__(self, n: int, n_blocked: int):
        self.n = n
        self.n_blocked = n_blocked

    @staticmethod
    def run_test(solver: Solver, name) -> Tuple[int, float]:
        start_time: float = timer()
        solutions, iterations = solver.solve()
        if solutions is None:
            iterations = -1

        end_time: float = timer()
        elapsed_time: float = end_time - start_time

        print("- %s in %d iterazioni e %f secondi:" % (name, iterations, elapsed_time))
        # solver.print_solutions()

        return iterations, elapsed_time

    def compare(self, attempt_number: int = 3):
        solver_numbers: int = len(solver_names)

        avg_iterations, avg_times, max_times, min_times, fails_number = [0] * solver_numbers, [0] * solver_numbers, \
                                                                        [-1] * solver_numbers, \
                                                                        [-1] * solver_numbers, [-0] * solver_numbers

        for attempt in range(attempt_number):
            print("Tentativo #%d/%d" % (attempt + 1, attempt_number))
            blocked_queens: Dict[int, int] = NQueensCompletionGenerator(self.n, self.n_blocked).generate()

            solvers: List[Solver] = []
            standard_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                          False, False, False)
            solvers.append(standard_CSP)

            ac3_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                     True, False, False)
            solvers.append(ac3_CSP)
            ac3_fc_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                        True, True, False)
            solvers.append(ac3_fc_CSP)
            complete_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                          True, True, True)
            solvers.append(complete_CSP)
            complete_LCV_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.LEAST_CONSTRAINT,
                                                              True, True, True)
            solvers.append(complete_LCV_CSP)

            min_conflicts: MinConflictsSolver = MinConflictsSolver(self.n, blocked_queens)
            solvers.append(min_conflicts)

            for i in range(len(solvers)):
                iteration, time = self.run_test(solvers[i], "Solver %s" % solver_names[i])
                if iteration < 0:
                    fails_number[i] += 1
                    time = 61  # Faccio fallire

                avg_iterations[i] += iteration
                avg_times[i] += time

                if time > max_times[i]:
                    max_times[i] = time
                if time < min_times[i] or min_times[i] < 0:
                    min_times[i] = time

        avg_iterations, avg_times = list((x / attempt_number for x in avg_iterations)), \
                                    list((x / attempt_number for x in avg_times))

        return avg_times, min_times, max_times, fails_number

    def compare_values_sorter(self, attempt_number: int = 3):
        solver_numbers: int = len(alternative_solver_names)

        avg_iterations, avg_times, max_times, min_times, fails_number = [0] * solver_numbers, [0] * solver_numbers, \
                                                                        [-1] * solver_numbers, \
                                                                        [-1] * solver_numbers, [-0] * solver_numbers

        for attempt in range(attempt_number):
            print("Tentativo #%d/%d" % (attempt + 1, attempt_number))
            blocked_queens: Dict[int, int] = NQueensCompletionGenerator(self.n, self.n_blocked).generate()

            solvers: List[Solver] = []
            complete_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.DEFAULT,
                                                          True, True, True)
            solvers.append(complete_CSP)

            complete_random_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.RANDOM,
                                                                 True, True, True)
            solvers.append(complete_random_CSP)

            complete_LCV_CSP: CSPQueenSolver = CSPQueenSolver(self.n, blocked_queens, ValuesSorter.LEAST_CONSTRAINT,
                                                              True, True, True)
            solvers.append(complete_LCV_CSP)

            for i in range(len(solvers)):
                iteration, time = self.run_test(solvers[i], "Solver %s" % solver_names[i])
                if iteration < 0:
                    fails_number[i] += 1
                    time = 61  # Faccio fallire

                avg_iterations[i] += iteration
                avg_times[i] += time

                if time > max_times[i]:
                    max_times[i] = time
                if time < min_times[i] or min_times[i] < 0:
                    min_times[i] = time

        avg_iterations, avg_times = list((x / attempt_number for x in avg_iterations)), \
                                    list((x / attempt_number for x in avg_times))

        return avg_times, min_times, max_times, fails_number


def test(sizes: List[int] = None, granularity: int = 2, alternative:bool = False):
    """
    Svolge il test, i cui risultati sono riportati nella relazione.

    In pratica, sottomette alle 4 versioni di CSP e a Min-Conflicts lo stesso problema, variando n da 4 a 29, e k da 0
    (per ottenere la baseline) a 28
    Returns:

    """
    max_n: int = config.benchmark_max_n
    min_n: int = config.benchmark_min_n

    file_name: str = config.output_file
    if alternative:
        file_name = config.alternative_output_file

    if sizes is None:
        sizes = range(min_n, max_n + 1, 5)

    results_file = open(file_name, "r")
    try:
        output: Dict = json.load(results_file)
        print("Output: %r" % output)
    except JSONDecodeError:
        print("JSONDecodeError")
        output: Dict = {}

    results_file.close()
    print("%r" % output)

    for n in sizes:
        for k in range(0, n, granularity):
            if alternative:
                avg_times, min_times, max_times, fails = Benchmark(n, k)\
                                                                    .compare_values_sorter(config.benchmark_iterations)
            else:
                avg_times, min_times, max_times, fails = Benchmark(n, k).compare(config.benchmark_iterations)
            output["%d;%d" % (n, k)] = {
                "avg_times": avg_times,
                "min_times": min_times,
                "max_times": max_times,
                "fails": fails
            }

            results_file: TextIO = open(file_name, "w")
            print("(n=%d,k=%d): %r" % (n, k, output["%d;%d" % (n, k)]))
            json.dump(output, results_file)
            results_file.close()

    return output


def show_test_result():
    file_name: str = config.output_file
    file_content = json.load(open(file_name, "r"))

    parsed_result: Dict[int, Dict[int, object]] = {}
    parameter_translation: Dict[str, str] = {
        "fails": "Numero di fallimenti",
        "avg_times": "Tempo medio di esecuzione (s)",
        "max_times": "Tempo massimo di esecuzione (s)",
        "min_times": "Tempo minimo di esecuzione (s)"
    }

    for key in file_content.keys():
        n, k = [int(a) for a in key.split(";")]

        if n not in parsed_result.keys():
            parsed_result[int(n)] = {}

        parsed_result[n][k] = file_content[key]

    for n in parsed_result.keys():
        for parameter_considered in ["fails", "avg_times", "max_times", "min_times"]:
            y = []
            for i in range(len(solver_names)):
                y.append([])

            x: List[int] = []
            max_value: float = -1

            plt.figure()  # reset del grafico

            for k in parsed_result[n].keys():
                x.append(k)
                for i in range(len(parsed_result[n][k][parameter_considered])):
                    if parameter_considered != "fails":
                        if parsed_result[n][k][parameter_considered][i] >= config.timeout or \
                                parsed_result[n][k][parameter_considered][i] <= 0.0:
                            parsed_result[n][k][parameter_considered][i] = config.timeout

                    y[i].append(parsed_result[n][k][parameter_considered][i])

                    if parsed_result[n][k][parameter_considered][i] > max_value:
                        max_value = parsed_result[n][k][parameter_considered][i]
                    # x_size += 1
            # print("n: %d, max_value: %f, parameter: %s" % (n, max_value, parameter_considered))
            for solver_index in range(len(y)):
                plt.plot(x, y[solver_index], label=solver_names[solver_index])
                plt.xlabel("Numero di regine bloccate (k)")
                plt.ylabel(parameter_translation[parameter_considered])

            if "time" in parameter_considered:
                if max_value > 10:
                    plt.axhline(y=config.timeout, linestyle=':')
            else:
                plt.axhline(y=config.benchmark_iterations, linestyle=':')

            plt.xticks(x, x)
            plt.grid(True)

            plt.title("%d-Queens Completion, %s" % (n, parameter_translation[parameter_considered]))
            plt.legend()
            plt.savefig("%s/%d_queens_%s.png" % (config.plot_folder, n, parameter_considered))
            plt.close()


if __name__ == "__main__":
    if not path.exists(config.output_file):
        test([29], alternative=True)

    show_test_result()
