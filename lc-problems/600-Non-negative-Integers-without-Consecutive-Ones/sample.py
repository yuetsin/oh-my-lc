#!/usr/bin/env python


class Solution:
    def findIntegers(self, num: int) -> int:
        # no consecutive ones
        f = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
             17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]

        i = 30
        sam = 0
        prev_bit = 0

        while i >= 0:
            if (num & (1 << i)) != 0:
                sam += f[i]
                if prev_bit == 1:
                    sam -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
            i -= 1
        return sam + 1
