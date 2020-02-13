#!/usr/bin/env python
#
# written by @je390


class RangeModule:

    def __init__(self): self.markers = []

    def f(self, v):
        lo, hi = 0, len(self.markers) - 1
        while(lo < hi):
            med = (lo + hi) // 2
            if self.markers[med] >= v:
                hi = med
            else:
                lo = med + 1
        return lo if (lo < len(self.markers)) and (self.markers[lo] >= v) else len(self.markers)

    def g(self, v):
        lo, hi = 0, len(self.markers) - 1
        while(lo < hi):
            med = (lo + hi) // 2
            if self.markers[med] > v:
                hi = med
            else:
                lo = med + 1
        return lo if (lo < len(self.markers)) and (self.markers[lo] > v) else len(self.markers)

    def addRange(self, left, right):
        i, j = self.f(left), self.g(right)
        self.markers = self.markers[:i] + ([left] if i % 2 == 0 else []) + (
            [right] if j % 2 == 0 else []) + self.markers[j:]

    def queryRange(self, left, right):
        i, j = self.g(left), self.f(right)
        return self.markers and (i == j) and i % 2 == 1 and i < len(self.markers)

    def removeRange(self, left, right):
        i, j = self.f(left), self.g(right)
        self.markers = self.markers[:i] + ([left] if i % 2 == 1 else []) + (
            [right] if j % 2 == 1 else []) + self.markers[j:]


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
