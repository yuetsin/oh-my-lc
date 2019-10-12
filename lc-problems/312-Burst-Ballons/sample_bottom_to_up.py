#!/usr/bin/env python

class Solution:
    def maxCoins(self, nums) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        _len = len(nums)
        dp = [[0]*_len for _ in range(_len)]

        for l in range(1, _len+1):
            for i in range(1, _len-l):
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])
        return dp[1][_len-2]
