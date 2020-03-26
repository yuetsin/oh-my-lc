#!/usr/bin/env python


class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:

        solved = (1, 2, 3, 4, 5, 0)

        visited = set()

        def slidingPuzzleWrapped(board: tuple) -> int:
            print("======")
            print(board)
            assert(len(board) == 6)

            if board in visited:
                # no return back
                return -1

            visited.add(board)

            if board == solved:
                return 0

            chance_3 = None

            if board[0] == 0:
                # 0 x x
                # x x x
                chance_1 = (board[1], board[0]) + board[2:]
                chance_2 = (board[3], board[1], board[2], board[0]) + board[4:]
            elif board[1] == 0:
                # x 0 x
                # x x x
                chance_1 = (board[1], board[0]) + board[2:]
                chance_2 = (board[0], board[4], board[2],
                            board[3], board[1], board[5])
                chance_3 = (board[0], board[2], board[1]) + board[3:]
            elif board[2] == 0:
                # x x 0
                # x x x
                chance_1 = (board[0], board[2], board[1]) + board[3:]
                chance_2 = board[:2] + (board[5], board[3], board[4], board[2])
            elif board[3] == 0:
                # x x x
                # 0 x x
                chance_1 = (board[3], board[1], board[2], board[0]) + board[4:]
                chance_2 = board[:3] + (board[4], board[3], board[5])
            elif board[4] == 0:
                # x x x
                # x 0 x
                chance_1 = board[:3] + (board[4], board[3], board[5])
                chance_2 = (board[0], board[4], board[2],
                            board[3], board[1], board[5])
                chance_3 = board[:4] + (board[5], board[4])
            elif board[5] == 0:
                # x x x
                # x x 0
                chance_1 = board[:2] + (board[5], board[3], board[4], board[2])
                chance_2 = board[:4] + (board[5], board[4])
            else:
                assert(False)

            chances = [chance_1, chance_2]

            if chance_3:
                chances.append(chance_3)

            ops = float('+inf')
            # print(chances)
            for chance in chances:
                assert(len(chance) == 6)
                sc = slidingPuzzleWrapped(chance)
                if sc != -1:
                    ops = min(ops, sc + 1)

            visited.remove(board)

            # print("!=====")
            return ops if ops != float('+inf') else -1

        return slidingPuzzleWrapped(tuple(board[0] + board[1]))
