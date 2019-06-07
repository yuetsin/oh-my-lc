#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        self.org_nodes = []

        node = head
        while node != None:
            self.org_nodes.append(node)
            node = node.next

        new_nodes = []
        for i in range(len(self.org_nodes)):
            new_nodes.append(
                Node(self.org_nodes[i].val, None, self.org_nodes[i].random))
        new_nodes.append(None)
        for i in range(len(new_nodes) - 1):
            new_nodes[i].next = new_nodes[i + 1]

            if new_nodes[i].random != None:
                new_nodes[i].random = new_nodes[self.org_nodes.index(
                    new_nodes[i].random)]
        return new_nodes[0]
