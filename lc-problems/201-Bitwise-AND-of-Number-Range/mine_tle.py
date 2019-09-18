#!/usr/bin/env python


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        value = n
        for i in range(m, n):
            value &= i
        return value
