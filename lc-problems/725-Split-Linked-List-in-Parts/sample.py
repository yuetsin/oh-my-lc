#!/usr/bin/env python


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        current = root
        length = 0
        while current:
            current, length = current.next, length + 1
        cs = length // k
        lcs = length % k
        result = [cs + 1] * lcs + [cs] * (k - lcs)
        print(result)
        prev = None
        current = root
        for i, num in enumerate(result):
            if prev:
                prev.next = None
            result[i] = current
            for i in range(num):
                prev, current = current, current.next
        return result
