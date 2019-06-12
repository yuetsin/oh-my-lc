#!/usr/bin/env python

class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = None
        for i in range(len(nums)):
            if last and nums[i] < last:
                return nums[i]
            last = nums[i]
        return nums[0]