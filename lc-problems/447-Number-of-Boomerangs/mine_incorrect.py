#!/usr/bin/env python


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        point_cnt = len(points)
        if point_cnt < 3:
            return 0

        pairs = {}
        for i in range(point_cnt):
            for j in range(i + 1, point_cnt):
                p1 = points[i]
                p2 = points[j]
                distance = (j, (p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2)

                if distance in pairs:
                    pairs[distance] += 1
                else:
                    pairs.update({distance: 1})

        print(pairs)
        result = 0
        for _, v in pairs.items():
            # v = v_tuple[1]
            # 1 -> 0
            # 2 -> 2
            # 3 -> 6
            # 4 -> 12
            result += 2 * v * (v - 1)
        return result
