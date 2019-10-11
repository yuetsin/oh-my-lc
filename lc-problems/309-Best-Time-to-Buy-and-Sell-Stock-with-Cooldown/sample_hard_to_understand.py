#!/usr/bin/env python


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0
        N = len(prices)
        buy = [0] * N
        s1 = [0] * N
        sell = [0] * N
        s2 = [0] * N
        s1[0] = buy[0] = -prices[0]
        sell[0] = s2[0] = 0
        for i in range(1, N):
            buy[i] = s2[i - 1] - prices[i]
            s1[i] = max(buy[i - 1], s1[i - 1])
            sell[i] = max(buy[i - 1], s1[i - 1]) + prices[i]
            s2[i] = max(s2[i - 1], sell[i - 1])
        return max(sell[N - 1], s2[N - 1])
