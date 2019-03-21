# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    empty_head = None

    def get_remain_len(self, node: ListNode) -> int:
        tmp_nod = node
        cnt = 0
        while tmp_nod != None:
            tmp_nod = tmp_nod.next
            cnt += 1
        return cnt

    def get_k_following(self, node: ListNode, cnt: int) -> ListNode:
        tmp_nod = node
        while cnt > 0 and tmp_nod.next != None:
            tmp_nod = tmp_nod.next
            cnt -= 1
        return tmp_nod

    def performFlip(self, head: ListNode, k: int):
        print("head = %d, remain = %d" % (head.val, self.get_remain_len(head)))
        if self.get_remain_len(head) < k + 1:
            # No enough nodes for a new flip
            # print("No enough nodes for a new flip. get_remain_len = %d, k = %d" % (self.get_remain_len(head), k))
            return
            # Let's stop them all

        else:

            preStart = head
            start = head.next

            for _ in range(k - 1):
                temp = start.next
                start.next = temp.next
                temp.next = preStart.next
                preStart.next = temp

            # print("OK Here")
            # print("Now, prev_node = %d, k = %d" % (self.get_k_following(head, k).val, k))
            return self.get_k_following(preStart, k)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        self.empty_head = ListNode(42)
        self.empty_head.next = head

        # print("Flip k = %d since %d" % (k, self.empty_head.val))

        rst = self.performFlip(self.empty_head, k)
        # return self.empty_head.next

        while rst != None:
            # print("rst_val = %d" % rst.val)
            # break
            rst = self.performFlip(rst, k)
            # break

        return self.empty_head.next
