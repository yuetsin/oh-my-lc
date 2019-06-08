#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        if head == None:
            return
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        alla = []
        while head != None:
            alla.append(head)
            head = head.next
        startp = 0
        endp = len(alla) - 1
        lenlimit = endp
        # for i in alla:
        # i.next = None
        while endp - startp > 1:
            print endp, startp
            alla[startp].next = alla[endp]
            alla[endp].next = alla[startp + 1]
            endp -= 1
            startp += 1
        if endp == startp + 1:
            alla[startp].next = alla[endp]
        else:
            if endp < lenlimit:
                alla[endp + 1].next = alla[endp]
        alla[endp].next = None
