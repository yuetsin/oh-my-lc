#!/usr/bin/env python


class Solution:
    def diffWaysToCompute(self, input_str: str) -> List[int]:

        def getPossible(string: str) -> List[int]:

            op_count = string.count(
                '+') + string.count('-') + string.count('*')
            if op_count == 0:
                return [int(string)]

            to_return = []

            # Right Combination, Left Priority

            token_li = len(string)

            valPlus = string.find('+')
            valMinus = string.find('-')
            valMult = string.find('*')

            if valPlus != -1:
                token_li = min(valPlus, token_li)
            if valMinus != -1:
                token_li = min(valMinus, token_li)
            if valMult != -1:
                token_li = min(valMult, token_li)

            left_num = int(string[:token_li])
            token = string[token_li]
            right_possible = getPossible(string[token_li + 1:])
            for right_num in right_possible:
                if token == '+':
                    to_return.append(left_num + right_num)
                elif token == '-':
                    to_return.append(left_num - right_num)
                elif token == '*':
                    to_return.append(left_num * right_num)

            if op_count == 1:
                to_return
            # Left Combination, Right Priority

            token_ri = -1

            valPlus = string.rfind('+')
            valMinus = string.rfind('-')
            valMult = string.rfind('*')

            if valPlus != -1:
                token_ri = max(valPlus, token_ri)
            if valMinus != -1:
                token_ri = max(valMinus, token_ri)
            if valMult != -1:
                token_ri = max(valMult, token_ri)

            right_num = int(string[token_ri + 1:])
            token = string[token_ri]
            left_possible = getPossible(string[:token_ri])
            for left_num in left_possible:
                if token == '+':
                    to_return.append(left_num + right_num)
                elif token == '-':
                    to_return.append(left_num - right_num)
                elif token == '*':
                    to_return.append(left_num * right_num)

            return to_return
        return getPossible(input_str)
