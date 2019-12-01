#!/usr/bin/env python


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for i in sorted(people, key=lambda x: (x[0], -x[1]), reverse=True):
            res.insert(i[1], i)
        return res
