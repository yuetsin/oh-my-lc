#!/usr/bin/env python


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.DP = {}
        self.nums = nums
        self.numlen = len(nums)

        def robSince(i: int) -> int:
            if i in self.DP:
                return self.DP[i]
            if i >= self.numlen:
                self.DP.update({i: 0})
                return 0
            elif i == self.numlen - 1:
                self.DP.update({i: self.nums[i]})
                return self.nums[i]
            else:
                # give up this house or rob this house?
                val_max = max(robSince(i + 1), robSince(i + 2) + self.nums[i])
                self.DP.update({i: val_max})
                return val_max
        return robSince(0)
