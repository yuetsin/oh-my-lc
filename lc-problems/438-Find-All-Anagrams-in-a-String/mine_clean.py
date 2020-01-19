#!/usr/bin/env python


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen = len(s)
        plen = len(p)

        if slen < plen:
            return []

        mmap = dict(collections.Counter(p))
        init = dict(collections.Counter(s[:plen]))
        if mmap == init:
            result = [0]
        else:
            result = []
        for i in range(slen - plen):
            # print("i = ", i)
            # print(mmap, init)
            init[s[i]] -= 1
            if init[s[i]] == 0:
                del init[s[i]]
            if s[i + plen] in init:
                init[s[i + plen]] += 1
            else:
                init.update({s[i + plen]: 1})

            if init == mmap:
                result.append(i + 1)

        return result
