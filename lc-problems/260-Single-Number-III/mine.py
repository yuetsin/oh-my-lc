#!/usr/bin/env python


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        visited = set()
        for num in nums:
            if not num in visited:
                visited.add(num)
            else:
                visited.remove(num)

        return list(visited)
