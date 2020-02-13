#!/usr/bin/env python

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sumup = 0
        
        for i in range(len(nums)):
            start = i
            count = 0
            
            product = 1
            
            for j in range(i, len(nums)):
                product *= nums[j]
                if product >= k:
                    break
                count += 1
            
            sumup += count
        
        return sumup