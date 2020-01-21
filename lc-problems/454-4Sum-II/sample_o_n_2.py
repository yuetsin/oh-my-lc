#!/usr/bin/env python


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if len(A) == 0 or len(B) == 0 or len(C) == 0 or len(D) == 0:
            return 0
        sum_ab = {}
        for a in A:
            for b in B:
                sum_ = a+b
                if sum_ in sum_ab:
                    sum_ab[sum_] += 1
                else:
                    sum_ab[sum_] = 1
        ret = 0
        for c in C:
            for d in D:
                key = -1*(c+d)
                if key in sum_ab:
                    ret += sum_ab[key]

        return ret
