#!/usr/bin/env python


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        mmaps = {}
        for pair in intervals:
            begin, end = pair
            if begin in mmaps:
                mmaps[begin] += 1
            else:
                mmaps.update({begin: 1})

            if end in mmaps:
                mmaps[end] -= 1
            else:
                mmaps.update({end: -1})

        ret = sorted(mmaps.items())

        last = None
        level = 0

        nums = 0
        for val, count in ret:
            if level >= 2 and last:
                nums += (val - last)
            level += count
            last = val

        return nums
