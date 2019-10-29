#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        nums.sort()
        @lru_cache(maxsize=None)
        def possibleCount(val: int) -> int:
            if val == 0:
                return 1

            possibles = 0
            for num in nums:
                if num > val:
                    break
                possibles += possibleCount(val - num)
            return possibles

        return possibleCount(target)
