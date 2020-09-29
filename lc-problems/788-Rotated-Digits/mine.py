#!/usr/bin/env python3

from functools import lru_cache

class Solution:
    def rotatedDigits(self, N: int) -> int:
        
        diff_rot = '2569'
        ident_rot = '018'
        bad_rot = '347'
        
        @lru_cache(maxsize=10000)
        def isGood(n: int) -> bool:
            s = str(n)
            for bad_token in bad_rot:
                if bad_token in s:
                    return False
                
            for diff_tok in diff_rot:
                if diff_tok in s:
                    return True
                
            return False
        
        return sum([1 if isGood(v) else 0 for v in range(1, N + 1)])