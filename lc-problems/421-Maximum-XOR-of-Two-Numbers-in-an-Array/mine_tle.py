#!/usr/bin/env python


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_v = 0
        num_c = len(nums)
        for i in range(num_c):
            for j in range(i + 1, num_c):
                max_v = max(max_v, nums[i] ^ nums[j])

        return max_v
