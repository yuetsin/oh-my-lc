#!/usr/bin/env python


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = head
        to_append = None
        stack = []
        while head:
            if head.child:
                stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            if stack and not head.next:
                to_append = stack.pop()
                if to_append:
                    to_append.prev = head
                head.next = to_append
            head = head.next
        return dummy
