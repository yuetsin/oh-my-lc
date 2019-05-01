# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder == []:
            return
        root = inorder.index(postorder[-1])
        node = TreeNode(postorder[-1])
        node.left = self.buildTree(inorder[:root], postorder[:root])
        node.right = self.buildTree(inorder[root + 1:], postorder[root:-1])
        return node
