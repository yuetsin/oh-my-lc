#!/usr/bin/env python

from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        seen = Counter(nums)
        for k, v in seen.items():
            if v == 2:
                res.append(k)
        return res
