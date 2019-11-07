#!/usr/bin/env python


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        sptr = 0
        tch = s[sptr]
        slen = len(s)
        for ch in t:
            if tch == ch:
                sptr += 1
                if sptr == slen:
                    return True
                tch = s[sptr]
        return False
