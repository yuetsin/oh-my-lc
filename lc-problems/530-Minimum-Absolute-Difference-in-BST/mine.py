#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import bisect


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []

        def traverse(node: TreeNode):
            if not node:
                return
            bisect.insort_left(nums, node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        if len(nums) < 2:
            return 2147483647

        result = float('+inf')
        for i in range(len(nums) - 1):
            result = min(nums[i + 1] - nums[i], result)

        return result
        # print(nums)
