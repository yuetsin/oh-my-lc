#!/usr/bin/env python

import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        if len(w) < 1:
            return

        self.w_sum = []

        total = 0
        for ww in w:
            total += ww
            self.w_sum.append(total)

        # print(self.w_sum)

        self.total = total

    def pickIndex(self) -> int:
        rand_v = random.randint(1, self.total)
        # print(rand_v)
        return bisect.bisect_left(self.w_sum, rand_v)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
