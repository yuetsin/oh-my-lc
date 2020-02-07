#!/usr/bin/env python


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, cur = 0, k - 1, 0  # initialization
        for i in range(k):  # first k elements
            cur += nums[i]
        res = cur
        while right + 1 < len(nums):
            left, right = left + 1, right + 1  # move on
            cur = cur - nums[left - 1] + nums[right]
            res = cur if cur > res else res
        return res / k
