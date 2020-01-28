#!/usr/bin/env python
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        numlen = len(nums)

        median_shuttle = nums[:k]
        median_shuttle.sort()

        result = []

        for lp in range(numlen - k):
            val = nums[lp + k]
            # print("+ ", val)

            # print("Window now at [%d:%d]" % (lp, lp + k - 1))
            if k % 2 == 0:
                result.append(
                    (median_shuttle[k // 2 - 1] + median_shuttle[k // 2]) / 2)
            else:
                result.append(median_shuttle[k // 2])
            bisect.insort_left(median_shuttle, val)
            # print(median_shuttle)
            # print("- ", nums[lp])
            del median_shuttle[bisect.bisect_left(median_shuttle, nums[lp])]
            # print(median_shuttle)

        if k % 2 == 0:
            result.append(
                (median_shuttle[k // 2 - 1] + median_shuttle[k // 2]) / 2)
        else:
            result.append(median_shuttle[k // 2])
        return result
