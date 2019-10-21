#!/usr/bin/env python


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        num_edge = 0
        for ticket in tickets:
            src, dst = ticket
            num_edge += 1
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)

        path_tmp = list()
        path_left = list()
        path_right = list()

        stk = ["JFK"]
        num_edge_visited = 0
        while len(stk) > 0:
            node = stk.pop()
            num_edge_visited += 1
            path_tmp.append(node)
            if len(graph[node]) > 0:
                next_node = graph[node].pop()
                stk.append(next_node)
            else:
                path = path_left + path_tmp + path_right
                if num_edge_visited - 1 < num_edge:

                    N = len(path)
                    for i in range(N-1, -1, -1):
                        if len(graph[path[i]]) > 0:
                            node_next = graph[path[i]].pop()
                            stk.append(node_next)
                            path_left = path[:i+1]
                            path_right = path[i+1:]
                            path_tmp = list()
                            break
                else:
                    return path
