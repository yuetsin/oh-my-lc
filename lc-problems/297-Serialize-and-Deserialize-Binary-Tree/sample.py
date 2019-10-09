#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ""
        d = collections.deque()
        d.append(root)
        while d:
            n = d.popleft()
            if n == "None":
                res.append(n)
                continue
            else:
                res.append(str(n.val))
            if n.left:
                d.append(n.left)
            else:
                d.append("None")
            if n.right:
                d.append(n.right)
            else:
                d.append("None")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        d = collections.deque()
        l = data.split(",")
        root = TreeNode(l[0])
        d.append(root)
        i = 0
        while d:
            n = d.popleft()
            left = i+1
            right = i+2
            if l[left] == "None":
                n.left = None
            else:
                n.left = TreeNode(l[left])
                d.append(n.left)
            if l[right] == "None":
                n.right = None
            else:
                n.right = TreeNode(l[right])
                d.append(n.right)
            i += 2

        return root
