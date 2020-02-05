#!/usr/bin/env python


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        p0 = p1 = -1
        for bi, bed in enumerate(flowerbed):
            if bed == 1:
                if p0 != -1:
                    p1 = bi
                    cnt += (p1-2-p0)//2
                    p0 = bi
                    p1 = -1
                else:
                    p0 = bi
                    cnt += p0//2
        cnt += (len(flowerbed)-1-p0)//2 if p0 != - \
            1 else (len(flowerbed)-1)//2+1
        return cnt >= n
