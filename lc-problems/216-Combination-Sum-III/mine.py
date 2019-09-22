#!/usr/bin/env python


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # DP = {}

        def getCal(k: int, n: int, usable: set) -> List[List[int]]:
            # print("k, n, usable: ", k, n, usable)
            # if (k, n) in DP:
            #     return DP[(k, n)]
            if k == 1:
                if n in usable:
                    return [[n]]
                else:
                    return []
            possible = []
            for num in list(usable):
                if num >= n:
                    continue
                suffixList = getCal(
                    k - 1, n - num, usable.difference(set([num])))
                for suffix in suffixList:
                    result = sorted([num] + suffix)
                    if not result in possible:
                        possible.append(result)
            # DP.update({(k, n): possible})

            return possible
        return getCal(k, n, set(range(1, 10)))
