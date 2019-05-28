#!/usr/bin/env python

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        q = []
        q.append(root)

        while len(q) > 0:
            size = len(q)
            prev = None
            while size > 0:
                size -= 1
                node = q[0]
                q = q[1:]

                if prev != None:
                    prev.next = node
                prev = node
                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

        return root
