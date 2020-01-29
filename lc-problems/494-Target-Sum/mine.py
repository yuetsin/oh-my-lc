#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        num_cnt = len(nums)
        @lru_cache(maxsize=None)
        def chanceSince(since: int, current: int) -> int:
            if since == num_cnt:
                return 1 if current == S else 0

            chance = 0
            return chanceSince(since + 1, current + nums[since]) + chanceSince(since + 1, current - nums[since])

        return chanceSince(0, 0)
