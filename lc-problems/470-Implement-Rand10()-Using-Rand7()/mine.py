#!/usr/bin/env python

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        #   1 2 3 4 5 6 7
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        picked = [
            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
            (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)
        ]
        while True:
            x = rand7()
            y = rand7()
            if (x, y) in picked:
                idx = picked.index((x, y)) % 10
                return idx if idx != 0 else 10
