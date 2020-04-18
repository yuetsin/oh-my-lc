#!/usr/bin/env python

from functools import lru_cache


class Solution:

    lru_cache(maxsize=None)

    def kthBit(self, N: int, K: int) -> bool:
        # print("check", N, K)
        if N == 0:
            return False
        if K % 2 == 1:
            return not self.kthBit(N - 1, (K - 1) // 2)
        else:
            return self.kthBit(N - 1, K // 2)

    def kthGrammar(self, N: int, K: int) -> int:
        return 1 if self.kthBit(N - 1, K - 1) else 0
