#!/usr/bin/env python


class Solution:
    def bulbSwitch(self, n: int) -> int:
        starts = 1

        counter = 0
        while starts ** 2 <= n:
            counter += 1
            starts += 1

        return counter
