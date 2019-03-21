from math import log, ceil, pow


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        x += 0.001
        len = round(ceil(log(x, 10)))
        for i in range(len):
            if (int(x / pow(10, i)) % 10) != (int(x / pow(10, len - i - 1)) % 10):
                return False
        return True
