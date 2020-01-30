#!/usr/bin/env python


def convertToBase7(self, num: int) -> str:
    if not num:
        return '0'
    ans = ''
    x = abs(num)
    while x:
        ans += str(x % 7)
        x //= 7
    if num < 0:
        return '-'+str(ans[::-1])
    return str(ans[::-1])
