#!/usr/bin/env python

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        return sum(nums) - n * (n + 1) // 2