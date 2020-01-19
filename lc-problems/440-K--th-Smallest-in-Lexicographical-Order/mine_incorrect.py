#!/usr/bin/env python


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        counter = 1
        val = 1

        stacks = [1]

        while counter < k and stacks != []:
            v = stacks.pop()
            times_v = v * 10
            while times_v <= n:
                stacks.append(times_v)
                times_v *= 10

            counter += 1

        return val
