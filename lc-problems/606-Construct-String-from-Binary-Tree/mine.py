#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""
        ret = str(t.val)

        if t.left:
            ret += '(%s)' % self.tree2str(t.left)
            if t.right:
                ret += '(%s)' % self.tree2str(t.right)
        else:
            if t.right:
                ret += '()(%s)' % self.tree2str(t.right)
        return ret
