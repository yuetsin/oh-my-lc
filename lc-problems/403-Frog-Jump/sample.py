#!/usr/bin/env python


class Solution(object):
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        for i in range(3, len(stones)):
            if stones[i] > stones[i-1] * 2:
                return False
        if len(stones) == 2:
            return True

            # total stone distance and number of steps to reach this stone
            q = [(1, 1)]
        stoneset = set(stones)

        while(q):
            stone_num, k = q.pop()
            for i in range(k-1, k+2):
                if i == 0:
                    continue
                if stone_num+i in stoneset:
                    if stone_num + i == stones[-1]:
                        return True
                    q.append((stone_num + i, i))

        return False
