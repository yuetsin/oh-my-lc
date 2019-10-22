#!/usr/bin/env python


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(int(math.sqrt(num)) - 1, int(math.sqrt(num)) + 1):
            if i * i == num:
                return True

        return False
