#!/usr/bin/env python


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums)
        while count > 2:
            first = nums[0]
            flag = True
            for i in range(count - 1, 0, -1):
                if nums[i] != first:
                    del nums[i]
                    del nums[0]
                    count -= 2
                    flag = False
                    break
            if flag:
                # All equal
                break
        return nums[0]
