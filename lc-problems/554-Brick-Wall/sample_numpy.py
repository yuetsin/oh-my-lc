#!/usr/bin/env python

import numpy as np


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = []
        for x in wall:
            edges.append(np.cumsum(np.asarray(x[:-1])))
        edges = np.concatenate(edges)
        _, cnt = np.unique(edges, return_counts=True)
        return len(wall) - cnt.max(initial=0)
