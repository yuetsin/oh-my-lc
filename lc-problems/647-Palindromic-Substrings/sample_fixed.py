#!/usr/bin/env python


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        memo = [[False] * length for _ in range(length)]
        count = 0
        for i in range(length):
            for r in range(length - i):
                c = r + i
                if r == c:
                    memo[r][c] = True
                elif r + 1 == c:
                    memo[r][c] = (s[r] == s[c])
                else:
                    memo[r][c] = (memo[r + 1][c - 1] and s[r] == s[c])
                if memo[r][c]:
                    count += 1

        return count
