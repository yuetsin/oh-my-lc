#!/usr/bin/env python


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        result = []

        def calcC(n: int, m: int):
            return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

        for i in range(numRows):
            layer = []
            for j in range(i + 1):
                layer.append(calcC(j, i))
            result.append(layer)

        return result
