# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    max_level = 0

    def maxDepth(self, root: TreeNode) -> int:
        def goLevel(node: TreeNode, level: int):
            if node == None:
                return
            while level >= self.max_level:
                self.max_level += 1
            goLevel(node.left, level + 1)
            goLevel(node.right, level + 1)
        goLevel(root, 0)
        return self.max_level
