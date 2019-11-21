#!/usr/bin/env python


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        res = 0
        S = sum(A)

        for i in range(len(A)):
            res += i * A[i]
        f = res
        for j in range(1, n):
            item = A.pop()
            f = f + S - n*item
            if f > res:
                res = f
        return res
