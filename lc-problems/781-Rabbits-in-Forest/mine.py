#!/usr/bin/env python

from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = dict(Counter(answers))
        
        count = 0
        for colSet, rabCount in dic.items():
            count += (rabCount // (colSet + 1) + ( 1 if rabCount % (colSet + 1) else 0)) * (colSet + 1)
        return count