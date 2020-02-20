#!/usr/bin/env python


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        ylen = len(grid)
        xlen = len(grid[0])

        def goestoA(x: int, y: int) -> int:
            # print("called ", x, y)
            pick = 0
            if grid[y][x] == 1:
                pick = 1
                grid[y][x] = 0

            if x == xlen - 1 and y == ylen - 1:
                return pick + goestoB(xlen - 1, ylen - 1)

            mmax = float('-inf')

#             if x > 0 and grid[y][x - 1] != -1:
#                 mmax = max(mmax, goesto(x - 1, y) + pick)

            if x < xlen - 1 and grid[y][x + 1] != -1:
                mmax = max(mmax, goestoA(x + 1, y) + pick)

#             if y > 0 and grid[y - 1][x] != -1:
#                 mmax = max(mmax, goesto(x, y - 1) + pick)

            if y < ylen - 1 and grid[y + 1][x] != -1:
                mmax = max(mmax, goestoA(x, y + 1) + pick)

            grid[y][x] = pick
            return mmax

        def goestoB(x: int, y: int) -> int:
            # print("called ", x, y)
            pick = 0
            if grid[y][x] == 1:
                pick = 1
                grid[y][x] = 0

            if x == 0 and y == 0:
                return pick

            mmax = float('-inf')

            if x > 0 and grid[y][x - 1] != -1:
                mmax = max(mmax, goestoB(x - 1, y) + pick)

            # if x < xlen - 1 and grid[y][x + 1] != -1:
                # mmax = max(mmax, goesto(x + 1, y) + pick)

            if y > 0 and grid[y - 1][x] != -1:
                mmax = max(mmax, goestoB(x, y - 1) + pick)

            # if y < ylen - 1 and grid[y + 1][x] != -1:
                # mmax = max(mmax, goesto(x, y + 1) + pick)

            grid[y][x] = pick
            return mmax

        one_way = goestoA(0, 0)
        if one_way == float('-inf'):
            return 0

        return one_way
