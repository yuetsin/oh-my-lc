#!/usr/bin/env python
#
# written by @hongsenyu

'''
UnionFind
Use a dict to store elevation:position of each position.
At time t, we fetch all positions with elevation of t and try to union its neighbors with less or equal elevation.
At time t, use UnionFind to check if top left and bottom right are connected.
If they are connected, return t
Time: O(n), n is the size of grid, row length * col length
Space: O(n)
'''


class Solution:
    def find(self, cur, my_union):
        if cur not in my_union:
            my_union[cur] = cur
            return cur
        root = cur
        while root != my_union[root]:
            root = my_union[root]
        while cur != root:  # Path compression, optional.
            nxt = my_union[cur]
            my_union[cur] = root
            cur = nxt
        return root

    def union(self, left, right, my_union):
        left_r, right_r = self.find(left, my_union), self.find(right, my_union)
        if left_r < right_r:
            my_union[right_r] = left_r
        elif right_r < left_r:
            my_union[left_r] = right_r
        return

    def swimInWater(self, grid: List[List[int]]) -> int:
        my_union = {}
        elevation_dict = collections.defaultdict(list)
        row_len, col_len = len(grid), len(grid[0])
        for r in range(row_len):
            for c in range(col_len):
                elevation_dict[grid[r][c]].append((r, c))
        t = 0
        while True:
            self.helper(t, elevation_dict, my_union, grid, row_len, col_len)
            if self.find((0, 0), my_union) == self.find((row_len-1, col_len-1), my_union):
                return t
            t += 1

    def helper(self, t, elevation_dict, my_union, grid, row_len, col_len):
        cur_lst = elevation_dict[t]
        for cur_r, cur_c in cur_lst:
            for nxt_r, nxt_c in [(cur_r, cur_c+1), (cur_r, cur_c-1), (cur_r+1, cur_c), (cur_r-1, cur_c)]:
                if 0 <= nxt_r < row_len and 0 <= nxt_c < col_len and grid[nxt_r][nxt_c] <= grid[cur_r][cur_c]:
                    self.union((cur_r, cur_c), (nxt_r, nxt_c), my_union)
