#!/usr/bin/env python3

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = ['']
        for ch in S:
            if ch.isalpha():
                results = [v + ch.upper() for v in results] + [v + ch.lower() for v in results]
                
            else:
                results = [v + ch for v in results]
                
        return results