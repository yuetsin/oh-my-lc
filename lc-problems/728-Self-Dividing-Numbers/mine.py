#!/usr/bin/env python

from functools import lru_cache


class Solution:

    @lru_cache(maxsize=10000)
    def judge(self, i: int) -> bool:
        s = str(i)
        if '0' in s:
            return False

        for ch in s:
            if ch == 1:
                continue
            if i % int(ch) != 0:
                return False

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        result = []

        for i in range(left, right + 1):
            if self.judge(i):
                result.append(i)

        return result
