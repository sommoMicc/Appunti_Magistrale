import random
from typing import Generic, TypeVar, Dict, List, Optional, Tuple

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class BlockedNQueens:
    def __init__(self, n: int, blocked_queens: Dict[V, D]):
        self.blocked_queens: Dict[V, D] = blocked_queens
        self.board, self.queenPositions = self.get_new_board(n, blocked_queens)
        self.n = n

    @staticmethod
    def get_new_board(n: int, blocked_queens: Dict[V, D]) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
        # queens are represented as ones in 2d list of all zeros
        # Since it's a 2d list, each element is a row of zeros except for the queen
        board: List[List[int]] = []
        queens_pos: List[Tuple[int, int]] = []
        for x in range(n):  # makes n x n board of zeros
            board.append([0] * n)

        blocked_queens_number: int = len(blocked_queens.keys())
        for column in blocked_queens.keys():
            row = blocked_queens[column]
            board[row][column] = 1
            queens_pos.append((row, column))

        for x in range(n - blocked_queens_number):  # sets a random value of each row to be 1, denoting the queen
            random_column: int = random.randint(0, n - 1)
            while board[x][random_column] == 1:  # La posizione potrebbe essere già occupata da una regina bloccata
                random_column: int = random.randint(0, n - 1)

            board[x][random_column] = 1
            queens_pos.append((x, random_column))

        return board, queens_pos

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

    def pick_random_queen(self):  # returns position of random queen
        random_index = random.randint(0, self.n - 1)
        row, column = self.queenPositions[random_index]

        if self.queen_is_blocked(row, column):
            return self.pick_random_queen()

        return row, column

    def print_board(self):  # prints out all positions of queens
        for queen in self.queenPositions:
            print(queen)

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
            available_pos.append((pos[0], x))

        return available_pos
