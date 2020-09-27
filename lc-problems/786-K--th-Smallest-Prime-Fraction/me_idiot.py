#!/usr/bin/env python

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        dic = {}
        for top in A:
            for bottom in A:
                dic.update({(top, bottom): top / bottom})

        return list(sorted(dic.items(), key=lambda d: d[1])[K - 1][0])
