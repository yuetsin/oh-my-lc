#!/usr/bin/env python

class Solution:
    def maxCoins(self, nums) -> int:
        if not nums:
            return 0
        _len = len(nums)
        dp = [[-1]*_len for _ in range(_len)]

        def _burst(left, right, b, e):
            if e < b:
                return 0
            if dp[b][e] != -1:
                return dp[b][e]
            _max = 0
            if b == e:
                dp[b][e] = left * nums[b] * right
            else:
                for i in range(b, e+1):
                    last = left * nums[i] * right
                    lhalf = _burst(left, nums[i], b, i-1)
                    rhalf = _burst(nums[i], right, i+1, e)
                    _max = max(_max, last+lhalf+rhalf)
                dp[b][e] = _max
            return dp[b][e]

        return _burst(1, 1, 0, _len-1)
