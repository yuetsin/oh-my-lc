#!/usr/bin/env python


class Solution:
    def maxProfit(self, prices) -> int:
        upDown = []
        for i in range(1, len(prices)):
            upDown.append(prices[i] - prices[i - 1])

        prof = 0
        for i in upDown:
            if i > 0:
                prof += i

        return prof


# Another solution

class Solution2:
    def maxProfit(self, prices) -> int:
        last = None
        prof = 0
        for i in prices:
            if last == None:
                last = i
                continue
            if i - last > 0:
                prof += (i - last)
            last = i
        return prof
