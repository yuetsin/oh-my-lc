# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def enqueue(self, queue: List[ListNode], num: ListNode):
        queue[:-1] = queue[1:]
        queue[-1] = num

    queue_list = []

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        queue_list = [None] * (n + 1)
        node = head
        while node != None:
            self.enqueue(queue_list, node)
            node = node.next
        # print([nod.val for nod in queue_list[1:]])
        # print(queue_list[0])

        if queue_list[0] == None:
            try:
                return queue_list[2]
            except:
                return None

        if len(queue_list) < 3:
            queue_list[0].next = None
            return head

        queue_list[0].next = queue_list[2]
        return head
