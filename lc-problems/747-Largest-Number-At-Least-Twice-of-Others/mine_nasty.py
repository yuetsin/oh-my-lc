#!/usr/bin/env python


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = sorted(nums)

        if n[-1] >= n[-2] * 2:
            return nums.index(n[-1])

        return -1
