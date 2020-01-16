#!/usr/bin/env python


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if nums == []:
            return
        els = []

        for n in list(set(nums)):
            els.append(n)
            els.sort(reverse=True)
            if len(els) > 3:
                els.pop(-1)

        return els[-1] if len(els) == 3 else els[0]
