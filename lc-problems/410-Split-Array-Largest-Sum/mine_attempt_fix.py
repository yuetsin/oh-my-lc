#!/usr/bin/env python

from functools import lru_cache


class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:

        @lru_cache(maxsize=None)
        def sumup(since: int, till: int) -> int:
            return sum(nums[since: till])

        @lru_cache(maxsize=None)
        def splitArrayAt(since: int, till: int, slices: int) -> int:
            if slices <= 1:
                # print("slice %s // %d => %d" % (nums[since : till + 1], slices, sum(nums[since : till + 1])))
                return sumup(since, till + 1)

            max_return = float("+inf")

            for cutpoint in range(since + 1, till + 1 - slices + 2):
                left = sumup(since, cutpoint)
                right = splitArrayAt(cutpoint, till, slices - 1)

                max_return = min(max_return, max(left, right))

            # print("slice %s // %d => %d" % (nums[since : till + 1], slices, max_return))
            return max_return

        return splitArrayAt(0, len(nums) - 1, m)
