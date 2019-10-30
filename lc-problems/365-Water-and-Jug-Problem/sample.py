#!/usr/bin/env python


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x + y < z:
            return False

        gcd = self._gcd2(x, y)
        if gcd == 0:
            return False

        if z % gcd == 0:
            return True
        return False

    def _gcd(self, x, y):
        if x == 1:
            return 1
        if y == 1:
            return 1
        if x == y:
            return x

        xx = x & 1
        yy = y & 1

        if xx and yy:
            return self._gcd(min(x, y), abs(x - y))
        elif xx:
            return self._gcd(x, y >> 1)
        elif yy:
            return self._gcd(x >> 1, y)
        else:
            return self._gcd(x >> 1, y >> 1) << 1

    def _gcd1(self, x, y):
        if x == 0:
            return y
        if y == 0:
            return x
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x

    def _gcd2(self, x, y):
        if y == 0:
            return x

        temp = x % y
        while temp != 0:
            x, y = y, temp
            temp = x % y

        return y
