#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        node = head
        while node != None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
