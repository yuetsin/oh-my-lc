#!/usr/bin/env python

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i) # (1), (2)
        degree = max(list(map(len, dic.values()))) # (3)
        res = (1 << 63) - 1
        for k, v in dic.items():
            if len(v) < degree:
                continue
            res = min(res, v[-1] - v[0] + 1) # (4)
        return res