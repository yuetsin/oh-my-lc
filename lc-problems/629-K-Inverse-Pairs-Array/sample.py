#!/usr/bin/env python


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10 ** 9 + 7

        DP = [0] * (k + 1)

        for i in range(1, n + 1):
            temp = [0] * (k + 1)
            temp[0] = 1
            for j in range(1, k + 1):
                val = (DP[j] + M - (DP[j - i] if j - i >= 0 else 0)) % M
                temp[j] = (temp[j - 1] + val) % M
            DP = temp

        return (DP[k] + M - (DP[k - 1] if k > 0 else 0)) % M
