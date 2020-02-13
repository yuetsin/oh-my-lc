#!/usr/bin/env python

import random


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.count = N - len(blacklist)

    def pick(self) -> int:
        # random.randint is [a, b]
        index = random.randint(0, self.count - 1)
        # print("origin = %d" % index)

        for i in self.blacklist:
            if index >= i:
                index += 1

        # print("fixed = %d" % index)
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
