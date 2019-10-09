#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    lst = []

    def expandList(self, count: int):
        toAdd = count - len(self.lst)
        if toAdd <= 0:
            return
        for _ in range(toAdd):
            self.lst.append('N')

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.lst = []

        def serial(node, since):
            if node == None:
                return
            self.expandList(since)
            self.lst[since - 1] = str(node.val)
            serial(node.left, since * 2)
            serial(node.right, since * 2 + 1)
        serial(root, 1)
        print("serialized: %s" % ','.join(self.lst))
        return ','.join(self.lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(',')
        nodes = []
        for k in tokens:
            if k == 'N':
                nodes.append(None)
            else:
                try:
                    nodes.append(TreeNode(int(k)))
                except:
                    nodes.append(None)

        limit = len(nodes) // 2

        for i in range(limit):
            if nodes[i] == None:
                continue
            if (i + 1) * 2 - 1 < len(nodes):
                nodes[i].left = nodes[(i + 1) * 2 - 1]
            if (i + 1) * 2 < len(nodes):
                nodes[i].right = nodes[(i + 1) * 2]
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
