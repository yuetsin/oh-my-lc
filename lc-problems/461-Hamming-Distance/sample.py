#!/usr/bin/env python

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(((x >> n) ^ (y >> n)) & 1 for n in range(32))