#!/usr/bin/env python


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        if not arr:
            return 0

        sarr = sorted(arr)

        bag = set()
        s_bag = set()

        count = 0

        for i in range(len(arr)):
            bag.add(arr[i])
            s_bag.add(sarr[i])

            if bag == s_bag:
                count += 1
                bag.clear()
                s_bag.clear()

        return count
