#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    max_result = None

    DP = {}

    def maxPathSum(self, root: TreeNode) -> int:

        if root == None:
            return -2147483648

        def maxPathSince(node: TreeNode) -> int:
            if node == None:
                return 0

            if not node in self.DP:

                max_val = 0

                if node.left != None:
                    max_val = maxPathSince(node.left)

                if node.right != None:
                    max_val = max(max_val, maxPathSince(node.right))

                self.DP.update({node: max(max_val + node.val, node.val)})

            return self.DP[node]

        def getMax(node: TreeNode):

            if node == None:
                return
            curr_val = max(maxPathSince(node.left), 0) + \
                max(maxPathSince(node.right), 0) + node.val
            if self.max_result == None or curr_val > self.max_result:
                self.max_result = curr_val

            getMax(node.left)
            getMax(node.right)

        getMax(root)
        return self.max_result
