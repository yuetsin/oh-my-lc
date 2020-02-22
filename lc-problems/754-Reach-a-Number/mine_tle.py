#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def reachNumber(self, target: int) -> int:

        # 为了到达 target，需要的步数最多是 abs（2 * target），
        # 这种方式是我们总是退一步，进一步，这样就相当于净进了一步。

        maxx = abs(2 * target)

        @lru_cache(maxsize=None)
        def step(since: int, to: int, stride: int, elapsed: int) -> int:

            if since == to:
                return 0

            if elapsed > maxx:
                return float('+inf')

            return min(1 + step(since - stride, to, stride + 1, elapsed + 1), 1 + step(since + stride, to, stride + 1, elapsed + 1))

        return step(0, target, 1, 0)
