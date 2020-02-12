#!/usr/bin/env python

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        if s == '':
            return 0
        
        last = None
        counter = 0
        
        sums = []
        
        for i in range(len(s)):
            char = s[i]
            if char == last:
                counter += 1
            else:
                sums.append(counter)
                last = char
                counter = 1
        
        sums.pop(0)
        sums.append(counter)
        
        res = 0
        
        for i in range(len(sums) - 1):
            res += min(sums[i], sums[i + 1])
        
        return res