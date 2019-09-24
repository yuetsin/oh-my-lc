#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        node = head
        vals = []
        while node != None:
            vals.append(node.val)
            node = node.next

        for i in range(len(vals) // 2):
            if vals[i] != vals[len(vals) - i - 1]:
                return False
        return True
