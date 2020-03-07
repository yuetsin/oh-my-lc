#!/usr/bin/env python

from functools import lru_cache

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        
        mines_set = set()
        
        for mine in mines:
            mines_set.add((mine[0], mine[1]))
        
        max_aaps = 0
        
        @lru_cache(maxsize=None)
        def judge(x: int, y: int) -> bool:
            if x < 0 or x >= N or y < 0 or y >= N:
                return False
            
            return not ((x, y) in mines_set)
        
        for x in range(N):
            if x < max_aaps or x >= N - max_aaps:
                continue
            for y in range(N):
                if y < max_aaps or y >= N - max_aaps:
                    continue
                if not (x, y) in mines_set:
                    aaps = 1
                    while True:
                        if judge(x - aaps, y) and judge(x + aaps, y) and judge(x, y - aaps) and judge(x, y + aaps):
                            aaps += 1
                        else:
                            break
                    
                    max_aaps = max(max_aaps, aaps)
                    
        return max_aaps