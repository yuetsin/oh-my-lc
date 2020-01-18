#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        result = []

        def traverseNode(node: 'Node', level: int):
            while len(result) <= level:
                result.append([])
            result[level].append(node.val)
            for ch in node.children:
                traverseNode(ch, level + 1)

        traverseNode(root, 0)

        return result
