# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        value = sum - root.val
        if value == 0 and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, value) or self.hasPathSum(root.right, value)
