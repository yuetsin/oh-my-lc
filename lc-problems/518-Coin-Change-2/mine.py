#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        coin_count = len(coins)

        @lru_cache(maxsize=None)
        def get_change(amount: int, since_coin: int = 0) -> int:
            if amount == 0:
                return 1

            if since_coin >= coin_count:
                return 0

            possible = 0
            for coin_i in range(since_coin, coin_count):
                if coins[coin_i] > amount:
                    break
                possible += get_change(amount - coins[coin_i], coin_i)

            return possible

        return get_change(amount)
