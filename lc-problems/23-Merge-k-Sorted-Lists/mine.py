# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return

        # if lists[0] == None:
        #     return

        def insertValInto(node: ListNode, value: int):
            # if value == None:
            #     return
            # print("Insert value %d" % value)
            while node.next != None:
                if node.val >= value:
                    new_node = ListNode(node.val)
                    new_node.next = node.next
                    node.val = value
                    node.next = new_node
                    return
                node = node.next

            node.next = ListNode(value)
            if node.val > value:
                node.val, node.next.val = value, node.val

        newList = ListNode(-1000000)

        # listscount = len(lists)

        # ptrs = lists

        # node = newList

        # remove_count = 0
        while len(lists) != 0:
            # print("ptrs.count(None) = %d, listscount = %d. ptrs = %s" % (ptrs.count(None), listscount, ptrs))

            for idx in range(len(lists)):
                if lists[idx] == None:
                    continue
                insertValInto(newList, lists[idx].val)
                lists[idx] = lists[idx].next

            lists = list(filter(lambda a: a != None, lists))
            # print("Delete None values. now len(ptrs) = %d" % len(lists))

        return newList.next
