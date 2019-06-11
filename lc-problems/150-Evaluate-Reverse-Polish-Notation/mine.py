#!/usr/bin/env python


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not token in '+-*/':
                # print("numeric")
                stack.append(int(token))
            elif token == '+':
                # print("+")
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                # print("-")
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
                # print("-, get",b , a, b - a)
            elif token == '*':
                # print("*")
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                if a * b > 0:
                    stack.append(b // a)
                else:
                    stack.append(int(math.ceil(b / a)))
        return stack[0] if len(stack) > 0 else None
