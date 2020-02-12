#!/usr/bin/env python

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        y_max = len(grid)
        if y_max == 0:
            return 0
        x_max = len(grid[0])
        
        def dfs(x: int, y: int) -> int:
            # assert that grid[y][x] == 1.
            
            grid[y][x] = 0
            
            area = 1
            
            if x > 0 and grid[y][x - 1]:
                area += dfs(x - 1, y)
            
            if x < x_max - 1 and grid[y][x + 1]:
                area += dfs(x + 1, y)
                
            if y > 0 and grid[y - 1][x]:
                area += dfs(x, y - 1)
            
            if y < y_max - 1 and grid[y + 1][x]:
                area += dfs(x, y + 1)
                
            return area
        
        # dfs() will never be called twice.
        
        result = 0
        
        for x in range(x_max):
            for y in range(y_max):
                if grid[y][x]:
                    result = max(result, dfs(x, y))
        
        return result