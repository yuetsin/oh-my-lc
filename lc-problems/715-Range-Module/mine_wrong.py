#!/usr/bin/env python

from functools import lru_cache


class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        # print("before addRange(%d, %d), self.ranges = %s" % (left, right, self.ranges))
        self.ranges.append((left, right))

    def queryRange(self, left: int, right: int) -> bool:
        # print("before queryRange(%d, %d), self.ranges = %s" % (left, right, self.ranges))

        if left >= right:
            return True

        for rng in self.ranges:
            # range[0], range[1], left, right
            # or
            # left, right, range[0], range[1]
            # has nothing go
            if rng[1] <= left or rng[0] >= right:
                continue

            # left, rng[0], right, rng[1]
            if left <= rng[0] and rng[0] <= right and right <= rng[1]:
                if self.queryRange(left, rng[0]):
                    return True

            # rng[0], left, rng[1], right
            if rng[0] <= left and left <= rng[1] and rng[1] <= right:
                if self.queryRange(rng[1], right):
                    return True

            # left, rng[0], rng[1], right
            if left <= rng[0] and rng[0] <= rng[1] and rng[1] <= right:
                if self.queryRange(left, rng[0]) and self.queryRange(rng[1], right):
                    return True

            # rng[0], left, right, rng[1]
            if rng[0] <= left and right <= rng[1]:
                return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        # print("before removeRange(%d, %d), self.ranges = %s" % (left, right, self.ranges))
        new_rng = []
        for rng in self.ranges:

            # left, rng[0], right, rng[1]
            if left <= rng[0] and rng[0] <= right and right <= rng[1]:
                if left < rng[0]:
                    new_rng.append((left, rng[0]))

            # rng[0], left, rng[1], right
            elif rng[0] <= left and left <= rng[1] and rng[1] <= right:
                if rng[1] < right:
                    new_rng.append((rng[1], right))

            # left, rng[0], rng[1], right
            elif left <= rng[0] and rng[1] <= right:
                pass

            # rng[0], left, right, rng[1]
            elif rng[0] <= left and right <= rng[1]:
                if rng[0] < left:
                    new_rng.append((rng[0], left))

                if right < rng[1]:
                    new_rng.append((right, rng[1]))
            else:
                # totally irrelevant!
                new_rng.append(rng)

        self.ranges = new_rng


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
