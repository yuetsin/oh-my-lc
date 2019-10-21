#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    DP = {}

    def rob(self, node: TreeNode, canRob: bool = True) -> int:

        # 偷出一棵 Tree 了…
        # 下次要不要去 Graph 里偷啊
        if (node, canRob) in self.DP:
            return self.DP[(node, canRob)]

        if node == None:
            return 0

        possible = 0
        if canRob:
            possible = max(possible,
                           self.rob(node.left, False) +
                           self.rob(node.right, False) +
                           node.val)
        # 不偷
        possible = max(possible,
                       self.rob(node.left) +
                       self.rob(node.right))

        self.DP.update({
            (node, canRob): possible
        })
        # print("node val: ", node.val, "canRob: ", canRob, "result: ", possible)
        return possible
