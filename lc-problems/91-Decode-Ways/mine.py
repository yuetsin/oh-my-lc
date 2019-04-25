#!/usr/bin/env python

class Solution:
    def numDecodings(self, s: str) -> int:
        # return 0
        max_idx = len(s) - 1
        dp_table = [None] * (len(s) + 1)
        def decode(at: int) -> int:
            # print("at: %d" % at)
            if at > max_idx:
                return 1
            if at == max_idx:
                if s[at] != '0':
                    return 1
                return 0
            rst = 0
            as_1 = int(s[at])
            as_2 = int(s[at:at + 2])
            if as_1 != 0:
                if dp_table[at + 1] == None:
                    dp_table[at + 1] = decode(at + 1)
                rst += dp_table[at + 1]
                if as_2 < 27:
                    if dp_table[at + 2] == None:
                        dp_table[at + 2] = decode(at + 2)
                    rst += dp_table[at + 2]
            return rst
        return decode(0)