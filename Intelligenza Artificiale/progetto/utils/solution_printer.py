from typing import Dict, List
from prettytable import PrettyTable, ALL


class SolutionPrinter:
    """
    Classe che incapsula il metodo per stampare a console una scacchiera con delle regine posizionate
    """
    @staticmethod
    def print_solutions(n: int, queens_coord: Dict[int, int]):
        """
        Stampa la configurazione di regine definita in "queens_coord" su una scacchiera n x n
        Args:
            n: la dimensione della scacchiera
            queens_coord: le coordinate delle regine, indicizzate per colonna

        Returns:
            Void
        """
        pretty_table = PrettyTable(header=False, hrules=ALL)

        grid: Dict[int, List[str]] = {}
        for i in range(n):
            grid[i] = []
            for j in range(n):
                grid[i].append("  ")

        for column in queens_coord.keys():
            row: int = queens_coord[column]

            grid[row][column] = "Q%d" % column
            # i,y = solution[queen]
            # grid[i,j] = "%d" % queen

        for row in grid:
            pretty_table.add_row(grid[row])

        print(pretty_table)
