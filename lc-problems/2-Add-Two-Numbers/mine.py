# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def makeCarry(node):
    if node.val < 9:
        node.val += 1
    else:
        node.val = 0
        if node.next != None:
            makeCarry(node.next)
        else:
            node.next = ListNode(1)


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        start = ListNode(-1)
        node = start
        while l1 != None and l2 != None:
            this_val = (l1.val + l2.val + carry) % 10
            carry = 1 if l1.val + l2.val + carry > 9 else 0
            node.next = ListNode(this_val)
            l1 = l1.next
            l2 = l2.next
            node = node.next

        if l1 != None:
            node.next = l1
            if carry == 1:
                makeCarry(l1)
            return start.next
        elif l2 != None:
            node.next = l2
            if carry == 1:
                makeCarry(l2)
            return start.next
        else:
            if carry == 1:
                node.next = ListNode(1)
            return start.next
