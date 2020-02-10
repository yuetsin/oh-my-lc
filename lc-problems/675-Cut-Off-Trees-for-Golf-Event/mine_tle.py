#!/usr/bin/env python


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        max_y = len(forest)
        if max_y == 0:
            return 0

        max_x = len(forest[0])

        visited = []

        def goesThrough(since: tuple, to: tuple) -> int:
            if since == to:
                return 0

            x, y = since[0], since[1]

            if forest[y][x] == 0:
                return float('+inf')

            visited.append(since)

            steps = float('+inf')
            if x > 0 and (not (x - 1, y) in visited) and forest[y][x - 1] != 0:
                steps = min(steps, 1 + goesThrough((x - 1, y), to))

            if x < max_x - 1 and (not (x + 1, y) in visited) and forest[y][x + 1] != 0:
                steps = min(steps, 1 + goesThrough((x + 1, y), to))

            if y > 0 and (not (x, y - 1) in visited) and forest[y - 1][x] != 0:
                steps = min(steps, 1 + goesThrough((x, y - 1), to))

            if y < max_y - 1 and (not (x, y + 1) in visited) and forest[y + 1][x] != 0:
                steps = min(steps, 1 + goesThrough((x, y + 1), to))

            visited.pop(-1)
            return steps

        trees = []

        for x in range(max_x):
            for y in range(max_y):
                if forest[y][x] > 1:
                    trees.append((forest[y][x], x, y))

        trees.sort(key=lambda x: x[0])

        total_steps = 0

        last_p = (0, 0)
        for tree in trees:
            tree_pos = (tree[1], tree[2])
            step = goesThrough(last_p, tree_pos)
            if step == float('+inf'):
                return -1
            total_steps += step
            last_p = tree_pos

        return total_steps
