#!/usr/bin/env python


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        return (self.minheap[0] + (-self.maxheap[0]))/2 if len(self.minheap) == len(self.maxheap) else self.minheap[0]
