#!/usr/bin/env python

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        result = 0

        for num in nums:
            result += abs(mid - num)
        
        return result