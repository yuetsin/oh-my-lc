#!/usr/bin/env python


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        d = [str(x) for x in range(1, n+1)]
        d.sort()
        return d
