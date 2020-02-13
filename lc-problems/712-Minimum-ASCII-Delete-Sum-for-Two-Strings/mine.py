#!/usr/bin/env python

from functools import lru_cache


class Solution:

    @lru_cache(maxsize=None)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        if s1 == s2:
            return 0

        # print("called with (%s, %s)" % (s1, s2))
        if not s1:
            return sum([ord(ch) for ch in s2])
        elif not s2:
            return sum([ord(ch) for ch in s1])

        ptr = 0
        lena = min(len(s1), len(s2))

        while ptr < lena:
            if s1[ptr] != s2[ptr]:
                return min(self.minimumDeleteSum(s1[ptr + 1:], s2[ptr:]) + ord(s1[ptr]), self.minimumDeleteSum(s1[ptr:], s2[ptr + 1:]) + ord(s2[ptr]))
            ptr += 1

        if ptr == len(s1):
            # s2 has some kind of trails
            return sum([ord(ch) for ch in s2[lena:]])
        else:
            return sum([ord(ch) for ch in s1[lena:]])
