# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = []
        more = []
        node = head
        while node != None:
            if node.val < x:
                less.append(node)
            else:
                more.append(node)
            node = node.next
        
        less += more
        less.append(None)
        for i in range(len(less) - 1):
            less[i].next = less[i + 1]
        
        return less[0]