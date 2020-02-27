from json import JSONDecodeError

from base.solver import Solver
from min_conflicts.min_conflicts import MinConflictsSolver
from csp.queens import CSPQueenSolver, ValuesSorter
from utils.generator import NQueensCompletionGenerator
import utils.config as config

from typing import Dict, Tuple, List
from timeit import default_timer as timer

from matplotlib import pyplot as plt
import numpy as np
import json
from os import path

from utils.solution_printer import SolutionPrinter

solver_names: List[str] = ["Standard", "AC3", "AC3+FC", "AC3+FC+MRV", "AC3+FC+MRV+LCV", "Min-Conflicts"]


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


def test(sizes: List[int] = None, granularity: int = 2):
    """
    Svolge il test, i cui risultati sono riportati nella relazione.

    In pratica, sottomette alle 4 versioni di CSP e a Min-Conflicts lo stesso problema, variando n da 4 a 29, e k da 0
    (per ottenere la baseline) a 28
    Returns:

    """
    max_n: int = config.benchmark_max_n
    min_n: int = config.benchmark_min_n

    if sizes is None:
        sizes = range(min_n, max_n + 1, 5)

    results_file = open(config.output_file, "r")
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
            avg_times, min_times, max_times, fails = Benchmark(n, k).compare(config.benchmark_iterations)
            output["%d;%d" % (n, k)] = {
                "avg_times": avg_times,
                "min_times": min_times,
                "max_times": max_times,
                "fails": fails
            }
            results_file = open(config.output_file, "w")
            print("(n=%d,k=%d): %r" % (n, k, output["%d;%d" % (n, k)]))
            json.dump(output, results_file)
            results_file.close()

    return output


def show_test_result():
    file_name: str = config.output_file
    file_content = json.load(open(file_name, "r"))

    parsed_result: Dict[int, Dict[int, object]] = {}

    for key in file_content.keys():
        n, k = [int(a) for a in key.split(";")]

        if n not in parsed_result.keys():
            parsed_result[int(n)] = {}

        parsed_result[n][k] = file_content[key]

    for n in parsed_result.keys():
        """
        tot_iterations = config.benchmark_iterations
        parameter_to_normalize: List[str] = ["max_times", "avg_times"]
        for parameter in parameter_to_normalize:
            for k in parsed_result[n].keys():
                for solver in range(len(solver_names)):
                    old_value = parsed_result[n][k][parameter][solver]
                    n_fails: int = parsed_result[n][k]["fails"][solver]
                    if n_fails > 0:
                        time_to_add = n_fails * config.timeout
                        old_weight = tot_iterations - n_fails
                        parsed_result[n][k][parameter][solver] = (old_value * old_weight + time_to_add) / tot_iterations
        """
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
                            parsed_result[n][k][parameter_considered][i] = np.nan

                    y[i].append(parsed_result[n][k][parameter_considered][i])

                    if parsed_result[n][k][parameter_considered][i] > max_value:
                        max_value = parsed_result[n][k][parameter_considered][i]
                    # x_size += 1
            print("n: %d, max_value: %f, parameter: %s" % (n, max_value, parameter_considered))
            for solver_index in range(len(y)):
                plt.plot(x, y[solver_index], label=solver_names[solver_index])
                plt.xlabel("# of blocked queens (k)")
                plt.ylabel(parameter_considered.capitalize())

            if "time" in parameter_considered:
                if max_value > 10:
                    plt.axhline(y=config.timeout, linestyle=':')
            else:
                plt.axhline(y=config.benchmark_iterations, linestyle=':')

            plt.xticks(x, x)
            plt.grid(True)

            plt.title("%d-Queens, %s" % (n, parameter_considered))
            plt.legend()
            plt.savefig("%s/%d_queens_%s.png" % (config.plot_folder, n, parameter_considered))
            plt.close()


if __name__ == "__main__":
    if not path.exists(config.output_file):
        test()

    show_test_result()
