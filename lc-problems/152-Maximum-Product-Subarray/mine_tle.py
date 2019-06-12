#!/usr/bin/env python


class Solution:
    # I expect this code would be forcefully stabbed by the test cases
    def maxProduct(self, nums: List[int]) -> int:
        max_val = float('-inf')
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] > 0:
                continue
            this_roll_max = float('-inf')
            result = 1
            for j in range(i, len(nums)):
                result *= nums[j]
                if result > this_roll_max:
                    this_roll_max = result
            # print("roll", i, "result", this_roll_max)
            if this_roll_max > max_val:
                max_val = this_roll_max
        return max_val
