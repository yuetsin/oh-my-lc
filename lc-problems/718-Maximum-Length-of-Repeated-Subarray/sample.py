#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        m, n = len(A), len(B)
        dp = [[0 for i in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if(i == 0 or j == 0):
                    dp[i][j] = 0
                elif(A[i-1] == B[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res
