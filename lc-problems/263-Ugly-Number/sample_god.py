#!/usr/bin/env python


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # n = (2**30)*(3**20)*(5**13) = 4570198050078720000000000000L
        return False if num < 1 or (4570198050078720000000000000) % num != 0 else True


# 被这个解法吓死了…
# StefanPochmann says:

# Nice idea. Shorter implementation:

def isUgly(self, num):
    return num > 0 == 30**32 % num
# Don't worry about the runtime, it's mostly judge overhead. Check this out:


def isUgly(self, num):
    return [num > 0 == 30**32 % num for _ in range(1000)][-1]
# That does it 1000 times and gets accepted in about 420 ms. Meaning the actual solution takes only about 0.4 ms and the rest of the ~60 ms is judge overhead, and it varies considerably.

# 这个方法比另一个文件里的要快。
