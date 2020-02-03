#!/usr/bin/env python


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sol = 0
        i = 0
        while i < len(nums):
            sol += nums[i]
            i += 2

        return sol
