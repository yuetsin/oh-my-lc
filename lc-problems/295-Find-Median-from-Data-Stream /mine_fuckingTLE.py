#!/usr/bin/env python


class MedianFinder:

    data = []
    length = 0

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.data.append(num)

        insert_point = self.length
        for i in range(self.length):
            if self.data[i] >= num:
                insert_point = i
                break
        self.data.insert(insert_point, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length == 0:
            return 0.0
        if self.length % 2 == 1:
            return self.data[self.length // 2]
        else:
            return (self.data[self.length // 2] + self.data[self.length // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
