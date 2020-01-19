#!/usr/bin/env python


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        last_char = ''
        for ch in chars:
            if ch == last_char:
                result[-1][1] += 1
            else:
                last_char = ch
                result.append([ch, 1])

        index = 0
        for item in result:
            chars[index] = item[0]
            index += 1
            if item[1] != 1:
                value = str(item[1])
                for digit_char in value:
                    chars[index] = digit_char
                    index += 1

        return index
