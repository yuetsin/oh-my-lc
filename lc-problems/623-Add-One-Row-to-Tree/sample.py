#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def addarow(self, root, temp, v, d):
        if(not root):
            return

        if(d == 2):

            if(root.left):
                node = TreeNode(v)
                node.left = root.left
                root.left = node
            else:
                root.left = TreeNode(v)

            if(root.right):
                node = TreeNode(v)
                node.right = root.right
                root.right = node
            else:
                root.right = TreeNode(v)

            return root

        if(not root):
            return

        self.addarow(root.left, temp, v, d-1)
        self.addarow(root.right, temp, v, d-1)

        return temp

    def addOneRow(self, root, v, d):
        temp = root
        if(d == 1):
            node = TreeNode(v)
            node.left = root
            return node

        root = self.addarow(root, root, v, d)
        return(temp)
