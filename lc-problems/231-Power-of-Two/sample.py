#!/usr/bin/env python


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x = x*2
        return x == n
