#!/usr/bin/env python


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        count = 0
        sumup = 0
        for i in sorted(nums, reverse=True):
            sumup += i
            count += 1
            if sumup >= s:
                return count
        return 0
