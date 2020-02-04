import sys
import random
from typing import Dict


class BlockedQueensGenerator:
    def __init__(self, n_queens: int, n_blocked_queens: int):
        self.n_queens = n_queens
        self.n_blocked_queens = n_blocked_queens
        self.mininfile = 2
        random.seed(10)

    def generate(self) -> Dict[int, int]:
        for attempt in range(100000):
            queensorder = [[i, j] for i in range(self.n_queens) for j in range(self.n_queens)]
            random.shuffle(queensorder)

            rows = [[j for j in range(self.n_queens)] for i in range(self.n_queens)]
            cols = [[j for j in range(self.n_queens)] for i in range(self.n_queens)]

            answer: Dict[int, int] = {}

            for q in queensorder:
                r = q[0]
                c = q[1]
                if len(rows[r]) > self.mininfile and len(cols[c]) > self.mininfile:
                    rows[r].remove(c)
                    cols[c].remove(r)
                    answer[c] = r  # because old blocked queens instances are from 1
                    if len(answer) == self.n_blocked_queens:
                        print("Blocked Queens: %r" % answer)
                        return answer
