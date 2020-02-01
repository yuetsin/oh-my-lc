#!/usr/bin/env python


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(nums[::2])-sum(nums[1::2])
