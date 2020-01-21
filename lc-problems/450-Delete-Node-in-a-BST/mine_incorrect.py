#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        super_node = TreeNode('')
        super_node.right = root
        return self.deleteNodeWrapped(super_node, key).right

    def deleteNodeWrapped(self, super_node: TreeNode, key: int) -> TreeNode:

        def findNode(node: TreeNode, its_parent: TreeNode, left_and_not_right: bool) -> TreeNode:
            if not node:
                return None
            if node.val == key:
                return node, its_parent, left_and_not_right
            lf = findNode(node.left, node, True)
            if lf:
                return lf
            return findNode(node.right, node, False)

        rs = findNode(super_node, None, False)

        if rs:
            found_node, its_parent, is_left = rs
        else:
            # 没找到，那算了
            return super_node

        if found_node.left == None:
            # 没有左子树
            if found_node.right == None:
                # 也没有柚子树：叶子结点
                # 直接改父亲指针
                if is_left:
                    its_parent.left = None
                else:
                    its_parent.right = None
            else:
                # 是只有柚子树的中间节点，直接让父亲结点跳过它
                if is_left:
                    its_parent.left = found_node.right
                else:
                    its_parent.right = found_node.right
        elif found_node.right == None:
            # 此时不可能有是叶子结点的情况。因为上面处理过了 l r 都 None 的情况。
            if is_left:
                its_parent.left = found_node.left
            else:
                its_parent.right = found_node.left
        else:
            # 左右子结点都不是 None。难办了。
            # 先找出其值需要满足的条件

            parent_v = its_parent.val
            if is_left:
                # new node should be lesser than parent_v
                found_node.val, found_node.left.val = found_node.left.val, found_node.val
                return self.deleteNodeWrapped(super_node, key)
            else:
                # new node should be greater than parent_v
                found_node.val, found_node.right.val = found_node.right.val, found_node.val
                return self.deleteNodeWrapped(super_node, key)

        return super_node
