#!/usr/bin/env python


class Solution:
    def magicalString(self, n: int) -> int:
        # The string S is magical because
        # concatenating the number of contiguous occurrences of characters '1' and '2'
        # generates the string S itself.
        #
        pre_d = [0, 1]
        if n < 2:
            return pre_d[n]
        # True = 1
        # False = 2
        current_index = 0
        digits = [True]

        last_tweak = True

        counter = 0

        n -= 1
        while current_index < n:
            if digits[current_index]:
                # It's a 1
                digits.append(not last_tweak)
                counter += 1
            else:
                digits.append(not last_tweak)
                digits.append(not last_tweak)
            last_tweak = not last_tweak
            current_index += 1
        # print(digits)
        return counter

# 1 2 2 1 1 2 1 2 2 1 2 2 1 1 2 1 1 2 2
#   1 2 1 1 2 1 2 2 1 2 2 1 1 2 1 1 2 2
