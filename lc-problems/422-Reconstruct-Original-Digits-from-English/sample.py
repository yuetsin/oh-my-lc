#!/usr/bin/env python

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        ls = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
        cnt = Counter(s)
        res = ["" for _ in range(10)]
        check_ls = [["z", 0], ["x", 6], ["w", 2], ["g", 8], [
            "h", 3], ["u", 4], ["o", 1], ["f", 5], ["s", 7], ["i", 9]]
        for i in range(10):
            if check_ls[i][0] in cnt and cnt[check_ls[i][0]] > 0:
                n = cnt[check_ls[i][0]]
                res[check_ls[i][1]] = str(check_ls[i][1])*n
                for j in ls[check_ls[i][1]]:
                    cnt[j] -= n
                    if cnt[j] == 0:
                        cnt.pop(j)
        return "".join(res)
