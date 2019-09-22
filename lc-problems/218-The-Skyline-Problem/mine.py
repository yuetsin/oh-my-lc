#!/usr/bin/env python


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if buildings == []:
            return []
        width = max(tup[1] for tup in buildings) + 1
        height_map = [0] * width

        for building in buildings:
            for i in range(building[0], building[1]):
                height_map[i] = max(height_map[i], building[2])
        print(height_map)
        skylines = []
        for i in range(0, width):
            if height_map[i] != height_map[i - 1]:
                skylines.append([i, height_map[i]])
        return skylines
