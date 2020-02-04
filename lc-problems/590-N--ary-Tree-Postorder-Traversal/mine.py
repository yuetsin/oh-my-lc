#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        vals = []

        def traverse(node: 'Node'):
            if not node:
                return

            for child in node.children:
                traverse(child)

            vals.append(node.val)

        traverse(root)

        return vals
