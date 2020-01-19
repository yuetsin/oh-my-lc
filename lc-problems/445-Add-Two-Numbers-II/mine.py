#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = 0
        v2 = 0
        while l1:
            v1 *= 10
            v1 += l1.val
            l1 = l1.next

        while l2:
            v2 *= 10
            v2 += l2.val
            l2 = l2.next

        result = v1 + v2

        if result == 0:
            return ListNode(0)

        last = None
        while result != 0:
            node = ListNode(result % 10)
            node.next = last
            last = node
            result = result // 10

        return node
