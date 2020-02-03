#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isIdentical(s: TreeNode, t: TreeNode) -> bool:
            if (not s) and (not t):
                return True
            if s and t:
                return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
            return False

        def isSub(s: TreeNode, t: TreeNode) -> bool:
            if isIdentical(s, t):
                return True

            if s:
                return isSub(s.left, t) or isSub(s.right, t)

            return False

        return isSub(s, t)
