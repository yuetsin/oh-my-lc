#!/usr/bin/env python


class Solution:
    def numSquares(self, n: int) -> int:
        factors = []
        counter = 1
        while counter ** 2 <= n:
            factors.append(counter ** 2)
            counter += 1

#         factors.reverse()

        minDP = {}

        def findMin(n: int) -> int:
            # print("findMin called with n: ", n)
            if n == 0:
                return 0
            if n in minDP:
                return minDP[n]

            totMin = -1
            for v in factors:
                if v > n:
                    break
                ret = findMin(n - v)
                if ret != -1:
                    if totMin != -1:
                        totMin = min(totMin, ret)
                    else:
                        totMin = ret
            # print("findMin %d got %d" % (n, totMin + 1))
            minDP.update({n: totMin + 1})
            return totMin + 1
        return findMin(n)
