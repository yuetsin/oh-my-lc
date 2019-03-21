# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        head_node = ListNode(42)
        head_node.next = head

        def swap_its_following(node: ListNode) -> ListNode:
            try:
                former = node.next
                latter = former.next
                latter.next
            except:
                return

            node.next = latter
            former.next = latter.next
            latter.next = former

            return former

        node = head_node

        while node != None:
            node = swap_its_following(node)

        return head_node.next
