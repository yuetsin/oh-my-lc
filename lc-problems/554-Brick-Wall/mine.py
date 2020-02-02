#!/usr/bin/env python


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        separators = {}
        for line in wall:
            init = 0
            for brick in line[:-1]:
                init += brick

                if init in separators:
                    separators[init] += 1
                else:
                    separators.update({
                        init: 1
                    })

        if len(separators) == 0:
            return len(wall)

        max_v = max([v for k, v in separators.items()])

        return len(wall) - max_v
