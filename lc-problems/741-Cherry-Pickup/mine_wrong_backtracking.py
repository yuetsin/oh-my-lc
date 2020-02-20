#!/usr/bin/env python


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        ylen = len(grid)
        xlen = len(grid[0])

        destx = xlen - 1
        desty = ylen - 1

        def goesto(x: int, y: int) -> int:
            # print("called ", x, y)
            pick = 0
            if grid[y][x] == 1:
                pick = 1

            grid[y][x] = -1

            if x == destx and y == desty:
                return pick

            mmax = float('-inf')

            if x > 0 and grid[y][x - 1] != -1:
                mmax = max(mmax, goesto(x - 1, y) + pick)

            if x < xlen - 1 and grid[y][x + 1] != -1:
                mmax = max(mmax, goesto(x + 1, y) + pick)

            if y > 0 and grid[y - 1][x] != -1:
                mmax = max(mmax, goesto(x, y - 1) + pick)

            if y < ylen - 1 and grid[y + 1][x] != -1:
                mmax = max(mmax, goesto(x, y + 1) + pick)

            grid[y][x] = 0
            return mmax

        one_way = goesto(0, 0)
        if one_way == float('-inf'):
            return 0
        destx = 0
        desty = 0

        two_way = goesto(xlen - 1, ylen - 1)

        return one_way + two_way
