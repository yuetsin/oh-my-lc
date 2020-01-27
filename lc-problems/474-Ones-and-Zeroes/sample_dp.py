#!/usr/bin/env python


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for s in strs:
            m1, n1 = 0, 0
            for ch in s:
                if ch == '1':
                    n1 += 1
                else:
                    m1 += 1
            for j in range(n, n1-1, -1):
                for k in range(m, m1 - 1, -1):
                    if j >= n1 and k >= m1:
                        dp[j][k] = max(dp[j][k], dp[j - n1][k - m1] + 1)

        return dp[-1][-1]
