#!/usr/bin/env python

'''
Union Find
'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        students = len(M)
        students_union = {}
        for i in range(students):
            for j in range(students):
                if j > i:
                    break
                if M[i][j] == 1:
                    self.union(i, j, students_union)
        res = set()
        for i in range(students):
            res.add(self.find(i, students_union))
        return len(res)

    def find(self, cur, my_union):
        if cur not in my_union:
            return None
        root = cur
        while root != my_union[root]:
            root = my_union[root]
        while cur != root:
            nxt = my_union[cur]
            my_union[cur] = root
            cur = nxt
        return root

    def union(self, left, right, my_union):
        left_root = self.find(left, my_union)
        right_root = self.find(right, my_union)
        if not left_root and not right_root:
            my_union[left] = my_union[right] = left
        elif not left_root and right_root:
            my_union[left] = right_root
        elif left_root and not right_root:
            my_union[right] = left_root
        else:
            my_union[right_root] = left_root


'''
DFS
'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        students = len(M)
        for i in range(students):
            for j in range(students):
                if j > i:
                    break
                if M[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        seen = set()
        res = 0
        for s in range(students):
            if s not in seen:
                res += 1
                self.DFS(s, graph, seen)
        return res

    def DFS(self, cur, graph, seen):
        seen.add(cur)
        for nxt in graph[cur]:
            if nxt not in seen:
                self.DFS(nxt, graph, seen)
        return
