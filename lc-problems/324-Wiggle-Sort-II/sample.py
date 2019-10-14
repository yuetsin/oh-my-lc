#!/usr/bin/env python


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        n = len(nums) // 2
        pos = len(nums) // 2
        while n > 0:
            nums.insert(pos, nums.pop(0))
            n -= 1
            pos += 1
