#!/usr/bin/env python


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if A == []:
            return 0
        # n is guaranteed to be less than 10^5...
        # I'm afraid that's too big...
        n = len(A)
        # m = max(A)
        # max_index = [i for i, j in enumerate(A) if j == m]

        result = []
        for v in range(n):
            rs = 0
            for i in range(n):
                if i > v:
                    k = i - v - 1
                else:
                    k = i - v + n - 1
                # print(k, " * ", A[i])
                rs += k * A[i]
            result.append(rs)

        return max(result)
