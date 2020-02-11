#!/usr/bin/env python


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dic = {}

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in dic[source])

        for u, v in edges:
            seen = set()
            if u in dic and v in dic and dfs(u, v):
                return u, v
            if not u in dic:
                dic.update({
                    u: set()
                })

            if not v in dic:
                dic.update({
                    v: set()
                })

            dic[u].add(v)
            dic[v].add(u)
