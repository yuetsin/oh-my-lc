#!/usr/bin/env python3

from functools import lru_cache


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        travels = {}
        for sr, ds, cost in flights:
            travels.update({(sr, ds): cost})

        @lru_cache(maxsize=None)
        def get_price(at: int, flight_left: int) -> int:
            # print(at, flight_left)
            if at == dst:
                return 0
            if flight_left < 0:
                return -1
            min_cost = float('+inf')
            for target in range(n):
                if target == at:
                    continue
                if not (at, target) in travels:
                    continue
                cost = get_price(target, flight_left - 1)
                if cost != -1:
                    min_cost = min(min_cost, cost + travels[(at, target)])

            return min_cost if min_cost != float('+inf') else -1

        return get_price(src, K)
