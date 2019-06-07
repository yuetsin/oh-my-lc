#!/usr/bin/env python
#
# It's an O(N) space complexity solution.
#


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        impossible = set()
        likely = set()
        for i in nums:
            if i in likely:
                likely.remove(i)
                impossible.add(i)
            elif not i in impossible:
                likely.add(i)
        return list(likely)[0]
