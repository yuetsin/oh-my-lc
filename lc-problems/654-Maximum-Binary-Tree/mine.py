#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def constructMBT(since: int, till: int) -> TreeNode:
            if since >= till:
                return None
            max_v = float('-inf')
            max_i = None

            for i in range(since, till):
                if nums[i] > max_v:
                    max_v = nums[i]
                    max_i = i

            node = TreeNode(max_v)
            node.left = constructMBT(since, max_i)
            node.right = constructMBT(max_i + 1, till)

            return node

        return constructMBT(0, len(nums))
