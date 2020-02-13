#!/usr/bin/env python

import random


class Solution:
    def __init__(self, n, blacklist):
        sblacklist = set(blacklist)
        ptr = [n - len(blacklist)]
        ll = len(blacklist)
        h = {b: self.f(ptr, sblacklist) for b in blacklist if b < n - ll}
        self.n = n - ll
        self.h = h

    def f(self, ptr, sb):
        while(ptr[0] in sb):
            ptr[0] += 1
        ptr[0] += 1
        return ptr[0] - 1

    def pick(self):
        r = random.randint(0, self.n - 1)
        return self.h.get(r, r)
