#!/usr/bin/env python


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # get len, total
        l1, t1 = len(s1), sum([ord(c) for c in s1])
        l2, t2 = len(s2), sum([ord(c) for c in s2])

        # quick return
        if not s1:
            return t2
        if not s2:
            return t1

        # dp: find the common subsequence with largets ascii sum
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:  # get new match, charge with ord(s1[i])
                    if i == 0 or j == 0:
                        dp[i][j] = ord(s1[i])
                    else:
                        dp[i][j] = dp[i-1][j-1] + ord(s1[i])
                else:
                    # inherit, no charge
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # return
        return t1 + t2 - 2*dp[-1][-1]
