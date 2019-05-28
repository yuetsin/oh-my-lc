#!/usr/bin/env python3


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return [1]

        def calcC(n: int, m: int):
            return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

        layer = []
        for j in range(rowIndex + 1):
            layer.append(calcC(j, rowIndex))

        return layer
