#!/usr/bin/env python


class Solution:
    def countPrimes(self, n: int) -> int:
        s = set()
        for i in range(2, n):
            s.add(i)
        for k in range(2, int(n / 2) + 1):
            if not k in s:
                continue
            value = k
            while value < n:
                value += k
                if value in s:
                    s.remove(value)
        return len(list(s))


s
