#!/usr/bin/env python


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        # print("called", nums)
        rst = []

        for key in nums:
            vals = []
            for num in nums:
                if key == num:
                    continue
                if key % num == 0 or num % key == 0:
                    vals.append(num)
            # if vals == []:
            #     continue
            curls = self.largestDivisibleSubset(vals)

            if len(curls) + 1 > len(rst):
                rst = curls
                rst.append(key)
            # print("trying key = ", key, ", result = ", rst)
        return rst
