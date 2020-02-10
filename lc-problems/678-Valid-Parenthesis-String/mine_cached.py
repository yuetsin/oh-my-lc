#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:

        lens = len(s)

        @lru_cache(maxsize=None)
        def checkVS(since: int, depth: int) -> bool:
            if depth < 0:
                return False

            if since >= lens:
                return depth == 0

            char = s[since]
            if char == '(':
                return checkVS(since + 1, depth + 1)
            elif char == ')':
                return checkVS(since + 1, depth - 1)
            elif char == '*':
                return checkVS(since + 1, depth + 1) or checkVS(since + 1, depth) or checkVS(since + 1, depth - 1)

            return False

        return checkVS(0, 0)
