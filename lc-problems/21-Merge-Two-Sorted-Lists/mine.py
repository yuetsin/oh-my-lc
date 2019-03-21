# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(42)

        lptr = l1
        rptr = l2

        node = newList
        while lptr != None and rptr != None:

            idx = 0
            min =
            if lptr.val < rptr.val:
                node.next = ListNode(lptr.val)
                lptr = lptr.next
            else:
                node.next = ListNode(rptr.val)
                rptr = rptr.next
            node = node.next

        if lptr != None:
            node.next = lptr
        elif rptr != None:
            node.next = rptr
        return newList.next
