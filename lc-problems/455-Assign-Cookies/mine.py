#!/usr/bin/env python


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        for child_i in range(len(g)):
            for cookie_i in range(len(s)):
                if g[child_i] <= s[cookie_i]:
                    del s[cookie_i]
                    count += 1
                    break

        return count
