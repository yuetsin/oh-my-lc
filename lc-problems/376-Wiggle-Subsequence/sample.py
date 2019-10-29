#!/usr/bin/env python


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # index means the index of last num in nums
        # flag means 1,-1,up or down
        result = 1
        index = 0
        flag = 0
        for i in range(1, len(nums)):
            n = nums[i]
            n_index = nums[index]
            if n > n_index:
                index = i
                if flag <= 0:
                    flag = 1
                    result += 1
            if n < n_index:
                index = i
                if flag >= 0:
                    flag = -1
                    result += 1
        return result
