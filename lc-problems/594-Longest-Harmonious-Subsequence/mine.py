#!/usr/bin/env python

from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        dic = dict(Counter(nums))

        return_l = 0
        for k, v in dic.items():
            if k + 1 in dic:
                return_l = max(return_l, v + dic[k + 1])

        return return_l
