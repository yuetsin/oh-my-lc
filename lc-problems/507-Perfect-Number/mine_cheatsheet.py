#!/usr/bin/env python


class Solution:
    nums = {6, 28, 496, 8128, 33550336}

    def checkPerfectNumber(self, num: int) -> bool:
        return num in self.nums
