#!/usr/bin/env python


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.umap = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.umap:
            self.umap[key] += 1
        else:
            self.umap.update({key: 1})

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.umap:
            self.umap[key] -= 1
            if self.umap[key] == 0:
                del self.umap[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        result = ""
        max_v = float('-inf')
        for k, v in self.umap.items():
            if v > max_v:
                max_v = v
                result = k
        return result

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        result = ""
        min_v = float('+inf')
        for k, v in self.umap.items():
            if v < min_v:
                min_v = v
                result = k
        return result


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
