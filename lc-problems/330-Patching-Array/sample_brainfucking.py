#!/usr/bin/env python


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch, miss, i = 0, 1, 0
        while miss <= n:
            # loop till miss = max of the covered range + 1 = (K+1)
            if i < len(nums) and nums[i] <= miss:
                                                    # if nums[i] > miss then nums[i] is out of range even after patching miss e.g. 23 in [1,2,4,23,43]
                # get to the max of the covered range + 1, where +1 comes from initializing miss to be 1
                miss += nums[i]
                i += 1
            else:
                # patch miss and lift miss from (K+1) to (2K+2) for finding the new (K+1) for the remaining numbers in nums
                miss += miss
                patch += 1     # no. of patches + 1
        return patch
