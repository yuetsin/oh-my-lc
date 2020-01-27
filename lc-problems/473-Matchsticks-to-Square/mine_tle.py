#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if nums == []:
            return False

        sumup = sum(nums)
        numcnts = len(nums)

        if sumup % 4 != 0:
            return False

        target = sumup // 4

        if max(nums) > target:
            return False

        @lru_cache(maxsize=1000)
        def dfs(idx: int, l1: int = 0, l2: int = 0, l3: int = 0, l4: int = 0) -> bool:
            if idx == numcnts:
                return l1 == l2 and l2 == l3 and l3 == l4
            return dfs(idx + 1, l1 + nums[idx], l2, l3, l4) or dfs(idx + 1, l1, l2 + nums[idx], l3, l4) or dfs(idx + 1, l1, l2, l3 + nums[idx], l4) or dfs(idx + 1, l1, l2, l3, l4 + nums[idx])

        return dfs(0)
