# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxVal(self, node: TreeNode) -> int:
        if node == None:
            return float('-inf')
        while node.right != None:
            node = node.right
        return node.val
    
    def minVal(self, node: TreeNode) -> int:
        if node == None:
            return float('inf')
        while node.left != None:
            node = node.left
        return node.val
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isValidBST(root.left) and \
    self.isValidBST(root.right) and \
    (self.maxVal(root.left) < root.val) and \
    (self.minVal(root.right) > root.val)