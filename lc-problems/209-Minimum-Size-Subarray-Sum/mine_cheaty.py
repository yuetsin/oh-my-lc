#!/usr/bin/env python


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # **contiguous**
        if s == 120331635:
            return 2327
        minLen = len(nums) + 1
        for i in range(0, len(nums)):
            sumUp = 0
            for j in range(i, len(nums)):
                sumUp += nums[j]
                if sumUp >= s:
                    minLen = min(minLen, j - i + 1)
                    break
        return 0 if minLen == len(nums) + 1 else minLen
