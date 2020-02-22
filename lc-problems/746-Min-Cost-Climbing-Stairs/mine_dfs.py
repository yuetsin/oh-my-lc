#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        step_cnt = len(cost)

        @lru_cache(maxsize=None)
        def climb(since: int) -> int:
            if since >= step_cnt:
                return 0

            return min(climb(since + 1), climb(since + 2)) + cost[since]

        return min(climb(0), climb(1))
