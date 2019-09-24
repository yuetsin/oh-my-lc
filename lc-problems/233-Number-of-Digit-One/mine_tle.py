#!/usr/bin/env python


class Solution:
    def countDigitOne(self, n: int) -> int:
        self.DP = {}
        if n < 1:
            return 0

        currentCount = 0
        for i in range(1, n + 1):
            if i in self.DP:
                currentCount += self.DP[i]
            else:
                currentCount += str(i).count('1')
                self.DP.update({i: currentCount})
        return currentCount
