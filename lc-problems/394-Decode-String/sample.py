#!/usr/bin/env python


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):

            if s[i].isnumeric():
                num = []
                while s[i].isnumeric():
                    num.append(s[i])
                    i += 1
                stack.append(''.join(num))

            elif s[i] == '[':
                stack.append(s[i])
                i += 1

            elif s[i].isalpha():
                ss = []
                while i < len(s) and s[i] != ']' and not s[i].isnumeric():
                    ss.append(s[i])
                    i += 1
                stack.append(''.join(ss))

            elif s[i] == ']':
                ss = []
                while stack[-1].isalpha():
                    ss.insert(0, stack.pop())

                ss = ''.join(ss)
                stack.pop()
                stack.append(int(stack.pop())*ss)
                i += 1

        return ''.join(stack)
