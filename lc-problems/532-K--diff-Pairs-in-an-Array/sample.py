#!/usr/bin/env python


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_uni = list(set(nums))
        if k == 0:
            nums_count = [nums.count(i) > 1 for i in nums_uni]
            #res = len([1 for i in nums_count if i > 1])
            res = nums_count.count(True)
        elif k < 0:
            res = 0
        else:
            new_nums = set([i+k for i in nums_uni])
            res = len(new_nums.intersection(set(nums_uni)))
        return(res)
