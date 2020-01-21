#!/usr/bin/env python


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s == '':
            return False

        counts = dict(collections.Counter(s))
        cnnt = [v for _, v in counts.items()]

        if len(cnnt) >= 2:
            gcd = math.gcd(cnnt[0], cnnt[1])

            for i in range(2, len(cnnt)):
                gcd = m ath.gcd(gcd, cnnt[i])
        else:
            return len(s) != 1

        cnnt = gcd

        if cnnt == 1:
            return False

        for k, v in counts.items():
            if v % cnnt != 0:
                return False

        each_w = len(s) // cnnt
        sample = s[:each_w]
        print(each_w)
        for k in range(1, cnnt):
            print("Judge", s[(k * each_w): (k * each_w + each_w)])
            if s[k * each_w: k * each_w + each_w] != sample:
                return False

        return True
