#!/usr/bin/env python


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []

        arrowGoesUp = True
        px, py = 0, 0

        y_max = len(matrix)
        x_max = len(matrix[0])

        result = []

        while True:
            # print("going on (x, y) = (%d, %d)" % (px, py))
            if px >= 0 and px < x_max and py >= 0 and py < y_max:
                result.append(matrix[py][px])
            if px == x_max - 1 and py == y_max - 1:
                break
            if arrowGoesUp:
                if px < x_max - 1 and py > 0:
                    px += 1
                    py -= 1
                elif px == x_max - 1:
                    py += 1
                    arrowGoesUp = False
                elif py == 0:
                    px += 1
                    arrowGoesUp = False
                else:
                    break
            else:
                if px > 0 and py < y_max - 1:
                    px -= 1
                    py += 1
                elif px == 0:
                    py += 1
                    arrowGoesUp = True
                elif py == y_max - 1:
                    px += 1
                    arrowGoesUp = True
                else:
                    break

        return result
