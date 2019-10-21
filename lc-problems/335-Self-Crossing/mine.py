#!/usr/bin/env python


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        # 请题目作者用制表符来画图形
        # 不要使用 | - ' ' 这些不等宽字符来瞎人眼

        visited_points = set()

        visited_points.add((0, 0))

        cur_x = 0
        cur_y = 0

        xs = len(x)

        if xs == 0:
            return False

        for i in range(xs):
            flag = i % 4

            steps = x[i]

            for _ in range(steps):
                if flag == 0:
                    # ⬆️
                    cur_y += 1
                elif flag == 1:
                    cur_x -= 1
                elif flag == 2:
                    cur_y -= 1
                elif flag == 3:
                    cur_x += 1

                if (cur_x, cur_y) in visited_points:
                    return True
                visited_points.add((cur_x, cur_y))
        return False
