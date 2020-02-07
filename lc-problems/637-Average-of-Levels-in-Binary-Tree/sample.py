#!/usr/bin/env python


def averageOfLevels(self, root: TreeNode) -> List[float]:

    if not root:
        return

    result = []

    queue = [[root, 1]]

    hsh = collections.defaultdict(int)
    hsh1 = collections.defaultdict(int)

    while queue:
        root, level = queue.pop(0)

        hsh[level] += root.val
        hsh1[level] += 1
        if root.left:
            queue.append([root.left, level+1])
        if root.right:
            queue.append([root.right, level+1])

    for a, b in zip(hsh.values(), hsh1.values()):
        result.append(a/b)

    return result
