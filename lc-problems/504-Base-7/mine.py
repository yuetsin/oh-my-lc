#!/usr/bin/env python


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            minus = True
            num = -num
        else:
            minus = False

        result = []
        if minus:
            result.append('-')

        trailing_zero = True
        for i in range(8, -1, -1):
            # i goes from 8, 7, 6, ... till 0
            val = pow(7, i)
            bit = num // val
            if bit != 0:
                num -= bit * val
                result.append(str(bit))
                trailing_zero = False
            elif not trailing_zero:
                result.append('0')

        # print(result)
        return ''.join(result)
