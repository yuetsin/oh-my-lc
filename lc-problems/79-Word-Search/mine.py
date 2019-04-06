class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        y_max = len(board)
        if y_max != 0:
            x_max = len(board[0])
        else:
            x_max = 0

        visited = set()

        def startGo(at: (int, int), board: List[List[str]], word: str) -> bool:
            visited.add(at)
            if len(word) == 0:
                return True
            result = False
            if at[0] + 1 < x_max and (not (at[0] + 1, at[1]) in visited):
                if board[at[1]][at[0] + 1] == word[0]:
                    result = result or startGo(
                        (at[0] + 1, at[1]), board, word[1:])
            if at[0] > 0 and (not (at[0] - 1, at[1]) in visited):
                if board[at[1]][at[0] - 1] == word[0]:
                    result = result or startGo(
                        (at[0] - 1, at[1]), board, word[1:])
            if at[1] + 1 < y_max and (not (at[0], at[1] + 1) in visited):
                if board[at[1] + 1][at[0]] == word[0]:
                    result = result or startGo(
                        (at[0], at[1] + 1), board, word[1:])
            if at[1] > 0 and (not (at[0], at[1] - 1) in visited):
                if board[at[1] - 1][at[0]] == word[0]:
                    result = result or startGo(
                        (at[0], at[1] - 1), board, word[1:])
            if not result:
                visited.remove(at)
            return result

        for y in range(y_max):
            for x in range(x_max):
                if board[y][x] == word[0]:
                    visited = set()
                    if startGo((x, y), board, word[1:]):
                        return True
        return False
