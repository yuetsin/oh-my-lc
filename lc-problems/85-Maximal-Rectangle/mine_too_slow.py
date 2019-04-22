class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def checkIfRectangle(matrix, x1, x2, y1, y2) -> bool:
            if x1 < 0 or y1 < 0:
                return False
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    try:
                        if matrix[y][x] != '1':
                            return False
                    except:
                        return False

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    try:
                        start_point.remove((x, y))
                    except:
                        pass
            return True

        def checkMaximum(matrix, x1, x2, y1, y2) -> int:
            if not checkIfRectangle(matrix, x1, x2, y1, y2):
                return -1
            current = (x2 - x1 + 1) * (y2 - y1 + 1)
            # print("CURRENT: x %d ～ %d, y %d ～ %d. SQR = %d" % (x1, x2, y1, y2, current))
            v1 = checkMaximum(matrix, x1, x2 + 1, y1, y2)
            v2 = checkMaximum(matrix, x1 - 1, x2, y1, y2)
            v3 = checkMaximum(matrix, x1, x2, y1 - 1, y2)
            v4 = checkMaximum(matrix, x1, x2, y1, y2 + 1)

            return max(current, v1, v2, v3, v4)

        start_point = []
        # visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    start_point.append((j, i))

        max_result = 0

        while len(start_point) != 0:
            pt = start_point[0]
            val = checkMaximum(matrix, pt[0], pt[0], pt[1], pt[1])
            if val > max_result:
                max_result = val

        return max_result
