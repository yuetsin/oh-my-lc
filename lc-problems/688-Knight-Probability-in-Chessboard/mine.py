#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        # DP = {}

        @lru_cache(maxsize=None)
        def getP(x: int, y: int, steps: int) -> float:
            if steps == 0:
                return 1
            # if (x, y) in DP:
            #     return DP[(x, y)]
            goesto = [
                (x - 1, y - 2),
                (x - 2, y - 1),
                (x - 2, y + 1),
                (x - 1, y + 2),
                (x + 1, y + 2),
                (x + 2, y + 1),
                (x + 2, y - 1),
                (x + 1, y - 2)
            ]

            cs = 0
            for xi, yi in goesto:
                if xi < 0 or xi >= N or yi < 0 or yi >= N:
                    continue
                cs += getP(xi, yi, steps - 1)

            retv = cs / 8
            # DP.update({
            #     (x, y): retv
            # })

            return retv

        return getP(r, c, K)
