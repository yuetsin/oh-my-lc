#!/usr/bin/env python

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1len = len(s1)
        s2len = len(s2)

        if s2len < s1len:
            return False

        dic = dict(Counter(s1))
        act = dict(Counter(s2[:s1len]))

        if act == dic:
            return True

        for i in range(s1len, s2len):
            pop_c = s2[i - s1len]
            push_c = s2[i]

            if act[pop_c] > 1:
                act[pop_c] -= 1
            else:
                del act[pop_c]

            if push_c in act:
                act[push_c] += 1
            else:
                act.update({
                    push_c: 1
                })

            if act == dic:
                return True

        return False
