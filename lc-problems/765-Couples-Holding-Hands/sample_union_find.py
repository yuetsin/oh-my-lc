#!/usr/bin/env python


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        d = [0] * N

        def find(a: int) -> int:
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]

        def union(a: int, b: int) -> int:
            d[find(a)] = find(b)

        # Initialize DS
        for i in range(0, N, 2):
            d[i] = d[i+1] = i

        # Union find
        for i in range(0, N, 2):
            union(row[i], row[i+1])

        # Total sets - available sets
        return (N//2) - sum([1 for i in range(0, N, 2) if i == d[i] == d[i+1]])
