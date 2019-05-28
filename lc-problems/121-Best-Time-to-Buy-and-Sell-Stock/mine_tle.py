#!/usr/bin/env python3


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max([max(prices[i:]) - prices[i] for i in range(len(prices))])
