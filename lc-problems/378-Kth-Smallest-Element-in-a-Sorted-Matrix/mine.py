#!/usr/bin/env python


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = len(matrix)

        nums = []

        def addNum(val: int):
            bisect.insort_left(nums, val)
            if len(nums) > k:
                nums.pop(-1)

        for i in matrix:
            for j in i:
                addNum(j)
        print(nums)
        return nums[-1]
