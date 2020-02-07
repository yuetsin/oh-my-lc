#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from statistics import mean


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        sums = []

        def traverse(node: TreeNode, depth: int):
            if not node:
                return

            while len(sums) <= depth:
                sums.append([])

            sums[depth].append(node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        res = []
        for tra in sums:
            res.append(mean(tra))
        return res
