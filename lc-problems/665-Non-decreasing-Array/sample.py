#!/usr/bin/env python


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # can always make it if len(nums) <= 2
        if len(nums) <= 2:
            return True

        # sigbit
        modified = False

        for i in range(len(nums) - 1):

            # fine. non-decreasing pair.
            if nums[i] <= nums[i+1]:
                continue

            if modified:
                return False

            # we can do and only do one swap:
            # move nums[i] to nums[i+1].
            # that works only when nums[i - 1] > nums[i + 1].
            # if that doesn't ease all non-decresing pairs,
            # nothing could help at all.
            if i > 0 and nums[i-1] > nums[i+1]:
                nums[i+1] = nums[i]

            modified = True
        return True
