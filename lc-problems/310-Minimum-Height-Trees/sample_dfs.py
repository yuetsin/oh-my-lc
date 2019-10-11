#!/usr/bin/env python


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def get_leaves(graph):
            leaves = []
            for node in graph.keys():
                if len(graph[node]) == 1:
                    leaves.append(node)
            return leaves

        if n == 1:
            return [0]
        g = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in g:
                g[u] = set()
            if v not in g:
                g[v] = set()
            g[u].add(v)
            g[v].add(u)

        while len(g) > 2:
            to_delete = get_leaves(g)
            for d in to_delete:
                u, v = d, g[d].pop()
                g[v].remove(u)
                del g[d]
        return list(g.keys())
