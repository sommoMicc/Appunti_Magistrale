import random


class NQueens:
    def __init__(self, n):
        self.board, self.queenPositions = self.get_new_board(n)
        self.n = n

    @staticmethod
    def get_new_board(n):
        # queens are represented as ones in 2d list of all zeros
        # Since it's a 2d list, each element is a row of zeros except for the queen
        board = []
        queens_pos = []
        for x in range(n):  # makes n x n board of zeros
            board.append([0] * n)

        for x in range(n):  # sets a random value of each row to be 1, denoting the queen
            random_index = random.randint(0, n - 1)
            board[x][random_index] = x
            queens_pos.append((x, random_index))

        return board, queens_pos

    def all_queens_safe(self):  # returns true if problem is solved and all queens safe, false otherwise
        for pos in self.queenPositions:
            if (self.under_attack(pos)):
                return False
        return True

    def attack_via_col(self, pos):
        for queen in self.queenPositions:
            if pos[1] == queen[1] and queen != pos:  # last inqueality checks to make sure you arent comparing the same queen
                return True
        return False

    def attack_via_row(self, pos):
        for queen in self.queenPositions:
            if (pos[0] == queen[0] and queen != pos):
                return True
        return False

    def attack_via_diagonal(self, pos):
        for queen in self.queenPositions:
            if (abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                return True
        return False

    def under_attack(self, position):
        if (self.attack_via_diagonal(position)):
            return True

        if (self.attack_via_row(position)):
            return True

        if (self.attack_via_col(position)):
            return True

        return False

    def specific_queen_conflicts(self, pos):  # returns number of pieces attacking queen at position pos
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
        newIndex = random.randint(0, self.n - 1)
        return self.queenPositions[newIndex]

    def print_board(self):  # prints out all positions of queens
        for queen in self.queenPositions:
            print(queen)

    def move_queen(self, start_pos, endPos):  # moves queen from startpos to endpos
        assert self.board[start_pos[0]][start_pos[1]] == 1
        # above assert will fail if the start position does not have a queen
        self.board[start_pos[0]][start_pos[1]] = 0
        self.board[endPos[0]][endPos[1]] = 1
        self.queenPositions.remove(start_pos)
        self.queenPositions.append(endPos)

    def available_positions(self, pos):
        # returns list of tuples with all positions queen can go
        available_pos = []
        for x in range(self.n):
            available_pos.append((pos[0], x))

        return available_pos
