#!/usr/bin/env python3

# A bad solution. Recording this
# for it's my first Memory Limit Exceeded


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Alike Chinese Go Game
        height = len(board)
        width = len(board[0]) if height != 0 else 0

        if width == 0 or height == 0:
            return

        def getAll(start: (int, int), board: List[List[str]]) -> set:
            stack = [start]
            found = set()
            while stack != []:
                for i in stack:
                    stack.append((i[0] + 1, i[1]))
                    stack.append((i[0], i[1] + 1))
                    stack.append((i[0] - 1, i[1]))
                    stack.append((i[0], i[1] - 1))

                new_stack = []
                for rf in stack:
                    if rf in found:
                        continue

                    if rf[0] < 0 or rf[0] >= height:
                        continue

                    if rf[1] < 0 or rf[1] >= width:
                        continue

                    if board[rf[0]][rf[1]] == 'X':
                        continue

                    new_stack.append(rf)
                    found.add(rf)
                stack = new_stack
            return found

        # print(width, height)
        def findNeighbour(board: List[List[str]]):
            existed_area = []
            for h_i in range(height):
                for w_i in range(width):
                    if board[h_i][w_i] == 'X':
                        continue
                    for area in existed_area:
                        if board[h_i][w_i] in area:
                            continue
                    print("called ", h_i, w_i)
                    return
                    existed_area.append(getAll((h_i, w_i), board))
                    print(existed_area)
                    return

        findNeighbour(board)
