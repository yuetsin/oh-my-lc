#!/usr/bin/env python


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []

        def getPossibleTokens(before: List[str], num: str) -> List[str]:
            prepare_rst = []
            for bf in before:
                if len(bf) == 0:
                    return [num]
                if bf[-1] != '0':
                    prepare_rst.append(bf + num)
                prepare_rst.append(bf + '+' + num)
                prepare_rst.append(bf + '-' + num)
                prepare_rst.append(bf + '*' + num)
            return prepare_rst
        counter = 0

        gotta_tokens = [""]
        while counter < len(num):
            gotta_tokens = getPossibleTokens(gotta_tokens, num[counter])
            counter += 1

        rst = []
        for tok in gotta_tokens:
            if eval(tok) == target:
                rst.append(tok)
        return rst
