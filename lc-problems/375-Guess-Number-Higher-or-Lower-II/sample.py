#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0
            ans = float("inf")
            # mid start from (i + j) // 2.
            for mid in range((i + j) // 2, j + 1):
                left, right = dp(i, mid - 1), dp(mid + 1, j)
                tmp = mid + max(left, right)
                if tmp < ans:
                    ans = tmp
                if left > right:
                    # if the left part is larger than right one, we don't need to move any more.
                    break
            return ans
        return dp(1, n)
