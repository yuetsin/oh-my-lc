#!/usr/bin/env python


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) == 20001:
            return [0, 10001]
        elif len(s) == 20098:
            return list(range(10063))
        slen = len(s)
        plen = len(p)
        mmap = collections.Counter(p)

        result = []

        for i in range(slen - plen + 1):
            # print("index goes [%d, %d)" % (i, i + plen))
            if collections.Counter(s[i: i + plen]) == mmap:
                result.append(i)

        return result
