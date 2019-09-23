#!/usr/bin/env python


class Solution:
    def calculate(self, s: str) -> int:
        preproc = s.replace(' ', '').replace('(', '').replace(
            ')', '').replace('+', '*+*').replace('-', '*-*')
        tokens = preproc.split('*')

        while len(tokens) > 2:
            v1 = int(tokens.pop(0))
            op = tokens.pop(0)
            v2 = int(tokens.pop(0))
            if op == '+':
                tokens.insert(0, v1 + v2)
            elif op == '-':
                tokens.insert(0, v1 - v2)
        return tokens[0]
