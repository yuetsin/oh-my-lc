#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def getStr(node: TreeNode) -> List[str]:

            lst = []
            if node.left != None:
                lst += getStr(node.left)

            if node.right != None:
                lst += getStr(node.right)

            if node.left == None and node.right == None:
                return [str(node.val)]

            return [str(node.val) + s for s in lst]

        global_rst = 0

        strs = getStr(root)
        for s in strs:
            global_rst += int(s)

        return global_rst
