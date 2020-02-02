#!/usr/bin/env python

import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        string = str(n)

        last_c = -1

        decrease_len = 0

        nums = []

        for char in string[::-1]:
            dig = int(char)
            if dig >= last_c:
                decrease_len += 1
                last_c = dig
                nums.append(dig)
            else:
                break

        # print(decrease_len)
        if len(string) == decrease_len:
            return -1

        to_insert_i = len(string) - decrease_len - 1
        bisect.insort_left(nums, int(string[to_insert_i]))

        ret = string[:to_insert_i] + ''.join([str(i) for i in nums[::-1]])
        # print(ret)

        return ret
