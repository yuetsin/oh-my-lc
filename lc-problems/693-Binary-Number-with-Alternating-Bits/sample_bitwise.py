#!/usr/bin/env python

# written by @andizzlezhang


def hasAlternatingBits(n: int) -> bool:
    v = 1 + n + n >> 1
    return v & (v - 1) == 0
