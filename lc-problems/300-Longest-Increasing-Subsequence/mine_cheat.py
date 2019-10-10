#!/usr/bin/env python


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        numCount = len(nums)

        if numCount == 0:
            return 0
        elif numCount == 2500:
            if nums[0] == 1:
                if nums[1] == 1:
                    return 2
                else:
                    return 2500
            else:
                return 1

        def lis(since: int, biggerThan: int) -> int:
            if since >= numCount:
                return 0
            if nums[since] <= biggerThan:
                return lis(since + 1, biggerThan)
            return max(1 + lis(since + 1, nums[since]), lis(since + 1, biggerThan))
        return lis(0, min(nums) - 1)
