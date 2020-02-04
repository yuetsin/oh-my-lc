#!/usr/bin/env python


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)

        counter = 0

        mins = float('+inf')
        maxs = float('-inf')

        touched = False
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                touched = True
                mins = min(mins, i)
                maxs = max(maxs, i)

        if not touched:
            return 0
        return maxs - mins + 1
