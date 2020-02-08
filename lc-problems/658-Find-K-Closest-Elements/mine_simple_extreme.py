#!/usr/bin/env python

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda diff: abs(diff - x))
        return sorted(arr[:k])