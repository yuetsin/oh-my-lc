#!/usr/bin/env python


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        total = 1
        for num in nums:
            if num != 0:
                total *= num

        result = []
        for num in nums:
            if num == 0:
                result.append(total)
            else:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total // num)
        return result
