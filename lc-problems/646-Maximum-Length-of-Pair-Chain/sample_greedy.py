#!/usr/bin/env python


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans
