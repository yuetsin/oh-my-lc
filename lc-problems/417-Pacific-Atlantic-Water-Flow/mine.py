#!/usr/bin/env python


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # 简单说，找出那些可以流到「左或上」边沿和「右或下」边沿的点。
        # 「流」只能沿着上下左右方向，且只能往同高或更低的地方流。

        height = len(matrix)
        width = len(matrix[0]) if height != 0 else 0

        pacificDP = [[False] * width for _ in range(height)]
        atlanticDP = [[False] * width for _ in range(height)]

        pacStack = []
        atlStack = []

        visitedPac = set()
        visitedAtl = set()

        for x in range(width):
            # pacificDP[0][x] = True
            pacStack.append((0, x))

            # atlanticDP[height - 1][x] = True
            atlStack.append((height - 1, x))

        for y in range(height):
            # pacificDP[y][0] = True
            pacStack.append((y, 0))

            # atlanticDP[y][width - 1] = True
            atlStack.append((y, width - 1))

        # print(pacStack)
        # print(atlStack)

        # print(pacificDP)
        # print(atlanticDP)
        while pacStack:
            y, x = pacStack.pop(0)

            if (x, y) in visitedPac:
                continue
            # print("pac add (", y, x, ")")
            visitedPac.add((x, y))

            value = matrix[y][x]
            pacificDP[y][x] = True
            neighbors = []
            if x > 0:
                neighbors.append((x - 1, y))
            if y < height - 1:
                neighbors.append((x, y + 1))
            if y > 0:
                neighbors.append((x, y - 1))
            if x < width - 1:
                neighbors.append((x + 1, y))
            for nb in neighbors:
                if matrix[nb[1]][nb[0]] >= value:
                    # could flow this way
                    if not nb in visitedPac:
                        pacStack.append((nb[1], nb[0]))
                        # print("(%d, %d) has neighbor (%d, %d)" % (y, x, nb[1], nb[0]))

        while atlStack:
            y, x = atlStack.pop(0)

            if (x, y) in visitedAtl:
                continue
            visitedAtl.add((x, y))
            value = matrix[y][x]
            atlanticDP[y][x] = True
            # print("atl add (", y, x, ")")
            neighbors = []
            if x > 0:
                neighbors.append((x - 1, y))
            if y < height - 1:
                neighbors.append((x, y + 1))
            if y > 0:
                neighbors.append((x, y - 1))
            if x < width - 1:
                neighbors.append((x + 1, y))
            for nb in neighbors:
                if matrix[nb[1]][nb[0]] >= value:
                    # could flow this way
                    if not nb in visitedAtl:
                        atlStack.append((nb[1], nb[0]))
                        # print("(%d, %d) has neighbor (%d, %d)" % (y, x, nb[1], nb[0]))

        # print(pacificDP)
        # print(atlanticDP)

        result = []
        for y in range(height):
            for x in range(width):
                if pacificDP[y][x] and atlanticDP[y][x]:
                    result.append([y, x])

        return result
