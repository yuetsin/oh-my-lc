#!/usr/bin/env python


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        N = len(A)
        if N <= 0:
            return 0

        counter = 0
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    for l in range(N):
                        if A[i] + B[j] + C[k] + D[l] == 0:
                            counter += 1

        return counter
