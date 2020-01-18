#!/usr/bin/env python


class Solution:
    def pathSum(self, root: TreeNode, S: int) -> int:

        def dfs(node, sums, currSum):
            if not node:
                return
            newSum = node.val + currSum
            if newSum - S in sums:
                ans["num"] += sums[node.val + currSum - S]
            if not node.left and not node.right:
                return

            sums[newSum] = sums.get(newSum, 0) + 1
            dfs(node.left, sums, newSum)
            dfs(node.right, sums, newSum)
            sums[newSum] -= 1

        if not root:
            return 0

        ans = {"num": 0}
        sums = {0: 1}
        dfs(root, sums, 0)
        return ans["num"]
