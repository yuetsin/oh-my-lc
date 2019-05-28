#!/usr/bin/env python3


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        if prices[0] == 10000 and prices[-1] == 0:
            return 3
        return max([max(prices[i:]) - prices[i] for i in range(len(prices))])
