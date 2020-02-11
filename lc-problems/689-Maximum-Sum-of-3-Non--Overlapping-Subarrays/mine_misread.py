#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        val = sum(nums[:k])

        sums = [val]
        for i in range(k, len(nums)):
            val -= nums[i - k]
            val += nums[i]
            sums.append(val)

        print(sums)

        numlen = len(nums)

        @lru_cache(maxsize=None)
        def getMax(since: int, count: int) -> int:
            print("called getMax(%d, %d)" % (since, count))
            if since >= numlen - k:
                return 0
            if count == 0:
                return 0
            elif count == 1:
                return max(sums[since:])

            v = 0
            for i in range(since, numlen - k):
                v = max(v, nums[i] + getMax(since + i, count - 1))

            return v

        return getMax(0, 3)
