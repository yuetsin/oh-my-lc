# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        last = None
        while node:
            if last:
                if last.val == node.val:
                    last.next = node.next
                    node = node.next
                    continue

            last = node
            node = node.next

        return head
