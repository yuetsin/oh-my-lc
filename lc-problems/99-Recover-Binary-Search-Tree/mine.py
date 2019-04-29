# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        def getInOrder(root: TreeNode):
            if root == None:
                return
            getInOrder(root.left)
            inorder.append(root)
            getInOrder(root.right)
        
        getInOrder(root)
        
        nums = []
        numb = []
        for i in inorder:
            nums.append(i)
            numb.append(i)
        
        numb.sort(key=lambda i : i.val)
        
        for k in range(len(nums)):
            if nums[k] != numb[k]:
                nums[k].val, numb[k].val = numb[k].val, nums[k].val
                break
        