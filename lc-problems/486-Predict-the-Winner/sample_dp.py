#!/usr/bin/env python


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp: dp(i, j) = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
        # base case: dp(a, a) <- dp(a+1, a), dp(a,a-1)
        dp = [0]
        for i in reversed(range(len(nums))):
            new = [0]
            for j in range(i, len(nums)):
                c1 = nums[i] - dp[j-i]
                c2 = nums[j] - new[-1]
                new.append(max(c1, c2))
            dp = new
        return dp[-1] >= 0
