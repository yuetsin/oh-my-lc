class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkDuplicate(block: List[str]) -> bool:
            for ch in "0123456789":
                if block.count(ch) > 1:
                    return False
            return True
        for row in board:
            if not checkDuplicate(row):
                return False
        for column in range(9):
            col = []
            for i in range(9):
                col.append(board[i][column])
            if not checkDuplicate(col):
                return False

        for r3 in range(3):
            for c3 in range(3):
                block = []
                for i in range(3):
                    block += board[3 * r3 + i][3 * c3: 3 * c3 + 3]

                if not checkDuplicate(block):
                    return False
        return True
