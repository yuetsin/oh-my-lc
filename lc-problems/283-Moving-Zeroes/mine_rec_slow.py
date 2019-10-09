#!/usr/bin/env python

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numlen = len(nums)
        
        def moveZeroesSince(index: int):
            if sum(nums[index:]) == 0:
                return
            # print("called move with index = %d. now nums:" % index, nums)
            if index >= numlen:
                return

            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                moveZeroesSince(index)
            else:
                moveZeroesSince(index + 1)
        
        moveZeroesSince(0)