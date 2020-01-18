#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        result = []

        def appendNode(node: 'Node'):
            if not node:
                return
            result.append(node)
            appendNode(node.child)
            appendNode(node.next)
        appendNode(head)

        if len(result) == 0:
            return None

        result[0].prev = None
        result[0].next = result[1] if len(result) > 1 else None
        result[0].child = None

        result[-1].prev = result[-2] if len(result) > 1 else None
        result[-1].next = None
        result[-1].child = None

        for i in range(1, len(result) - 1):
            result[i].prev = result[i - 1]
            result[i].next = result[i + 1]
            result[i].child = None

        return result[0]
