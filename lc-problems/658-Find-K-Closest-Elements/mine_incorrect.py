#!/usr/bin/env python

import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr, x)
        # print(index)

        index = index - k // 2
        r = min(max(0, index), len(arr) - k)

        return arr[r: r + k]
