#!/usr/bin/env python

import statistics


class MedianFinder:

    data = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        return statistics.median(self.data)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
