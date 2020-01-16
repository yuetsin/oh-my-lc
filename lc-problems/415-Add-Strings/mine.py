#!/usr/bin/env python


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1 = num1[::-1]
        s2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)

        chr_map = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

        ord_map = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9'
        }

        carry = 0
        result = []

        for i in range(max(l1, l2)):
            if i >= l1:
                ch1 = 0
            else:
                ch1 = chr_map[s1[i]]

            if i >= l2:
                ch2 = 0
            else:
                ch2 = chr_map[s2[i]]
            val = ch1 + ch2 + carry

            if val < 10:
                result.append(ord_map[val])
                carry = 0
            else:
                result.append(ord_map[val - 10])
                carry = 1

        if carry == 1:
            result.append('1')

        result.reverse()
        return ''.join(result)
