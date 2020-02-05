#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def isTriangle(a: int, b: int, c: int) -> bool:
            return a + b > c and a + c > b and b + c > a

        counter = 0
        num_cnt = len(nums)

        if num_cnt < 3:
            return 0

        for i in range(num_cnt - 2):
            for j in range(i + 1, num_cnt - 1):
                for k in range(j + 1, num_cnt):
                    if isTriangle(nums[i], nums[j], nums[k]):
                        counter += 1
        return counter
