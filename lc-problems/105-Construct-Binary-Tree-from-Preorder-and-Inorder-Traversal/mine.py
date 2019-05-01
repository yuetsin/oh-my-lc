# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return
        root = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1: root + 1], inorder[:root])
        node.right = self.buildTree(preorder[root + 1:], inorder[root + 1:])

        return node
