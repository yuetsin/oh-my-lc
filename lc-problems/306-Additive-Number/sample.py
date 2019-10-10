#!/usr/bin/env python


class Solution(object):
    def search(self, num, i, j):
        N = len(num)
        a, b = int(num[:i+1]), int(num[i+1:j+1])
        idx = j + 1
        while idx < N:
            c = a + b
            cs = str(c)
            n = len(cs)
            if n + idx > N or num[idx:idx+n] != cs:
                return False
            idx += n
            a, b = b, c
        return True

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        N = len(num)
        if N < 3:
            return False

        if num[:2] == '00':
            return int(num) == 0

        if num[0] == '0':
            for i in range(1, N-1):
                if self.search(num, 0, i):
                    return True
            return False

        for i in range(N//2):
            if num[i+1] == '0':
                if self.search(num, i, i+1):
                    return True
            else:
                j = i + 1
                while max(i+1, j-i) <= (N-j-1):
                    if self.search(num, i, j):
                        return True
                    j += 1
        return False
