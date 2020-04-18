#!/usr/bin/env python

from functools import lru_cache

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        
        if N <= 1:
            # por una cabeza
            return 0
        
        visited = set()
        
        def tryArrive(x: int, y: int, depth: int) -> int:
            # print("entered tryArrive with", x, y, depth)
            
            if x == N - 1 and y == N - 1:
                return 0
            
            if (x, y) in visited:
                return float('+inf')
            
            visited.add((x, y))
            
            minSteps = float('+inf')
            
            if x > 0 and grid[y][x - 1] <= depth:
                minSteps = min(minSteps, tryArrive(x - 1, y, depth))
            if x < N - 1 and grid[y][x + 1] <= depth:
                minSteps = min(minSteps, tryArrive(x + 1, y, depth))
            if y > 0 and grid[y - 1][x] <= depth:
                minSteps = min(minSteps, tryArrive(x, y - 1, depth))
            if y < N - 1 and grid[y + 1][x] <= depth:
                minSteps = min(minSteps, tryArrive(x, y + 1, depth))
            
            visited.remove((x, y))
            
            # nowhere to go, currently
            if minSteps == float('+inf'):
                minSteps = 1 + tryArrive(x, y, depth + 1)
                
            return minSteps
                
        
        result = tryArrive(0, 0, grid[0][0])
        
        if result == float('+inf'):
            return -1
        
        return result + grid[0][0]

