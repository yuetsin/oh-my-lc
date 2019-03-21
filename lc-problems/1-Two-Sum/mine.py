#!/usr/bin/env python

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        itr = 0
        for i in nums[:-1]:
            inner_itr = itr + 1
            for j in nums[itr + 1:]:
                if i + j == target:
                    return [itr, inner_itr]
                inner_itr += 1
            itr += 1
        return []