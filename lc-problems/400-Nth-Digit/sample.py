#!/usr/bin/env python


class Solution:
    def findNthDigit(self, n: int) -> int:
        buckets = [0, 9, 180, 27e2, 36e3, 45e4, 54e5, 63e6, 72e7, 81e8, 90e9]
        bucket = count = 0
        while True:
            curr = count + buckets[bucket]
            if n < curr:
                break
            count = curr
            bucket += 1

        n = n - count - 1
        size = bucket  # number of digits our number has
        position = n // size
        number = int(position + 10 ** (size - 1))
        digitPos = size - n % size - 1

        while digitPos > 0:
            digitPos -= 1
            number //= 10
        return number % 10
