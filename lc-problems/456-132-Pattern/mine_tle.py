#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        num_count = len(nums)

        @lru_cache(maxsize=512)
        def findBetween(since: int, bottom: int, top: int) -> bool:
            for i in range(since, num_count):
                if nums[i] > bottom and nums[i] < top:
                    return True
            return False

        def find132PatternSince(since: int) -> bool:
            if since >= num_count - 2:
                return False

            current_v = nums[since]
            for i in range(since + 1, num_count - 1):
                top_v = nums[i]
                if top_v > current_v:
                    if findBetween(i + 1, current_v, top_v):
                        return True

            return False

        for since in range(num_count - 2):
            if find132PatternSince(since):
                return True

        return False
