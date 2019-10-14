#!/usr/bin/env python


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        coins.sort()

        DP = {}

        def count(amount: int) -> int:
            if amount in DP:
                return DP[amount]
            possible = []

            for coin in coins:
                if coin > amount:
                    break
                elif coin == amount:
                    return 1
                rest = count(amount - coin)

                if rest == -1:
                    continue

                possible.append(rest + 1)

            DP.update({
                amount: min(possible) if possible else -1
            })
            return min(possible) if possible else -1

        return count(amount)
