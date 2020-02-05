#!/usr/bin/env python


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i] == 0:
                continue
            for j in range(i + 1, len(nums) - 1):
                while (k < len(nums)) and (nums[i] + nums[j] > nums[k]):
                    k += 1
                count += (k - j - 1)

        return count
