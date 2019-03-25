class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidSudoku(board: List[List[str]], row: int, col: int, c: str) -> bool:
            # org = board[row][col]
            # board[row][col] = c
            for i in range(9):
                if board[i][col] != '.' and board[i][col] == c:
                    # board[row][col] = org
                    return False
                if board[row][i] != '.' and board[row][i] == c:
                    # board[row][col] = org
                    return False
                if board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + i % 3] != '.' and board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + i % 3] == c:
                    # board[row][col] = org
                    return False

            # board[row][col] = org
            return True

        def solve(board: List[List[str]]) -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ch in "123456789":
                            if isValidSudoku(board, i, j, ch):
                                # print("Write. (%d, %d) = %s" % (i, j, ch))
                                board[i][j] = ch
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                                    # print("Write. (%d, %d) = %s" % (i, j, '.'))
                        return False
            return True

        solve(board)
