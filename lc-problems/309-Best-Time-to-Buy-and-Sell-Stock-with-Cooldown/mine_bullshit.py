#!/usr/bin/env python


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)

        DP = {}

        def getProfit(since: int, bought: bool, lastBought: int = 0) -> int:
            if since >= length:
                return 0
            if (since, bought, lastBought) in DP:
                return DP[(since, bought, lastBought)]
            result = None
            if bought:
                # 可以卖掉, 所以多一个 cooldown
                result = max(getProfit(
                    since + 2, False) + prices[since] - lastBought, getProfit(since + 1, True, lastBought))
            else:
                # 不买或者买
                result = max(getProfit(since + 1, False),
                             getProfit(since + 1, True, prices[since]))

            DP.update({
                (since, bought, lastBought): result
            })
            return result

        return getProfit(0, False)
