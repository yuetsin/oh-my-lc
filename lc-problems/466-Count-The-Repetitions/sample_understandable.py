#!/usr/bin/env python

class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        d, l1, l2, i1, i2 = {}, len(s1), len(s2), 0, 0
        tot = l1 * n1

        while i1 < tot:
            if s1[i1 % l1] == s2[i2 % l2]:
                if (i1 % l1, i2 % l2) in d:
                    prev1, prev2 = d[(i1 % l1, i2 % l2)]
                    cir1, cir2 = i1 - prev1, i2 - prev2
                    count_cir1 = (tot - i1) // cir1
                    i1 += count_cir1 * cir1
                    i2 += count_cir1 * cir2
                    if i1 >= tot: break
                else:
                    d[(i1 % l1, i2 % l2)] = (i1, i2)
                i2 += 1
            i1 += 1
        return i2 // l2 // n2