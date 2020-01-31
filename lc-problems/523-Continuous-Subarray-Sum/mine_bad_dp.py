#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_cnt = len(nums)
        if num_cnt < 2:
            return False

        dp = [[-1] * num_cnt for _ in range(num_cnt)]

        @lru_cache(maxsize=None)
        def getDp(since: int, till: int) -> int:
            return getDp(since, till - 1) + nums[till]
