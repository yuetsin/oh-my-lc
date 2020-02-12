#!/usr/bin/env python

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.r = [False] * 1000001

    def add(self, key: int) -> None:
        self.r[key] = True

    def remove(self, key: int) -> None:
        self.r[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.r[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)