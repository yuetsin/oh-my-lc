#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    copied = {}
    head = None

    def cloneGraph(self, node: 'Node') -> 'Node':
        self.copied = {}
        head = None
        queue = [node]
        while queue != []:
            nod = queue.pop(0)
            self.copied.update({nod.val: Node(nod.val, nod.neighbors)})
            if self.head == None:
                self.head = self.copied[nod.val]
            for i in nod.neighbors:
                if not i.val in self.copied:
                    queue.append(i)

        for i in self.copied:
            newngs = []
            for ng in self.copied[i].neighbors:
                newngs.append(self.copied[ng.val])
            self.copied[i].neighbors = newngs
        return self.head
