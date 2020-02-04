#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10 ** 9 + 7

        # global_map = [[0] * n for _ in range(m)]

        @lru_cache(maxsize=None)
        def dfs(steps: int, i: int, j: int) -> int:
            if steps == 0:
                return 0
            simple_v = 0
            if i == 0:
                simple_v += 1
            if i == m - 1:
                simple_v += 1
            if j == 0:
                simple_v += 1
            if j == n - 1:
                simple_v += 1

            # global_map[i][j] = -1
            # visited mark

            poss = simple_v
            if i > 0:  # and global_map[i - 1][j] != -1:
                poss += dfs(steps - 1, i - 1, j)
            if i < m - 1:  # and global_map[i + 1][j] != -1:
                poss += dfs(steps - 1, i + 1, j)
            if j > 0:  # and global_map[i][j - 1] != -1:
                poss += dfs(steps - 1, i, j - 1)
            if j < n - 1:  # and global_map[i][j + 1] != -1:
                poss += dfs(steps - 1, i, j + 1)

            # global_map[i][j] = 0
            return poss

        return dfs(N, i, j) % MOD
