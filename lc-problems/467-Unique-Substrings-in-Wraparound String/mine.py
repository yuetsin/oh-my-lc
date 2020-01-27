#!/usr/bin/env python

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # s = 'abcdefghijklmnopqrstuvwxyz'
        possible = set()
        
        for i in range(len(p)):
            # find the start point from p
            chains = [p[i]]
            last = p[i]
            possible.add(p[i])
            for j in range(i + 1, len(p)):
                if (ord(p[j]) - ord(last)) % 26 == 1:
                    chains.append(p[j])
                    last = p[j]
                    possible.add(''.join(chains))
        
        # print(possible)
        return len(possible)