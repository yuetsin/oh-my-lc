#!/usr/bin/env python


class Solution(object):
    def splitArray(self, nums, p):
        lo, hi = max(nums), sum(nums)

        while lo <= hi:
            mid = (lo + hi) / 2
            curr, partitions = 0, 1

            for num in nums:
                curr += num
                if curr > mid:
                    partitions += 1
                    curr = num

            if partitions <= p:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
