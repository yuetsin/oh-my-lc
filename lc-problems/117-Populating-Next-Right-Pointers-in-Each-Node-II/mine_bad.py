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

    special_value = 21748594028

    def root_connect(self, root: 'Node') -> 'Node':
        if root == None:
            return

        pre = root

        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left

        return root

    def fix_next(self, root: 'Node'):
        if root == None:
            return
        next_rec = root.left
        node = root

        while node:
            next_node = node.next
            if next_node == None:
                break
            while next_node.val != self.special_value:
                next_node = next_node.next
                if next_node == None:
                    node.next = None
                    break

            node.next = next_node
            node = node.next
        self.fix_next(next_rec)

    def connect(self, root: 'Node') -> 'Node':
        def initEmpty(root: 'Node'):
            if root.left == None and root.right == None:
                return

            if root.left == None:
                root.left = Node(self.special_value, None, None, None)
            if root.right == None:
                root.right = Node(self.special_value, None, None, None)

            initEmpty(root.left)
            initEmpty(root.right)

        initEmpty(root)
        self.root_connect(root)
        self.fix_next(root)

        return root
