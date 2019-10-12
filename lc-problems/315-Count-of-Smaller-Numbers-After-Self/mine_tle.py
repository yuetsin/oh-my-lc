#!/usr/bin/env python


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        result = []
        for i in range(len(nums) - 1):
            cur = nums[i]
            result.append(sum([num < cur for num in nums[i + 1:]]))
        result.append(0)
        return result
