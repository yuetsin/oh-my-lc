#!/usr/bin/env python


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = res = 0
        seen = {0: 0}

        for i, num in enumerate(nums):
            curr += 1 if num else -1
            if curr in seen:
                res = max(res, i - seen[curr] if curr != 0 else i + 1)
            else:
                seen[curr] = i
        return res
