#!/usr/bin/env python


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0, ] * (num+1)
        dp[0] = 0
        if(num > 0):
            dp[1] = 1
        curr = 2
        for i in range(2, num+1):
            if(i == curr*2):
                curr = curr * 2

            dp[i] = dp[i % curr] + 1

        return dp
