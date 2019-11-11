#!/usr/bin/env python


class Solution:
    def decodeString(self, s: str) -> str:
        lastBracketPlace = -1

        depth = 0
        times = 0
        result = ''
        for i in range(len(s)):
            if s[i] == '[':
                depth += 1
                if depth == 1:
                    lastBracketPlace = i
            elif s[i] == ']':
                depth -= 1
                if depth == 0:
                    result += times * \
                        self.decodeString(s[lastBracketPlace + 1: i])
                    times = 0
            elif s[i] in '1234567890':
                if depth == 0:
                    times *= 10
                    times += int(s[i])
            else:
                if depth == 0:
                    result += s[i]
        return result
