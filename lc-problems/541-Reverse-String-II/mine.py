#!/usr/bin/env python


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 0:
            return k[::-1]
        counter = 0
        slen = len(s)

        reverse = True

        result = []
        while counter < slen:
            if not reverse:
                result.append(s[counter: min(counter + k, slen)])
            else:
                if counter == 0:
                    result.append(s[min(counter + k, slen) - 1::-1])
                else:
                    result.append(
                        s[min(counter + k, slen) - 1: counter - 1: -1])
            counter += k
            reverse = not reverse
        # print(result)
        return ''.join(result)
