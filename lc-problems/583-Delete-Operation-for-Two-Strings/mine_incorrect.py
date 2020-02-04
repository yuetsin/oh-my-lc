#!/usr/bin/env python

from collections import Counter


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cnt1 = dict(Counter(word1))
        cnt2 = dict(Counter(word2))

        vals = 0
        for ch in 'qwertyuiopasdfghjklzxcvbnm':
            v1 = cnt1[ch] if ch in cnt1 else 0
            v2 = cnt2[ch] if ch in cnt2 else 0
            vals += abs(v1 - v2)

        return vals
