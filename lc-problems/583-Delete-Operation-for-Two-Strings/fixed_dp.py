#!/usr/bin/env python


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = [0] * (len(word2) + 1)
        for i in range(len(word1) + 1):
            temp = [0] * (len(word2) + 1)
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    temp[j] = DP[j - 1]
                else:
                    temp[j] = 1 + min(DP[j], temp[j - 1])
            DP = temp
        return DP[len(word2)]
