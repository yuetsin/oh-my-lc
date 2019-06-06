#!/usr/bin/env python


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        possible = set(nums)
        visited = set()
        for i in nums:
            if i in visited:
                possible.remove(i)
            else:
                visited.add(i)
        return list(possible)[0]
