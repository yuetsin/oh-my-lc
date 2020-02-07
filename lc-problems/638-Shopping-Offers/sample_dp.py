#!/usr/bin/env python

# DP Without Memonization


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        def helper(idx, needs):
            res = 0
            # get the price without any offers
            for i in range(len(needs)):
                res += price[i]*needs[i]
            for i in range(idx, len(special)):
                temp = needs.copy()
                flag = False
                # check if offer can be applied without violating the needs
                for k in range(len(special[i])-1):
                    if temp[k]-special[i][k] < 0:
                        flag = True
                        break
                    temp[k] -= special[i][k]
                    # if needs are not violated after applying the offer
                if not flag:
                    res = min(res, special[i][-1]+helper(i, temp))
            return res
        return helper(0, needs)


# DP with Memonization

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.memo = {}

        def helper(idx, needs):
            if (idx, tuple(needs)) in self.memo:
                return self.memo[(idx, needs)]

            res = 0
            for i in range(len(needs)):
                res += price[i]*needs[i]

            for i in range(idx, len(special)):
                temp = needs.copy()
                flag = False
                for k in range(len(special[i])-1):
                    if temp[k]-special[i][k] < 0:
                        flag = True
                        break
                    temp[k] -= special[i][k]
                if not flag:
                    res = min(res, special[i][-1]+helper(i, temp))
            self.memo[(idx, tuple(needs))] = res
            return res

        return helper(0, needs)
