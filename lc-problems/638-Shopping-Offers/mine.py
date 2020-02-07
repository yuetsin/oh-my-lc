#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs_org: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(needs: tuple) -> int:
            # print(needs)
            res = 0

            for i in range(len(needs)):
                res += price[i] * needs[i]

            if res == 0:
                return 0

            for coupon in special:
                ok = True

                takens = []
                for i in range(len(needs)):
                    # print("compare %d and %d" % (coupon[i + 1], needs[i]))
                    if coupon[i] > needs[i]:
                        # cannot buy this one!
                        ok = False
                        break
                    takens.append(needs[i] - coupon[i])

                if ok:
                    # print("can take", takens)
                    res = min(res, coupon[-1] + dfs(tuple(takens)))

            return res

        return dfs(tuple(needs_org))
