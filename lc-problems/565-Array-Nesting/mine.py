#!/usr/bin/env python


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        visited = []

        def findNest(since: int) -> int:
            if since in visited:
                return 0

            visited.append(since)
            v = findNest(nums[since])
            visited.pop(-1)

            return v + 1

        return max([findNest(i) for i in range(len(nums))])
