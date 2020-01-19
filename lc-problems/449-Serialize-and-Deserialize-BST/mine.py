#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        nodes = []

        def putnodes(node: TreeNode):
            if node:
                nodes.append(node)
                putnodes(node.left)
                putnodes(node.right)

        putnodes(root)

        final_strs = []
        for node in nodes:
            left_i = nodes.index(node.left) if node.left else -1
            right_i = nodes.index(node.right) if node.right else -1
            final_strs.append("%d,%d,%d" % (node.val, left_i, right_i))

        return '\n'.join(final_strs)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        node_strs = data.split('\n')
        nodes = []
        for node in node_strs:
            if node == '':
                continue
            val, _, _ = node.split(',')
            nodes.append(TreeNode(int(val)))

        counter = 0
        for node in node_strs:
            if node == '':
                continue
            _, left, right = node.split(',')
            nodes[counter].left = nodes[int(left)] if int(left) != -1 else None
            nodes[counter].right = nodes[int(right)] if int(
                right) != -1 else None
            counter += 1

        return nodes[0] if nodes != [] else None
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
