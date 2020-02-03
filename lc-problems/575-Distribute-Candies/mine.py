#!/usr/bin/env python


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        sets = set()

        for candy in candies:
            sets.add(candy)

        return min(len(sets), len(candies) // 2)
