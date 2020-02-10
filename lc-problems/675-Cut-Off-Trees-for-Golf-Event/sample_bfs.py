#!/usr/bin/env python

from collections import defaultdict


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        tree = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    tree.append([forest[i][j], (i, j)])

        tree = sorted(tree)
        steps = 0
        st = (0, 0)
        c = 0
        last = None
        for entry in tree:
            to = entry[1]
            c = self.bfs(st, to, forest)
            if c == -1:
                return -1
            steps += c
            st = to

        return steps

    def bfs(self, fr, target, forest):
        l = []
        l.append((0, fr[0], fr[1]))
        vis = set()
        vis.add(fr)
        ll = 0
        while ll < len(l):
            c, i, j = l[ll]
            ll += 1
            if (i, j) == target:
                forest[i][j] = 1
                return c
            for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if x >= 0 and x < len(forest) and y >= 0 and y < len(forest[0]) and (x, y) not in vis and forest[x][y] > 0:
                    l.append((c+1, x, y))
                    vis.add((x, y))

        return -1
