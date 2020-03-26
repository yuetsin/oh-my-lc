#!/usr/bin/env python

import collections


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        ret_0 = collections.defaultdict(int)
        ret_1 = collections.defaultdict(int)
        lst_0, lst_1 = [[]] * 2
        r0, r1 = [""] * 2
        i = 0
        while i < len(start):
            if start[i] in "LR":
                ret_0[start[i]] += 1
                r0 += start[i]
            if end[i] in "LR":
                ret_1[end[i]] += 1
                r1 += end[i]
            if ret_0["R"] >= ret_1["R"] and ret_0["L"] <= ret_1["L"]:
                pass
            else:
                return False
            i += 1

        return True if r0 == r1 else False
