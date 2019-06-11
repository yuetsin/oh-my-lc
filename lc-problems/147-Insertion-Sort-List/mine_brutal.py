#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def getVal(elm):
            return elm.val
        # InsertionSort 这排序方法……
        # 甚至还没有我全提取出来之后排序快吧
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=getVal)
        nodes.append(None)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]
