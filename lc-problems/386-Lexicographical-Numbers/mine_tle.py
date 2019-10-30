#!/usr/bin/env python


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1] * n
        last = 1
        for i in range(1, n):
            psbl = []
            if last * 10 <= n:
                last *= 10
            elif last + 1 <= n:
                last += 1
                while last % 10 == 0:
                    last //= 10
            else:
                last = last // 10 + 1
            result[i] = last
        return result
