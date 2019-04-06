# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        last = None
        node = head
        while node != None and node.next != None:
            if node.val == node.next.val:
                nextNode = node
                prev = None
                while nextNode != None and (prev == None or nextNode.val == prev.val):
                    prev = nextNode
                    nextNode = nextNode.next
                if last != None:
                    last.next = nextNode
                    node = nextNode
                else:
                    head = nextNode
                    return self.deleteDuplicates(head)
            else:
                last = node
                node = node.next
        return head
