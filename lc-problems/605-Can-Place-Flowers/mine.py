#!/usr/bin/env python


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        counter = 0

        length = len(flowerbed)

        for flow in range(length):
            if flowerbed[flow] == 1:
                continue
            if flow == 0:
                if length < 2 or flowerbed[flow + 1] == 0:
                    counter += 1
                    flowerbed[flow] = 1
            elif flow == length - 1:
                if length < 2 or flowerbed[flow - 1] == 0:
                    counter += 1
                    flowerbed[flow] = 1
            else:
                if flowerbed[flow - 1] == 0 and flowerbed[flow + 1] == 0:
                    counter += 1
                    flowerbed[flow] = 1

        # print(flowerbed)
        return counter >= n
