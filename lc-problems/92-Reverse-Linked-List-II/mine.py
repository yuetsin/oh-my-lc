# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        plist = []
        node = head
        while node != None:
            plist.append(node)
            node = node.next
        inv = plist[m - 1 : n]
        inv.reverse()
        plist = plist[: m - 1] + inv + plist[n:] + [None]
        for i in range(len(plist) - 1):
            plist[i].next = plist[i + 1]
        return plist[0]