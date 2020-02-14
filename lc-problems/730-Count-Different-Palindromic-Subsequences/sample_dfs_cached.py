#!/usr/bin/env python
#
# written by @flamesofmoon

from functools import lru_cache


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        # returns the number of distinct palindromes in S[start:end]
        def dfs(start, end):
            count = 0
            segment = S[start:end]

            for x in 'abcd':
                try:
                    i = segment.index(x) + start  # the starting index in S
                    j = segment.rindex(x) + start  # the ending index in S
                except:
                    continue

                count += dfs(i+1, j) + 2 if i != j else 1

            return count % MOD

        return dfs(0, len(S))
