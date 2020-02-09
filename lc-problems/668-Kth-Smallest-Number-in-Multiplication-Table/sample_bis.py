#!/usr/bin/env python


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Don't you dare construct the actual table.

        def enough(x):
            count = 0
            for i in xrange(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
