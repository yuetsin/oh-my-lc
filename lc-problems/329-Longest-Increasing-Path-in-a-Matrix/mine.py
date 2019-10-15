#!/usr/bin/env python


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if matrix == []:
            return 0
        DP = {}

        ymax = len(matrix)
        xmax = len(matrix[0]) if ymax != 0 else 0

        def findNext(x: int, y: int) -> int:
            if (x, y) in DP:
                return DP[(x, y)]

            current = matrix[y][x]
            matrix[y][x] = -1

            possible = 1

            if x > 0:
                if matrix[y][x - 1] > current:
                    possible = max(possible, findNext(x - 1, y) + 1)

            if x < xmax - 1:
                if matrix[y][x + 1] > current:
                    possible = max(possible, findNext(x + 1, y) + 1)

            if y > 0:
                if matrix[y - 1][x] > current:
                    possible = max(possible, findNext(x, y - 1) + 1)

            if y < ymax - 1:
                if matrix[y + 1][x] > current:
                    possible = max(possible, findNext(x, y + 1) + 1)

            matrix[y][x] = current
            DP.update({
                (x, y): possible
            })
            return possible

        maxV = 1
        for x in range(xmax):
            for y in range(ymax):
                maxV = max(maxV, findNext(x, y))

        return maxV
