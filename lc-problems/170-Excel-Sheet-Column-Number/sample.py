#!/usr/bin/env python


def titleToNumber(s):
    return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))
