#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next
        self.len = len(self.vals)

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.vals[random.randint(0, self.len - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
