#!/usr/bin/env python


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        counter = 0

        current = 0
        last = float('-inf')
        for i in range(len(nums)):
            # print("%d" % nums[i])
            if last < nums[i]:
                # print("+1")
                current += 1
            else:
                # print("clear")
                counter = max(counter, current)
                current = 1

            last = nums[i]

        return max(counter, current)
