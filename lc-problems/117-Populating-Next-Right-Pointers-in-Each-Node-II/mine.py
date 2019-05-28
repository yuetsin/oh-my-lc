#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return

        pre = root

        while True:
            cur = pre
            this_layer = []
            while cur:
                if cur.left != None:
                    this_layer.append(cur.left)
                if cur.right != None:
                    this_layer.append(cur.right)
                cur = cur.next

            if len(this_layer) == 0:
                break

            for i in range(len(this_layer) - 1):
                this_layer[i].next = this_layer[i + 1]

            expect = pre
            while True:
                expect = pre.left
                if expect == None:
                    expect = pre.right
                    if expect == None:
                        pre = pre.next
                    else:
                        break
                else:
                    break
            pre = expect
        return root
