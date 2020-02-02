#!/usr/bin/env python


class Solution:
    def intersect(self, tree1: 'Node', tree2: 'Node') -> 'Node':

        if tree1.isLeaf or tree2.isLeaf:
            tree, leaf = [tree1, tree2][::(None if tree2.isLeaf else -1)]
            return leaf if leaf.val else tree

        else:
            tl = self.intersect(tree1.topLeft, tree2.topLeft)
            tr = self.intersect(tree1.topRight, tree2.topRight)
            bl = self.intersect(tree1.bottomLeft, tree2.bottomLeft)
            br = self.intersect(tree1.bottomRight, tree2.bottomRight)

            if (
                tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                and tl.val == tr.val == bl.val == br.val
            ):
                return Node(tl.val, True, None, None, None, None)

            return Node(False, False, tl, tr, bl, br)
