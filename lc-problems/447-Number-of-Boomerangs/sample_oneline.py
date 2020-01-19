#!/usr/bin/env python


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        return sum(v*(v-1) for a in points for v in collections.Counter((a[0]-b[0])**2+(a[1]-b[1])**2 for b in points).values())
