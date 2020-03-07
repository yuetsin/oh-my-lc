#!/usr/bin/env python

from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        types = dict(Counter(S))
        
        lens = len(S)
        
        array = []
        for k, v in sorted(types.items(), key=lambda v: v[1]):
            if v > (lens + 1) // 2:
                # Impossible to accomplish!
                return ''
            array.extend(k * v)
        
        ans = [None] * lens
        ans[::2], ans[1::2] = array[lens // 2:], array[:lens // 2]
        return "".join(ans)