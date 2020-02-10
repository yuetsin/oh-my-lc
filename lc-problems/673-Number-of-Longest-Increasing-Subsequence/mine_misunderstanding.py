#!/usr/bin/env python


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        numlen = len(nums)

        def dfs(since: int, minv: int) -> int:
            if since >= numlen:
                return 0
            elif nums[since] <= minv:
                return dfs(since + 1, minv)
            else:
                return max(dfs(since + 1, minv), dfs(since + 1, nums[since]) + 1)

        return dfs(0, nums[0])
