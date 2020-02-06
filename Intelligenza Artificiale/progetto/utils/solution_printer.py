from typing import Dict, List
from prettytable import PrettyTable, ALL


class SolutionPrinter:
    @staticmethod
    def print_solutions(n: int, queens_coord: Dict[int, int]):
        pretty_table = PrettyTable(header=False, hrules=ALL)

        grid: Dict[int, List[str]] = {}
        for i in range(n):
            grid[i] = []
            for j in range(n):
                grid[i].append("")

        for row in queens_coord.keys():
            column: int = queens_coord[row]

            grid[row][column] = "Q%d" % column
            # i,y = solution[queen]
            # grid[i,j] = "%d" % queen

        for row in grid:
            pretty_table.add_row(grid[row])

        print(pretty_table)
