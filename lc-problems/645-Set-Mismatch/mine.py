#!/usr/bin/env python


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sets = set()
        sums = sum(nums)
        lens = len(nums)
        actu = lens * (lens + 1) // 2

        duplica = None
        for num in nums:
            if num in sets:
                duplica = num
                break
            sets.add(num)

        # assert(duplica)
        return[duplica, actu - sums + duplica]
