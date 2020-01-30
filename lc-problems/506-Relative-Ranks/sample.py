#!/usr/bin/env python


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums = [[nums[a], a] for a in range(len(nums))]
        nums.sort(key=lambda x: x[0])
        rank = len(nums)
        ret = [None] * rank
        end = len(nums) - 3

        for a in range(end):
            ret[nums[a][1]] = str(rank)
            rank -= 1

        if (len(nums) >= 3):
            ret[nums[-3][1]] = "Bronze Medal"

        if (len(nums) >= 2):
            ret[nums[-2][1]] = "Silver Medal"

        if (len(nums)):
            ret[nums[-1][1]] = "Gold Medal"

        return ret
