#!/usr/bin/env python


class Solution:
    visited = set()

    def isHappy(self, n: int) -> bool:
        self.visited = set()
        return self.isHappyInterior(n)

    def isHappyInterior(self, n: int) -> bool:
        if n == 0:
            return False
        # print("determine ", n)
        if n == 1:
            return True
        if n in self.visited:
            return False
        self.visited.add(n)
        result = 0
        for digits in str(n):
            result += pow(int(digits), 2)

        return self.isHappyInterior(result)
