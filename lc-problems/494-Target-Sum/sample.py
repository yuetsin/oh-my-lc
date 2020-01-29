#!/usr/bin/env python


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        dp = {}
        dp[nums[0]] = 1
        dp[-nums[0]] = 1 if nums[0] != 0 else 2
        for i in range(1, len(nums)):
            temp = {}
            for sum in dp:
                temp[sum+nums[i]] = temp.get(sum+nums[i], 0)+dp.get(sum, 0)
                temp[sum-nums[i]] = temp.get(sum-nums[i], 0)+dp.get(sum, 0)
            dp = temp
        if S in dp:
            return dp[S]
        return 0
