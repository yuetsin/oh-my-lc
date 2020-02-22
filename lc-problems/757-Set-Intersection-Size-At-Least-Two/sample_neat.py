#!/usr/bin/env python


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end-point
        ans = 0
        pre = []
        for (s, t) in intervals:
            if not pre or pre[1] < s:
                ans += 2
                pre = [t-1, t]
            elif pre[0] < s:
                pre = [pre[1], t]
                ans += 1
        return ans
