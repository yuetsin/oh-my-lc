#!/usr/bin/env python


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        y_max = len(board)

        if y_max == 0:
            return []

        x_max = len(board[0])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def dfs(x: int, y: int):
            if board[y][x] != 'E':
                return
            # print("Called dfs(%d, %d)" % (x, y))
            neighbors = []
            if x > 0:
                neighbors.append((y, x - 1))

            if x < x_max - 1:
                neighbors.append((y, x + 1))

            if y < y_max - 1:
                neighbors.append((y + 1, x))

            if y > 0:
                neighbors.append((y - 1, x))

            if y > 0 and x > 0:
                neighbors.append((y - 1, x - 1))

            if y > 0 and x < x_max - 1:
                neighbors.append((y - 1, x + 1))

            if y < y_max - 1 and x > 0:
                neighbors.append((y + 1, x - 1))

            if y < y_max - 1 and x < x_max - 1:
                neighbors.append((y + 1, x + 1))

            counter = 0

            for point in neighbors:
                if board[point[0]][point[1]] == 'M':
                    counter += 1

            if counter == 0:
                board[y][x] = 'B'
                for point in neighbors:
                    dfs(point[1], point[0])
            else:
                board[y][x] = str(counter)

        dfs(click[1], click[0])

        return board
