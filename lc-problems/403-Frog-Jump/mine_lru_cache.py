#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        start = stones[0]

        if start != 0:
            return False

        target = stones[-1]

        @lru_cache(maxsize=None)
        def canCrossM(since: int, lastjump=None) -> bool:

            if since == target:
                return True

            if lastjump:
                if lastjump > 1:
                    canjmp = [lastjump - 1, lastjump, lastjump + 1]
                else:
                    canjmp = [lastjump, lastjump + 1]
            else:
                canjmp = [1]

            for step in canjmp:
                if since + step in stones:
                    if canCrossM(since + step, step):
                        return True

            return False

        return canCrossM(0)
