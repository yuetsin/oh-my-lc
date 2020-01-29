#!/usr/bin/env python


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double_nums = []
        double_nums += nums
        double_nums += nums

        num2len = len(double_nums)
        # print(double_nums)

        results = []
        for num_i in range(len(nums)):
            num1 = nums[num_i]
            found = False
            for i in range(num_i + 1, num2len):
                if double_nums[i] > num1:
                    results.append(double_nums[i])
                    found = True
                    break

            if not found:
                results.append(-1)

        return results
