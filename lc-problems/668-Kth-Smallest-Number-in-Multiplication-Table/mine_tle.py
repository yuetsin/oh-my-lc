#!/usr/bin/env python


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Don't you dare construct the actual table.

        count = 0

        types = {}
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = i * j
                if v in types:
                    types[v] += 1
                else:
                    types.update({v: 1})

        print(types)
