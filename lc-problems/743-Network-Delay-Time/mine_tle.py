#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        visited = set()

        # @lru_cache(maxsize=None)
        def minTime(to: int) -> int:
            if to == K:
                return 0

            visited.add(to)
            min_t = float('+inf')
            for src, dst, time in times:
                if dst == to:
                    if src in visited:
                        continue
                    min_t = min(min_t, time + minTime(src))
            visited.remove(to)
            return min_t

        ret = 0
        for i in range(1, N + 1):
            visited.clear()
            ret = max(ret, minTime(i))

        return ret if ret != float('+inf') else -1
