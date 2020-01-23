#!/usr/bin/env python

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 求周长…
        height = len(grid)
        if height == 0:
            return 0
        
        width = len(grid[0])
        
        total_perimeter = 0
        
        for x in range(width):
            for y in range(height):
                if grid[y][x] == 0:
                    continue
                
                perimeter = 4
                if y > 0 and grid[y - 1][x] == 1:
                    perimeter -= 1
                if y < height - 1 and grid[y + 1][x] == 1:
                    perimeter -= 1
                if x > 0 and grid[y][x - 1] == 1:
                    perimeter -= 1
                if x < width - 1 and grid[y][x + 1] == 1:
                    perimeter -= 1
                
                total_perimeter += perimeter
        
        return total_perimeter