#!/usr/bin/env python


class Solution:
    def reversePairs(self, nums):
        return sum([nums[j] > 2 * nums[i] for i in range(len(nums)) for j in range(0, i)])
