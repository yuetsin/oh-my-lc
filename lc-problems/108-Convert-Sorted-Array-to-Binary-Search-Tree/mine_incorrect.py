#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def insertNode(val: int, node: TreeNode):
            if val < node.val:
                if node.left != None:
                    insertNode(val, node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right != None:
                    insertNode(val, node.right)
                else:
                    node.right = TreeNode(val)
        if nums == []:
            return None
        root = TreeNode(nums[0])
        for i in nums[1:]:
            insertNode(i, root)
        return root
