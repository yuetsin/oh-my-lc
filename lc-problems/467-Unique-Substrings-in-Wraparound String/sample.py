#!/usr/bin/env python

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dl = defaultdict(int)
        maxlen = 0 
        for i in range(len(p)):
            maxlen = maxlen + 1 if i and (ord(p[i - 1]) - 96) % 26 == (ord(p[i]) - 97) else 1 
            dl[p[i]] = max(dl[p[i]], maxlen)
        return sum(dl.values())
# by @fire4fly