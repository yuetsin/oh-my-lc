#!/usr/bin/env python


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        height = len(board)
        width = len(board[0]) if height != 0 else 0

        counts = 0

        for y in range(height):
            for x in range(width):
                if board[y][x] == 'X':
                    if x < width - 1 and board[y][x + 1] == 'X':
                        # goes right
                        x0 = x
                        while x0 < width and board[y][x0] == 'X':
                            board[y][x0] = 'x'
                            x0 += 1

                    elif y < height - 1 and board[y + 1][x] == 'X':
                        # goes down
                        y0 = y
                        while y0 < height and board[y0][x] == 'X':
                            board[y0][x] = 'x'
                            y0 += 1

                    else:
                        board[y][x] = 'x'

                    counts += 1

        return counts
