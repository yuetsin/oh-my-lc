#!/usr/bin/env python


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tl = list(t)
        for s in list(s):
            tl.remove(s)
        return ''.join(tl[0]) if tl else ''
