#!/usr/bin/env python


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # arithmetic 定义：长度 >= 3 的等差数列。

        length = len(A)

        if length < 3:
            return 0

        count = 0
        for i in range(length - 2):
            # check the maximum arithmetic slice since p
            p = i
            cons = A[p + 1] - A[p]

            # by default there's 2 elements in the arithmetic slice
            slice_count = 2
            while True:
                p += 1
                if p >= length - 1:
                    break
                if A[p + 1] - A[p] == cons:
                    slice_count += 1
                else:
                    break

            if slice_count >= 3:
                count += slice_count - 2

            # print("i = %d, slice_count = %d" % (i, slice_count))
        return count
