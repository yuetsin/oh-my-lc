#!/usr/bin/env python

from collections import Counter


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort()
        llen = len(s)

        result = ""
        for word in d:
            if len(word) <= len(result):
                continue

            lptr, rptr = 0, 0
            rlen = len(word)

            ok = False

            while lptr < llen:
                if s[lptr] == word[rptr]:
                    rptr += 1
                lptr += 1
                if rptr == rlen:
                    ok = True
                    break

            if ok:
                result = word

        return result
