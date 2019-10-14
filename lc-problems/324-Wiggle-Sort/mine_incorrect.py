#!/usr/bin/env python


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = sorted(nums, reverse=True)
        lennums = len(nums)
        half = lennums // 2
        print(half)

        if lennums % 2 == 1:
            for i in range(lennums):
                if i < half:
                    print(i, " => ", i * 2)
                    nums[i * 2] = new_nums[i]
                else:
                    i = i - half
                    print(i + half, " => ", i * 2 - 1)
                    nums[i * 2 - 1] = new_nums[i + half]
        else:
            for i in range(lennums):
                if i < half:
                    print(i, " => ", i * 2)
                    nums[i * 2] = new_nums[i]
                else:
                    i = i - half
                    print(i + half, " => ", i * 2 + 1)
                    nums[i * 2 + 1] = new_nums[i + half]
