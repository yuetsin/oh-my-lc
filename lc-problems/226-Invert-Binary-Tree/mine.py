#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Trivia:
        # This problem was inspired by this original tweet by Max Howell:

        # Google: 90% of our engineers use the software you wrote (Homebrew),
        # but you can’t invert a binary tree on a whiteboard so f*** off.

        def invert(node: TreeNode):
            if node == None:
                return None
            if node.left != None and node.right != None:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
            elif node.left != None:
                node.left, node.right = None, node.left
                invert(node.right)
            elif node.right != None:
                node.left, node.right = node.right, None
                invert(node.left)
        invert(root)
        return root
