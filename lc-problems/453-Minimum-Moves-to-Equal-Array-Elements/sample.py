#!/usr/bin/env python


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        length = len(nums)
        total = sum(nums)
        return total - length * minimum
