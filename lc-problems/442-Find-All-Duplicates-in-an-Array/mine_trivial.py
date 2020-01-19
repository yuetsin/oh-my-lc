#!/usr/bin/env python


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        existed = set()
        duplica = []

        for num in nums:
            if num in existed:
                duplica.append(num)
            else:
                existed.add(num)

        return duplica
