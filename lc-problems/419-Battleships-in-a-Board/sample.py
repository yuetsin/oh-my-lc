#!/usr/bin/env python


def countBattleships(self, board: List[List[str]]) -> int:
    l_n = len(board)
    l_m = len(board[0])

    count = 0

    for i in range(l_n):
        for j in range(l_m):
            if board[i][j] == ".":
                continue

            if (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                count += 1

    return count
