#!/usr/bin/env python


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2:
            return '/'.join(nums)

        tokens = ['%d/(%d' % (nums[0], nums[1])]

        for i in range(2, len(nums)):
            tokens.append('/%d' % nums[i])

        tokens.append(')')
        return ''.join(tokens)
