#!/usr/bin/env python


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:

        if sum(machines) % len(machines) != 0:
            return -1

        target = sum(machines) // len(machines)
        over, res = 0, 0

        for m in machines:
            over += (m - target)
            res = max(res, max(abs(over), m - target))

        return res
