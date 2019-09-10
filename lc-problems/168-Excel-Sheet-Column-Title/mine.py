#!/usr/bin/env python


class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        numbersCount = len(alphabet)

        result = ""
        while n != 0:
            if n < numbersCount:
                result = alphabet[n - 1] + result
                return result
            prefix = n % numbersCount
            n = (n - 1) // numbersCount
            result = alphabet[prefix - 1] + result
            # print(prefix, n)
        return result
