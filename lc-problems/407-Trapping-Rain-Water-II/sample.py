#!/usr/bin/env python

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0] or len(heightMap)<3 or len(heightMap[0])<3:
            return 0
        
        row_limit, col_limit = len(heightMap), len(heightMap[0])
        height_dict = {}
        water_top_heap = []
        # Check bondary first
        for c in range(col_limit):
            # Top boundary
            water_top_heap.append( (heightMap[0][c], (0, c)) )
            height_dict[(0, c)] = (heightMap[0][c])
            # Bottom boundary
            water_top_heap.append( (heightMap[row_limit-1][c], (row_limit-1, c)) )
            height_dict[(row_limit-1, c)] = (heightMap[row_limit-1][c])
        for r in range(row_limit):
            if (r, 0) not in height_dict:
                # Left boundary
                water_top_heap.append( (heightMap[r][0], (r, 0)) )
                height_dict[(r, 0)] = (heightMap[r][0])
            if (r, col_limit-1) not in height_dict:
                # Right boundary
                water_top_heap.append( (heightMap[r][col_limit-1], (r, col_limit-1)) )
                height_dict[(r, col_limit-1)] = (heightMap[r][col_limit-1])
        heapq.heapify(water_top_heap)
    
        res = 0
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        while water_top_heap:
            cur_height, cur_pos = heapq.heappop(water_top_heap)
            for i in range(4):
                nr, nc = cur_pos[0] + dr[i], cur_pos[1] + dc[i]
                if 0<=nr<row_limit and 0<=nc<col_limit and (nr, nc) not in height_dict:
                    if heightMap[nr][nc] > height_dict[cur_pos]: 
                        height_dict[(nr, nc)] = heightMap[nr][nc]
                    else:
                        height_dict[(nr, nc)] = height_dict[cur_pos]
                    res += height_dict[(nr, nc)] - heightMap[nr][nc]
                    heapq.heappush(water_top_heap, (heightMap[nr][nc], (nr, nc)) )
        return res