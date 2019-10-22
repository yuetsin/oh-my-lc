#!/usr/bin/env python


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = set()

    def addNum(self, val: int) -> None:
        self.numbers.add(val)

    def getIntervals(self) -> List[List[int]]:
        pairs = []
        lastNum = None
        lastEnds = None
        for num in sorted(list(self.numbers)):
            if lastEnds != None:
                if num - lastEnds == 1:
                    lastEnds = num
                else:
                    pairs.append([lastNum, lastEnds])
                    lastNum = num
                    lastEnds = num
            else:
                lastNum = num
                lastEnds = num
        pairs.append([lastNum, lastEnds])
        return pairs


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
