class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x = 0
        y = 0

        y_max = len(matrix)
        if y_max == 0:
            return []
        x_max = len(matrix[0])
        len_limit = x_max * y_max

        y_min = -1
        x_min = -1
        rst = [matrix[0][0]]
        rst_cnt = 1
        flag = 0

        flag_emojis = ["➡️", "⬇️", "⬅️", "⬆️"]

        # 0: ➡️
        # 1: ⬇️
        # 2: ⬅️
        # 3: ⬆️

        while rst_cnt < len_limit:
            # print("flag = %s. x in (%d, %d) y in (%d, %d)" % (flag_emojis[flag], x_min, x_max, y_min, y_max))
            if x_max - x_min < 2 or y_max - y_min < 2:
                break
            if flag == 0:
                x += 1
                if x < x_max:
                    rst.append(matrix[y][x])
                    rst_cnt += 1
                else:
                    flag = 1
                    x -= 1
                    y_min = y
            elif flag == 1:
                y += 1
                if y < y_max:
                    rst.append(matrix[y][x])
                    rst_cnt += 1
                else:
                    flag = 2
                    y -= 1
                    x_max = x
            elif flag == 2:
                x -= 1
                if x > x_min:
                    rst.append(matrix[y][x])
                    rst_cnt += 1
                else:
                    flag = 3
                    x += 1
                    y_max = y
            else:
                y -= 1
                if y > y_min:
                    rst.append(matrix[y][x])
                    rst_cnt += 1
                else:
                    flag = 0
                    y += 1
                    x_min = x
        return rst
