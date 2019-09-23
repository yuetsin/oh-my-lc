#!/usr/bin/env python


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        yMax = len(matrix)
        xMax = len(matrix[0]) if yMax > 0 else 0

        def couldExpand(x: int, y: int, towards: int) -> List[List[int]]:
            # towards: 0 - ↖️
            # towards: 1 - ↗️
            # towards: 2 - ↙️
            # towards: 3 - ↘️
            if towards == 0:
                if x <= 0 or y <= 0:
                    return
                possible = [[y - 1, x - 1], [y - 1, x], [y, x - 1]]
            elif towards == 1:
                if x >= xMax - 1 or y <= 0:
                    return
                possible = [[y - 1, x + 1], [y, x + 1], [y - 1, x]]
            elif towards == 2:
                if x <= 0 or y >= yMax - 1:
                    return
                possible = [[x - 1, y + 1], [x - 1, y], [x, y + 1]]
            else:
                if x >= xMax - 1 or y >= yMax - 1:
                    return
                possible = [[x + 1, y + 1], [x + 1, y], [x, y + 1]]
            for point in possible:
                if matrix[possible[1]][possible[0]] != 1:
                    return
            for point in possible:
                matrix[possible[1]][possible[0]] = -1
            return possible

        span = 0

        for y in range(yMax):
            for x in range(xMax):
                if matrix[y][x] != 1:
                    continue
                span = max(span, 1)
                matrix[y][x] = -1
                stack = [[y, x]]
                while True:
                    point = stack.pop()
                    listA = couldExpand(x, y, 0)
                    listB = couldExpand(x, y, 1)
                    listC = couldExpand(x, y, 2)
                    listD = couldExpand(x, y, 3)
