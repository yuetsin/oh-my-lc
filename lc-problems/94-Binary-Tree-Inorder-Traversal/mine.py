# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 中序遍历
        result = []
        def inOrder(node: TreeNode):
            if node != None:
                inOrder(node.left)
                result.append(node.val)
                inOrder(node.right)
        inOrder(root)
        return result