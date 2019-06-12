#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        inset = set()
        inset.add(headA)
        while headA != None:
            if headA.next != None:
                if not headA.next in inset:
                    inset.add(headA.next)
                else:
                    return headA.next
            headA = headA.next

        if headB in inset:
            return headB

        while headB != None:
            if headB.next != None:
                if not headB.next in inset:
                    inset.add(headB.next)
                else:
                    return headB.next
            headB = headB.next
