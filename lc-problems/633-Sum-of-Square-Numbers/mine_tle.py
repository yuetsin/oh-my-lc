#!/usr/bin/env python

from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        max_v = int(sqrt(c))

        if max_v * max_v == c:
            return True

        for x in range(1, max_v + 1):
            for y in range(1, max_v + 1):
                if x ** 2 + y ** 2 == c:
                    return True

        return False
