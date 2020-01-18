#!/usr/bin/env python


class Node:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.next = self.prev = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.head = Node(0)
        self.tail = Node(float("inf"))

        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.map:
            if self.head.next.val == 1:
                self.head.next.keys.add(key)
                self.map[key] = self.head.next
            else:
                new_node = Node(1)
                new_node.keys.add(key)

                next_to_head = self.head.next

                self.head.next = new_node
                new_node.prev = self.head
                next_to_head.prev = new_node
                new_node.next = next_to_head

                self.head.next = new_node
                self.map[key] = self.head.next

            return

        node = self.map[key]
        next_node = node.next

        val = node.val + 1
        node.keys.remove(key)

        if len(node.keys) == 0:
            tmp_p = node.prev
            tmp_n = node.next

            tmp_p.next = tmp_n
            tmp_n.prev = tmp_p
            node.next = None
            node.prev = None
            node = tmp_p

        if next_node.val == val:
            next_node.keys.add(key)
            self.map[key] = next_node
            return

        new_node = Node(val)
        new_node.keys.add(key)

        node.next = new_node
        new_node.prev = node

        next_node.prev = new_node
        new_node.next = next_node
        self.map[key] = new_node

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        prev_node = node.prev
        val = node.val - 1

        if len(node.keys) == 0:
            tmp_p = node.prev
            tmp_n = node.next

            tmp_p.next = tmp_n
            tmp_n.prev = tmp_p
            node.next = None
            node.prev = None
            node = tmp_n

        if val == 0:
            del self.map[key]
            return

        if prev_node.val == val:
            prev_node.keys.add(key)
            self.map[key] = prev_node
            return

        new_node = Node(val)
        new_node.keys.add(key)

        prev_node.next = new_node
        new_node.prev = prev_node

        node.prev = new_node
        new_node.next = node
        self.map[key] = new_node

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        max_node = self.tail.prev

        if max_node.val == 0:
            return ""

        for k in max_node.keys:
            return k

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        min_node = self.head.next

        if min_node.val == float("inf"):
            return ""

        for k in min_node.keys:
            return k


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
