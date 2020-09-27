import collections


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # BFS
        color = {}
        for i in range(len(graph)):
            if i not in color and graph[i]:
                q = collections.deque([i])
                color[i] = 0
                while q:
                    node = q.popleft()
                    for nextNode in graph[node]:
                        if nextNode not in color:
                            color[nextNode] = color[node] ^ 1
                            q.append(nextNode)
                        else:
                            if color[nextNode] == color[node]:
                                print(i, color)
                                return False
        return True

        # DFS
        color = {}

        def findConflict(i):
            for j in graph[i]:
                if j not in color:
                    color[j] = color[i] ^ 1
                    if findConflict(j):
                        return True
                else:
                    if color[j] == color[i]:
                        return True
            return False

        for i in range(len(graph)):
            if i not in color and graph[i]:
                color[i] = 0
                if findConflict(i):
                    return False
        return True
