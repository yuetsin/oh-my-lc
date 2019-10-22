#!/usr/bin/env python


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ylen = len(matrix)
        if ylen == 0:
            return 0

        # [1, 0,1]
        # [0,-2,3]

        xlen = len(matrix[0])

        sumUps = [['s'] * xlen for _ in range(ylen)]

        sumUps[0][0] = matrix[0][0]

        for x in range(1, xlen):
            sumUps[0][x] = sumUps[0][x - 1] + matrix[0][x]

        for y in range(1, ylen):
            sumUps[y][0] = sumUps[y - 1][0] + matrix[y][0]

        def getSumUp(y: int, x: int) -> int:
            if y < 0 or x < 0:
                return 0
            if sumUps[y][x] != 's':
                return sumUps[y][x]
            return getSumUp(y, x - 1) + getSumUp(y - 1, x) - getSumUp(y - 1, x - 1) + matrix[y][x]

        result = float('-inf')

        for xmin in range(-1, xlen - 1):
            for xmax in range(xmin + 1, xlen):
                for ymin in range(-1, ylen - 1):
                    for ymax in range(ymin + 1, ylen):
                        # print("x: ", xmin, xmax, "y: ", ymin, ymax)
                        square = getSumUp(
                            ymax, xmax) - getSumUp(ymin, xmax) - getSumUp(ymax, xmin) + getSumUp(ymin, xmin)
                        # print("got", result)
                        if square <= k:
                            result = max(result, square)

        return result
