#!/usr/bin/env python


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        flag = True
        if not val in self.list:
            flag = False
        self.list.insert(random.randint(0, self.count), val)
        self.count += 1
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.list:
            return False
        self.list.remove(val)
        self.count -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.count <= 0:
            return
        val = self.list[0]
        self.remove(val)
        self.insert(val)
        return val


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
