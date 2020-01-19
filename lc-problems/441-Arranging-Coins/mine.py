#!/usr/bin/env python


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1 => 1  2
        # 2 => 3  6
        # 3 => 6  12
        # 4 => 10 20
        #         n = i * (i + 1) // 2
        #         i ^ 2 + i = 2n
        #         i ^ 2 + i - 2n = 0
        #        {{j -> 1/2 (-1 - Sqrt[1 + 8 n])}, {j -> 1/2 (-1 + Sqrt[1 + 8 n])}}

        return int((math.sqrt(1 + 8 * n) - 1) // 2)
