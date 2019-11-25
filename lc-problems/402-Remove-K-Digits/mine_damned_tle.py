#!/usr/bin/env python

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def removeKdigits(self, num: str, k: int) -> str:

        length = len(num)

        def __removeKdigits(since: int, k: int) -> str:
            # print("decide #", since, "with k =", k)

            if length - since == k:
                return ""

            if k == 0:
                return num[since:]

            v1 = __removeKdigits(since + 1, k - 1)
            v2 = num[since] + __removeKdigits(since + 1, k)

            if int(v1) > int(v2):
                return v2
            return v1

        v = __removeKdigits(0, k)
        if v == "":
            return "0"
        return str(int(v))
