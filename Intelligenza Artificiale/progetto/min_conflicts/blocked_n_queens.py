import random
from typing import Generic, TypeVar, Dict, List, Optional, Tuple

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class BlockedNQueens:
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        self.blocked_queens: Dict[V, D] = blocked_queens
        self.n = n
        self.board, self.queenPositions = self.get_new_board(n, blocked_queens)

    def shuffle(self):
        self.board, self.queenPositions = self.get_new_board(self.n, self.blocked_queens)

    def get_new_board(self, n: int, blocked_queens: Dict[V, D]) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
        # queens are represented as ones in 2d list of all zeros
        # Since it's a 2d list, each element is a row of zeros except for the queen
        board: List[List[int]] = []
        queens_pos: List[Tuple[int, int]] = []
        for x in range(n):  # makes n x n board of zeros
            board.append([0] * n)

        for column in blocked_queens.keys():
            row = blocked_queens[column]
            board[row][column] = 1
            queens_pos.append((row, column))

        column: int = 0
        while column < n:
            if not self.column_clear(board, column):
                column = column + 1
                continue

            random_row: int = random.randint(0, n - 1)

            board[random_row][column] = 1
            queens_pos.append((random_row, column))

            column = column + 1
        return board, queens_pos

    def column_clear(self, board: List[List[int]], column: int) -> bool:
        for row in range(self.n):
            if board[row][column] == 1:
                return False
        return True

    def queen_is_blocked(self, row: int, column: int):
        if column not in self.blocked_queens.keys():
            # Non c'è nessuna regina bloccata in questa colonna
            return False

        return self.blocked_queens[column] == row

    def all_queens_safe(self):  # returns true if problem is solved and all queens safe, false otherwise
        for pos in self.queenPositions:
            if self.under_attack(pos):
                return False
        return True

    def attack_via_col(self, pos):
        for queen in self.queenPositions:
            if pos[1] == queen[
                1] and queen != pos:  # last inqueality checks to make sure you arent comparing the same queen
                return True
        return False

    def attack_via_row(self, pos):
        for queen in self.queenPositions:
            if (pos[0] == queen[0] and queen != pos):
                return True
        return False

    def attack_via_diagonal(self, pos):
        for queen in self.queenPositions:
            if abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos:
                return True
        return False

    def under_attack(self, position):
        return self.attack_via_diagonal(position) or self.attack_via_row(position) or self.attack_via_col(position)

    def queen_number_conflicts(self, pos):  # returns number of pieces attacking queen at position pos
        assert pos in self.queenPositions  # checks to make sure given position is a queen
        count = 0
        for queen in self.queenPositions:
            if abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos:
                count += 1

            if pos[0] == queen[0] and queen != pos:
                count += 1

            if pos[1] == queen[1] and queen != pos:
                count += 1

        return count

    def print_conflict_board(self):
        from prettytable import PrettyTable, ALL
        pretty_table = PrettyTable(header=False, hrules=ALL)

        grid: Dict[int, List[str]] = {}
        for i in range(self.n):
            grid[i] = []
            for j in range(self.n):
                grid[i].append("  ")

        for row, column in self.queenPositions:
            grid[row][column] = "Q: %d" % self.queen_number_conflicts((row,column))
            # i,y = solution[queen]
            # grid[i,j] = "%d" % queen

        for row in grid:
            pretty_table.add_row(grid[row])

        print(pretty_table)

    def pick_random_queen(self, source="ASD"):  # returns position of random queen
        random.shuffle(self.queenPositions)
        for i in range(len(self.queenPositions)):
            row, column = self.queenPositions[i]
            if not self.queen_is_blocked(row, column) or True:
                return row, column

        return None

    def get_solution(self) -> Dict[int, int]:  # prints out all positions of queens
        solution: Dict[int, int] = {}
        for queen in self.queenPositions:
            row, column = queen
            solution[column] = row
        return solution

    def move_queen(self, start_pos, end_pos):  # moves queen from startpos to end_pos
        assert self.board[start_pos[0]][start_pos[1]] == 1
        # above assert will fail if the start position does not have a queen
        self.board[start_pos[0]][start_pos[1]] = 0
        self.board[end_pos[0]][end_pos[1]] = 1
        self.queenPositions.remove(start_pos)
        self.queenPositions.append(end_pos)

    def available_positions(self, pos):
        # returns list of tuples with all positions queen can go
        available_pos = []
        for x in range(self.n):
            if x != pos[0] and (x, pos[1]) not in self.queenPositions:
                available_pos.append((x, pos[1]))

        return available_pos
