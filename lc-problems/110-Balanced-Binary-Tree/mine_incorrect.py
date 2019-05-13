#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getDepth(self, root: TreeNode) -> (int, int):
        if root == None:
            return (0, 0)

        left = max(self.getDepth(root.left)) + 1
        right = max(self.getDepth(root.right)) + 1
        return (left, right)
    
    def checkValid(self, tpl: (int, int)) -> bool:
        return abs(tpl[0] - tpl[1]) <= 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not self.checkValid(self.getDepth(root)):
            return False
        return self.checkValid(self.getDepth(root.left)) and self.checkValid(self.getDepth(root.right))