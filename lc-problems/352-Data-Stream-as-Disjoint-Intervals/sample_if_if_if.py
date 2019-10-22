#!/usr/bin/env python

import bisect


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inter = []

    def addNum(self, val: int) -> None:
        print(val)
        idx = bisect.bisect_left(self.inter, [val, val])
        left = idx-1
        right = idx
        if not self.inter:
            self.inter.append([val, val])
            return
        if left >= 0 and self.inter[left][0] <= val and self.inter[left][1] >= val:
            return
        if right <= len(self.inter)-1 and self.inter[right][0] <= val and self.inter[right][1] >= val:
            return
        if left >= 0 and right <= len(self.inter)-1 and self.inter[left][1] == val-1 and self.inter[right][0] == val+1:
            newi = [self.inter[left][0], self.inter[right][1]]
            del self.inter[right]
            del self.inter[left]
            bisect.insort(self.inter, newi)
        elif left >= 0 and self.inter[left][1] == val-1:
            newi = [self.inter[left][0], val]
            del self.inter[left]
            bisect.insort(self.inter, newi)
        elif right <= len(self.inter)-1 and self.inter[right][0] == val+1:
            newi = [val, self.inter[right][1]]
            del self.inter[right]
            bisect.insort(self.inter, newi)
        else:
            bisect.insort(self.inter, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.inter
