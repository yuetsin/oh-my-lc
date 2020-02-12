#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return TreeNode(val)
        
        def doInsert(node: TreeNode):
            if node.val < val:
                if node.right:
                    doInsert(node.right)
                else:
                    node.right = TreeNode(val)
            elif node.val > val:
                if node.left:
                    doInsert(node.left)
                else:
                    node.left = TreeNode(val)
        
        doInsert(root)
        return root