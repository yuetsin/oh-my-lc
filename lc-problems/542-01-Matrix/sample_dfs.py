#!/usr/bin/env python


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 4 directions
        # at least one 0
        # int < 10,000
        # only, 0 and 1

        # get coords of 0s, and 1s
        visited = set()  # 0s
        to_visit = set()  # 1s
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    visited.add((r, c))
                else:
                    to_visit.add((r, c))

        # bfs search, update to_visit, visited, until to_visit is empty
        cur = 1  # current value to put
        while to_visit:
            next_to_visit = set()
            for coord in to_visit:
                r, c = coord[0], coord[1]
                # check left/right/up/down
                if (r-1, c) in visited or (r+1, c) in visited or (r, c-1) in visited or (r, c+1) in visited:
                    matrix[r][c] = cur
                else:
                    next_to_visit.add((r, c))

            # update cur, visited, and to_visit
            cur += 1
            visited.update(to_visit - next_to_visit)
            to_visit = next_to_visit
        # return
        return matrix
