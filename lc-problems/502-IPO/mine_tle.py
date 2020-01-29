#!/usr/bin/env python


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:

        max_id = len(Profits)

        used = set()

        def getProfit(k: int, W: int) -> int:
            # print("called getProfit(k: %d, W: %d)" % (k, W))
            if k == 0:
                # That's all.
                return W

            prof = W
            for i in range(max_id):
                if i in used:
                    # 严禁双投
                    continue
                if Capital[i] <= W:
                    # 有本钱可以投资
                    used.add(i)
                    prof = max(prof, getProfit(k - 1, W + Profits[i]))
                    used.remove(i)

            return prof

        return getProfit(k, W)
