#!/usr/bin/env python3


class Solution():
    def maxProfit(self, prices):
        return sum([b-a for a, b in zip(prices, prices[1:]) if b-a > 0])
