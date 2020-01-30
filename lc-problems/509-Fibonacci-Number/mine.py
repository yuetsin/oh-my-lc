#!/usr/bin/env python

from functools import lru_cache


class Solution:
    dicts = {
        0: 0,
        1: 1,
        2: 1
    }

    @lru_cache(maxsize=None)
    def fib(self, N: int) -> int:
        if N in self.dicts:
            return self.dicts[N]
        return self.fib(N - 1) + self.fib(N - 2)
