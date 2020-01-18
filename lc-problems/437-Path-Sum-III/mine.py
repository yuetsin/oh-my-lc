#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, node: TreeNode, sum_v: int, selected: bool = False) -> int:

        if not node:
            return 0

        val = node.val

        choices = 0
        if val == sum_v:
            choices += 1
            # we can just stop here anyway

        choices += self.pathSum(node.left, sum_v - val, True)
        choices += self.pathSum(node.right, sum_v - val, True)

        if not selected:
            choices += self.pathSum(node.left, sum_v, False)
            choices += self.pathSum(node.right, sum_v, False)
        # print("node.val = %d, target sum = %d, choices = %d" % (val, sum_v, choices))
        return choices
