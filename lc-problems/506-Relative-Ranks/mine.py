#!/usr/bin/env python

import bisect


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        numcnt = len(nums)
        sorts = copy.deepcopy(nums)
        sorts.sort()
        results = []
        for num in nums:
            idx = bisect.bisect_left(sorts, num)
            if numcnt >= 1 and idx == numcnt - 1:
                results.append("Gold Medal")
            elif numcnt >= 2 and idx == numcnt - 2:
                results.append("Silver Medal")
            elif numcnt >= 3 and idx == numcnt - 3:
                results.append("Bronze Medal")
            else:
                results.append(str(numcnt - idx))

        return results
