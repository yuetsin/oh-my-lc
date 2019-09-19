#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        nodes = []
        node = head
        while node != None:
            if node.val != val:
                nodes.append(node)
            node = node.next
        if len(nodes) == 0:
            return None
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
