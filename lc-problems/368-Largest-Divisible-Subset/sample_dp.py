#!/usr/bin/env python


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # (previous divisible index, length of divisible subset)
        dp = [(-1, 1)] * n
        # (last divisible index, maximum length of divisible subsets)
        maxl = (0, 1)
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][1] < dp[j][1] + 1:
                        dp[i] = (j, dp[j][1] + 1)
                        if maxl[1] < dp[i][1]:
                            maxl = (i, dp[i][1])
        ret = []
        x = maxl[0]
        while x > -1:
            ret.append(nums[x])
            x = dp[x][0]
        return ret[::-1]
