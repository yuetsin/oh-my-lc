#!/usr/bin/env python


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if nums[-1] != 0:
            nums.append(0)
        max_cons = 0
        current_cons = 0
        for num in nums:
            if num == 0:
                max_cons = max(current_cons, max_cons)
                current_cons = 0
            else:
                current_cons += 1

        nums.pop(-1)
        return max_cons
