#!/usr/bin/env python


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islandList = []
        self.y_len = len(grid)

        self.x_len = len(grid[0]) if self.y_len != 0 else 0

        def findIsland(x: int, y: int):
            neighbors = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]

            land_neighbors = []
            for neighbor in neighbors:
                x_i = neighbor[0]
                y_i = neighbor[1]
                if x_i < self.x_len and x_i >= 0 and y_i < self.y_len and y_i >= 0 and grid[y_i][x_i] == '1':
                    land_neighbors.append(neighbor)
            print("land neighbors: ", land_neighbors)

            neighbor_len = len(land_neighbors)
            if neighbor_len == 0:
                self.islandList.append(set())
                self.islandList[-1].add((x, y))
            elif neighbor_len == 1:
                added = False
                for land in self.islandList:
                    if land_neighbors[0] in land:
                        land.add((x, y))
                        added = True
                if not added:
                    existed = False
                    for land in self.islandList:
                        if (neighbor[0], neighbor[1]) in land:
                            land.add((x, y))
                            existed = True
                    if not existed:
                        self.islandList.append(set())
                        self.islandList[-1].add((neighbor[0], neighbor[1]))
                        self.islandList[-1].add((x, y))
            elif neighbor_len >= 2:
                belonged_lands = []

                for neighbor in land_neighbors:
                    added = False
                    for land in self.islandList:
                        if neighbor in land:
                            land.add((x, y))
                            belonged_lands.append(self.islandList.index(land))
                            added = True
                    if not added:
                        self.islandList.append(set())
                        self.islandList[-1].add((neighbor[0], neighbor[1]))
                        belonged_lands.append(len(self.islandList) - 1)

                combine_landlist = belonged_lands
                if len(combine_landlist) == 1:
                    pass
                else:
                    combined_land = set()
                    print("perform land combine :")
                    for land in sorted(combine_landlist, reverse=True):
                        del self.islandList[land]
                    print("as whole :", combined_land)
                    self.islandList.append(combined_land)
            print("island list: ", self.islandList)
        for y in range(self.y_len):
            for x in range(self.x_len):
                if grid[y][x] == '1':
                    print("query ", x, y)
                    findIsland(x, y)
        return len(self.islandList)
