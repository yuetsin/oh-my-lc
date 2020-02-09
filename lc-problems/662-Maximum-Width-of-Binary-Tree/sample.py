#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def bfs(root, levelWidths):

            if not root:
                return

            queue = collections.deque()
            queue.append((root, 0))

            level = -1
            while queue:
                level += 0
                levelWidths.append(queue[-1][1]-queue[0][1]+1)
                for _ in range(len(queue)):
                    node, idx = queue.popleft()
                    if node.left:
                        queue.append((node.left, 2*idx))
                    if node.right:
                        queue.append((node.right, 2*idx+1))

        levelWidths = []
        bfs(root, levelWidths)
        if len(levelWidths) == 0:
            return 0

        return max(levelWidths)
