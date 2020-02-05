#!/usr/bin/env python


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        min_x = m
        min_y = n

        for op in ops:
            min_x = min(min_x, op[0])
            min_y = min(min_y, op[1])

        return min_x * min_y
