#!/usr/bin/env python

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        
        # O(N^2)? is that fine?
        placed = []
        result = []
        
        current_max = 0
        for square in positions:
            left, right, height = square[0], square[0] + square[1], square[1]
            
            related = []
            for item in placed:
                if item[0] >= right or item[1] <= left:
                    # no overlapping things
                    continue
                
                related.append(item)
            
            # print(related)
            if related:
                floor = max([v[2] for v in related])
                heig = floor + height
            else:
                heig = height
            
            current_max = max(current_max, heig)
            result.append(current_max)
            placed.append((square[0], square[0] + square[1], heig))
            
        return result