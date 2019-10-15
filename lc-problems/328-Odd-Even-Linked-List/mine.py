#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = []
        evens = []

        node = head

        Even = True
        while node:
            if Even:
                odds.append(node)
            else:
                evens.append(node)
            Even = not Even
            node = node.next

        result = odds + evens + [None]

        for i in range(len(result) - 1):
            result[i].next = result[i + 1]
        return result[0]
