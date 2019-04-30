# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def isMirror(p: TreeNode, q: TreeNode) -> bool:
            if p == None:
                return q == None
            if q == None:
                return p == None
            return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
        return isMirror(root.left, root.right)