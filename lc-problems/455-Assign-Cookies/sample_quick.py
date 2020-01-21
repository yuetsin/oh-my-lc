#!/usr/bin/env python


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        end_g = n - 1
        end_s = m - 1
        count = 0
        while end_s >= 0 and end_g >= 0:
            if s[end_s] >= g[end_g]:
                count = count + 1
                end_g = end_g - 1
                end_s = end_s - 1
            else:
                end_g = end_g - 1
        return count
