#!/usr/bin/env python

import random
import bisect


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.visited = []
        self.x_max = n_rows
        self.y_max = n_cols
        self.total_cnt = n_rows * n_cols
        self.current_cnt = 0

    def flip(self) -> List[int]:

        rand_v = random.randint(0, self.total_cnt - self.current_cnt - 1)

        for pair in self.visited:
            if pair <= rand_v:
                rand_v += 1
            else:
                break

        y = rand_v // self.x_max
        x = rand_v % self.x_max

        self.current_cnt += 1
        bisect.insort_left(self.visited, rand_v)

        return [x, y]

    def reset(self) -> None:
        self.visited.clear()
        self.current_cnt = 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
