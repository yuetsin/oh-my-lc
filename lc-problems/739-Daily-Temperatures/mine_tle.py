#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        lent = len(T)

        results = []
        for i in range(len(T)):

            target = T[i]

            # counter = 0

            ok = False
            for j in range(i + 1, len(T)):
                if T[j] > target:
                    ok = True
                    break

            if not ok:
                results.append(0)
            else:
                results.append(j - i)

        return results
