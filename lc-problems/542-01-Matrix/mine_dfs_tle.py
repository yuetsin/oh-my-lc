#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        y_max = len(matrix)
        if y_max == 0:
            return []
        x_max = len(matrix[0])

        result = [[None] * x_max for _ in range(y_max)]

        visited = set()

        # @lru_cache(maxsize=None)
        def dfs(y: int, x: int) -> int:
            if matrix[y][x] == 0:
                return 0

            if (x, y) in visited:
                return float('+inf')

            # print("called dfs(%d, %d)" % (x, y))
            visited.add((x, y))

            max_v = float('+inf')
            if y > 0:
                max_v = min(dfs(y - 1, x) + 1, max_v)

            if y < y_max - 1:
                max_v = min(dfs(y + 1, x) + 1, max_v)

            if x > 0:
                max_v = min(dfs(y, x - 1) + 1, max_v)

            if x < x_max - 1:
                max_v = min(dfs(y, x + 1) + 1, max_v)

            visited.remove((x, y))
            return max_v

        for y in range(y_max):
            for x in range(x_max):
                if matrix[y][x] == 0:
                    result[y][x] = 0
                else:
                    result[y][x] = dfs(y, x)
                    # print("%d, %d => %d" % (x, y, result[y][x]))

        return result
