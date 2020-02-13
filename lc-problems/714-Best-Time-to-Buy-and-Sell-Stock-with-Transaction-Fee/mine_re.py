#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        pricelen = len(prices)

        @lru_cache(maxsize=None)
        def doTrans(current: int, bought: int) -> int:
            if current >= pricelen:
                return 0

            if bought == -1:
                return max(doTrans(current + 1, -1), doTrans(current + 1, prices[current]))
            else:
                return max(doTrans(current + 1, -1) + prices[current] - bought - fee, doTrans(current + 1, bought))

        return doTrans(0, -1)
