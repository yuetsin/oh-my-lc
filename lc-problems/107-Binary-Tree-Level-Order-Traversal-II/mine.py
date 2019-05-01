# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    max_level = -1

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        global_lst = []

        def goLevel(node: TreeNode, level: int):
            if node == None:
                return
            while level > self.max_level:
                global_lst.append([])
                self.max_level += 1
            global_lst[level].append(node.val)
            goLevel(node.left, level + 1)
            goLevel(node.right, level + 1)
        goLevel(root, 0)
        global_lst.reverse()
        return global_lst
