#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        def getVal(elm):
            return elm.val
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key = getVal)
        nodes.append(None)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]